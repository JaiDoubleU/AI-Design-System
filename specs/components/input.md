# Input

**Name:** Input  
**Category:** Form  
**Status:** Stable  
**File:** `src/components/input.css`

---

## Overview

### When to use
- Single-line text entry: names, emails, search queries, short values.
- Multi-line text entry: use `.textarea`.
- Option selection from a list: use `.select`.
- Boolean choices: use `.checkbox` or `.radio`.

### When NOT to use
- Read-only data display without editing intent — use plain text or a `<code>` block.
- Rich text — use a dedicated editor component.

---

## Anatomy

```
┌─ .field ──────────────────────────────────┐
│  .label  "Email address"  .label-required  │
│                                            │
│ ┌─ .input ────────────────────────────────┐│
│ │  placeholder text                        ││
│ └─────────────────────────────────────────┘│
│                                            │
│  .field-hint  "We'll never share your…"   │
│  .field-error-msg  "Invalid email format" │
└────────────────────────────────────────────┘
```

1. **Field wrapper** (`.field`) — flex column, provides consistent gap
2. **Label** (`.label`) — descriptive text, required/optional modifiers
3. **Input** (`.input`) — the `<input>` or `<textarea>` element
4. **Helper text** (`.field-hint`) — guidance below the input
5. **Error message** (`.field-error-msg`) — validation feedback

---

## Tokens used

| Property | Token |
|---|---|
| `padding-block` | `--spacing-2` (default), `--spacing-1` (sm), `--spacing-3` (lg) |
| `padding-inline` | `--spacing-3` (default), `--spacing-2` (sm), `--spacing-4` (lg) |
| `font-family` | `--font-sans` |
| `font-size` | `--text-sm` (default), `--text-xs` (sm), `--text-md` (lg) |
| `font-weight` | `--weight-normal` |
| `line-height` | `--leading-normal` |
| `color` | `--color-text` |
| `background-color` | `--color-bg` |
| `border-color` | `--color-border-emphasis` (default), `--color-border-danger` (error), `--color-border-success` (success) |
| `border-radius` | `--radius-md` (default), `--radius-sm` (sm), `--radius-lg` (lg) |
| `box-shadow` | `--shadow-xs` |
| Focus `border-color` | `--color-border-focus` |
| Focus `box-shadow` | `--shadow-xs` + `--color-interactive-muted` ring |
| Disabled `background` | `--color-bg-muted` |
| Disabled `color` | `--color-text-disabled` |
| Placeholder `color` | `--color-text-muted` |
| `.field` `gap` | `--spacing-1` |
| `.label` `font-size` | `--text-sm` |
| `.label` `font-weight` | `--weight-medium` |
| `.field-hint` `font-size` | `--text-xs` |
| `.field-hint` `color` | `--color-text-muted` |
| `.field-error-msg` `color` | `--color-text-danger` |

---

## Props / API

| Class | Description |
|---|---|
| `.input` | Single-line text input |
| `.textarea` | Multi-line text area |
| `.select` | Native `<select>` dropdown |
| `.input-sm` | Small size |
| `.input-lg` | Large size |
| `.input-error` | Error state (red border + red focus ring) |
| `.input-success` | Success state (green border) |
| `.field` | Wrapper for label + input + hint |
| `.label` | Form label |
| `.label-required` | Appends red `*` |
| `.label-optional` | Appends grey "(optional)" |
| `.field-hint` | Helper text below input |
| `.field-error-msg` | Validation error below input |
| `.input-group` | Row of input + addon |
| `.input-addon` | Prefix or suffix element in input group |
| `.checkbox` | Checkbox wrapper |
| `.radio` | Radio wrapper |
| `.checkbox-label` / `.radio-label` | Label text next to checkbox/radio |

---

## States

| State | Behaviour |
|---|---|
| **Default** | `--color-border-emphasis` border, `--shadow-xs` |
| **Hover** | Border darkens slightly |
| **Focus** | `--color-border-focus`, blue focus ring |
| **Error** | `--color-border-danger`, red focus ring |
| **Success** | `--color-border-success` |
| **Disabled** | `--color-bg-muted` background, `--color-text-disabled` text, `cursor: not-allowed` |
| **Read-only** | `--color-bg-subtle` background, `cursor: default` |

---

## Code examples

```html
<!-- Basic field -->
<div class="field">
  <label class="label label-required" for="email">Email</label>
  <input class="input" id="email" type="email" placeholder="you@example.com">
  <span class="field-hint">We'll never share your email.</span>
</div>

<!-- Error state -->
<div class="field">
  <label class="label" for="email-err">Email</label>
  <input class="input input-error" id="email-err" type="email" aria-invalid="true">
  <span class="field-error-msg" role="alert">Enter a valid email address.</span>
</div>

<!-- Textarea -->
<div class="field">
  <label class="label label-optional" for="bio">Bio</label>
  <textarea class="input textarea" id="bio" rows="4"></textarea>
</div>

<!-- Select -->
<div class="field">
  <label class="label" for="country">Country</label>
  <select class="input select" id="country">
    <option>United States</option>
    <option>Canada</option>
  </select>
</div>

<!-- Input group (prefix addon) -->
<div class="input-group">
  <span class="input-addon">https://</span>
  <input class="input" type="url" placeholder="yoursite.com">
</div>

<!-- Checkbox -->
<label class="checkbox">
  <input type="checkbox">
  <span class="checkbox-label">Subscribe to newsletter</span>
</label>
```

---

## Cross-references

- `button.css` — submit buttons pair with `.field` wrappers
- `alert.css` — form-level validation messages use `.alert-danger`
