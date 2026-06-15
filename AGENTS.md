# AI Design System — Agent Instructions

> **Active library: shadcn/ui v4**
> Component docs: `shadcn-docs/` · Adapter: `lib-adapters/shadcn.css`
> Switch library: `npm run docs -- --library=<shadcn|antdesign|mui>`
> This file is auto-maintained — do not edit the "Active library" section manually.

---

## Project overview

An LLM-ready CSS design system built on a three-layer custom property
architecture. Provides a complete token layer, component CSS utilities,
LLM-readable specs, and adapter bridges for popular component libraries.

Key capabilities:
- Token-first CSS with semantic aliases (`--color-*`, `--spacing-*`, etc.)
- Component CSS: button, card, input, badge, alert, typography
- Library adapters: shadcn/ui, Ant Design, Material UI, custom
- CI-ready token audit script

---

## Non-negotiable rules

1. **Tokens only in component CSS.** Use `var(--color-*)`, `var(--spacing-*)`,
   `var(--text-*)`, `var(--radius-*)`. Never raw `px`, `#hex`, or `--prim-*`.
2. **Read component docs before writing code.** Check `shadcn-docs/{component}.md`
   for shadcn/ui-specific usage, then `specs/components/` for AI DS class names.
3. **Read specs before writing CSS.** Check `specs/tokens/token-reference.md` first.
4. **Audit must pass.** Run `npm run audit` before every commit. Exit 0 required.
5. **Adapter files are exempt** from the token audit (`lib-adapters/` is skipped).

---

## Token architecture

```
Layer 1  --prim-*        Raw values in tokens.css only. Never use in components.
Layer 2  --color-*       Semantic aliases. ALL component CSS uses only these.
         --spacing-*
         --text-*              --color-text: var(--ds-text, var(--prim-neutral-900))
         --radius-*
         --shadow-*     Each Layer 2 token has a --ds-* upstream hook + prim fallback.
         --font-*
Layer 3  src/ CSS        References Layer 2 exclusively.
```

---

## Before writing any CSS

1. Read `specs/tokens/token-reference.md` — master token map.
2. Read the relevant `specs/foundations/` file for the property type.
3. Read `specs/components/{name}.md` if modifying an AI DS component.

---

## Running the audit

```bash
npm run audit        # scan all CSS
npm run audit:src    # scan src/ only
```

**Exit 0** = clean. **Exit 1** = errors; fix before committing.

---

## File map

```
tokens.css                     ← Layer 1 + Layer 2 tokens (source of truth)
shadcn-docs/                        ← Active library docs (59 components)
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
  shadcn.css                    ← Active adapter (shadcn/ui → --ds-*)
  component-map.js             ← Cross-library component equivalence
  index.js                     ← detectLibrary, applyAdapter, createAdapter
specs/
  tokens/token-reference.md    ← Every token, its value and purpose
  foundations/                 ← color, spacing, typography, radius, elevation, motion
  components/                  ← Per-component anatomy, API, token table, examples
  adapters/shadcn.md               ← Active adapter setup guide
scripts/
  build-docs.js                ← Switch active library (npm run docs:shadcn etc.)
  token-audit.js               ← CI audit script
```

---

<!-- ACTIVE-LIBRARY:START -->
## Active component library: shadcn/ui v4

**Component docs:** `shadcn-docs/` (59 components — read before generating code)
**Index:** `shadcn-docs/INDEX.md`
**Adapter CSS:** `lib-adapters/shadcn.css`
**Adapter spec:** `specs/adapters/shadcn.md`
**Official docs:** https://ui.shadcn.com/docs/components

### Setup

Requires shadcn/ui v4 with globals.css defining --primary, --background, --foreground, --border, --ring, --radius.

```css
/* 1. shadcn globals */
@import '@/styles/globals.css';

/* 2. AI Design System adapter */
@import 'ai-design-system/lib-adapters/shadcn.css';

/* 3. AI Design System tokens */
@import 'ai-design-system/tokens.css';
```

```js
import { applyAdapter } from 'ai-design-system/lib-adapters';
applyAdapter('shadcn');
```

### AI Design System → shadcn/ui class map

| AI DS class | shadcn/ui equivalent |
|---|---|
| `.btn` | `<Button>` |
| `.card` | `<Card>` |
| `.input` | `<Input>` |
| `.badge` | `<Badge>` |
| `.alert` | `<Alert>` |
| `.select` | `<Select>` |
| `.checkbox` | `<Checkbox>` |
| `.radio` | `<RadioGroupItem>` |

### Rules when writing code with this library

- Read `shadcn-docs/{component}.md` before generating code for any component.
- Use `getComponentInfo(concept, 'shadcn')` from `lib-adapters/component-map.js`
  to find the correct import and props for any AI DS concept.
- Apply the CSS adapter before `tokens.css` so `--ds-*` hooks resolve correctly.
- Never hard-code colours, spacing, or typography — use `var(--color-*)`, `var(--spacing-*)`, etc.
<!-- ACTIVE-LIBRARY:END -->
