# Card

**Library:** Vanilla HTML/CSS/JS  
**CSS file:** `src/components/card.css`  
**Spec:** `specs/components/card.md`

---

## Overview

Groups related content into a visual container. All parts (header, body, footer, media) are optional.

---

## Setup

### HTML — link tags

```html
<!-- In your <head> — link order matters -->
<link rel="stylesheet" href="tokens.css">
<link rel="stylesheet" href="src/base/reset.css">
<link rel="stylesheet" href="src/components/card.css">
<link rel="stylesheet" href="src/components/button.css">
```

### CSS — bundler / PostCSS

```css
/* Via CSS @import (PostCSS / Vite / webpack) */
@import 'ai-design-system/tokens.css';
@import 'ai-design-system/src/base/reset.css';
@import 'ai-design-system/src/components/card.css';
@import 'ai-design-system/src/components/button.css';
```

---

## HTML examples

### Minimal card

```html
<div class="card">
  <div class="card-body">
    <p>Simple content with no header or footer.</p>
  </div>
</div>
```

### Full structure

```html
<div class="card">
  <div class="card-header">
    <div>
      <h3 class="card-title">Project Alpha</h3>
      <p class="card-subtitle">Last updated 2 hours ago</p>
    </div>
    <button class="btn btn-ghost btn-sm">Edit</button>
  </div>
  <div class="card-body">
    <p>Main card content goes here.</p>
  </div>
  <div class="card-footer">
    <button class="btn btn-secondary btn-sm">Cancel</button>
    <button class="btn btn-primary btn-sm">Save</button>
  </div>
</div>
```

### Card with media

```html
<article class="card">
  <img class="card-media" src="cover.jpg" alt="Article cover image">
  <div class="card-body">
    <h3 class="card-title">Article headline</h3>
    <p>Summary text that introduces the article.</p>
  </div>
</article>
```

### Interactive (clickable) card

```html
<article class="card card-interactive" tabindex="0" role="button" aria-label="Open Project Alpha">
  <div class="card-body">
    <h3 class="card-title">Clickable card</h3>
    <p>Entire card surface is interactive.</p>
  </div>
</article>
```

### Variants

```html
<div class="card card-elevated">
  <div class="card-body">Elevated — stronger shadow, no border</div>
</div>

<div class="card card-flat">
  <div class="card-body">Flat — subtle background, no shadow</div>
</div>

<div class="card card-danger">
  <div class="card-body"><strong>Action required:</strong> Your subscription expired.</div>
</div>

<div class="card card-success">
  <div class="card-body"><strong>Setup complete:</strong> Your account is ready.</div>
</div>
```

### Card grid

```html
<div class="card-group card-group-3">
  <div class="card"><div class="card-body">Card one</div></div>
  <div class="card"><div class="card-body">Card two</div></div>
  <div class="card"><div class="card-body">Card three</div></div>
</div>
```

> Use `.card-group-2`, `.card-group-3`, or `.card-group-4` for responsive column grids.

---

## JavaScript

```js
// Handle interactive card click (keyboard + mouse)
document.querySelectorAll('.card-interactive').forEach(card => {
  function activate() {
    const href = card.dataset.href;
    if (href) window.location.href = href;
  }

  card.addEventListener('click', activate);
  card.addEventListener('keydown', e => {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      activate();
    }
  });
});
```

---

## Class reference

See full API table: [`specs/components/card.md`](../specs/components/card.md)
