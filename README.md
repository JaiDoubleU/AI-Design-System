# AI Design System

An LLM-ready design system built on a three-layer CSS custom property
architecture. Works standalone or as a token bridge over shadcn/ui, Ant Design,
or Material UI — no component CSS changes required.

---

## Contents

- [What this is](#what-this-is)
- [Repository structure](#repository-structure)
- [Quick start](#quick-start)
- [Token architecture](#token-architecture)
- [Using the component CSS](#using-the-component-css)
- [Multi-library adapter system](#multi-library-adapter-system)
  - [shadcn/ui](#shadcnui)
  - [Ant Design](#ant-design)
  - [Material UI](#material-ui)
  - [Custom / in-house library](#custom--in-house-library)
- [Token audit (CI)](#token-audit-ci)
- [Specs and documentation](#specs-and-documentation)
- [shadcn/ui component docs](#shadcnui-component-docs)
- [Writing new components](#writing-new-components)
- [Contributing](#contributing)

---

## What this is

This repository provides:

| Piece | What it does |
|---|---|
| `tokens.css` | The single source of truth for all design values — colors, spacing, type, radius, shadows, motion |
| `src/` | Ready-to-use CSS components (button, card, input, badge, alert, typography) |
| `lib-adapters/` | CSS + JS bridges that map any upstream library's variables to the token layer |
| `specs/` | LLM-readable markdown specs for every foundation, token, and component |
| `shadcn-docs/` | Scraped and structured shadcn/ui component documentation |
| `scripts/token-audit.js` | CI-ready audit script that catches hardcoded values |

---

## Repository structure

```
tokens.css                     ← Layer 1 primitives + Layer 2 semantic aliases
src/
  base/
    reset.css                  ← Opinionated CSS reset using tokens
    typography.css             ← .heading-*, .text-*, .prose, .code-inline …
  components/
    button.css                 ← .btn, .btn-primary, .btn-secondary …
    card.css                   ← .card, .card-header, .card-body …
    input.css                  ← .input, .select, .checkbox, .field …
    badge.css                  ← .badge, .badge-success, .badge-count …
    alert.css                  ← .alert, .alert-danger, .alert-toast …
lib-adapters/
  shadcn.css                   ← shadcn/ui v4 variable bridge (CSS-only)
  ant-design.css               ← Ant Design v5 variable bridge (CSS-only)
  material-ui.css              ← Material UI v6 variable bridge (CSS-only)
  component-map.js             ← Cross-library component equivalence table
  index.js                     ← JS: detectLibrary, applyAdapter, createAdapter
specs/
  foundations/                 ← color, spacing, typography, radius, elevation, motion
  tokens/token-reference.md    ← Master map of every token
  components/                  ← Per-component anatomy, API, token table, examples
  adapters/                    ← Adapter usage guides + custom adapter guide
shadcn-docs/                   ← Structured docs for all 59 shadcn/ui components
  INDEX.md
  accordion.md, alert.md …
scripts/
  token-audit.js               ← Audit script (npm run audit)
  build-shadcn-docs.py         ← Script that generated shadcn-docs/
```

---

## Quick start

### Standalone (no upstream library)

Copy `tokens.css` and whichever `src/` files you need into your project.

```html
<link rel="stylesheet" href="tokens.css">
<link rel="stylesheet" href="src/base/reset.css">
<link rel="stylesheet" href="src/base/typography.css">
<link rel="stylesheet" href="src/components/button.css">
<link rel="stylesheet" href="src/components/card.css">
```

Or with a bundler:

```css
@import 'ai-design-system/tokens.css';
@import 'ai-design-system/src/base/reset.css';
@import 'ai-design-system/src/base/typography.css';
@import 'ai-design-system/src/components/button.css';
```

Use the classes directly in HTML:

```html
<button class="btn btn-primary">Save changes</button>

<div class="card">
  <div class="card-header">
    <h3 class="card-title">Project Alpha</h3>
  </div>
  <div class="card-body">
    <p class="text-md">Main content here.</p>
  </div>
  <div class="card-footer">
    <button class="btn btn-secondary btn-sm">Cancel</button>
    <button class="btn btn-primary btn-sm">Confirm</button>
  </div>
</div>

<div class="alert alert-danger" role="alert">
  <div class="alert-content">
    <strong class="alert-title">Payment failed</strong>
    <p class="alert-description">Your card ending in 4242 was declined.</p>
  </div>
</div>
```

---

## Token architecture

The system uses three layers. **Only Layer 2 tokens are used in component CSS.**

```
Layer 1  --prim-*        Raw values (colors, px, ms).
                         Defined in tokens.css only. Never use in components.

Layer 2  --color-*       Semantic aliases that resolve through an upstream
         --spacing-*     library hook (--ds-*) with a primitive fallback:
         --text-*
         --radius-*         --color-text: var(--ds-text, var(--prim-neutral-900))
         --shadow-*
         --weight-*      This is what ALL component CSS references.
         --font-*
         --leading-*
         --motion-*
         --z-*

Layer 3  Component CSS   src/ files that reference Layer 2 exclusively.
```

### Using tokens in your own CSS

```css
/* Correct — Layer 2 token */
.my-component {
  color:         var(--color-text);
  background:    var(--color-bg);
  padding:       var(--spacing-4);
  font-size:     var(--text-sm);
  border-radius: var(--radius-md);
  border:        1px solid var(--color-border);
}

/* Wrong — raw value */
.my-component {
  color:   #212529;
  padding: 16px;
}
```

### Overriding individual values

Set `--ds-*` variables before importing `tokens.css`:

```css
:root {
  --ds-interactive: #6366f1;   /* overrides primary action colour */
  --ds-font-sans:   'Inter', sans-serif;
  --ds-radius-md:   8px;
}

@import 'ai-design-system/tokens.css';
```

Full list of overrideable `--ds-*` hooks: [`specs/adapters/custom.md`](specs/adapters/custom.md)

---

## Using the component CSS

### Button

```html
<!-- Variants -->
<button class="btn btn-primary">Primary</button>
<button class="btn btn-secondary">Secondary</button>
<button class="btn btn-ghost">Ghost</button>
<button class="btn btn-danger">Delete</button>

<!-- Sizes -->
<button class="btn btn-primary btn-sm">Small</button>
<button class="btn btn-primary btn-lg">Large</button>
<button class="btn btn-primary btn-xl">Extra large</button>

<!-- Icon-only -->
<button class="btn btn-ghost btn-icon" aria-label="Settings">⚙</button>

<!-- States -->
<button class="btn btn-primary" disabled>Disabled</button>
<button class="btn btn-primary btn-loading" aria-busy="true">Saving…</button>
```

Full spec: [`specs/components/button.md`](specs/components/button.md)

### Card

```html
<!-- Basic -->
<div class="card">
  <div class="card-body">Content</div>
</div>

<!-- Full structure -->
<div class="card">
  <div class="card-header">
    <div>
      <h3 class="card-title">Title</h3>
      <p class="card-subtitle">Subtitle</p>
    </div>
    <button class="btn btn-ghost btn-sm">Edit</button>
  </div>
  <div class="card-body">Body content</div>
  <div class="card-footer">
    <button class="btn btn-secondary btn-sm">Cancel</button>
    <button class="btn btn-primary btn-sm">Save</button>
  </div>
</div>

<!-- Variants: card-elevated, card-flat, card-ghost, card-interactive -->
<!-- Status tints: card-danger, card-success, card-warning, card-info -->
<!-- Grid: card-group card-group-3 -->
```

Full spec: [`specs/components/card.md`](specs/components/card.md)

### Input / Form

```html
<div class="field">
  <label class="field-label" for="email">Email</label>
  <input class="input" id="email" type="email" placeholder="you@example.com">
  <p class="field-hint">We'll never share your email.</p>
</div>

<!-- Error state -->
<div class="field field-error">
  <label class="field-label" for="name">Name</label>
  <input class="input" id="name" value="x" aria-describedby="name-err">
  <p class="field-error-msg" id="name-err">Name must be at least 2 characters.</p>
</div>

<!-- Select, textarea, checkbox, radio also available -->
<select class="select">…</select>
<textarea class="textarea">…</textarea>
<input class="checkbox" type="checkbox">
<input class="radio" type="radio">
```

Full spec: [`specs/components/input.md`](specs/components/input.md)

### Badge

```html
<span class="badge badge-success badge-dot">Active</span>
<span class="badge badge-danger">Expired</span>
<span class="badge badge-warning">Pending</span>
<span class="badge badge-solid-primary">New</span>
<span class="badge badge-count badge-solid-danger">5</span>
```

Full spec: [`specs/components/badge.md`](specs/components/badge.md)

### Alert

```html
<!-- Info with actions -->
<div class="alert alert-info" role="status">
  <div class="alert-content">
    <strong class="alert-title">Heads up</strong>
    <p class="alert-description">Your trial ends in 3 days.</p>
    <div class="alert-actions">
      <button class="btn btn-sm btn-secondary">Dismiss</button>
      <button class="btn btn-sm btn-primary">Upgrade</button>
    </div>
  </div>
</div>

<!-- Banner -->
<div class="alert alert-warning alert-banner" role="status">…</div>

<!-- Toast (place at body level) -->
<div class="toast-region" aria-live="polite">
  <div class="alert alert-toast alert-success" role="status">…</div>
</div>
```

Full spec: [`specs/components/alert.md`](specs/components/alert.md)

### Typography

```html
<h1 class="display-md">Hero headline</h1>
<h2 class="heading-lg">Section title</h2>
<p class="text-md">Body copy</p>
<p class="text-sm text-muted">Secondary text</p>
<code class="code-inline">npm install</code>

<!-- Long-form content -->
<article class="prose">
  <h2>Introduction</h2>
  <p>Paragraph…</p>
  <ul><li>Item</li></ul>
</article>
```

Full spec: [`specs/components/typography.md`](specs/components/typography.md)

---

## Multi-library adapter system

Adapters let the AI Design System token layer sit transparently on top of an
existing component library. The library's native CSS variables are mapped to
`--ds-*` hooks — no component CSS is touched.

### shadcn/ui

**Requires:** shadcn/ui v4 with `globals.css` loaded.

```css
/* CSS entry point */
@import '@/styles/globals.css';                      /* defines --primary, --background … */
@import 'ai-design-system/lib-adapters/shadcn.css';  /* maps them to --ds-* */
@import 'ai-design-system/tokens.css';
```

```js
// Or at runtime (e.g., after dynamic theme switch)
import { applyAdapter } from 'ai-design-system/lib-adapters';
applyAdapter('shadcn');
```

Full guide: [`specs/adapters/shadcn.md`](specs/adapters/shadcn.md)

---

### Ant Design

**Requires:** Ant Design v5 with `cssVar: true` in `ConfigProvider`.

```jsx
<ConfigProvider theme={{ cssVar: true, hashed: false }}>
  <App />
</ConfigProvider>
```

```css
@import 'antd/dist/reset.css';
@import 'ai-design-system/lib-adapters/ant-design.css';
@import 'ai-design-system/tokens.css';
```

```js
// Runtime (after ConfigProvider mounts)
import { applyAdapter } from 'ai-design-system/lib-adapters';
applyAdapter('antDesign');
```

Full guide: [`specs/adapters/ant-design.md`](specs/adapters/ant-design.md)

---

### Material UI

**Requires:** MUI v6 with `cssVariables: true`, or v5 with `Experimental_CssVarsProvider`.

```jsx
const theme = createTheme({ cssVariables: true });
// Wrap your app in <ThemeProvider theme={theme}>
```

```css
@import 'ai-design-system/lib-adapters/material-ui.css';
@import 'ai-design-system/tokens.css';
```

```js
// Recommended: apply after ThemeProvider mounts
import { applyAdapter } from 'ai-design-system/lib-adapters';
useEffect(() => { applyAdapter('materialUI'); }, []);
```

Full guide: [`specs/adapters/material-ui.md`](specs/adapters/material-ui.md)

---

### Custom / in-house library

**Option A — CSS file:**

```css
/* my-adapter.css */
:root {
  --ds-text:        var(--brand-color-text);
  --ds-bg:          var(--brand-surface-default);
  --ds-interactive: var(--brand-action-default);
  --ds-border:      var(--brand-stroke);
  --ds-font-sans:   var(--brand-font-body);
  --ds-radius-md:   var(--brand-radius-base);
}
```

**Option B — JavaScript:**

```js
import { createAdapter } from 'ai-design-system/lib-adapters';

const myAdapter = createAdapter({
  '--ds-text':        '--brand-color-text',
  '--ds-interactive': '--brand-action-default',
  '--ds-border':      '--brand-stroke',
});

myAdapter(); // apply to :root
myAdapter(document.querySelector('#scoped-section')); // or scope to an element
```

Full guide and complete `--ds-*` reference: [`specs/adapters/custom.md`](specs/adapters/custom.md)

---

### Auto-detect the active library

```js
import { detectLibrary, applyAdapter } from 'ai-design-system/lib-adapters';

// Inspects loaded CSS variables and returns 'shadcn' | 'antDesign' | 'materialUI' | null
const lib = detectLibrary();
if (lib) applyAdapter(lib);
```

---

### Component equivalence map

Find the nearest library component for any AI DS concept:

```js
import { getComponentInfo } from 'ai-design-system/lib-adapters';

getComponentInfo('button', 'antDesign');
// → {
//     description: 'Clickable element that triggers an action',
//     designSystem: { class: '.btn', … },
//     antDesign: { component: 'Button', import: "import { Button } from 'antd'", … }
//   }

getComponentInfo('alert', 'materialUI');
// → { …, materialUI: { component: 'Alert', import: "import Alert from '@mui/material/Alert'", … } }
```

All 13 concepts mapped (button, input, select, checkbox, radio, card, badge,
alert, dialog, tooltip, table, tabs, toast): [`lib-adapters/component-map.js`](lib-adapters/component-map.js)

---

## Token audit (CI)

The audit script scans all CSS files (except `tokens.css`, `reset.css`, and
`lib-adapters/`) for hardcoded design values.

```bash
npm run audit          # scan everything
npm run audit:src      # scan src/ only
node scripts/token-audit.js path/to/dir
```

**Exit codes:**
- `0` — clean (zero errors; warnings are informational)
- `1` — errors found; commit blocked

**Errors (must fix):**

| Violation | Example | Suggested fix |
|---|---|---|
| Hardcoded hex color | `color: #212529` | `color: var(--color-text)` |
| Raw rgb/hsl | `background: rgb(248,249,250)` | `background: var(--color-bg-subtle)` |
| Raw px spacing | `padding: 16px` | `padding: var(--spacing-4)` |
| Raw font-size | `font-size: 14px` | `font-size: var(--text-sm)` |
| Numeric font-weight | `font-weight: 600` | `font-weight: var(--weight-semibold)` |
| Raw border-radius | `border-radius: 6px` | `border-radius: var(--radius-md)` |
| Bare box-shadow | `box-shadow: 0 2px 4px …` | `box-shadow: var(--shadow-sm)` |

**Warnings (should review):**

| Violation | Example |
|---|---|
| Hardcoded z-index | `z-index: 100` |
| Raw transition duration | `transition: all 200ms` |

---

## Specs and documentation

All specs are in `specs/` and are structured for LLM consumption — each file
covers anatomy, token table, props/API, states, and code examples.

### Foundation specs

| File | Covers |
|---|---|
| [`specs/foundations/color.md`](specs/foundations/color.md) | Semantic color palette, usage rules |
| [`specs/foundations/spacing.md`](specs/foundations/spacing.md) | 4px-grid spacing scale |
| [`specs/foundations/typography.md`](specs/foundations/typography.md) | Type scale, weight, line-height |
| [`specs/foundations/radius.md`](specs/foundations/radius.md) | Border radius scale |
| [`specs/foundations/elevation.md`](specs/foundations/elevation.md) | Shadows and z-index |
| [`specs/foundations/motion.md`](specs/foundations/motion.md) | Transition durations and easings |
| [`specs/tokens/token-reference.md`](specs/tokens/token-reference.md) | **Master map of every token** |

### Component specs

| File | Component |
|---|---|
| [`specs/components/button.md`](specs/components/button.md) | Button |
| [`specs/components/card.md`](specs/components/card.md) | Card |
| [`specs/components/input.md`](specs/components/input.md) | Input, Select, Checkbox, Radio |
| [`specs/components/badge.md`](specs/components/badge.md) | Badge |
| [`specs/components/alert.md`](specs/components/alert.md) | Alert, Toast |
| [`specs/components/typography.md`](specs/components/typography.md) | Typography utilities |

### Adapter specs

| File | Covers |
|---|---|
| [`specs/adapters/overview.md`](specs/adapters/overview.md) | System overview, all `--ds-*` hooks |
| [`specs/adapters/shadcn.md`](specs/adapters/shadcn.md) | shadcn/ui setup, mapping table |
| [`specs/adapters/ant-design.md`](specs/adapters/ant-design.md) | Ant Design setup, mapping table |
| [`specs/adapters/material-ui.md`](specs/adapters/material-ui.md) | MUI setup, mapping table |
| [`specs/adapters/custom.md`](specs/adapters/custom.md) | Custom adapter guide, full `--ds-*` reference |

---

## shadcn/ui component docs

`shadcn-docs/` contains structured `.md` files for all 59 shadcn/ui
components. Each file has: Overview, Import, Usage, Props & Variants,
Accessibility (ARIA roles, keyboard, attributes, screen reader notes),
Tailwind Tokens, and Notes.

Start with the index:

```
shadcn-docs/INDEX.md
```

These files are intended as AI coding context — paste the relevant file into
your LLM context when generating code that uses a shadcn component.

---

## Writing new components

1. **Read** `specs/tokens/token-reference.md` — know the available tokens.
2. **Create a spec** in `specs/components/your-component.md` using the template in [`CLAUDE.md`](CLAUDE.md).
3. **Write CSS** in `src/components/your-component.css` — Layer 2 tokens only.
4. **Run the audit** — zero errors required before committing.

```bash
npm run audit
```

### Component spec template

```markdown
# ComponentName

**Name:** …
**Category:** …
**Status:** Draft | Stable | Deprecated
**File:** src/components/name.css

## Overview
### When to use
### When NOT to use

## Anatomy
(ASCII diagram of parts)

## Tokens used
(table: Property | Token)

## Props / API
(table: Class | Description)

## States
(table: State | Behaviour)

## Code examples

## Cross-references
```

### Token rules

```css
/* Correct */
.my-component {
  color:      var(--color-text);         /* --color-* for color */
  padding:    var(--spacing-4);          /* --spacing-* for spacing */
  font-size:  var(--text-sm);            /* --text-* for type size */
  border-radius: var(--radius-md);       /* --radius-* for radius */
}

/* Wrong */
.my-component {
  color:      var(--prim-neutral-900);   /* never reference --prim-* */
  padding:    16px;                      /* never raw values */
}
```

---

## Contributing

**Before committing any CSS:**

```bash
npm run audit   # must exit 0
```

**Branch:** `claude/design-system-tokens-6bucp6`

**AI instructions:** [`CLAUDE.md`](CLAUDE.md) contains the full ruleset for
any LLM working on this codebase — token layer rules, audit requirements,
spec templates, and adapter guidance.
