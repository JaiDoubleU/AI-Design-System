# Border Radius Foundation

**Category:** Foundation  
**Status:** Stable

## Overview

Border radius tokens establish a consistent rounding system. All `border-radius` declarations in component CSS must reference a token.

---

## Scale

| Token | px | rem | When to use |
|---|---|---|---|
| `--radius-none` | 0 | `0` | Sharp corners (tables, code blocks) |
| `--radius-sm` | 2 px | `0.125rem` | Subtle rounding (tags, kbd) |
| `--radius-md` | 4 px | `0.25rem` | Small components (buttons-sm, inputs) |
| `--radius-lg` | 8 px | `0.5rem` | Default for most UI (buttons, inputs-lg) |
| `--radius-xl` | 12 px | `0.75rem` | Cards, panels |
| `--radius-2xl` | 16 px | `1rem` | Large panels, modals |
| `--radius-full` | 9999 px | — | Pills, avatar circles, badges |

---

## Decision guide

| Component | Recommended token |
|---|---|
| Button (default) | `--radius-md` |
| Button (large) | `--radius-lg` |
| Input | `--radius-md` |
| Card | `--radius-xl` |
| Modal / Dialog | `--radius-2xl` |
| Badge / Pill | `--radius-full` |
| Avatar | `--radius-full` |
| Tooltip | `--radius-md` |
| Code block | `--radius-lg` |
| Table cell | `--radius-none` |

---

## Usage rules

1. Never write `border-radius: 8px` — always use `var(--radius-lg)`.
2. Composite radii are fine: `border-radius: var(--radius-xl) var(--radius-none)`.
3. `border-top-left-radius` etc. follow the same rule.

---

## Examples

```css
.btn   { border-radius: var(--radius-md); }
.card  { border-radius: var(--radius-xl); }
.badge { border-radius: var(--radius-full); }
.modal { border-radius: var(--radius-2xl); }
```
