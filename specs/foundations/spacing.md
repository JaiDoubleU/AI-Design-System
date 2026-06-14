# Spacing Foundation

**Category:** Foundation  
**Status:** Stable

## Overview

Spacing uses a 4 px base grid. All layout values — `padding`, `margin`, `gap`, `top/right/bottom/left` — must reference a spacing token. Never use raw pixel or rem values in component CSS.

---

## Scale

| Token | px equivalent | rem value | Use case |
|---|---|---|---|
| `--spacing-0` | 0 px | `0` | Reset / explicit zero |
| `--spacing-1` | 4 px | `0.25rem` | Icon gap, tight padding |
| `--spacing-2` | 8 px | `0.5rem` | Small padding, inline gap |
| `--spacing-3` | 12 px | `0.75rem` | Compact inputs, button padding |
| `--spacing-4` | 16 px | `1rem` | Default padding, form spacing |
| `--spacing-5` | 20 px | `1.25rem` | Section padding (compact) |
| `--spacing-6` | 24 px | `1.5rem` | Card padding, section gaps |
| `--spacing-8` | 32 px | `2rem` | Large card padding, between sections |
| `--spacing-10` | 40 px | `2.5rem` | Feature section spacing |
| `--spacing-12` | 48 px | `3rem` | Page section gaps |
| `--spacing-16` | 64 px | `4rem` | Hero sections |
| `--spacing-20` | 80 px | `5rem` | Large hero sections |
| `--spacing-24` | 96 px | `6rem` | Full-page section spacing |

---

## Usage rules

1. **Always use a token.** `padding: var(--spacing-4)` not `padding: 16px`.
2. **Composite spacing is fine.** `padding: var(--spacing-2) var(--spacing-4)` uses two tokens — both are valid.
3. **`calc()` is allowed** when combining tokens: `calc(var(--spacing-4) + var(--spacing-2))`.
4. **Percentage values** (`width: 50%`, `margin: auto`) do not require tokens.
5. **Viewport units** (`100vh`, `100vw`) do not require tokens.
6. **`0` without a unit** is always valid and needs no token.

---

## When to deviate

If a one-off measurement cannot be expressed as a token, add a component-local custom property with a descriptive name:

```css
.modal {
  --modal-max-width: 42rem;  /* deliberate override, not a token */
  max-width: var(--modal-max-width);
}
```

Never hardcode the value directly in a property declaration.

---

## Common patterns

```css
/* Card with standard padding */
.card-body      { padding: var(--spacing-5); }

/* Button padding */
.btn            { padding-block: var(--spacing-2); padding-inline: var(--spacing-4); }
.btn-sm         { padding-block: var(--spacing-1); padding-inline: var(--spacing-3); }
.btn-lg         { padding-block: var(--spacing-3); padding-inline: var(--spacing-6); }

/* Grid gap */
.card-group     { gap: var(--spacing-4); }

/* Stack */
.stack > * + * { margin-top: var(--spacing-4); }
```
