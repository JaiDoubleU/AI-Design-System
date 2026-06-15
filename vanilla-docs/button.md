# Button

**Library:** Vanilla HTML/CSS/JS  
**CSS file:** `src/components/button.css`  
**Spec:** `specs/components/button.md`

---

## Overview

Triggers an action. Use semantic `<button>` or `<a>` elements. All styling is applied via CSS classes — no JavaScript required for basic usage.

---

## Setup

### HTML — link tags

```html
<!-- In your <head> — link order matters -->
<link rel="stylesheet" href="tokens.css">
<link rel="stylesheet" href="src/base/reset.css">
<link rel="stylesheet" href="src/components/button.css">
```

### CSS — bundler / PostCSS

```css
/* Via CSS @import (PostCSS / Vite / webpack) */
@import 'ai-design-system/tokens.css';
@import 'ai-design-system/src/base/reset.css';
@import 'ai-design-system/src/components/button.css';
```

---

## HTML examples

### Variants

```html
<button class="btn btn-primary">Primary</button>
<button class="btn btn-secondary">Secondary</button>
<button class="btn btn-ghost">Ghost</button>
<button class="btn btn-danger">Delete</button>
```

### Sizes

```html
<button class="btn btn-primary btn-sm">Small</button>
<button class="btn btn-primary">Default</button>
<button class="btn btn-primary btn-lg">Large</button>
<button class="btn btn-primary btn-xl">Extra large</button>
```

### Icon button

```html
<button class="btn btn-ghost btn-icon" aria-label="Settings">
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
    <circle cx="12" cy="12" r="3"/><path d="M12 1v4M12 19v4M4.22 4.22l2.83 2.83M16.95 16.95l2.83 2.83M1 12h4M19 12h4M4.22 19.78l2.83-2.83M16.95 7.05l2.83-2.83"/>
  </svg>
</button>
```

### Disabled state

```html
<button class="btn btn-primary" disabled>Disabled primary</button>
<button class="btn btn-secondary" disabled>Disabled secondary</button>
```

### Loading state

```html
<button class="btn btn-primary btn-loading" aria-busy="true" disabled>
  Saving…
</button>
```

> Add `.btn-loading` and `aria-busy="true"` while an async operation is in progress. Remove both when it resolves.

### Link styled as button

```html
<a href="/dashboard" class="btn btn-primary">Go to dashboard</a>
```

---

## JavaScript

```js
// Toggle a loading state during an async action
function setLoading(btn, loading) {
  btn.classList.toggle('btn-loading', loading);
  btn.setAttribute('aria-busy', String(loading));
  btn.disabled = loading;
}

document.querySelector('#save-btn').addEventListener('click', async function () {
  setLoading(this, true);
  try {
    await saveData();
  } finally {
    setLoading(this, false);
  }
});

// Confirm before a danger action
document.querySelector('#delete-btn').addEventListener('click', function () {
  if (!window.confirm('Delete this item? This cannot be undone.')) return;
  deleteItem();
});
```

---

## Class reference

See full API table: [`specs/components/button.md`](../specs/components/button.md)
