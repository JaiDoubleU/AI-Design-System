/**
 * AI Design System — multi-library adapter utility
 *
 * Usage (browser / bundler):
 *   import { applyAdapter, detectLibrary } from 'ai-design-system/lib-adapters';
 *   applyAdapter('shadcn');               // explicit
 *   applyAdapter(detectLibrary());        // auto-detect from loaded CSS vars
 *
 * Usage (Node / build scripts):
 *   const { getComponentMap } = require('ai-design-system/lib-adapters');
 *   const map = getComponentMap('shadcn');
 *
 * CSS-only approach (no JS required):
 *   Import the relevant CSS adapter before tokens.css. See each .css file.
 */

export { COMPONENT_MAP, getComponentInfo, getConceptsForLibrary } from './component-map.js';

/* ─────────────────────────────────────────────────────────────────────────
   Supported libraries
───────────────────────────────────────────────────────────────────────── */

const SUPPORTED_LIBRARIES = ['shadcn', 'antDesign', 'materialUI'];

/* ─────────────────────────────────────────────────────────────────────────
   detectLibrary()
   Inspects loaded CSS variables to guess which library is active.
   Returns the library name or null if detection fails.
───────────────────────────────────────────────────────────────────────── */

export function detectLibrary() {
  if (typeof getComputedStyle === 'undefined') return null;
  const style = getComputedStyle(document.documentElement);

  const hasVar = (name) => style.getPropertyValue(name).trim() !== '';

  if (hasVar('--ant-color-primary')) return 'antDesign';
  if (hasVar('--mui-palette-primary-main')) return 'materialUI';
  if (hasVar('--primary') && hasVar('--background') && hasVar('--foreground')) return 'shadcn';

  return null;
}

/* ─────────────────────────────────────────────────────────────────────────
   applyAdapter(library, options?)
   Injects --ds-* CSS variable overrides onto :root at runtime.
   This mirrors what the static CSS adapters do, for cases where
   the library initialises after page load (e.g. MUI CssVarsProvider).

   Options:
     target  — Element to apply variables to (default: document.documentElement)
     verbose — Log applied mappings to console (default: false)
───────────────────────────────────────────────────────────────────────── */

const ADAPTER_FACTORIES = {
  shadcn: buildShadcnMappings,
  antDesign: buildAntDesignMappings,
  materialUI: buildMaterialUIMappings,
};

export function applyAdapter(library, options = {}) {
  if (!library) {
    console.warn('[AI-DS] applyAdapter: no library specified. Call detectLibrary() first.');
    return;
  }
  if (!SUPPORTED_LIBRARIES.includes(library)) {
    throw new Error(`[AI-DS] Unsupported library "${library}". Choose: ${SUPPORTED_LIBRARIES.join(', ')}`);
  }

  const { target = document.documentElement, verbose = false } = options;
  const style = getComputedStyle(target);
  const mappings = ADAPTER_FACTORIES[library](style);

  for (const [dsVar, value] of Object.entries(mappings)) {
    if (value && value !== ' ') {
      target.style.setProperty(dsVar, value);
      if (verbose) console.log(`[AI-DS] ${dsVar} = ${value}`);
    }
  }
}

/* ─────────────────────────────────────────────────────────────────────────
   createAdapter(mappings)
   Build a custom adapter from an arbitrary { '--ds-var': '--source-var' } map.
   Returns an apply(target?) function.

   Example:
     const myAdapter = createAdapter({
       '--ds-interactive': '--my-brand-blue',
       '--ds-text':        '--my-body-color',
     });
     myAdapter(); // applies to :root
───────────────────────────────────────────────────────────────────────── */

export function createAdapter(mappings) {
  return function apply(target = document.documentElement) {
    const style = getComputedStyle(target);
    for (const [dsVar, sourceVar] of Object.entries(mappings)) {
      const value = style.getPropertyValue(sourceVar).trim();
      if (value) target.style.setProperty(dsVar, `var(${sourceVar})`);
    }
  };
}

/* ─────────────────────────────────────────────────────────────────────────
   getComponentMap(library?)
   Returns the cross-library component equivalence data, optionally
   filtered to a single library's info + the design system reference.
───────────────────────────────────────────────────────────────────────── */

export function getComponentMap(library) {
  const { COMPONENT_MAP } = require('./component-map.js');
  if (!library) return COMPONENT_MAP;

  return Object.fromEntries(
    Object.entries(COMPONENT_MAP).map(([concept, data]) => [
      concept,
      {
        description: data.description,
        designSystem: data.designSystem,
        ...(data[library] ? { [library]: data[library] } : {}),
      },
    ])
  );
}

/* ─────────────────────────────────────────────────────────────────────────
   Private mapping builders — mirror the static CSS adapters
───────────────────────────────────────────────────────────────────────── */

function readVar(style, name, fallback = '') {
  return style.getPropertyValue(name).trim() || fallback;
}

