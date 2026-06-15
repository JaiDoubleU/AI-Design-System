#!/usr/bin/env node
/**
 * build-docs.js — Component library documentation builder
 *
 * Scrapes component documentation for the specified UI library (if not already
 * present), then updates CLAUDE.md and AGENTS.md to reference the chosen
 * library's docs directory, adapter files, and component map.
 *
 * Usage:
 *   node scripts/build-docs.js --library=shadcn
 *   node scripts/build-docs.js --library=antdesign
 *   node scripts/build-docs.js --library=mui
 *   node scripts/build-docs.js --library=shadcn --force   # re-scrape even if docs exist
 *
 * npm aliases:
 *   npm run docs -- --library=shadcn
 *   npm run docs:shadcn
 *   npm run docs:antd
 *   npm run docs:mui
 */

'use strict';

const fs        = require('fs');
const path      = require('path');
const { spawnSync, execFileSync } = require('child_process');

const ROOT = path.resolve(__dirname, '..');

/* ─── Library registry ───────────────────────────────────────────────────── */

const LIBRARIES = {
  shadcn: {
    name:           'shadcn/ui',
    version:        'v4',
    docsDir:        'shadcn-docs',
    scraper:        path.join(__dirname, 'build-shadcn-docs.py'),
    adapterCss:     'lib-adapters/shadcn.css',
    adapterSpec:    'specs/adapters/shadcn.md',
    componentKey:   'shadcn',
    docsUrl:        'https://ui.shadcn.com/docs/components',
    setupNote:      'Requires shadcn/ui v4 with globals.css defining --primary, --background, --foreground, --border, --ring, --radius.',
    importBlock: `\
/* 1. shadcn globals */
@import '@/styles/globals.css';

/* 2. AI Design System adapter */
@import 'ai-design-system/lib-adapters/shadcn.css';

/* 3. AI Design System tokens */
@import 'ai-design-system/tokens.css';`,
    jsSetup: `\
import { applyAdapter } from 'ai-design-system/lib-adapters';
applyAdapter('shadcn');`,
    classMap: {
      '.btn':   '<Button>',
      '.card':  '<Card>',
      '.input': '<Input>',
      '.badge': '<Badge>',
      '.alert': '<Alert>',
      '.select': '<Select>',
      '.checkbox': '<Checkbox>',
      '.radio': '<RadioGroupItem>',
    },
  },

  antdesign: {
    name:           'Ant Design',
    version:        'v5',
    docsDir:        'antd-docs',
    scraper:        path.join(__dirname, 'build-antd-docs.py'),
    adapterCss:     'lib-adapters/ant-design.css',
    adapterSpec:    'specs/adapters/ant-design.md',
    componentKey:   'antDesign',
    docsUrl:        'https://ant.design/components/overview',
    setupNote:      'Requires Ant Design v5 with cssVar: true in ConfigProvider. Recommended: hashed: false.',
    importBlock: `\
/* 1. Ant Design reset */
@import 'antd/dist/reset.css';

/* 2. AI Design System adapter */
@import 'ai-design-system/lib-adapters/ant-design.css';

/* 3. AI Design System tokens */
@import 'ai-design-system/tokens.css';`,
    jsSetup: `\
import { applyAdapter } from 'ai-design-system/lib-adapters';
// Call after ConfigProvider has mounted:
applyAdapter('antDesign');`,
    classMap: {
      '.btn':      '<Button>',
      '.card':     '<Card>',
      '.input':    '<Input>',
      '.select':   '<Select>',
      '.badge':    '<Tag> (label) / <Badge> (count)',
      '.alert':    '<Alert>',
      '.checkbox': '<Checkbox>',
      '.radio':    '<Radio>',
    },
  },

  mui: {
    name:           'Material UI',
    version:        'v6',
    docsDir:        'mui-docs',
    scraper:        path.join(__dirname, 'build-mui-docs.py'),
    adapterCss:     'lib-adapters/material-ui.css',
    adapterSpec:    'specs/adapters/material-ui.md',
    componentKey:   'materialUI',
    docsUrl:        'https://mui.com/material-ui/all-components/',
    setupNote:      'Requires MUI v6 with cssVariables: true in createTheme, or v5 with Experimental_CssVarsProvider.',
    importBlock: `\
/* MUI injects its own styles via JS — import the adapter then tokens */
@import 'ai-design-system/lib-adapters/material-ui.css';
@import 'ai-design-system/tokens.css';`,
    jsSetup: `\
import { applyAdapter } from 'ai-design-system/lib-adapters';
// Inside a component, after ThemeProvider mounts:
useEffect(() => { applyAdapter('materialUI'); }, []);`,
    classMap: {
      '.btn':      '<Button>',
      '.card':     '<Card>',
      '.input':    '<TextField>',
      '.select':   '<Select>',
      '.badge':    '<Chip> (label) / <Badge> (count)',
      '.alert':    '<Alert>',
      '.checkbox': '<Checkbox>',
      '.radio':    '<Radio>',
    },
  },

  vanilla: {
    name:           'Vanilla HTML/CSS/JS',
    version:        'native',
    docsDir:        'vanilla-docs',
    scraper:        path.join(__dirname, 'build-vanilla-docs.js'),
    adapterCss:     'lib-adapters/vanilla.css',
    adapterSpec:    'specs/adapters/custom.md',
    componentKey:   null,
    docsUrl:        'https://developer.mozilla.org/en-US/docs/Web/HTML',
    setupNote:      'No framework required. Link tokens.css and the component CSS files directly in your HTML.',
    importBlock: `\
<!-- In your <head> — order matters -->
<link rel="stylesheet" href="tokens.css">
<link rel="stylesheet" href="src/base/reset.css">
<link rel="stylesheet" href="src/base/typography.css">

<!-- Add only the components you use -->
<link rel="stylesheet" href="src/components/button.css">
<link rel="stylesheet" href="src/components/card.css">
<link rel="stylesheet" href="src/components/input.css">
<link rel="stylesheet" href="src/components/badge.css">
<link rel="stylesheet" href="src/components/alert.css">`,
    jsSetup: `\
// No adapter or framework required.
// Optional: override tokens before importing tokens.css
// :root { --ds-interactive: #6366f1; }`,
    classMap: {
      '.btn .btn-primary':     '<button class="btn btn-primary">',
      '.card':                 '<div class="card">',
      '.input (in .field)':    '<input class="input" type="text">',
      '.badge .badge-success': '<span class="badge badge-success">',
      '.alert .alert-info':    '<div class="alert alert-info" role="status">',
      '.prose':                '<article class="prose">',
    },
  },
};

