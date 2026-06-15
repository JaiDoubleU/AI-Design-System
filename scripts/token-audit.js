#!/usr/bin/env node
/**
 * token-audit.js
 *
 * Scans CSS/SCSS files for hardcoded design values and suggests token
 * replacements. Exits with code 1 when errors are present (CI-ready).
 *
 * When ds.config.json is present (written by `npm run docs`) the audit
 * also checks for layer violations:
 *   - var(--prim-*) in component CSS  → always an error
 *   - var(--ds-*)   in component CSS  → always an error
 *   - Direct library variable usage   → warning (shadcn globals, --ant-*, --mui-*)
 *
 * Errors   — must be fixed before commit:
 *   colors (hex, rgb, rgba, hsl, hsla), spacing/sizing (px/rem on
 *   layout properties), font-size, font-weight, border-radius, box-shadow,
 *   layer violations (--prim-* / --ds-* in component CSS)
 *
 * Warnings — should be reviewed:
 *   z-index numbers, transition/animation durations,
 *   direct library variable bypass (--ant-*, --mui-*, shadcn globals)
 *
 * Usage:
 *   node scripts/token-audit.js [directory]   # defaults to cwd
 *   npm run audit
 */

'use strict';

const fs   = require('fs');
const path = require('path');

/* ── Skip lists ─────────────────────────────────────────────────── */

// These files are allowed to contain raw values (primitive layer).
const SKIP_FILES = new Set(['tokens.css', 'reset.css']);

// These directories are never scanned.
const SKIP_DIRS = new Set([
  'node_modules', '.git', 'scripts', 'specs', 'dist', 'build',
  '.cache', 'coverage', 'lib-adapters',
]);

/* ── Token suggestion maps ───────────────────────────────────────── */

const COLOR_MAP = {
  '#ffffff': '--color-bg',        '#fff': '--color-bg',
  '#f8f9fa': '--color-bg-subtle',
  '#f1f3f5': '--color-bg-muted',
  '#e9ecef': '--color-border-subtle',
  '#dee2e6': '--color-border',
  '#ced4da': '--color-border-emphasis',
  '#adb5bd': '--color-text-disabled',
  '#868e96': '--color-text-muted',
  '#495057': '--color-text-subtle',
  '#343a40': '--color-text',
  '#212529': '--color-text',
  '#000000': '--color-bg-inverse', '#000': '--color-bg-inverse',
  '#e8f4fd': '--color-interactive-muted',
  '#3182ce': '--color-interactive',
  '#2b6cb0': '--color-interactive-hover',
  '#2c5282': '--color-interactive-active',
  '#e53e3e': '--color-interactive-danger',
  '#c53030': '--color-interactive-danger-hover',
  '#fff5f5': '--color-bg-danger',
  '#38a169': '--color-text-success',
  '#f0fff4': '--color-bg-success',
  '#d69e2e': '--color-text-warning',
  '#fffff0': '--color-bg-warning',
  '#4299e1': '--color-interactive',
  '#bee3f8': '--color-bg-info',
};

const SPACING_MAP = {
  '4px': '--spacing-1',   '0.25rem': '--spacing-1',
  '8px': '--spacing-2',   '0.5rem':  '--spacing-2',
  '12px': '--spacing-3',  '0.75rem': '--spacing-3',
  '16px': '--spacing-4',  '1rem':    '--spacing-4',
  '20px': '--spacing-5',  '1.25rem': '--spacing-5',
  '24px': '--spacing-6',  '1.5rem':  '--spacing-6',
  '32px': '--spacing-8',  '2rem':    '--spacing-8',
  '40px': '--spacing-10', '2.5rem':  '--spacing-10',
  '48px': '--spacing-12', '3rem':    '--spacing-12',
  '64px': '--spacing-16', '4rem':    '--spacing-16',
  '80px': '--spacing-20', '5rem':    '--spacing-20',
  '96px': '--spacing-24', '6rem':    '--spacing-24',
};

