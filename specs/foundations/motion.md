# Motion Foundation

**Category:** Foundation  
**Status:** Stable

## Overview

Motion tokens govern transition durations and easing curves. All `transition` and `animation` declarations should reference motion tokens for duration. Easing curves are also tokenized.

---

## Duration scale

| Token | Value | When to use |
|---|---|---|
| `--motion-instant` | 0 ms | No animation (reduced-motion, programmatic) |
| `--motion-fast` | 150 ms | Small state changes: hover color, focus ring |
| `--motion-normal` | 250 ms | Standard enter/exit: dropdown, tooltip |
| `--motion-slow` | 400 ms | Larger motion: modal open, panel slide |
| `--motion-slower` | 600 ms | Page transitions, skeleton loading |

---

## Easing curves

| Token | Curve | When to use |
|---|---|---|
| `--ease-linear` | `linear` | Progress bars, loading indicators |
| `--ease-in` | `cubic-bezier(0.4, 0, 1, 1)` | Exit animations (elements leaving screen) |
| `--ease-out` | `cubic-bezier(0, 0, 0.2, 1)` | Enter animations (elements entering screen) |
| `--ease-in-out` | `cubic-bezier(0.4, 0, 0.2, 1)` | State changes (already visible elements) |
| `--ease-spring` | `cubic-bezier(0.175, 0.885, 0.32, 1.275)` | Playful micro-interactions (badge bounce, etc.) |

---

## Usage rules

1. Duration tokens are **warnings** in the audit, not errors. Fix them before finalising a component.
2. Easing tokens have no audit check — use them voluntarily.
3. `0ms` / `0s` transitions are allowed without a token (they carry no visual intent).
4. Always add `prefers-reduced-motion` support:

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: var(--motion-instant) !important;
    transition-duration: var(--motion-instant) !important;
  }
}
```

---

## Standard patterns

```css
/* Hover state change */
.btn {
  transition: background-color var(--motion-fast) var(--ease-out),
              border-color     var(--motion-fast) var(--ease-out);
}

/* Focus ring */
.input {
  transition: box-shadow var(--motion-fast) var(--ease-out),
              border-color var(--motion-fast) var(--ease-out);
}

/* Modal enter */
.modal {
  transition: opacity    var(--motion-normal) var(--ease-out),
              transform  var(--motion-normal) var(--ease-out);
}

/* Badge pop */
.badge-dot {
  animation: pop var(--motion-fast) var(--ease-spring);
}
```

---

## Anti-patterns

```css
/* BAD — raw duration */
.btn { transition: all 0.2s ease; }

/* GOOD */
.btn {
  transition: background-color var(--motion-fast) var(--ease-out),
              border-color     var(--motion-fast) var(--ease-out);
}
```

Avoid `transition: all` — it animates every property and causes unexpected jank on paint-only properties.
