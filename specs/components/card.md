# Card

**Name:** Card  
**Category:** Layout / Container  
**Status:** Stable  
**File:** `src/components/card.css`

---

## Overview

### When to use
- Group related content into a visual unit: article previews, settings panels, profile summaries.
- Present a discrete item in a list or grid.
- Contain an action + context together (e.g., a pricing tier).

### When NOT to use
- Full-page layout sections — use semantic HTML and spacing tokens directly.
- Simple text groupings that don't need visual separation.
- Lists of data that would be clearer in a table.

---

## Anatomy

```
┌─ .card ─────────────────────────────────────┐
│ ┌─ .card-header ────────────────────────── ┐ │
│ │  .card-title         [action button]     │ │
│ │  .card-subtitle                          │ │
│ └──────────────────────────────────────────┘ │
│                                              │
│ ┌─ .card-media ─────────────────────────── ┐ │
│ │  <img>                                   │ │
│ └──────────────────────────────────────────┘ │
│                                              │
│ ┌─ .card-body ──────────────────────────── ┐ │
│ │  Content                                 │ │
│ └──────────────────────────────────────────┘ │
│                                              │
│ ┌─ .card-footer ────────────────────────── ┐ │
│ │  [secondary action]    [primary action]  │ │
│ └──────────────────────────────────────────┘ │
└──────────────────────────────────────────────┘
```

Parts are all optional — use only what the content requires.

---

## Tokens used

| Property | Token |
|---|---|
| `background-color` | `--color-bg` (default), `--color-bg-subtle` (flat), transparent (ghost) |
| `border-color` | `--color-border` (default), transparent (elevated/ghost) |
| `border-radius` | `--radius-xl` |
| `box-shadow` | `--shadow-sm` (default), `--shadow-md` (elevated), `--shadow-none` (flat/ghost) |
| `.card-header` `padding` | `--spacing-4` block, `--spacing-5` inline |
| `.card-header` `border-color` | `--color-border-subtle` |
| `.card-header` `gap` | `--spacing-3` |
| `.card-body` `padding` | `--spacing-5` |
| `.card-footer` `padding` | `--spacing-4` block, `--spacing-5` inline |
| `.card-footer` `background` | `--color-bg-subtle` |
| `.card-footer` `gap` | `--spacing-3` |
| `.card-title` `font-size` | `--text-md` |
| `.card-title` `font-weight` | `--weight-semibold` |
| `.card-title` `line-height` | `--leading-tight` |
| `.card-title` `color` | `--color-text` |
| `.card-subtitle` `font-size` | `--text-sm` |
| `.card-subtitle` `color` | `--color-text-subtle` |
| `.card-interactive` `transition` | `--motion-fast` + `--ease-out` |
| Interactive hover `box-shadow` | `--shadow-md` |
| Interactive hover `border-color` | `--color-border-emphasis` |
| `.card-group` `gap` | `--spacing-4` |
| Danger `background` | `--color-bg-danger` |
| Danger `border-color` | `--color-border-danger` |
| Success `background` | `--color-bg-success` |
| Success `border-color` | `--color-border-success` |

---

## Props / API

| Class | Description |
|---|---|
| `.card` | Base card (border + shadow-sm) |
| `.card-elevated` | Stronger shadow, no border |
| `.card-flat` | Subtle background, no shadow |
| `.card-ghost` | Transparent, no border or shadow |
| `.card-interactive` | Hover/active state, pointer cursor |
| `.card-header` | Top section with border-bottom |
| `.card-body` | Main content area |
| `.card-body-sm` | Compact body padding |
| `.card-body-lg` | Generous body padding |
| `.card-footer` | Bottom section with border-top |
| `.card-title` | Card heading inside header |
| `.card-subtitle` | Sub-heading inside header |
| `.card-media` | Full-width image (16/9) |
| `.card-media-sm` | Image at 4/3 ratio |
| `.card-media-sq` | Square image |
| `.card-danger` | Red tinted card |
| `.card-success` | Green tinted card |
| `.card-warning` | Yellow tinted card |
| `.card-info` | Blue tinted card |
| `.card-group` | CSS grid wrapper |
| `.card-group-2` / `-3` / `-4` | 2/3/4 column grids |

---

## States

| State | Behaviour |
|---|---|
| **Default** | `--shadow-sm`, `--color-border` |
| **Hover** (interactive only) | `--shadow-md`, `--color-border-emphasis` |
| **Active** (interactive only) | `--shadow-xs` |
| **Focus** (interactive only) | 2px `--color-border-focus` outline |

---

## Code examples

```html
<!-- Basic card -->
<div class="card">
  <div class="card-body">
    <p>Content goes here.</p>
  </div>
</div>

<!-- Full structure -->
<div class="card">
  <div class="card-header">
    <div>
      <h3 class="card-title">Project Alpha</h3>
      <p class="card-subtitle">Last updated 2 hours ago</p>
    </div>
    <button class="btn btn-ghost btn-sm">Edit</button>
  </div>
  <div class="card-body">
    <p>Main card content.</p>
  </div>
  <div class="card-footer">
    <button class="btn btn-secondary btn-sm">Cancel</button>
    <button class="btn btn-primary btn-sm">Save</button>
  </div>
</div>

<!-- Interactive card (clickable) -->
<article class="card card-interactive" tabindex="0" role="button">
  <img class="card-media" src="cover.jpg" alt="Article cover">
  <div class="card-body">
    <h3 class="card-title">Article Title</h3>
    <p>Summary text…</p>
  </div>
</article>

<!-- Status variant -->
<div class="card card-danger">
  <div class="card-body">
    <strong>Action required:</strong> Your subscription expired.
  </div>
</div>

<!-- Card grid -->
<div class="card-group card-group-3">
  <div class="card"><div class="card-body">One</div></div>
  <div class="card"><div class="card-body">Two</div></div>
  <div class="card"><div class="card-body">Three</div></div>
</div>
```

---

## Cross-references

- `button.css` — footer actions
- `badge.css` — status badges in card headers
- `alert.css` — error state alternatives to `.card-danger`
- `typography.css` — `.prose` for long body content inside `.card-body`
