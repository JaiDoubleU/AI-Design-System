# Elevation Foundation

**Category:** Foundation  
**Status:** Stable

## Overview

Elevation communicates hierarchy through shadow depth. All `box-shadow` declarations in component CSS must reference an elevation token — never write raw shadow values.

---

## Shadow scale

| Token | Visual | When to use |
|---|---|---|
| `--shadow-none` | No shadow | Flat surfaces, ghost variants |
| `--shadow-xs` | Very subtle | Inline elements, small chips |
| `--shadow-sm` | Default card | Cards, dropdowns (subtle) |
| `--shadow-md` | Elevated card | Popovers, active card state |
| `--shadow-lg` | Floating element | Dropdown menus, tooltips |
| `--shadow-xl` | Modal | Dialogs, command palette |
| `--shadow-2xl` | Deep shadow | Drawer, large overlay panel |
| `--shadow-inner` | Inset | Pressed buttons, active inputs |

---

## Primitive values

These are resolved in `tokens.css` Layer 1. Never copy these values into component CSS.

```
--prim-shadow-xs:    0 1px 2px 0 rgb(0 0 0 / 0.05)
--prim-shadow-sm:    0 1px 3px 0 rgb(0 0 0 / 0.10), 0 1px 2px -1px rgb(0 0 0 / 0.10)
--prim-shadow-md:    0 4px 6px -1px rgb(0 0 0 / 0.10), 0 2px 4px -2px rgb(0 0 0 / 0.10)
--prim-shadow-lg:    0 10px 15px -3px rgb(0 0 0 / 0.10), 0 4px 6px -4px rgb(0 0 0 / 0.10)
--prim-shadow-xl:    0 20px 25px -5px rgb(0 0 0 / 0.10), 0 8px 10px -6px rgb(0 0 0 / 0.10)
--prim-shadow-2xl:   0 25px 50px -12px rgb(0 0 0 / 0.25)
--prim-shadow-inner: inset 0 2px 4px 0 rgb(0 0 0 / 0.05)
```

---

## Component mapping

| Component | Default | Hover / Active |
|---|---|---|
| Card (default) | `--shadow-sm` | `--shadow-md` |
| Card (elevated) | `--shadow-md` | `--shadow-lg` |
| Dropdown | `--shadow-lg` | — |
| Tooltip | `--shadow-md` | — |
| Modal / Dialog | `--shadow-xl` | — |
| Drawer | `--shadow-2xl` | — |
| Toast | `--shadow-lg` | — |
| Button (active) | `--shadow-inner` | — |
| Input (focus ring) | combined with `--shadow-xs` | — |

---

## Z-index scale

Elevation is also expressed through stacking order. Use the `--z-*` tokens:

| Token | Value | When to use |
|---|---|---|
| `--z-below` | -1 | Pseudo-elements behind content |
| `--z-base` | 0 | Default flow |
| `--z-raised` | 10 | Raised cards, sticky table headers |
| `--z-dropdown` | 100 | Dropdown menus, autocomplete |
| `--z-sticky` | 200 | Sticky navigation, header |
| `--z-overlay` | 300 | Backdrop / scrim |
| `--z-modal` | 400 | Dialogs |
| `--z-popover` | 500 | Popovers, floating panels |
| `--z-toast` | 600 | Toast notifications |
| `--z-tooltip` | 700 | Tooltips (always on top) |

---

## Rules

1. All `box-shadow:` values must use `var(--shadow-*)`.
2. All `z-index:` values must use `var(--z-*)`.
3. Never write raw numeric `z-index` values — they are impossible to audit systematically.
4. Layering order must match the scale: a modal (`--z-modal`) always sits above a dropdown (`--z-dropdown`).
