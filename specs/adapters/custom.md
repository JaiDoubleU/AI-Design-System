# Custom Adapter Guide

Use this guide to connect any design system, brand token set, or in-house
component library to the AI Design System.

---

## Option A — CSS file (static, build-time)

Create a CSS file that maps your library's CSS variables to `--ds-*`:

```css
/* my-brand-adapter.css */
:root {
  /* ── Text ─────────────────────────────────────────────── */
  --ds-text:               var(--brand-color-text-default);
  --ds-text-subtle:        var(--brand-color-text-secondary);
  --ds-text-inverse:       var(--brand-color-text-on-fill);
  --ds-text-danger:        var(--brand-color-text-error);
  --ds-text-success:       var(--brand-color-text-success);

  /* ── Backgrounds ──────────────────────────────────────── */
  --ds-bg:                 var(--brand-color-surface-default);
  --ds-bg-subtle:          var(--brand-color-surface-raised);
  --ds-bg-muted:           var(--brand-color-surface-sunken);

  /* ── Interactive ──────────────────────────────────────── */
  --ds-interactive:        var(--brand-color-action-default);
  --ds-interactive-hover:  var(--brand-color-action-hover);
  --ds-interactive-fg:     var(--brand-color-action-fg);
  --ds-interactive-danger: var(--brand-color-action-danger);

  /* ── Borders ──────────────────────────────────────────── */
  --ds-border:             var(--brand-color-border-default);
  --ds-border-focus:       var(--brand-color-border-focus);

  /* ── Radius ───────────────────────────────────────────── */
  --ds-radius-sm:          var(--brand-radius-sm);
  --ds-radius-md:          var(--brand-radius-md);
  --ds-radius-lg:          var(--brand-radius-lg);

  /* ── Typography ───────────────────────────────────────── */
  --ds-font-sans:          var(--brand-font-body);
  --ds-font-mono:          var(--brand-font-code);
}
```

Import order:

```css
@import 'my-library/styles.css';      /* defines --brand-* */
@import './my-brand-adapter.css';     /* maps --brand-* → --ds-* */
@import 'ai-design-system/tokens.css'; /* resolves --ds-* or --prim-* */
```

---

## Option B — JavaScript utility (runtime)

Use `createAdapter` for programmatic mapping, useful when variables are
injected dynamically (e.g., after a login that sets a tenant theme).

```js
import { createAdapter } from 'ai-design-system/lib-adapters';

const myAdapter = createAdapter({
  '--ds-text':               '--brand-color-text-default',
  '--ds-text-subtle':        '--brand-color-text-secondary',
  '--ds-bg':                 '--brand-color-surface-default',
  '--ds-interactive':        '--brand-color-action-default',
  '--ds-interactive-hover':  '--brand-color-action-hover',
  '--ds-interactive-fg':     '--brand-color-action-fg',
  '--ds-border':             '--brand-color-border-default',
  '--ds-border-focus':       '--brand-color-border-focus',
  '--ds-radius-md':          '--brand-radius-md',
  '--ds-font-sans':          '--brand-font-body',
});

// Apply to :root (default)
myAdapter();

// Or target a specific element for scoped theming
myAdapter(document.querySelector('#tenant-portal'));
```

---

## Option C — Direct `--ds-*` values (no source library)

If you have no upstream library and want to set values directly:

```css
:root {
  --ds-text:               #1a1a2e;
  --ds-bg:                 #f8fafc;
  --ds-interactive:        #6366f1;
  --ds-interactive-hover:  #4f46e5;
  --ds-interactive-fg:     #ffffff;
  --ds-border:             #e2e8f0;
  --ds-border-focus:       #6366f1;
  --ds-radius-md:          6px;
  --ds-font-sans:          'Inter', ui-sans-serif, system-ui, sans-serif;
}
```

Note: the token audit script allows hardcoded values in adapter files
(in `lib-adapters/`) since these are intentional bridge values, not
component-level violations.

