# Badge

**Library:** Vanilla HTML/CSS/JS  
**CSS file:** `src/components/badge.css`  
**Spec:** `specs/components/badge.md`

---

## Overview

Short status label or count indicator. Use `<span>` for non-interactive badges and `<button>` semantics when the badge itself is clickable.

---

## Setup

### HTML — link tags

```html
<!-- In your <head> — link order matters -->
<link rel="stylesheet" href="tokens.css">
<link rel="stylesheet" href="src/base/reset.css">
<link rel="stylesheet" href="src/components/badge.css">
```

### CSS — bundler / PostCSS

```css
/* Via CSS @import (PostCSS / Vite / webpack) */
@import 'ai-design-system/tokens.css';
@import 'ai-design-system/src/base/reset.css';
@import 'ai-design-system/src/components/badge.css';
```

---

## HTML examples

### Semantic variants

```html
<span class="badge badge-default">Default</span>
<span class="badge badge-primary">Primary</span>
<span class="badge badge-success">Active</span>
<span class="badge badge-danger">Expired</span>
<span class="badge badge-warning">Pending</span>
<span class="badge badge-info">Info</span>
```

### Solid variants

```html
<span class="badge badge-solid-primary">New</span>
<span class="badge badge-solid-success">Verified</span>
<span class="badge badge-solid-danger">Error</span>
<span class="badge badge-solid-warning">Review</span>
```

### Dot indicator

```html
<span class="badge badge-success badge-dot">Online</span>
<span class="badge badge-danger badge-dot">Offline</span>
<span class="badge badge-warning badge-dot">Away</span>
```

### Count badge

```html
<!-- Standalone count -->
<span class="badge badge-count badge-solid-danger" aria-label="12 unread">12</span>

<!-- Count adjacent to a nav link -->
<a href="/inbox" style="display:inline-flex;align-items:center;gap:6px;">
  Inbox
  <span class="badge badge-count badge-solid-danger" aria-label="3 unread">3</span>
</a>
```

### Removable tag

```html
<span class="badge badge-primary" id="tag-design">
  Design
  <button class="badge-remove" type="button" aria-label="Remove Design tag">×</button>
</span>

<span class="badge badge-primary" id="tag-ux">
  UX Research
  <button class="badge-remove" type="button" aria-label="Remove UX Research tag">×</button>
</span>
```

### Sizes

```html
<span class="badge badge-success badge-sm">Small</span>
<span class="badge badge-success">Default</span>
<span class="badge badge-success badge-lg">Large</span>
```

---

## JavaScript

```js
// Remove a tag when its × button is clicked
document.addEventListener('click', e => {
  const removeBtn = e.target.closest('.badge-remove');
  if (!removeBtn) return;
  const badge = removeBtn.closest('.badge');
  badge.remove();
});

// Dynamically update a count badge
function setCount(selector, count) {
  const el = document.querySelector(selector);
  if (!el) return;
  el.textContent = count;
  el.setAttribute('aria-label', `${count} unread`);
  el.style.display = count === 0 ? 'none' : '';
}

// Example: update unread count after reading messages
setCount('.badge-count[aria-label*="unread"]', 0);
```

---

## Class reference

See full API table: [`specs/components/badge.md`](../specs/components/badge.md)
