# Typography Foundation

**Category:** Foundation  
**Status:** Stable

## Overview

Typography tokens cover font families, size scale, weight, and line height. All `font-size`, `font-weight`, `font-family`, and `line-height` declarations in component CSS must reference a token.

---

## Font families

| Token | Value | When to use |
|---|---|---|
| `--font-sans` | Inter, system-ui … | Body copy, UI labels, headings |
| `--font-mono` | JetBrains Mono, Fira Code … | Code blocks, technical values |
| `--font-serif` | Georgia, Times New Roman | Editorial, long-form prose |

**Default font:** `--font-sans`. Every component inherits it from `body` in `reset.css`.

---

## Size scale

| Token | px | rem | Use case |
|---|---|---|---|
| `--text-xs` | 12 px | `0.75rem` | Labels, captions, badge text |
| `--text-sm` | 14 px | `0.875rem` | Secondary text, helper text, buttons |
| `--text-md` | 16 px | `1rem` | Body copy (base size) |
| `--text-lg` | 18 px | `1.125rem` | Large body, lead text |
| `--text-xl` | 20 px | `1.25rem` | Sub-heading, card title |
| `--text-2xl` | 24 px | `1.5rem` | Section heading (h2) |
| `--text-3xl` | 30 px | `1.875rem` | Page heading (h1 compact) |
| `--text-4xl` | 36 px | `2.25rem` | Display heading |
| `--text-5xl` | 48 px | `3rem` | Hero / marketing display |

---

## Weights

| Token | Value | When to use |
|---|---|---|
| `--weight-normal` | 400 | Body copy |
| `--weight-medium` | 500 | Buttons, labels |
| `--weight-semibold` | 600 | Headings, card titles |
| `--weight-bold` | 700 | Display headings, emphasis |

---

## Line heights

| Token | Value | When to use |
|---|---|---|
| `--leading-tight` | 1.2 | Large headings, display text |
| `--leading-snug` | 1.375 | Sub-headings |
| `--leading-normal` | 1.5 | Body copy, labels |
| `--leading-relaxed` | 1.625 | Long-form prose |
| `--leading-loose` | 2.0 | Spacious layouts |

---

## Semantic classes (typography.css)

The `typography.css` file exports ready-to-use utility classes:

- `.display-lg`, `.display-md`, `.display-sm` — marketing headings
- `.heading-xl` … `.heading-xs` — semantic h1–h6 equivalents
- `.text-lg`, `.text-md`, `.text-sm`, `.text-xs` — body sizes
- `.font-normal`, `.font-medium`, `.font-semibold`, `.font-bold`
- `.font-sans`, `.font-mono`, `.font-serif`
- `.text-subtle`, `.text-muted`, `.text-danger`, `.text-success`, `.text-warning`
- `.prose` — opinionated wrapper for long-form markdown content

---

## Usage rules

1. Never set `font-size` to a raw `px` or `rem` value in component CSS.
2. Never set `font-weight` to a raw number in component CSS.
3. Use semantic size classes (`.heading-md`) in HTML before writing bespoke CSS.
4. `letter-spacing` and `text-transform` have no tokens — use literal values only when the design calls for them.

---

## Examples

```css
.card-title {
  font-size:   var(--text-md);
  font-weight: var(--weight-semibold);
  line-height: var(--leading-tight);
  color:       var(--color-text);
}

.badge {
  font-size:   var(--text-xs);
  font-weight: var(--weight-medium);
  font-family: var(--font-sans);
}
```
