# Color Foundation

**Category:** Foundation  
**Status:** Stable

## Overview

The color system uses a three-layer model. Primitives (`--prim-*`) define the full hue palette. Semantic aliases (`--color-*`) map primitives to intent. Components always reference semantic aliases.

### When to use raw primitives
Never in components. Only in `tokens.css` to define semantic aliases.

### When to define a new alias
When a semantic role isn't covered (e.g., `--color-text-ai-generated`). Reference a primitive as the fallback.

---

## Primitive palette

### Neutral

| Token | Value | Usage |
|---|---|---|
| `--prim-neutral-0` | `#ffffff` | Pure white |
| `--prim-neutral-50` | `#f8f9fa` | Off-white backgrounds |
| `--prim-neutral-100` | `#f1f3f5` | Muted backgrounds |
| `--prim-neutral-200` | `#e9ecef` | Subtle borders |
| `--prim-neutral-300` | `#dee2e6` | Default borders |
| `--prim-neutral-400` | `#ced4da` | Emphasis borders |
| `--prim-neutral-500` | `#adb5bd` | Disabled text |
| `--prim-neutral-600` | `#868e96` | Muted text |
| `--prim-neutral-700` | `#495057` | Subtle text |
| `--prim-neutral-800` | `#343a40` | Strong text |
| `--prim-neutral-900` | `#212529` | Default text |
| `--prim-neutral-1000` | `#000000` | Pure black |

### Blue (interactive/primary)

| Token | Value |
|---|---|
| `--prim-blue-50` | `#e8f4fd` |
| `--prim-blue-100` | `#bee3f8` |
| `--prim-blue-400` | `#4299e1` |
| `--prim-blue-500` | `#3182ce` |
| `--prim-blue-600` | `#2b6cb0` |
| `--prim-blue-700` | `#2c5282` |

### Green (success), Red (danger), Yellow (warning)

See `tokens.css` Layer 1 for complete scales.

---

## Semantic aliases

### Text

| Token | Resolves to | When to use |
|---|---|---|
| `--color-text` | neutral-900 | Default body copy |
| `--color-text-subtle` | neutral-600 | Secondary information |
| `--color-text-muted` | neutral-500 | Tertiary, helper text |
| `--color-text-disabled` | neutral-400 | Disabled labels |
| `--color-text-inverse` | neutral-0 | Text on dark backgrounds |
| `--color-text-link` | blue-500 | Anchor text |
| `--color-text-link-hover` | blue-600 | Anchor hover |
| `--color-text-danger` | red-600 | Error messages |
| `--color-text-success` | green-600 | Success messages |
| `--color-text-warning` | yellow-600 | Warning messages |
| `--color-text-info` | blue-500 | Informational text |

### Background

| Token | Resolves to | When to use |
|---|---|---|
| `--color-bg` | neutral-0 | Page / card surface |
| `--color-bg-subtle` | neutral-50 | Slightly elevated surface |
| `--color-bg-muted` | neutral-100 | Recessed / input background |
| `--color-bg-emphasis` | neutral-800 | Inverted surface |
| `--color-bg-inverse` | neutral-900 | Dark-mode-ready base |
| `--color-bg-danger` | red-50 | Error state fill |
| `--color-bg-success` | green-50 | Success state fill |
| `--color-bg-warning` | yellow-50 | Warning state fill |
| `--color-bg-info` | blue-50 | Info state fill |

### Border

| Token | Resolves to | When to use |
|---|---|---|
| `--color-border` | neutral-200 | Default card/input border |
| `--color-border-subtle` | neutral-100 | Dividers, light separators |
| `--color-border-emphasis` | neutral-400 | Strong borders, focus rings |
| `--color-border-focus` | blue-400 | Keyboard focus outline |
| `--color-border-danger` | red-500 | Invalid input border |
| `--color-border-success` | green-500 | Valid input border |

### Interactive

| Token | Resolves to | When to use |
|---|---|---|
| `--color-interactive` | blue-500 | Button / link fill |
| `--color-interactive-hover` | blue-600 | Hover state |
| `--color-interactive-active` | blue-700 | Active / pressed state |
| `--color-interactive-muted` | blue-50 | Subtle interactive fill |
| `--color-interactive-fg` | neutral-0 | Text on interactive fill |
| `--color-interactive-danger` | red-500 | Destructive action fill |
| `--color-interactive-danger-hover` | red-600 | Destructive action hover |
| `--color-interactive-danger-fg` | neutral-0 | Text on danger fill |

---

## Upstream DS integration

Override any `--ds-*` variable before importing `tokens.css`:

```css
:root {
  --ds-interactive: #6366f1;   /* swap brand color */
  --ds-text:        #111827;
}
@import 'tokens.css';
```

The fallback chain ensures every alias still resolves even when only a subset of `--ds-*` variables are set.

---

## Accessibility

- Text on `--color-bg`: neutral-900 on neutral-0 → ≥ 13.5 : 1 (AAA)
- Text on `--color-bg-muted`: neutral-900 on neutral-100 → ≥ 12 : 1 (AAA)
- Interactive on white: blue-500 on neutral-0 → ≥ 4.6 : 1 (AA)
- Always verify contrast when overriding primitives.
