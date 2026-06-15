# Input

**Library:** Vanilla HTML/CSS/JS  
**CSS file:** `src/components/input.css`  
**Spec:** `specs/components/input.md`

---

## Overview

Form controls: text input, textarea, select, checkbox, and radio. Wrap inputs in `.field` for labels, hints, and error messages.

---

## Setup

### HTML — link tags

```html
<!-- In your <head> — link order matters -->
<link rel="stylesheet" href="tokens.css">
<link rel="stylesheet" href="src/base/reset.css">
<link rel="stylesheet" href="src/components/input.css">
```

### CSS — bundler / PostCSS

```css
/* Via CSS @import (PostCSS / Vite / webpack) */
@import 'ai-design-system/tokens.css';
@import 'ai-design-system/src/base/reset.css';
@import 'ai-design-system/src/components/input.css';
```

---

## HTML examples

### Text field

```html
<div class="field">
  <label class="field-label" for="username">Username</label>
  <input class="input" id="username" type="text" placeholder="e.g. jsmith" autocomplete="username">
  <p class="field-hint">Only letters, numbers, and underscores.</p>
</div>
```

### Error state

```html
<div class="field field-error">
  <label class="field-label" for="email">Email</label>
  <input class="input" id="email" type="email" value="not-an-email"
         aria-describedby="email-error" aria-invalid="true">
  <p class="field-error-msg" id="email-error" role="alert">
    Enter a valid email address.
  </p>
</div>
```

### Password field

```html
<div class="field">
  <label class="field-label" for="password">Password</label>
  <div class="input-group">
    <input class="input" id="password" type="password" autocomplete="current-password">
    <button class="btn btn-ghost btn-icon input-addon" type="button" aria-label="Show password">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
        <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/>
      </svg>
    </button>
  </div>
</div>
```

### Textarea

```html
<div class="field">
  <label class="field-label" for="bio">Bio</label>
  <textarea class="textarea" id="bio" rows="4"
            placeholder="Tell us about yourself…"
            maxlength="280" aria-describedby="bio-count"></textarea>
  <p class="field-hint" id="bio-count">0 / 280</p>
</div>
```

### Select

```html
<div class="field">
  <label class="field-label" for="country">Country</label>
  <select class="select" id="country">
    <option value="">Select a country…</option>
    <option value="us">United States</option>
    <option value="gb">United Kingdom</option>
    <option value="ca">Canada</option>
  </select>
</div>
```

### Checkbox group

```html
<fieldset>
  <legend class="field-label">Notifications</legend>
  <label class="field-checkbox">
    <input class="checkbox" type="checkbox" name="notify" value="email" checked>
    Email
  </label>
  <label class="field-checkbox">
    <input class="checkbox" type="checkbox" name="notify" value="sms">
    SMS
  </label>
  <label class="field-checkbox">
    <input class="checkbox" type="checkbox" name="notify" value="push">
    Push
  </label>
</fieldset>
```

### Radio group

```html
<fieldset>
  <legend class="field-label">Plan</legend>
  <label class="field-radio">
    <input class="radio" type="radio" name="plan" value="free" checked>
    Free
  </label>
  <label class="field-radio">
    <input class="radio" type="radio" name="plan" value="pro">
    Pro — $12/mo
  </label>
  <label class="field-radio">
    <input class="radio" type="radio" name="plan" value="team">
    Team — $39/mo
  </label>
</fieldset>
```

### Input group (prefix / suffix)

```html
<!-- With prefix -->
<div class="field">
  <label class="field-label" for="handle">Twitter handle</label>
  <div class="input-group">
    <span class="input-addon">@</span>
    <input class="input" id="handle" type="text" placeholder="username">
  </div>
</div>

<!-- With suffix -->
<div class="field">
  <label class="field-label" for="price">Price</label>
  <div class="input-group">
    <input class="input" id="price" type="number" min="0" step="0.01">
    <span class="input-addon">USD</span>
  </div>
</div>
```

---

## JavaScript

```js
// Live character counter for a textarea
const bio   = document.querySelector('#bio');
const count = document.querySelector('#bio-count');
bio.addEventListener('input', () => {
  count.textContent = `${bio.value.length} / ${bio.maxLength}`;
});

// Show/hide password toggle
document.querySelectorAll('[aria-label="Show password"]').forEach(btn => {
  btn.addEventListener('click', () => {
    const input = btn.closest('.input-group').querySelector('input');
    const isHidden = input.type === 'password';
    input.type = isHidden ? 'text' : 'password';
    btn.setAttribute('aria-label', isHidden ? 'Hide password' : 'Show password');
  });
});

// Inline validation — mark field invalid on blur
document.querySelectorAll('.field .input').forEach(input => {
  input.addEventListener('blur', () => {
    const field = input.closest('.field');
    const valid = input.checkValidity();
    field.classList.toggle('field-error', !valid);
    input.setAttribute('aria-invalid', String(!valid));

    const errEl = document.getElementById(input.getAttribute('aria-describedby'));
    if (errEl && !valid) errEl.textContent = input.validationMessage;
  });
});

// Reset field errors on focus
document.querySelectorAll('.field .input').forEach(input => {
  input.addEventListener('focus', () => {
    input.closest('.field').classList.remove('field-error');
    input.removeAttribute('aria-invalid');
  });
});
```

---

## Class reference

See full API table: [`specs/components/input.md`](../specs/components/input.md)