const FONT_SIZE_MAP = {
  '12px': '--text-xs',  '0.75rem':  '--text-xs',
  '14px': '--text-sm',  '0.875rem': '--text-sm',
  '16px': '--text-md',  '1rem':     '--text-md',
  '18px': '--text-lg',  '1.125rem': '--text-lg',
  '20px': '--text-xl',  '1.25rem':  '--text-xl',
  '24px': '--text-2xl', '1.5rem':   '--text-2xl',
  '30px': '--text-3xl', '1.875rem': '--text-3xl',
  '36px': '--text-4xl', '2.25rem':  '--text-4xl',
  '48px': '--text-5xl', '3rem':     '--text-5xl',
};

const RADIUS_MAP = {
  '2px':    '--radius-sm',
  '4px':    '--radius-md',
  '8px':    '--radius-lg',
  '12px':   '--radius-xl',
  '16px':   '--radius-2xl',
  '9999px': '--radius-full',
};

const DURATION_MAP = {
  '0ms':   '--motion-instant',
  '150ms': '--motion-fast',
  '250ms': '--motion-normal',
  '400ms': '--motion-slow',
  '600ms': '--motion-slower',
  '0.15s': '--motion-fast',
  '0.25s': '--motion-normal',
  '0.4s':  '--motion-slow',
};

const WEIGHT_MAP = {
  '400': '--weight-normal',
  '500': '--weight-medium',
  '600': '--weight-semibold',
  '700': '--weight-bold',
};

const Z_MAP = {
  '-1':  '--z-below',
  '0':   '--z-base',
  '10':  '--z-raised',
  '100': '--z-dropdown',
  '200': '--z-sticky',
  '300': '--z-overlay',
  '400': '--z-modal',
  '500': '--z-popover',
  '600': '--z-toast',
  '700': '--z-tooltip',
};

/* ── Layer-violation maps ─────────────────────────────────────────── */

// Maps --ds-* internal hooks to their Layer 2 equivalents for suggestions.
const DS_TO_LAYER2 = {
  '--ds-text':               '--color-text',
  '--ds-text-subtle':        '--color-text-subtle',
  '--ds-text-muted':         '--color-text-muted',
  '--ds-text-inverse':       '--color-text-inverse',
  '--ds-text-danger':        '--color-text-danger',
  '--ds-text-success':       '--color-text-success',
  '--ds-text-warning':       '--color-text-warning',
  '--ds-text-info':          '--color-text-info',
  '--ds-bg':                 '--color-bg',
  '--ds-bg-subtle':          '--color-bg-subtle',
  '--ds-bg-muted':           '--color-bg-muted',
  '--ds-bg-emphasis':        '--color-bg-emphasis',
  '--ds-bg-success':         '--color-bg-success',
  '--ds-bg-warning':         '--color-bg-warning',
  '--ds-bg-danger':          '--color-bg-danger',
  '--ds-bg-info':            '--color-bg-info',
  '--ds-interactive':        '--color-interactive',
  '--ds-interactive-hover':  '--color-interactive-hover',
  '--ds-interactive-active': '--color-interactive-active',
  '--ds-interactive-muted':  '--color-interactive-muted',
  '--ds-interactive-fg':     '--color-interactive-fg',
  '--ds-interactive-danger': '--color-interactive-danger',
  '--ds-border':             '--color-border',
  '--ds-border-subtle':      '--color-border-subtle',
  '--ds-border-emphasis':    '--color-border-emphasis',
  '--ds-border-focus':       '--color-border-focus',
  '--ds-border-success':     '--color-border-success',
  '--ds-border-danger':      '--color-border-danger',
  '--ds-radius-sm':          '--radius-sm',
  '--ds-radius-md':          '--radius-md',
  '--ds-radius-lg':          '--radius-lg',
  '--ds-radius-xl':          '--radius-xl',
  '--ds-radius-full':        '--radius-full',
  '--ds-radius-none':        '--radius-none',
  '--ds-font-sans':          '--font-sans',
  '--ds-font-mono':          '--font-mono',
  '--ds-font-serif':         '--font-serif',
  '--ds-shadow-sm':          '--shadow-sm',
  '--ds-shadow-md':          '--shadow-md',
  '--ds-shadow-lg':          '--shadow-lg',
};

