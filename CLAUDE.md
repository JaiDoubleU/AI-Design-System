# AI Design System — Project Instructions

## UI Development Rules

**Before writing or modifying any UI code, read the relevant spec file in `specs/`.
Use only tokens from `tokens.css`. Run the token audit script before committing.
Zero errors required.**

---

## Token system

This project uses a three-layer CSS token architecture:

| Layer | Prefix | Rule |
|---|---|---|
| Layer 1: Primitives | `--prim-*` | **Never reference in components.** Defined in `tokens.css` only. |
| Layer 2: Semantic aliases | `--color-*`, `--spacing-*`, `--text-*`, etc. | **Always use these in component CSS.** |
| Layer 3: Components | — | CSS files in `src/` that reference Layer 2 exclusively. |

### Correct usage

```css
/* CORRECT — Layer 2 token */
.my-component {
  color: var(--color-text);
  padding: var(--spacing-4);
  font-size: var(--text-sm);
}

/* WRONG — raw value */
.my-component {
  color: #212529;
  padding: 16px;
  font-size: 14px;
}
```

---

## Before writing CSS

1. Read `specs/tokens/token-reference.md` — master map of every token and its purpose.
2. Read the relevant foundation spec:
   - Colors → `specs/foundations/color.md`
   - Spacing → `specs/foundations/spacing.md`
   - Typography → `specs/foundations/typography.md`
   - Radius → `specs/foundations/radius.md`
   - Shadows / Z-index → `specs/foundations/elevation.md`
   - Transitions → `specs/foundations/motion.md`
3. If modifying a component, read its spec in `specs/components/`.

---

## Before writing a new component

1. Check `specs/components/` — if a spec exists, follow it exactly.
2. If the component is new, create a spec from the template in `specs/components/`.
3. Component CSS goes in `src/components/`. Base/utility CSS goes in `src/base/`.
4. Components reference **only** Layer 2 tokens (`--color-*`, `--spacing-*`, etc.).
   Never reference `--prim-*` primitives or raw values.

---

## Token audit

Run before every commit:

```bash
node scripts/token-audit.js .
# or
npm run audit
```

- **Exit 0** — zero errors (warnings are acceptable to review).
- **Exit 1** — errors found; fix before committing.

Errors (must fix):
- Hardcoded hex/rgb/hsl colors
- Raw `px`/`rem` values in spacing properties
- Raw `px`/`rem` in `font-size`
- Raw numeric `font-weight`
- Raw `px` in `border-radius`
- Raw `box-shadow` values

Warnings (review):
- Hardcoded `z-index` numbers
- Raw `transition` durations

Files `tokens.css` and `src/base/reset.css` are exempt (they contain intentional raw values in the primitive layer).

---

## Spec template (new components)

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

---

## File map

```
tokens.css                     ← Layer 1 + Layer 2 tokens
src/
  base/
    reset.css                  ← CSS reset (tokens only)
    typography.css             ← Typography utilities (tokens only)
  components/
    button.css
    card.css
    input.css
    badge.css
    alert.css
lib-adapters/
  shadcn.css                   ← shadcn/ui v4 → --ds-* mapping
  ant-design.css               ← Ant Design v5 → --ds-* mapping
  material-ui.css              ← Material UI v6 → --ds-* mapping
  component-map.js             ← Cross-library component equivalence table
  index.js                     ← JS utilities: detectLibrary, applyAdapter, createAdapter
specs/
  foundations/
    color.md
    spacing.md
    typography.md
    radius.md
    elevation.md
    motion.md
  tokens/
    token-reference.md         ← Master token map (read this first)
  components/
    button.md
    card.md
    input.md
    badge.md
    alert.md
    typography.md
  adapters/
    overview.md                ← Adapter system overview (read before using)
    shadcn.md
    ant-design.md
    material-ui.md
    custom.md                  ← Build your own adapter
scripts/
  build-docs.js                ← Doc builder (run to switch active library)
  token-audit.js               ← CI-ready audit script
<!-- DOCS-DIR:START -->
vanilla-docs/                   ← Active library docs (6 components — read before writing code)
  INDEX.md
<!-- DOCS-DIR:END -->
```

---

## Multi-library adapter system

The adapter system maps any upstream library's CSS variables to `--ds-*`
hooks so component CSS works unchanged across shadcn/ui, Ant Design, MUI,
or a custom brand token set.

**Read `specs/adapters/overview.md` before adding or modifying adapters.**

### CSS-only usage (preferred for static bundles)