/* ─── Argument parsing ───────────────────────────────────────────────────── */

function parseArgs() {
  const args = process.argv.slice(2);
  const result = { library: null, force: false };
  for (const arg of args) {
    if (arg.startsWith('--library=')) result.library = arg.split('=')[1].toLowerCase();
    if (arg === '--force') result.force = true;
  }
  return result;
}

/* ─── Python detection ───────────────────────────────────────────────────── */

function findPython() {
  for (const bin of ['python3', 'python']) {
    const r = spawnSync(bin, ['--version'], { encoding: 'utf8' });
    if (r.status === 0) return bin;
  }
  return null;
}

/* ─── Scraper runner ─────────────────────────────────────────────────────── */

function runScraper(lib, python) {
  const isNode = lib.scraper.endsWith('.js');
  const label  = isNode ? 'Generating' : 'Scraping';
  console.log(`\n📥  ${label} ${lib.name} docs…`);

  if (!fs.existsSync(lib.scraper)) {
    console.error(`✗  Scraper not found: ${lib.scraper}`);
    process.exit(1);
  }

  const runtime = isNode ? process.execPath : python;
  const r = spawnSync(runtime, [lib.scraper], {
    cwd: ROOT,
    stdio: 'inherit',
    encoding: 'utf8',
  });
  if (r.status !== 0) {
    console.error(`✗  Scraper exited with code ${r.status}`);
    process.exit(r.status);
  }
}

/* ─── CLAUDE.md updater ──────────────────────────────────────────────────── */

const MARKER_START    = '<!-- ACTIVE-LIBRARY:START -->';
const MARKER_END      = '<!-- ACTIVE-LIBRARY:END -->';
const DOCSDIR_START   = '<!-- DOCS-DIR:START -->';
const DOCSDIR_END     = '<!-- DOCS-DIR:END -->';

function buildLibrarySection(lib, docsCount) {
  const classRows = Object.entries(lib.classMap)
    .map(([cls, comp]) => `| \`${cls}\` | \`${comp}\` |`)
    .join('\n');

  return `${MARKER_START}
## Active component library: ${lib.name} ${lib.version}

**Component docs:** \`${lib.docsDir}/\` (${docsCount} components — read before generating code)
**Index:** \`${lib.docsDir}/INDEX.md\`
**Adapter CSS:** \`${lib.adapterCss}\`
**Adapter spec:** \`${lib.adapterSpec}\`
**Official docs:** ${lib.docsUrl}

### Setup

${lib.setupNote}

\`\`\`css
${lib.importBlock}
\`\`\`

\`\`\`js
${lib.jsSetup}
\`\`\`

### AI Design System → ${lib.name} class map

| AI DS class | ${lib.name} equivalent |
|---|---|
${classRows}

### Rules when writing code with this library

- Read \`${lib.docsDir}/{component}.md\` before generating code for any component.
- Use \`getComponentInfo(concept, '${lib.componentKey}')\` from \`lib-adapters/component-map.js\`
  to find the correct import and props for any AI DS concept.
- Apply the CSS adapter before \`tokens.css\` so \`--ds-*\` hooks resolve correctly.
- Never hard-code colours, spacing, or typography — use \`var(--color-*)\`, \`var(--spacing-*)\`, etc.
${MARKER_END}`;
}

