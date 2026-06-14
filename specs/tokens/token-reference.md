# Token Reference

**Master map of every CSS custom property, its resolved value, and when to use it.**  
All Layer 2 tokens live in `tokens.css`. Components must reference only Layer 2 tokens.

---

## How to read this table

| Column | Meaning |
|---|---|
| **Token** | CSS custom property name (Layer 2) |
| **Resolves to** | Layer 1 primitive or upstream DS hook |
| **Default value** | The rendered value when no upstream DS is set |
| **Use when** |  Guidance on correct usage |

---

## Colors — Text

| Token | Default value | Use when |
|---|---|---|
| `--color-text` | `#212529` | Default text on light background |
| `--color-text-subtle` | `#868e96` | Secondary labels, sub-text |
| `--color-text-muted` | `#adb5bd` | Placeholder, tertiary text |
| `--color-text-disabled` | `#ced4da` | Text in disabled state |
| `--color-text-inverse` | `#ffffff` | Text on dark / emphasis background |
| `--color-text-link` | `#3182ce` | Anchor / hyperlink color |
| `--color-text-link-hover` | `#2b6cb0` | Anchor hover/focus |
| `--color-text-danger` | `#c53030` | Error messages, destructive confirmations |
| `--color-text-success` | `#2f855a` | Confirmation messages |
| `--color-text-warning` | `#b7791f` | Caution messages |
| `--color-text-info` | `#3182ce` | Informational callouts |

## Colors — Background

| Token | Default value | Use when |
|---|---|---|
| `--color-bg` | `#ffffff` | Default page / card surface |
| `--color-bg-subtle` | `#f8f9fa` | Slightly raised surface |
| `--color-bg-muted` | `#f1f3f5` | Inputs, code blocks, chips |
| `--color-bg-emphasis` | `#343a40` | Inverted (dark) surface |
| `--color-bg-inverse` | `#212529` | Full dark background |
| `--color-bg-danger` | `#fff5f5` | Error state fill |
| `--color-bg-success` | `#f0fff4` | Success state fill |
| `--color-bg-warning` | `#fffff0` | Warning state fill |
| `--color-bg-info` | `#e8f4fd` | Info state fill |

## Colors — Border

| Token | Default value | Use when |
|---|---|---|
| `--color-border` | `#e9ecef` | Default card / container border |
| `--color-border-subtle` | `#f1f3f5` | Section dividers |
| `--color-border-emphasis` | `#ced4da` | Stronger borders, input default |
| `--color-border-focus` | `#4299e1` | Keyboard focus outline |
| `--color-border-danger` | `#e53e3e` | Invalid input border |
| `--color-border-success` | `#38a169` | Valid input border |

## Colors — Interactive

| Token | Default value | Use when |
|---|---|---|
| `--color-interactive` | `#3182ce` | Primary button fill, key actions |
| `--color-interactive-hover` | `#2b6cb0` | Primary button hover |
| `--color-interactive-active` | `#2c5282` | Primary button active/pressed |
| `--color-interactive-muted` | `#e8f4fd` | Subtle interactive fill, focus ring bg |
| `--color-interactive-fg` | `#ffffff` | Text / icon on interactive fill |
| `--color-interactive-danger` | `#e53e3e` | Destructive button fill |
| `--color-interactive-danger-hover` | `#c53030` | Destructive button hover |
| `--color-interactive-danger-fg` | `#ffffff` | Text on destructive fill |

## Colors — Overlay

| Token | Default value | Use when |
|---|---|---|
| `--color-overlay` | `#212529` | Backdrop base colour |
| `--color-overlay-alpha` | `rgb(33 37 41 / 0.5)` | Semi-transparent modal backdrop |

---

## Spacing

| Token | Default value | px |
|---|---|---|
| `--spacing-0` | `0` | 0 |
| `--spacing-1` | `0.25rem` | 4 |
| `--spacing-2` | `0.5rem` | 8 |
| `--spacing-3` | `0.75rem` | 12 |
| `--spacing-4` | `1rem` | 16 |
| `--spacing-5` | `1.25rem` | 20 |
| `--spacing-6` | `1.5rem` | 24 |
| `--spacing-8` | `2rem` | 32 |
| `--spacing-10` | `2.5rem` | 40 |
| `--spacing-12` | `3rem` | 48 |
| `--spacing-16` | `4rem` | 64 |
| `--spacing-20` | `5rem` | 80 |
| `--spacing-24` | `6rem` | 96 |

