# Badge

**Name:** Badge  
**Category:** Status / Label  
**Status:** Stable  
**File:** `src/components/badge.css`

---

## Overview

### When to use
- Communicate status, category, or count at a glance: "New", "Draft", "5 unread".
- Tag content with metadata that aids scanning: "Featured", "Beta".
- Show a count alongside a nav item or button.

### When NOT to use
- Long text labels (more than 3–4 words) — use a chip or tag component.
- Interactive affordances (clicking to filter) — add button semantics explicitly.
- Error / warning messages — use Alert instead.

---

## Anatomy

```
┌─ .badge ──────────────────┐
│  [dot]  Label text  [×]   │
└───────────────────────────┘
 ↑         ↑          ↑
 .badge-dot text      .badge-remove
 (opt)                (opt)
```

---

## Tokens used

| Property | Token |
|---|---|
| `padding-block` | `--spacing-1` (default), `--spacing-0` (sm), `--spacing-2` (lg) |
| `padding-inline` | `--spacing-2` (default), `--spacing-1` (sm), `--spacing-3` (lg) |
| `font-family` | `--font-sans` |
| `font-size` | `--text-xs` (default/sm), `--text-sm` (lg) |
| `font-weight` | `--weight-medium` |
| `line-height` | `--leading-tight` |
| `border-radius` | `--radius-full` (pill), `--radius-md` (lg variant) |
| `gap` | `--spacing-1` |
| **Default** `background` | `--color-bg-muted` |
| **Default** `color` | `--color-text-subtle` |
| **Default** `border-color` | `--color-border` |
| **Primary** `background` | `--color-interactive-muted` |
| **Primary** `color` | `--color-interactive-active` |
| **Primary** `border-color` | `--color-interactive` |
| **Success** `background` | `--color-bg-success` |
| **Success** `color` | `--color-text-success` |
| **Danger** `background` | `--color-bg-danger` |
| **Danger** `color` | `--color-text-danger` |
| **Warning** `background` | `--color-bg-warning` |
| **Warning** `color` | `--color-text-warning` |
| **Info** `background` | `--color-bg-info` |
| **Info** `color` | `--color-text-info` |
| `.badge-count` `min-width` | `--spacing-5` |
| `.badge-count` `height` | `--spacing-5` |
| `.badge-remove` `width/height` | `--spacing-3` |
| `.badge-remove` `transition` | `--motion-fast` + `--ease-out` |

---

## Props / API

| Class | Description |
|---|---|
| `.badge` | Required base class |
| `.badge-default` | Neutral grey |
| `.badge-primary` | Blue tinted |
| `.badge-success` | Green tinted |
| `.badge-danger` | Red tinted |
| `.badge-warning` | Yellow tinted |
| `.badge-info` | Blue tinted (same as primary but separate intent) |
| `.badge-solid-primary` | Solid blue fill |
| `.badge-solid-success` | Solid green fill |
| `.badge-solid-danger` | Solid red fill |
| `.badge-solid-warning` | Solid yellow fill |
| `.badge-sm` | Smaller padding |
| `.badge-lg` | Larger, rounded-md |
| `.badge-dot` | Adds a dot indicator before text |
| `.badge-count` | Square count chip (number bubbles) |
| `.badge-remove` | Dismiss button inside badge |

---

## States

| State | Behaviour |
|---|---|
| **Default** | Semantic variant colours |
| **Hover** (remove button) | `opacity: 1` |
| No interactive state on badge itself; add button semantics when needed |

---

## Code examples

```html
<!-- Status badges -->
<span class="badge badge-success badge-dot">Active</span>
<span class="badge badge-danger">Expired</span>
<span class="badge badge-warning">Pending</span>
<span class="badge badge-default">Draft</span>

<!-- Solid -->
<span class="badge badge-solid-primary">New</span>

<!-- Count -->
<span class="badge badge-count badge-solid-danger">5</span>

<!-- Removable tag -->
<span class="badge badge-primary">
  Design
  <button class="badge-remove" aria-label="Remove Design tag">×</button>
</span>

<!-- In nav (unread indicator) -->
<a href="/inbox">
  Inbox
  <span class="badge badge-count badge-solid-danger" aria-label="12 unread">12</span>
</a>
```

---

## Cross-references

- `card.css` — badges appear inside `.card-header`
- `button.css` — count badges appear adjacent to buttons
- `alert.css` — for message-level status (not just a label)
