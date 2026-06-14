# Alert

**Name:** Alert  
**Category:** Feedback  
**Status:** Stable  
**File:** `src/components/alert.css`

---

## Overview

### When to use
- System-level feedback that requires user awareness: errors, successes, warnings, information.
- Form submission results.
- Inline validation feedback at the field-group level.
- Persistent banners for site-wide announcements.

### When NOT to use
- Single-field validation errors — use `.field-error-msg` from `input.css`.
- Non-actionable decorative messaging.
- Confirmation dialogs that require a user decision — use a Modal.

---

## Anatomy

```
┌─ .alert ─────────────────────────────────────────┐
│  [icon]  ┌─ .alert-content ─────────────────────┐│
│          │  .alert-title    "Payment failed"     ││
│          │  .alert-description  "Your card…"    ││
│          │                                       ││
│          │  ┌─ .alert-actions ─────────────────┐ ││
│          │  │  [btn-sm]  [btn-sm]               │ ││
│          │  └───────────────────────────────────┘ ││
│          └───────────────────────────────────────┘│
│                                          [×] .alert-close
└──────────────────────────────────────────────────┘
```

1. **Container** (`.alert`) — coloured background + border
2. **Icon** (`.alert-icon`) — optional, illustrates intent
3. **Content** (`.alert-content`) — wraps title, description, actions
4. **Title** (`.alert-title`) — bold summary line
5. **Description** (`.alert-description`) — supporting detail
6. **Actions** (`.alert-actions`) — inline action buttons
7. **Close** (`.alert-close`) — optional dismiss button

---

## Tokens used

| Property | Token |
|---|---|
| `padding` | `--spacing-4` (default), `--spacing-3` (sm), `--spacing-5`/`--spacing-6` (lg) |
| `gap` | `--spacing-3` |
| `border-radius` | `--radius-lg` (default), `--radius-none` (banner) |
| `font-family` | `--font-sans` |
| `font-size` | `--text-sm` (default), `--text-xs` (sm), `--text-md` (lg) |
| `line-height` | `--leading-normal` |
| **Info** `background` | `--color-bg-info` |
| **Info** `border-color` | `--color-border-focus` |
| **Info** `color` | `--color-text-info` |
| **Success** `background` | `--color-bg-success` |
| **Success** `border-color` | `--color-border-success` |
| **Success** `color` | `--color-text-success` |
| **Warning** `background` | `--color-bg-warning` |
| **Warning** `border-color` | `--color-border-emphasis` |
| **Warning** `color` | `--color-text-warning` |
| **Danger** `background` | `--color-bg-danger` |
| **Danger** `border-color` | `--color-border-danger` |
| **Danger** `color` | `--color-text-danger` |
| **Neutral** `background` | `--color-bg-muted` |
| **Neutral** `border-color` | `--color-border` |
| **Neutral** `color` | `--color-text` |
| `.alert-title` `font-weight` | `--weight-semibold` |
| `.alert-title` `line-height` | `--leading-tight` |
| `.alert-title` `margin-bottom` | `--spacing-1` |
| `.alert-actions` `gap` | `--spacing-2` |
| `.alert-actions` `margin-top` | `--spacing-3` |
| `.alert-icon` `width/height` | `--spacing-5` |
| `.alert-close` `width/height` | `--spacing-5` |
| `.alert-close` `transition` | `--motion-fast` + `--ease-out` |
| Toast `box-shadow` | `--shadow-lg` |
| Toast `border-radius` | `--radius-xl` |
| Toast `max-width` | `calc(--spacing-12 × 5)` |
| Toast region `bottom/right` | `--spacing-6` |
| Toast region `gap` | `--spacing-3` |
| Toast region `z-index` | `--z-toast` |

---

## Props / API

| Class | Description |
|---|---|
| `.alert` | Required base class |
| `.alert-info` | Blue informational |
| `.alert-success` | Green success |
| `.alert-warning` | Yellow warning |
| `.alert-danger` | Red error |
| `.alert-neutral` | Grey neutral |
| `.alert-solid-info` | Solid blue fill |
| `.alert-solid-success` | Solid green fill |
| `.alert-solid-danger` | Solid red fill |
| `.alert-sm` | Compact padding + xs text |
| `.alert-lg` | Generous padding + md text |
| `.alert-banner` | Full-width, no border-radius |
| `.alert-toast` | Floating toast with shadow |
| `.alert-icon` | Icon slot (SVG wrapper) |
| `.alert-content` | Text content wrapper |
| `.alert-title` | Bold title |
| `.alert-description` | Supporting text |
| `.alert-actions` | Row of action buttons |
| `.alert-close` | Dismiss button |
| `.toast-region` | Fixed-position toast container |

---

## States

| State | Behaviour |
|---|---|
| **Default** | Visible with semantic colour |
| **Dismissed** | Hidden via JS (remove from DOM or `display: none`) |
| **Close hover** | `opacity: 1` on `.alert-close` |

---

## Code examples

```html
<!-- Info -->
<div class="alert alert-info" role="status">
  <svg class="alert-icon" aria-hidden="true">…</svg>
  <div class="alert-content">
    <strong class="alert-title">Heads up</strong>
    <p class="alert-description">Your free trial ends in 3 days.</p>
    <div class="alert-actions">
      <button class="btn btn-sm btn-secondary">Dismiss</button>
      <button class="btn btn-sm btn-primary">Upgrade</button>
    </div>
  </div>
</div>

<!-- Danger -->
<div class="alert alert-danger" role="alert">
  <div class="alert-content">
    <strong class="alert-title">Payment failed</strong>
    <p class="alert-description">Your card ending in 4242 was declined.</p>
  </div>
  <button class="alert-close" aria-label="Dismiss">×</button>
</div>

<!-- Success (no icon) -->
<div class="alert alert-success" role="status">
  <div class="alert-content">
    <strong class="alert-title">Profile saved</strong>
  </div>
</div>

<!-- Banner -->
<div class="alert alert-warning alert-banner" role="status">
  <div class="alert-content">
    <strong class="alert-title">Scheduled maintenance</strong>
    <p class="alert-description">We'll be down on Saturday 02:00–04:00 UTC.</p>
  </div>
</div>

<!-- Toast container (place at body level) -->
<div class="toast-region" aria-live="polite">
  <div class="alert alert-toast alert-success" role="status">
    <div class="alert-content">
      <strong class="alert-title">Saved successfully</strong>
    </div>
    <button class="alert-close" aria-label="Dismiss">×</button>
  </div>
</div>
```

---

## Cross-references

- `button.css` — action buttons inside `.alert-actions`
- `badge.css` — status labels that replace alerts for non-critical info
- `input.css` — `.field-error-msg` for single-field validation