---

## Typography — Families

| Token | Default value |
|---|---|
| `--font-sans` | Inter, system-ui, … |
| `--font-mono` | JetBrains Mono, Fira Code, … |
| `--font-serif` | Georgia, Times New Roman |

## Typography — Sizes

| Token | Default value | px |
|---|---|---|
| `--text-xs` | `0.75rem` | 12 |
| `--text-sm` | `0.875rem` | 14 |
| `--text-md` | `1rem` | 16 |
| `--text-lg` | `1.125rem` | 18 |
| `--text-xl` | `1.25rem` | 20 |
| `--text-2xl` | `1.5rem` | 24 |
| `--text-3xl` | `1.875rem` | 30 |
| `--text-4xl` | `2.25rem` | 36 |
| `--text-5xl` | `3rem` | 48 |

## Typography — Weights

| Token | Default value |
|---|---|
| `--weight-normal` | `400` |
| `--weight-medium` | `500` |
| `--weight-semibold` | `600` |
| `--weight-bold` | `700` |

## Typography — Line heights

| Token | Default value |
|---|---|
| `--leading-tight` | `1.2` |
| `--leading-snug` | `1.375` |
| `--leading-normal` | `1.5` |
| `--leading-relaxed` | `1.625` |
| `--leading-loose` | `2` |

---

## Border radius

| Token | Default value | px |
|---|---|---|
| `--radius-none` | `0` | 0 |
| `--radius-sm` | `0.125rem` | 2 |
| `--radius-md` | `0.25rem` | 4 |
| `--radius-lg` | `0.5rem` | 8 |
| `--radius-xl` | `0.75rem` | 12 |
| `--radius-2xl` | `1rem` | 16 |
| `--radius-full` | `9999px` | pill |

---

## Elevation — Shadows

| Token | When to use |
|---|---|
| `--shadow-none` | Flat / ghost variant |
| `--shadow-xs` | Chip, inline element |
| `--shadow-sm` | Default card |
| `--shadow-md` | Elevated card, popover |
| `--shadow-lg` | Dropdown menu, tooltip |
| `--shadow-xl` | Modal / dialog |
| `--shadow-2xl` | Drawer, deep overlay |
| `--shadow-inner` | Pressed state, inset input |

## Elevation — Z-index

| Token | Value | When to use |
|---|---|---|
| `--z-below` | `-1` | Pseudo behind content |
| `--z-base` | `0` | Normal flow |
| `--z-raised` | `10` | Sticky headers, raised cards |
| `--z-dropdown` | `100` | Dropdowns |
| `--z-sticky` | `200` | Sticky nav |
| `--z-overlay` | `300` | Backdrop |
| `--z-modal` | `400` | Dialogs |
| `--z-popover` | `500` | Floating panels |
| `--z-toast` | `600` | Toasts |
| `--z-tooltip` | `700` | Tooltips |

---

## Motion — Durations

| Token | Value | When to use |
|---|---|---|
| `--motion-instant` | `0ms` | Programmatic / no animation |
| `--motion-fast` | `150ms` | Hover, focus ring |
| `--motion-normal` | `250ms` | Standard enter/exit |
| `--motion-slow` | `400ms` | Modal, panel |
| `--motion-slower` | `600ms` | Page transitions |

## Motion — Easing

| Token | Curve | When to use |
|---|---|---|
| `--ease-linear` | `linear` | Progress |
| `--ease-in` | ease-in cubic | Exit |
| `--ease-out` | ease-out cubic | Enter |
| `--ease-in-out` | standard cubic | State change |
| `--ease-spring` | spring cubic | Playful |

---

## Upstream DS hook reference

Every Layer 2 token accepts a `--ds-*` override. The mapping is one-to-one:

```
--color-text          ← --ds-text
--color-bg            ← --ds-bg
--spacing-4           ← --ds-spacing-4
--text-md             ← --ds-text-md
--weight-semibold     ← --ds-weight-semibold
--leading-normal      ← --ds-leading-normal
--radius-lg           ← --ds-radius-lg
--shadow-md           ← --ds-shadow-md
--z-modal             ← --ds-z-modal
--motion-fast         ← --ds-motion-fast
--ease-out            ← --ds-ease-out
```

Set any subset of `--ds-*` variables to integrate a third-party design system.
