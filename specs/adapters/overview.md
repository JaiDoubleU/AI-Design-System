# Library Adapter System — Overview

**Status:** Stable  
**Location:** `lib-adapters/`

---

## What the adapter system does

The AI Design System's token architecture uses a two-step variable chain:

```
Component CSS
  → Layer 2 semantic token  (--color-text, --spacing-4 …)
    → --ds-* override hook  (--ds-text, --ds-spacing-4 …)
      → Layer 1 primitive   (--prim-neutral-900, --prim-space-4 …)
```

An **adapter** sets the `--ds-*` hooks to point at a specific library's
native CSS variables. Components automatically pick up those values through
the chain — no component CSS is modified.

---

## File structure

```
lib-adapters/
  shadcn.css          ← shadcn/ui v4 adapter (CSS-only)
  ant-design.css      ← Ant Design v5 adapter (CSS-only)
  material-ui.css     ← Material UI v6 adapter (CSS-only)
  component-map.js    ← Cross-library equivalence table
  index.js            ← JS utilities: detectLibrary, applyAdapter, createAdapter

specs/adapters/
  overview.md         ← this file
  shadcn.md
  ant-design.md
  material-ui.md
  custom.md
```

---

## Choosing an approach

| Scenario | Recommended approach |
|---|---|
| Static CSS bundle | Import the `.css` adapter before `tokens.css` |
| Library initialises after load (e.g. MUI CssVarsProvider) | `applyAdapter('materialUI')` in JS after mount |
| Custom / in-house design system | `createAdapter({ '--ds-interactive': '--brand-blue' })` |
| Auto-detect which library is active | `applyAdapter(detectLibrary())` |

---

## CSS-only usage (no JavaScript)

```html
<!-- In your HTML <head> or CSS entry point -->
<link rel="stylesheet" href="antd/dist/reset.css">
<link rel="stylesheet" href="lib-adapters/ant-design.css">
<link rel="stylesheet" href="tokens.css">
```

Or in CSS:

```css
@import 'antd/dist/reset.css';
@import 'ai-design-system/lib-adapters/ant-design.css';
@import 'ai-design-system/tokens.css';
```

---

## JavaScript usage

```js
import { applyAdapter, detectLibrary } from 'ai-design-system/lib-adapters';

// Option A — explicit
applyAdapter('shadcn');

// Option B — auto-detect from loaded CSS variables
applyAdapter(detectLibrary());

// Option C — verbose debugging
applyAdapter('antDesign', { verbose: true });
```

---

## Custom adapter

```js
import { createAdapter } from 'ai-design-system/lib-adapters';

const myAdapter = createAdapter({
  '--ds-interactive': '--brand-blue',
  '--ds-text':        '--body-copy-color',
  '--ds-bg':          '--surface-default',
  '--ds-border':      '--stroke-color',
});

myAdapter(); // applies to :root
```

---

## Component equivalence

`lib-adapters/component-map.js` maps every AI Design System concept
(Button, Input, Card, Alert…) to its nearest equivalent in shadcn/ui,
Ant Design, and Material UI — including import statements.

```js
import { getComponentInfo } from 'ai-design-system/lib-adapters';

getComponentInfo('button', 'antDesign');
// → { description, designSystem, antDesign: { component, import, variants, … } }
```

See `specs/adapters/` for per-library usage guides.

---

## Supported `--ds-*` hooks

All Layer 2 tokens support `--ds-*` override hooks. The most commonly
overridden are:

| `--ds-*` variable | Controls |
|---|---|
| `--ds-text` | Default body text colour |
| `--ds-text-subtle` | Secondary / muted text |
| `--ds-text-inverse` | Text on dark/filled surfaces |
| `--ds-bg` | Page / surface background |
| `--ds-bg-subtle` | Slightly off-white / receded surface |
| `--ds-bg-muted` | Chip/tag backgrounds |
| `--ds-interactive` | Primary action colour (button fill, link) |
| `--ds-interactive-hover` | Hover state of interactive colour |
| `--ds-interactive-fg` | Text/icon on filled interactive surfaces |
| `--ds-interactive-danger` | Danger/error action colour |
| `--ds-border` | Default border colour |
| `--ds-border-focus` | Focus ring colour |
| `--ds-radius-sm/md/lg/xl` | Border radius scale |
| `--ds-font-sans/mono/serif` | Font family stacks |
| `--ds-shadow-sm/md/lg` | Elevation shadows |

Full list: `specs/tokens/token-reference.md`