// Per-library patterns that flag direct use of upstream library variables in
// component CSS. Component CSS must go through the Layer 2 token chain, not
// reach past the adapter into the library's own variables.
const LIBRARY_VAR_PATTERNS = {
  shadcn: {
    // shadcn/ui v4 globals.css — bare variable names exposed by the library.
    // Use a lookahead so "--primary-color" doesn't match "--primary".
    patternSource: 'var\\(--(background|foreground|card|card-foreground|popover|popover-foreground|primary|primary-foreground|secondary|secondary-foreground|muted|muted-foreground|accent|accent-foreground|destructive|destructive-foreground|border|input|ring|radius|chart-\\d+)(?=[,)\\s/])',
    flags: 'g',
    label: 'shadcn/ui global variable',
    hint: 'Route through the adapter — use var(--color-*) or another Layer 2 token',
  },
  antdesign: {
    patternSource: 'var\\(--ant-[a-z][^)]*\\)',
    flags: 'g',
    label: 'Ant Design CSS variable',
    hint: 'Route through the adapter — use var(--color-*) or another Layer 2 token',
  },
  mui: {
    patternSource: 'var\\(--mui-[a-z][^)]*\\)',
    flags: 'g',
    label: 'Material UI CSS variable',
    hint: 'Route through the adapter — use var(--color-*) or another Layer 2 token',
  },
  vanilla: null, // no upstream library variables to flag
};

/* ── Library config loader ───────────────────────────────────────── */

function loadLibraryConfig(rootDir) {
  // Walk up from rootDir (and also try process.cwd()) to find ds.config.json.
  // This ensures `npm run audit:src` (scanning src/) finds the config at project root.
  const candidates = new Set([
    rootDir,
    process.cwd(),
  ]);
  let dir = rootDir;
  while (true) {
    candidates.add(dir);
    const parent = path.dirname(dir);
    if (parent === dir) break;
    dir = parent;
  }
  for (const candidate of candidates) {
    const configPath = path.join(candidate, 'ds.config.json');
    if (fs.existsSync(configPath)) {
      try { return JSON.parse(fs.readFileSync(configPath, 'utf8')); }
      catch { return null; }
    }
  }
  return null;
}

/* ── Utilities ───────────────────────────────────────────────────── */

function findCssFiles(dir) {
  const results = [];
  let entries;
  try { entries = fs.readdirSync(dir, { withFileTypes: true }); }
  catch { return results; }

  for (const entry of entries) {
    if (SKIP_DIRS.has(entry.name)) continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      results.push(...findCssFiles(full));
    } else if (/\.s?css$/.test(entry.name) && !SKIP_FILES.has(entry.name)) {
      results.push(full);
    }
  }
  return results;
}

function isCommentLine(line) {
  const t = line.trim();
  return t.startsWith('/*') || t.startsWith('*') || t.startsWith('//');
}