---

## Scoped theming (multi-tenant / embedded)

The adapter can target any element, not just `:root`. This lets you scope a
theme to a specific section of the page:

```css
/* CSS-only scoped adapter */
.tenant-a {
  --ds-interactive: var(--tenant-a-brand-color);
  --ds-font-sans:   var(--tenant-a-font);
}

.tenant-b {
  --ds-interactive: var(--tenant-b-brand-color);
  --ds-font-sans:   var(--tenant-b-font);
}
```

```js
// JS scoped adapter
const adapterA = createAdapter({ '--ds-interactive': '--tenant-a-brand-color' });
adapterA(document.querySelector('.tenant-a'));
```

All child components inherit the scoped `--ds-*` values.

---

## Full `--ds-*` reference

| Variable | Controls | Default (from tokens.css) |
|---|---|---|
| `--ds-text` | Body text colour | `--prim-neutral-900` |
| `--ds-text-subtle` | Secondary text | `--prim-neutral-600` |
| `--ds-text-muted` | Tertiary/disabled text | `--prim-neutral-400` |
| `--ds-text-inverse` | Text on dark fills | `--prim-neutral-0` (white) |
| `--ds-text-danger` | Error text | `--prim-red-700` |
| `--ds-text-success` | Success text | `--prim-green-700` |
| `--ds-text-warning` | Warning text | `--prim-yellow-800` |
| `--ds-text-info` | Info text | `--prim-blue-700` |
| `--ds-bg` | Page background | `--prim-neutral-0` |
| `--ds-bg-subtle` | Receded surface | `--prim-neutral-50` |
| `--ds-bg-muted` | Chip/tag background | `--prim-neutral-100` |
| `--ds-bg-emphasis` | Dark fill surface | `--prim-neutral-900` |
| `--ds-bg-success` | Success tint | `--prim-green-50` |
| `--ds-bg-warning` | Warning tint | `--prim-yellow-50` |
| `--ds-bg-danger` | Danger tint | `--prim-red-50` |
| `--ds-bg-info` | Info tint | `--prim-blue-50` |
| `--ds-interactive` | Primary action fill | `--prim-blue-500` |
| `--ds-interactive-hover` | Hover state | `--prim-blue-600` |
| `--ds-interactive-active` | Active/pressed | `--prim-blue-700` |
| `--ds-interactive-muted` | Subtle tint | `--prim-blue-50` |
| `--ds-interactive-fg` | Text on primary fill | `--prim-neutral-0` |
| `--ds-interactive-danger` | Destructive action | `--prim-red-600` |
| `--ds-border` | Default border | `--prim-neutral-200` |
| `--ds-border-subtle` | Lighter border | `--prim-neutral-100` |
| `--ds-border-emphasis` | Stronger border | `--prim-neutral-400` |
| `--ds-border-focus` | Focus ring | `--prim-blue-500` |
| `--ds-border-success` | Success border | `--prim-green-300` |
| `--ds-border-danger` | Danger border | `--prim-red-300` |
| `--ds-radius-none` | Square | `0px` |
| `--ds-radius-sm` | Small radius | `--prim-radius-sm` |
| `--ds-radius-md` | Medium radius | `--prim-radius-md` |
| `--ds-radius-lg` | Large radius | `--prim-radius-lg` |
| `--ds-radius-xl` | Extra-large radius | `--prim-radius-xl` |
| `--ds-radius-full` | Pill / circle | `9999px` |
| `--ds-font-sans` | Sans-serif stack | `--prim-font-sans` |
| `--ds-font-mono` | Monospace stack | `--prim-font-mono` |
| `--ds-font-serif` | Serif stack | `--prim-font-serif` |
| `--ds-shadow-sm` | Subtle shadow | `--prim-shadow-sm` |
| `--ds-shadow-md` | Medium shadow | `--prim-shadow-md` |
| `--ds-shadow-lg` | Large shadow | `--prim-shadow-lg` |