```css
/* Import order matters — adapter must come between library styles and tokens.css */
@import 'antd/dist/reset.css';
@import 'ai-design-system/lib-adapters/ant-design.css';
@import 'ai-design-system/tokens.css';
```

Supported static adapters:
- `lib-adapters/shadcn.css` — shadcn/ui v4
- `lib-adapters/ant-design.css` — Ant Design v5 (requires `cssVar: true`)
- `lib-adapters/material-ui.css` — MUI v6 (requires `cssVariables: true`)

### JavaScript runtime usage

```js
import { applyAdapter, detectLibrary, createAdapter } from 'ai-design-system/lib-adapters';

applyAdapter('shadcn');               // explicit
applyAdapter(detectLibrary());        // auto-detect from loaded CSS vars
```

### Custom adapter

```js
import { createAdapter } from 'ai-design-system/lib-adapters';
const myAdapter = createAdapter({ '--ds-interactive': '--brand-blue' });
myAdapter(); // applies to :root
```

### Component equivalence

When building with an upstream library, find the nearest equivalent:

```js
import { getComponentInfo } from 'ai-design-system/lib-adapters';
getComponentInfo('button', 'antDesign');
// → { component: 'Button', import: "import { Button } from 'antd'", … }
```

### Token audit exemption

Files in `lib-adapters/` are exempt from the audit script. Adapter files
intentionally contain bridge values (raw values or upstream `var(--*)` 
references) and are not component CSS.

---

## Upstream design system integration

To plug in any upstream DS (e.g., Material, Radix, a Figma-exported token set):

```css
/* 1. Override --ds-* variables */
:root {
  --ds-interactive: #6366f1;
  --ds-text:        #111827;
  --ds-font-sans:   'DM Sans', sans-serif;
}

/* 2. Import tokens.css — fallbacks resolve automatically */
@import 'tokens.css';
```

No component CSS needs to change. The `var(--ds-x, fallback)` chain handles it.

---

## Generating component docs

Run the doc builder to scrape a library's component docs and auto-update
this file and `AGENTS.md` with the correct references:

```bash
npm run docs -- --library=shadcn      # shadcn/ui (already scraped)
npm run docs -- --library=antdesign   # Ant Design v5
npm run docs -- --library=mui         # Material UI v6
npm run docs -- --library=shadcn --force  # re-scrape even if docs exist
```

Shorthand aliases: `npm run docs:shadcn`, `npm run docs:antd`, `npm run docs:mui`

<!-- ACTIVE-LIBRARY:START -->
## Active component library: Vanilla HTML/CSS/JS native

**Component docs:** `vanilla-docs/` (6 components — read before generating code)
**Index:** `vanilla-docs/INDEX.md`
**Adapter CSS:** `lib-adapters/vanilla.css`
**Adapter spec:** `specs/adapters/custom.md`
**Official docs:** https://developer.mozilla.org/en-US/docs/Web/HTML

### Setup

No framework required. Link tokens.css and the component CSS files directly in your HTML.

```css
<!-- In your <head> — order matters -->
<link rel="stylesheet" href="tokens.css">
<link rel="stylesheet" href="src/base/reset.css">
<link rel="stylesheet" href="src/base/typography.css">

<!-- Add only the components you use -->
<link rel="stylesheet" href="src/components/button.css">
<link rel="stylesheet" href="src/components/card.css">
<link rel="stylesheet" href="src/components/input.css">
<link rel="stylesheet" href="src/components/badge.css">
<link rel="stylesheet" href="src/components/alert.css">
```

```js
// No adapter or framework required.
// Optional: override tokens before importing tokens.css
// :root { --ds-interactive: #6366f1; }
```

### AI Design System → Vanilla HTML/CSS/JS class map

| AI DS class | Vanilla HTML/CSS/JS equivalent |
|---|---|
| `.btn .btn-primary` | `<button class="btn btn-primary">` |
| `.card` | `<div class="card">` |
| `.input (in .field)` | `<input class="input" type="text">` |
| `.badge .badge-success` | `<span class="badge badge-success">` |
| `.alert .alert-info` | `<div class="alert alert-info" role="status">` |
| `.prose` | `<article class="prose">` |

### Rules when writing code with this library

- Read `vanilla-docs/{component}.md` before generating code for any component.
- Use `getComponentInfo(concept, 'null')` from `lib-adapters/component-map.js`
  to find the correct import and props for any AI DS concept.
- Apply the CSS adapter before `tokens.css` so `--ds-*` hooks resolve correctly.
- Never hard-code colours, spacing, or typography — use `var(--color-*)`, `var(--spacing-*)`, etc.
<!-- ACTIVE-LIBRARY:END -->