function replaceMarker(content, start, end, replacement) {
  if (content.includes(start)) {
    const s = content.indexOf(start);
    const e = content.indexOf(end) + end.length;
    return content.slice(0, s) + replacement + content.slice(e);
  }
  return content;
}

function buildDocsDirEntry(lib, docsCount) {
  return `${DOCSDIR_START}
${lib.docsDir}/                   ← Active library docs (${docsCount} components — read before writing code)
  INDEX.md
${DOCSDIR_END}`;
}

function updateClaudeMd(lib, docsCount) {
  const filePath = path.join(ROOT, 'CLAUDE.md');
  if (!fs.existsSync(filePath)) {
    console.warn('⚠  CLAUDE.md not found — skipping update.');
    return;
  }

  let content = fs.readFileSync(filePath, 'utf8');

  // Update active library section
  const section = buildLibrarySection(lib, docsCount);
  if (content.includes(MARKER_START)) {
    content = replaceMarker(content, MARKER_START, MARKER_END, section);
  } else {
    content = content.trimEnd() + '\n\n---\n\n' + section + '\n';
  }

  // Update docs directory entry inside the file map
  const docsDirEntry = buildDocsDirEntry(lib, docsCount);
  if (content.includes(DOCSDIR_START)) {
    content = replaceMarker(content, DOCSDIR_START, DOCSDIR_END, docsDirEntry);
  }

  fs.writeFileSync(filePath, content, 'utf8');
  console.log('✓  Updated CLAUDE.md (active library + file map).');
}

/* ─── AGENTS.md writer ───────────────────────────────────────────────────── */

function writeAgentsMd(lib, docsCount) {
  const classRows = Object.entries(lib.classMap)
    .map(([cls, comp]) => `| \`${cls}\` | \`${comp}\` |`)
    .join('\n');

  const content = `# AI Design System — Agent Instructions

> **Active library: ${lib.name} ${lib.version}**
> Component docs: \`${lib.docsDir}/\` · Adapter: \`${lib.adapterCss}\`
> Switch library: \`npm run docs -- --library=<shadcn|antdesign|mui>\`
> This file is auto-maintained — do not edit the "Active library" section manually.

---

## Project overview

An LLM-ready CSS design system built on a three-layer custom property
architecture. Provides a complete token layer, component CSS utilities,
LLM-readable specs, and adapter bridges for popular component libraries.

Key capabilities:
- Token-first CSS with semantic aliases (\`--color-*\`, \`--spacing-*\`, etc.)
- Component CSS: button, card, input, badge, alert, typography
- Library adapters: shadcn/ui, Ant Design, Material UI, custom
- CI-ready token audit script

---

## Non-negotiable rules

1. **Tokens only in component CSS.** Use \`var(--color-*)\`, \`var(--spacing-*)\`,
   \`var(--text-*)\`, \`var(--radius-*)\`. Never raw \`px\`, \`#hex\`, or \`--prim-*\`.
2. **Read component docs before writing code.** Check \`${lib.docsDir}/{component}.md\`
   for ${lib.name}-specific usage, then \`specs/components/\` for AI DS class names.
3. **Read specs before writing CSS.** Check \`specs/tokens/token-reference.md\` first.
4. **Audit must pass.** Run \`npm run audit\` before every commit. Exit 0 required.
5. **Adapter files are exempt** from the token audit (\`lib-adapters/\` is skipped).

---

## Token architecture

\`\`\`
Layer 1  --prim-*        Raw values in tokens.css only. Never use in components.
Layer 2  --color-*       Semantic aliases. ALL component CSS uses only these.
         --spacing-*
         --text-*              --color-text: var(--ds-text, var(--prim-neutral-900))
         --radius-*
         --shadow-*     Each Layer 2 token has a --ds-* upstream hook + prim fallback.
         --font-*
Layer 3  src/ CSS        References Layer 2 exclusively.
\`\`\`

---

## Before writing any CSS

1. Read \`specs/tokens/token-reference.md\` — master token map.
2. Read the relevant \`specs/foundations/\` file for the property type.
3. Read \`specs/components/{name}.md\` if modifying an AI DS component.

---

## Running the audit

\`\`\`bash
npm run audit        # scan all CSS
npm run audit:src    # scan src/ only
\`\`\`

**Exit 0** = clean. **Exit 1** = errors; fix before committing.

---

## File map

\`\`\`
tokens.css                     ← Layer 1 + Layer 2 tokens (source of truth)
${lib.docsDir}/                        ← Active library docs (${docsCount} components)
  INDEX.md                     ← Component list — start here
  {component}.md               ← Per-component: import, props, DS token mapping
src/
  base/reset.css               ← CSS reset
  base/typography.css          ← .heading-*, .text-*, .prose, .code-inline
  components/button.css        ← .btn, .btn-primary, .btn-secondary, .btn-ghost …
  components/card.css          ← .card, .card-header, .card-body, .card-footer …
  components/input.css         ← .input, .select, .checkbox, .field …
  components/badge.css         ← .badge, .badge-success, .badge-count …
  components/alert.css         ← .alert, .alert-danger, .alert-toast …
lib-adapters/
  ${lib.adapterCss.replace('lib-adapters/', '')}${' '.repeat(Math.max(1, 30 - lib.adapterCss.replace('lib-adapters/', '').length))}← Active adapter (${lib.name} → --ds-*)
  component-map.js             ← Cross-library component equivalence
  index.js                     ← detectLibrary, applyAdapter, createAdapter
specs/
  tokens/token-reference.md    ← Every token, its value and purpose
  foundations/                 ← color, spacing, typography, radius, elevation, motion
  components/                  ← Per-component anatomy, API, token table, examples
  adapters/${lib.adapterSpec.replace('specs/adapters/', '')}${' '.repeat(Math.max(1, 24 - lib.adapterSpec.replace('specs/adapters/', '').length))}← Active adapter setup guide
scripts/
  build-docs.js                ← Switch active library (npm run docs:shadcn etc.)
  token-audit.js               ← CI audit script
\`\`\`

---

${buildLibrarySection(lib, docsCount)}
`;

  const filePath = path.join(ROOT, 'AGENTS.md');
  fs.writeFileSync(filePath, content, 'utf8');
  console.log('✓  Wrote AGENTS.md.');
}

