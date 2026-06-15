#!/usr/bin/env node
/**
 * token-audit.js
 *
 * Scans CSS/SCSS files for hardcoded design values and suggests token
 * replacements. Exits with code 1 when errors are present (CI-ready).
 *
 * Errors   — must be fixed before commit:
 *   colors (hex, rgb, rgba, hsl, hsla), spacing/sizing (px/rem on
 *   layout properties), font-size, font-weight, border-radius, box-shadow
 *
 * Warnings — should be reviewed:
 *   z-index numbers, transition/animation durations
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

function checkLine(rawLine, lineNum, filePath) {
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

function auditFile(filePath) {
  const content = fs.readFileSync(filePath, 'utf-8');
  const lines   = content.split('\n');
  const results = [];
  for (let i = 0; i < lines.length; i++) {
    results.push(...checkLine(lines[i], i + 1, filePath));
  }
  return results;
}

/* ── Main ────────────────────────────────────────────────────────── */

function main() {
  const rootDir = path.resolve(process.argv[2] || process.cwd());
  const files   = findCssFiles(rootDir).sort();

  const pad = n => String(n).padStart(String(files.length).length);
  console.log(`\n🔍  Token Audit`);
  console.log(`    Root: ${rootDir}`);
  console.log(`    Files scanned: ${files.length}\n`);

  if (files.length === 0) {
    console.log('No CSS files found.\n');
    process.exit(0);
  }

  let totalErrors   = 0;
  let totalWarnings = 0;
  const dirtyFiles  = [];

  for (const file of files) {
    const violations = auditFile(file);
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