function stripInlineComment(line) {
  return line.replace(/\/\*.*?\*\//g, '').replace(/\/\/.*$/, '');
}

/**
 * Extract { prop, value } from a CSS declaration line.
 * Returns null when the line doesn't look like a declaration.
 */
function parseDeclaration(line) {
  const stripped = stripInlineComment(line).trim();
  const ci = stripped.indexOf(':');
  if (ci === -1) return null;
  const prop  = stripped.slice(0, ci).trim().toLowerCase();
  const value = stripped.slice(ci + 1).replace(/\s*;\s*$/, '').trim();
  // Skip custom-property definitions (--foo: ...)
  if (prop.startsWith('--')) return null;
  if (!prop || !value) return null;
  return { prop, value };
}

/* ── Violation builders ──────────────────────────────────────────── */

function violation(file, lineNum, type, category, message, value, suggestion, context) {
  return { file, line: lineNum, type, category, message, value, suggestion,
           context: context.trim().slice(0, 90) };
}

/* ── Per-line analysis ───────────────────────────────────────────── */

function checkLine(rawLine, lineNum, filePath, libConfig) {
  const results = [];
  if (isCommentLine(rawLine)) return results;

  const stripped = stripInlineComment(rawLine);
  if (!stripped.trim()) return results;

  const decl = parseDeclaration(stripped);

  // If the value already uses a token, skip property-based checks.
  // (Accept the small false-negative for "var(--x) 16px" mixed lines.)
  const valueUsesToken = decl && decl.value.includes('var(--');
  const lineUsesToken  = stripped.includes('var(--');

  /* ── Color checks (run when no token on the line) ──────────────── */
  if (!lineUsesToken) {
    // Hex colors
    const hexRe = /#(?:[0-9a-fA-F]{3,4}|[0-9a-fA-F]{6,8})\b/g;
    let m;
    while ((m = hexRe.exec(stripped)) !== null) {
      const hex = m[0].toLowerCase();
      results.push(violation(
        filePath, lineNum, 'error', 'color',
        'Hardcoded hex color',
        m[0],
        COLOR_MAP[hex] ? `var(${COLOR_MAP[hex]})` : 'var(--color-*)',
        rawLine,
      ));
    }

    // rgb / rgba
    const rgbRe = /rgba?\s*\(\s*[\d.]+/g;
    while ((m = rgbRe.exec(stripped)) !== null) {
      results.push(violation(
        filePath, lineNum, 'error', 'color',
        'Hardcoded rgb/rgba color',
        m[0] + '…)',
        'var(--color-*)',
        rawLine,
      ));
    }

    // hsl / hsla
    const hslRe = /hsla?\s*\(\s*[\d.]+/g;
    while ((m = hslRe.exec(stripped)) !== null) {
      results.push(violation(
        filePath, lineNum, 'error', 'color',
        'Hardcoded hsl/hsla color',
        m[0] + '…)',
        'var(--color-*)',
        rawLine,
      ));
    }
  }

  /* ── Layer violation checks (always run, even when line uses a token) ── */

  // --prim-* in component CSS: direct primitive reference (Layer 1 bypass).
  {
    const primRe = /var\(--prim-([a-zA-Z0-9-]+)/g;
    let m;
    while ((m = primRe.exec(stripped)) !== null) {
      results.push(violation(
        filePath, lineNum, 'error', 'layer',
        'Direct Layer 1 primitive — use a Layer 2 token instead',
        `var(--prim-${m[1]})`,
        'var(--color-*) / var(--spacing-*) / var(--text-*) etc.',
        rawLine,
      ));
    }
  }

  // --ds-* in component CSS: internal adapter hook (should only appear in
  // tokens.css and lib-adapters/, both of which are in skip lists).
  {
    const dsRe = /var\(--ds-([a-zA-Z0-9-]+)/g;
    let m;
    while ((m = dsRe.exec(stripped)) !== null) {
      const dsVar  = `--ds-${m[1]}`;
      const layer2 = DS_TO_LAYER2[dsVar];
      results.push(violation(
        filePath, lineNum, 'error', 'layer',
        'Internal adapter hook in component CSS — use a Layer 2 token',
        `var(${dsVar})`,
        layer2 ? `var(${layer2})` : 'var(--color-*) or another Layer 2 token',
        rawLine,
      ));
    }
  }

  /* ── Library-specific bypass check ────────────────────────────── */
  // Warn when component CSS reaches past the adapter and references the
  // upstream library's own CSS variables directly.
  if (libConfig) {
    const libPattern = LIBRARY_VAR_PATTERNS[libConfig.library];
    if (libPattern) {
      const re = new RegExp(libPattern.patternSource, libPattern.flags);
      let m;
      while ((m = re.exec(stripped)) !== null) {
        results.push(violation(
          filePath, lineNum, 'warning', 'library',
          `Direct ${libPattern.label} — bypasses token layer`,
          m[0],
          libPattern.hint,
          rawLine,
        ));
      }
    }
  }

  /* ── Property-based checks ─────────────────────────────────────── */
  if (!decl || valueUsesToken) return results;
  const { prop, value } = decl;

  /* font-size */
  if (prop === 'font-size') {
    const re = /(\d+(?:\.\d+)?(?:px|rem|em))/g;
    let m;
    while ((m = re.exec(value)) !== null) {
      results.push(violation(
        filePath, lineNum, 'error', 'typography',
        'Hardcoded font-size',
        `font-size: ${m[1]}`,
        FONT_SIZE_MAP[m[1]] ? `var(${FONT_SIZE_MAP[m[1]]})` : 'var(--text-*)',
        rawLine,
      ));
    }
  }

  /* font-weight */
  if (prop === 'font-weight') {
    const v = value.trim();
    if (/^\d{3}$/.test(v)) {
      results.push(violation(
        filePath, lineNum, 'error', 'typography',
        'Hardcoded font-weight',
        `font-weight: ${v}`,
        WEIGHT_MAP[v] ? `var(${WEIGHT_MAP[v]})` : 'var(--weight-*)',
        rawLine,
      ));
    }
  }

  /* line-height */
  if (prop === 'line-height') {
    const v = value.trim();
    // Flag unitless numbers (1.5, 1.2, etc.) — not keywords
    if (/^\d+(?:\.\d+)?$/.test(v)) {
      results.push(violation(
        filePath, lineNum, 'error', 'typography',
        'Hardcoded line-height',
        `line-height: ${v}`,
        'var(--leading-*)',
        rawLine,
      ));
    }
  }

  /* Spacing properties */
  const spacingProps = new Set([
    'padding', 'padding-top', 'padding-right', 'padding-bottom', 'padding-left',
    'margin',  'margin-top',  'margin-right',  'margin-bottom',  'margin-left',
    'gap', 'row-gap', 'column-gap',
    'top', 'right', 'bottom', 'left',
    'width', 'height', 'min-width', 'max-width', 'min-height', 'max-height',
  ]);
  if (spacingProps.has(prop)) {
    const re = /(\d+(?:\.\d+)?(?:px|rem))/g;
    let m;
    while ((m = re.exec(value)) !== null) {
      const v = m[1];
      if (v === '0px' || v === '0rem') continue;
      results.push(violation(
        filePath, lineNum, 'error', 'spacing',
        'Hardcoded spacing/sizing value',
        `${prop}: ${v}`,
        SPACING_MAP[v] ? `var(${SPACING_MAP[v]})` : 'var(--spacing-*)',
        rawLine,
      ));
    }
  }

  /* border-radius */
  if (prop === 'border-radius') {
    const re = /(\d+(?:\.\d+)?px)/g;
    let m;
    while ((m = re.exec(value)) !== null) {
      if (m[1] === '0px') continue;
      results.push(violation(
        filePath, lineNum, 'error', 'radius',
        'Hardcoded border-radius',
        `border-radius: ${m[1]}`,
        RADIUS_MAP[m[1]] ? `var(${RADIUS_MAP[m[1]]})` : 'var(--radius-*)',
        rawLine,
      ));
    }
  }

  /* box-shadow — flag any non-var, non-none shadow */
  if (prop === 'box-shadow') {
    const v = value.trim().toLowerCase();
    if (v !== 'none' && v !== 'inherit' && v !== 'initial' && v !== 'unset') {
      results.push(violation(
        filePath, lineNum, 'error', 'elevation',
        'Hardcoded box-shadow value',
        `box-shadow: ${value.slice(0, 40)}…`,
        'var(--shadow-*)',
        rawLine,
      ));
    }
  }

  /* z-index — warning */
  if (prop === 'z-index') {
    const v = value.trim();
    if (/^-?\d+$/.test(v)) {
      results.push(violation(
        filePath, lineNum, 'warning', 'z-index',
        'Hardcoded z-index',
        `z-index: ${v}`,
        Z_MAP[v] ? `var(${Z_MAP[v]})` : 'var(--z-*)',
        rawLine,
      ));
    }
  }

  /* transition / animation-duration — warning */
  if (prop === 'transition' || prop === 'animation' || prop === 'animation-duration') {
    const re = /(\d+(?:\.\d+)?(?:ms|s))/g;
    let m;
    while ((m = re.exec(value)) !== null) {
      const v = m[1];
      if (v === '0ms' || v === '0s') continue;
      results.push(violation(
        filePath, lineNum, 'warning', 'motion',
        'Hardcoded transition duration',
        v,
        DURATION_MAP[v] ? `var(${DURATION_MAP[v]})` : 'var(--motion-*)',
        rawLine,
      ));
    }
  }

  return results;
}

/* ── File audit ──────────────────────────────────────────────────── */

function auditFile(filePath, libConfig) {
  const content = fs.readFileSync(filePath, 'utf8');
  const lines   = content.split('\n');
  const results = [];
  for (let i = 0; i < lines.length; i++) {
    results.push(...checkLine(lines[i], i + 1, filePath, libConfig));
  }
  return results;
}

/* ── Main ────────────────────────────────────────────────────────── */

function main() {
  const rootDir   = path.resolve(process.argv[2] || process.cwd());
  const libConfig = loadLibraryConfig(rootDir);
  const files     = findCssFiles(rootDir).sort();

  const pad = n => String(n).padStart(String(files.length).length);
  console.log(`\n🔍  Token Audit`);
  console.log(`    Root: ${rootDir}`);
  if (libConfig) {
    console.log(`    Library: ${libConfig.name} ${libConfig.version}  (${libConfig.adapterCss})`);
    const libEntry = LIBRARY_VAR_PATTERNS[libConfig.library];
    if (libEntry) {
      console.log(`    Library check: direct ${libConfig.name} variable usage → warning`);
    }
  } else {
    console.log(`    Library: not detected  (run "npm run docs -- --library=<name>" to enable library checks)`);
  }
  console.log(`    Layer checks: var(--prim-*) and var(--ds-*) in component CSS → error`);
  console.log(`    Files scanned: ${files.length}\n`);

  if (files.length === 0) {
    console.log('No CSS files found.\n');
    process.exit(0);
  }

  let totalErrors   = 0;
  let totalWarnings = 0;
  const dirtyFiles  = [];

  for (const file of files) {
    const violations = auditFile(file, libConfig);
    const errors     = violations.filter(v => v.type === 'error');
    const warnings   = violations.filter(v => v.type === 'warning');
    totalErrors   += errors.length;
    totalWarnings += warnings.length;
    if (violations.length > 0) dirtyFiles.push({ file, violations });
  }

  for (const { file, violations } of dirtyFiles) {
    const rel    = path.relative(rootDir, file);
    const errCnt = violations.filter(v => v.type === 'error').length;
    const wrnCnt = violations.filter(v => v.type === 'warning').length;
    console.log(`📄  ${rel}  (${errCnt} error${errCnt !== 1 ? 's' : ''}, ${wrnCnt} warning${wrnCnt !== 1 ? 's' : ''})`);

    for (const v of violations) {
      const icon  = v.type === 'error' ? '  ✖' : '  ⚠';
      const label = (v.type === 'error' ? 'ERROR  ' : 'WARNING').padEnd(7);
      console.log(`${icon}  ${label} [${v.category}] line ${v.line}: ${v.message}`);
      console.log(`        Value:   ${v.value}`);
      console.log(`        Fix:     ${v.suggestion}`);
      console.log(`        Context: ${v.context}`);
    }
    console.log('');
  }

  const line = '─'.repeat(60);
  console.log(line);

  if (totalErrors === 0 && totalWarnings === 0) {
    console.log(`✅  ${files.length} file(s) audited — zero violations.\n`);
    process.exit(0);
  }

  const summary = `${totalErrors} error(s)  ${totalWarnings} warning(s)  across ${dirtyFiles.length} file(s)`;

  if (totalErrors === 0) {
    console.log(`⚠   ${summary}`);
    console.log('    Warnings found — review and replace with tokens where possible.\n');
    process.exit(0);
  }

  console.log(`✖   ${summary}`);
  console.log('    Replace all errors with token references before committing.\n');
  process.exit(1);
}

main();