function buildShadcnMappings(style) {
  const r = (name, fb) => readVar(style, name, fb);
  return {
    '--ds-text':               `var(--foreground)`,
    '--ds-text-subtle':        `var(--muted-foreground)`,
    '--ds-text-muted':         `var(--muted-foreground)`,
    '--ds-text-inverse':       `var(--primary-foreground)`,
    '--ds-text-danger':        `var(--destructive)`,
    '--ds-bg':                 `var(--background)`,
    '--ds-bg-subtle':          `var(--muted)`,
    '--ds-bg-muted':           `var(--muted)`,
    '--ds-interactive':        `hsl(var(--primary))`,
    '--ds-interactive-hover':  `hsl(var(--primary) / 0.9)`,
    '--ds-interactive-active': `hsl(var(--primary) / 0.8)`,
    '--ds-interactive-muted':  `hsl(var(--primary) / 0.1)`,
    '--ds-interactive-fg':     `var(--primary-foreground)`,
    '--ds-interactive-danger': `hsl(var(--destructive))`,
    '--ds-border':             `var(--border)`,
    '--ds-border-focus':       `var(--ring)`,
    '--ds-radius-sm':          `calc(var(--radius) - 4px)`,
    '--ds-radius-md':          `calc(var(--radius) - 2px)`,
    '--ds-radius-lg':          `var(--radius)`,
    '--ds-radius-xl':          `calc(var(--radius) + 4px)`,
    '--ds-font-sans':          `var(--font-sans, ui-sans-serif, system-ui, sans-serif)`,
    '--ds-font-mono':          `var(--font-mono, ui-monospace, monospace)`,
  };
}

function buildAntDesignMappings(style) {
  return {
    '--ds-text':               `var(--ant-color-text)`,
    '--ds-text-subtle':        `var(--ant-color-text-secondary)`,
    '--ds-text-muted':         `var(--ant-color-text-quaternary)`,
    '--ds-text-inverse':       `var(--ant-color-text-light-solid, #fff)`,
    '--ds-text-danger':        `var(--ant-color-error-text)`,
    '--ds-text-success':       `var(--ant-color-success-text)`,
    '--ds-text-warning':       `var(--ant-color-warning-text)`,
    '--ds-text-info':          `var(--ant-color-info-text)`,
    '--ds-bg':                 `var(--ant-color-bg-base)`,
    '--ds-bg-subtle':          `var(--ant-color-bg-layout)`,
    '--ds-bg-muted':           `var(--ant-color-fill-quaternary)`,
    '--ds-bg-success':         `var(--ant-color-success-bg)`,
    '--ds-bg-warning':         `var(--ant-color-warning-bg)`,
    '--ds-bg-danger':          `var(--ant-color-error-bg)`,
    '--ds-bg-info':            `var(--ant-color-info-bg)`,
    '--ds-interactive':        `var(--ant-color-primary)`,
    '--ds-interactive-hover':  `var(--ant-color-primary-hover)`,
    '--ds-interactive-active': `var(--ant-color-primary-active)`,
    '--ds-interactive-muted':  `var(--ant-color-primary-bg)`,
    '--ds-interactive-fg':     `var(--ant-color-text-light-solid, #fff)`,
    '--ds-interactive-danger': `var(--ant-color-error)`,
    '--ds-border':             `var(--ant-color-border)`,
    '--ds-border-subtle':      `var(--ant-color-border-secondary)`,
    '--ds-border-focus':       `var(--ant-color-primary-border-hover)`,
    '--ds-radius-sm':          `var(--ant-border-radius-sm)`,
    '--ds-radius-md':          `var(--ant-border-radius)`,
    '--ds-radius-lg':          `var(--ant-border-radius-lg)`,
    '--ds-radius-xl':          `var(--ant-border-radius-xl)`,
    '--ds-font-sans':          `var(--ant-font-family)`,
    '--ds-font-mono':          `var(--ant-font-family-code)`,
  };
}

function buildMaterialUIMappings(style) {
  return {
    '--ds-text':               `var(--mui-palette-text-primary)`,
    '--ds-text-subtle':        `var(--mui-palette-text-secondary)`,
    '--ds-text-muted':         `var(--mui-palette-text-disabled)`,
    '--ds-text-inverse':       `var(--mui-palette-primary-contrastText)`,
    '--ds-text-danger':        `var(--mui-palette-error-main)`,
    '--ds-text-success':       `var(--mui-palette-success-main)`,
    '--ds-text-warning':       `var(--mui-palette-warning-main)`,
    '--ds-text-info':          `var(--mui-palette-info-main)`,
    '--ds-bg':                 `var(--mui-palette-background-default)`,
    '--ds-bg-subtle':          `var(--mui-palette-background-paper)`,
    '--ds-bg-muted':           `var(--mui-palette-action-hover)`,
    '--ds-interactive':        `var(--mui-palette-primary-main)`,
    '--ds-interactive-hover':  `var(--mui-palette-primary-dark)`,
    '--ds-interactive-active': `var(--mui-palette-primary-dark)`,
    '--ds-interactive-muted':  `var(--mui-palette-primary-light)`,
    '--ds-interactive-fg':     `var(--mui-palette-primary-contrastText)`,
    '--ds-interactive-danger': `var(--mui-palette-error-main)`,
    '--ds-border':             `var(--mui-palette-divider)`,
    '--ds-border-focus':       `var(--mui-palette-primary-main)`,
    '--ds-radius-sm':          `calc(var(--mui-shape-borderRadius) * 0.5px)`,
    '--ds-radius-md':          `calc(var(--mui-shape-borderRadius) * 1px)`,
    '--ds-radius-lg':          `calc(var(--mui-shape-borderRadius) * 1.5px)`,
    '--ds-radius-xl':          `calc(var(--mui-shape-borderRadius) * 2px)`,
    '--ds-font-sans':          `var(--mui-font-family, "Roboto","Helvetica","Arial",sans-serif)`,
    '--ds-font-mono':          `'Roboto Mono', ui-monospace, monospace`,
  };
}
