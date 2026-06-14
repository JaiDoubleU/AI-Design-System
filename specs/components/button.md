# Button

**Name:** Button  
**Category:** Action  
**Status:** Stable  
**File:** `src/components/button.css`

---

## Overview

### When to use
- Primary actions: submit a form, confirm a dialog, trigger a key workflow step.
- Secondary actions: cancel, go back, open a secondary panel.
- Destructive actions: delete, remove, revoke access.

### When NOT to use
- Navigation to another page — use an `<a>` tag styled as a button only when the action is truly link-like.
- Toggle states with visual on/off — prefer a Switch component.
- Inline text actions inside a paragraph — prefer a plain link.

---

## Anatomy

```
┌─────────────────────────────────┐
│  [icon]   Label text            │
└─────────────────────────────────┘
 ↑           ↑
 .btn-icon   text content
 (optional)
```

1. **Container** (`.btn`) — the clickable root element
2. **Icon** (optional) — leading or trailing SVG icon
3. **Label** — descriptive text

---

## Tokens used

| Property | Token |
|---|---|
| `padding-block` | `--spacing-2` (default), `--spacing-1` (sm), `--spacing-3` (lg) |
| `padding-inline` | `--spacing-4` (default), `--spacing-3` (sm), `--spacing-6` (lg) |
| `font-family` | `--font-sans` |
| `font-size` | `--text-sm` (default), `--text-xs` (sm), `--text-md` (lg) |
| `font-weight` | `--weight-medium` |
| `line-height` | `--leading-tight` |
| `border-radius` | `--radius-md` (default/sm), `--radius-lg` (lg/xl) |
| `gap` | `--spacing-2` |
| `transition-duration` | `--motion-fast` |
| `transition-easing` | `--ease-out` |
| `outline-color` | `--color-border-focus` |
| `outline-offset` | `--spacing-1` |
| **Primary** `background` | `--color-interactive` |
| **Primary** `color` | `--color-interactive-fg` |
| **Primary** hover `background` | `--color-interactive-hover` |
| **Primary** active `background` | `--color-interactive-active` |
| **Secondary** `background` | `--color-bg` |
| **Secondary** `color` | `--color-text` |
| **Secondary** `border-color` | `--color-border-emphasis` |
| **Ghost** `background` | transparent |
| **Ghost** hover `background` | `--color-bg-muted` |
| **Danger** `background` | `--color-interactive-danger` |
| **Danger** `color` | `--color-interactive-danger-fg` |

---

## Props / API

| Class | Description |
|---|---|
| `.btn` | Required base class |
| `.btn-primary` | Primary/filled variant |
| `.btn-secondary` | Outlined variant |
| `.btn-ghost` | Ghost/text variant |
| `.btn-danger` | Destructive variant |
| `.btn-sm` | Small size |
| `.btn-lg` | Large size |
| `.btn-xl` | Extra-large size |
| `.btn-icon` | Square icon-only button |
| `.btn-full` | Full-width block button |

HTML attributes:
- `disabled` — disables the button (cursor: not-allowed, opacity: 0.45)
- `aria-disabled="true"` — visually disabled but keyboard focusable
- `aria-busy="true"` — loading state (cursor: wait)

---

## States

| State | Behaviour |
|---|---|
| **Default** | Filled/outlined per variant |
| **Hover** | Darker background (`--color-interactive-hover`) |
| **Active** | Deeper shade (`--color-interactive-active`) |
| **Focus** | 2px `--color-border-focus` outline, offset `--spacing-1` |
| **Disabled** | `opacity: 0.45`, `cursor: not-allowed`, `pointer-events: none` |
| **Loading** | `aria-busy="true"`, `opacity: 0.7`, `cursor: wait` |

---

## Code examples

```html
<!-- Primary -->
<button class="btn btn-primary">Save changes</button>

<!-- Secondary -->
<button class="btn btn-secondary">Cancel</button>

<!-- Ghost -->
<button class="btn btn-ghost">Learn more</button>

<!-- Destructive -->
<button class="btn btn-danger">Delete account</button>

<!-- Small -->
<button class="btn btn-primary btn-sm">Add tag</button>

<!-- Large -->
<button class="btn btn-primary btn-lg">Get started</button>

<!-- Icon only -->
<button class="btn btn-secondary btn-icon" aria-label="Close">
  <svg>…</svg>
</button>

<!-- With icon -->
<button class="btn btn-primary">
  <svg aria-hidden="true">…</svg>
  Export CSV
</button>

<!-- Loading -->
<button class="btn btn-primary" aria-busy="true">
  Saving…
</button>

<!-- Disabled -->
<button class="btn btn-primary" disabled>Submit</button>

<!-- Full width -->
<button class="btn btn-primary btn-full">Sign in</button>
```

---

## Cross-references

- `input.css` — buttons are often paired with form inputs
- `alert.css` — alert action buttons use `.btn-sm`
- `badge.css` — removable badge uses a `.badge-remove` (not a button class)