/* ─── Library config writer ──────────────────────────────────────────────── */

function writeLibraryConfig(libKey, lib) {
  const config = {
    library:    libKey,
    name:       lib.name,
    version:    lib.version,
    docsDir:    lib.docsDir,
    adapterCss: lib.adapterCss,
  };
  const configPath = path.join(ROOT, 'ds.config.json');
  fs.writeFileSync(configPath, JSON.stringify(config, null, 2) + '\n', 'utf8');
  console.log('✓  Wrote ds.config.json.');
}

/* ─── Doc count helper ───────────────────────────────────────────────────── */

function countDocs(docsDir) {
  const full = path.join(ROOT, docsDir);
  if (!fs.existsSync(full)) return 0;
  return fs.readdirSync(full).filter(f => f.endsWith('.md') && f !== 'INDEX.md').length;
}

/* ─── Main ───────────────────────────────────────────────────────────────── */

function main() {
  const { library: libKey, force } = parseArgs();

  if (!libKey) {
    console.error('Usage: node scripts/build-docs.js --library=<shadcn|antdesign|mui|vanilla>');
    console.error('       node scripts/build-docs.js --library=vanilla --force');
    process.exit(1);
  }

  const lib = LIBRARIES[libKey];
  if (!lib) {
    console.error(`Unknown library "${libKey}". Supported: ${Object.keys(LIBRARIES).join(', ')}`);
    process.exit(1);
  }

  const isNodeScraper = lib.scraper.endsWith('.js');
  const docsIndex     = path.join(ROOT, lib.docsDir, 'INDEX.md');
  const docsExist     = fs.existsSync(docsIndex);

  if (docsExist && !force) {
    console.log(`✓  ${lib.name} docs already exist in ${lib.docsDir}/ (use --force to regenerate).`);
  } else {
    const python = isNodeScraper ? null : findPython();
    if (!isNodeScraper && !python) {
      console.error('✗  Python 3 not found. Install Python 3 to run the scraper.');
      process.exit(1);
    }
    runScraper(lib, python);
  }

  const docsCount = countDocs(lib.docsDir);

  updateClaudeMd(lib, docsCount);
  writeAgentsMd(lib, docsCount);
  writeLibraryConfig(libKey, lib);

  console.log(`\n✅  Done. Active library set to ${lib.name} ${lib.version}.`);
  console.log(`   Component docs: ${lib.docsDir}/ (${docsCount} files)`);
  console.log(`   Adapter:        ${lib.adapterCss}`);
  console.log(`   Agent configs:  CLAUDE.md, AGENTS.md\n`);
}

main();
