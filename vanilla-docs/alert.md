# Alert

**Library:** Vanilla HTML/CSS/JS  
**CSS file:** `src/components/alert.css`  
**Spec:** `specs/components/alert.md`

---

## Overview

Contextual feedback for user actions or system events. Use `role="alert"` for important errors and `role="status"` for informational or success messages.

---

## Setup

### HTML — link tags

```html
<!-- In your <head> — link order matters -->
<link rel="stylesheet" href="tokens.css">
<link rel="stylesheet" href="src/base/reset.css">
<link rel="stylesheet" href="src/components/alert.css">
<link rel="stylesheet" href="src/components/button.css">
```

### CSS — bundler / PostCSS

```css
/* Via CSS @import (PostCSS / Vite / webpack) */
@import 'ai-design-system/tokens.css';
@import 'ai-design-system/src/base/reset.css';
@import 'ai-design-system/src/components/alert.css';
@import 'ai-design-system/src/components/button.css';
```

---

## HTML examples

### Info alert

```html
<div class="alert alert-info" role="status">
  <div class="alert-content">
    <strong class="alert-title">Heads up</strong>
    <p class="alert-description">Your free trial ends in 3 days.</p>
    <div class="alert-actions">
      <button class="btn btn-sm btn-secondary">Dismiss</button>
      <button class="btn btn-sm btn-primary">Upgrade now</button>
    </div>
  </div>
</div>
```

### Danger alert

```html
<div class="alert alert-danger" role="alert">
  <div class="alert-content">
    <strong class="alert-title">Payment failed</strong>
    <p class="alert-description">Your card ending in 4242 was declined.</p>
  </div>
  <button class="alert-close" type="button" aria-label="Dismiss">×</button>
</div>
```

### Success alert

```html
<div class="alert alert-success" role="status">
  <div class="alert-content">
    <strong class="alert-title">Profile saved</strong>
    <p class="alert-description">Your changes have been applied.</p>
  </div>
</div>
```

### Warning alert

```html
<div class="alert alert-warning" role="status">
  <div class="alert-content">
    <strong class="alert-title">Storage almost full</strong>
    <p class="alert-description">You've used 90% of your 5 GB allowance.</p>
  </div>
</div>
```

### Banner (full-width, no radius)

```html
<div class="alert alert-warning alert-banner" role="status">
  <div class="alert-content">
    <strong class="alert-title">Scheduled maintenance</strong>
    <p class="alert-description">The service will be unavailable Saturday 02:00–04:00 UTC.</p>
  </div>
</div>
```

### Toast (floating notification)

```html
<!-- Place this at the end of <body> -->
<div class="toast-region" aria-live="polite" aria-atomic="false">
  <!-- Toasts are injected here by JavaScript — see JS section below -->
</div>
```

> The `.toast-region` is a fixed-position container. Inject `.alert-toast` elements into it via JavaScript.

---

## JavaScript

```js
// Dismiss an alert by clicking its close button
document.addEventListener('click', e => {
  const closeBtn = e.target.closest('.alert-close');
  if (!closeBtn) return;
  const alert = closeBtn.closest('.alert');
  alert.setAttribute('aria-hidden', 'true');
  // Remove after CSS transition completes (or immediately if no transition)
  alert.addEventListener('transitionend', () => alert.remove(), { once: true });
  setTimeout(() => alert.remove(), 400); // fallback
});

// Dismiss an alert programmatically
function dismissAlert(alertEl) {
  alertEl.setAttribute('aria-hidden', 'true');
  alertEl.addEventListener('transitionend', () => alertEl.remove(), { once: true });
  setTimeout(() => alertEl.remove(), 400);
}

// Create and show a toast notification
function showToast({ title, description = '', variant = 'info', duration = 5000 }) {
  const region = document.querySelector('.toast-region');
  if (!region) return;

  const toast = document.createElement('div');
  toast.className = `alert alert-toast alert-${variant}`;
  toast.setAttribute('role', variant === 'danger' ? 'alert' : 'status');
  toast.innerHTML = `
    <div class="alert-content">
      <strong class="alert-title">${title}</strong>
      ${description ? `<p class="alert-description">${description}</p>` : ''}
    </div>
    <button class="alert-close" type="button" aria-label="Dismiss">×</button>
  `;

  region.appendChild(toast);

  // Auto-dismiss
  const timer = duration > 0 ? setTimeout(() => dismissAlert(toast), duration) : null;

  // Manual dismiss
  toast.querySelector('.alert-close').addEventListener('click', () => {
    if (timer) clearTimeout(timer);
    dismissAlert(toast);
  });
}

// Usage examples:
// showToast({ title: 'Saved successfully', variant: 'success' });
// showToast({ title: 'Upload failed', description: 'File exceeds 10 MB limit.', variant: 'danger', duration: 0 });
```

---

## Class reference

See full API table: [`specs/components/alert.md`](../specs/components/alert.md)
