# Typography

**Name:** Typography  
**Category:** Base  
**Status:** Stable  
**File:** `src/base/typography.css`

---

## Overview

### When to use
- Apply consistent text sizing, weight, and color across all UI surfaces.
- Use semantic classes (`.heading-md`, `.text-sm`) before writing bespoke CSS.
- Wrap long-form markdown / CMS content in `.prose` for opinionated defaults.

### When NOT to use
- Override typography inside component CSS — component files define their own text tokens.
- Apply `.display-*` classes to body copy — these are for marketing/hero contexts only.

---

## Anatomy

Typography classes are single-responsibility utilities applied directly to elements:

```html
<h2 class="heading-lg">Section title</h2>
<p class="text-md text-subtle">Supporting description</p>
<code class="code-inline">npm install</code>
```

The `.prose` wrapper applies a pre-configured rhythm to all child elements:

```html
<article class="prose">
  <h2>Heading</h2>
  <p>Paragraph one…</p>
  <ul><li>List item</li></ul>
</article>
```

---

## Tokens used

| Class | Property | Token |
|---|---|---|
| `.display-lg` | `font-size` | `--text-5xl` |
| `.display-md` | `font-size` | `--text-4xl` |
| `.display-sm` | `font-size` | `--text-3xl` |
| `.heading-xl` / `h1` | `font-size` | `--text-2xl` |
| `.heading-lg` / `h2` | `font-size` | `--text-xl` |
| `.heading-md` / `h3` | `font-size` | `--text-lg` |
| `.heading-sm` / `h4` | `font-size` | `--text-md` |
| `.heading-xs` / `h5-6` | `font-size` | `--text-sm` |
| `.text-lg` | `font-size` | `--text-lg` |
| `.text-md` / `p` | `font-size` | `--text-md` |
| `.text-sm` | `font-size` | `--text-sm` |
| `.text-xs` | `font-size` | `--text-xs` |
| Display + headings | `font-weight` | `--weight-bold` / `--weight-semibold` |
| Display + headings | `line-height` | `--leading-tight` / `--leading-snug` |
| Body text | `line-height` | `--leading-relaxed` |
| `.font-normal` | `font-weight` | `--weight-normal` |
| `.font-medium` | `font-weight` | `--weight-medium` |
| `.font-semibold` | `font-weight` | `--weight-semibold` |
| `.font-bold` | `font-weight` | `--weight-bold` |
| `.font-sans` | `font-family` | `--font-sans` |
| `.font-mono` | `font-family` | `--font-mono` |
| `.font-serif` | `font-family` | `--font-serif` |
| `.text-subtle` | `color` | `--color-text-subtle` |
| `.text-muted` | `color` | `--color-text-muted` |
| `.text-inverse` | `color` | `--color-text-inverse` |
| `.text-danger` | `color` | `--color-text-danger` |
| `.text-success` | `color` | `--color-text-success` |
| `.text-warning` | `color` | `--color-text-warning` |
| `.text-info` | `color` | `--color-text-info` |
| `.code-inline` `font-size` | `font-size` | `--text-sm` |
| `.code-inline` `background` | `background-color` | `--color-bg-muted` |
| `.code-inline` `color` | `color` | `--color-text-danger` |
| `.code-inline` `padding-inline` | `padding-inline` | `--spacing-1` |
| `.code-inline` `border-radius` | `border-radius` | `--radius-sm` |
| `.code-block` padding | `padding` | `--spacing-4` |
| `.code-block` `border-radius` | `border-radius` | `--radius-lg` |
| `.code-block` `background` | `background-color` | `--color-bg-emphasis` |
| `.code-block` `color` | `color` | `--color-text-inverse` |
| `.prose` stack gap | `margin-top` | `--spacing-4` |
| `.prose` heading top gap | `margin-top` | `--spacing-8` |
| `.prose` heading bottom gap | `margin-bottom` | `--spacing-3` |
| `.prose` list padding | `padding-left` | `--spacing-6` |
| `.prose blockquote` border | `border-left` | `--color-border-emphasis` |
| `.prose blockquote` padding | `padding-left` | `--spacing-4` |

---

## Props / API

### Display
- `.display-lg` — 48 px, bold, tight
- `.display-md` — 36 px, bold, tight
- `.display-sm` — 30 px, semibold, snug

### Headings
- `.heading-xl` (≈ h1) — 24 px
- `.heading-lg` (≈ h2) — 20 px
- `.heading-md` (≈ h3) — 18 px
- `.heading-sm` (≈ h4) — 16 px
- `.heading-xs` (≈ h5/h6) — 14 px uppercase

### Body text
- `.text-lg`, `.text-md`, `.text-sm`, `.text-xs`

### Color modifiers
- `.text-subtle`, `.text-muted`, `.text-inverse`, `.text-danger`, `.text-success`, `.text-warning`, `.text-info`

### Weight modifiers
- `.font-normal`, `.font-medium`, `.font-semibold`, `.font-bold`

### Family modifiers
- `.font-sans`, `.font-mono`, `.font-serif`

### Inline code
- `.code-inline` — inline `<code>` styling

### Block code
- `.code-block` — pre-formatted block

### Prose
- `.prose` — opinionated long-form container (max-width: 65ch)

---

## Code examples

```html
<!-- Display headline -->
<h1 class="display-md">Build faster with tokens</h1>

<!-- Section heading -->
<h2 class="heading-lg">Getting started</h2>

<!-- Body copy -->
<p class="text-md">
  Use only <code class="code-inline">var(--token)</code> references in CSS.
</p>

<!-- Muted helper -->
<p class="text-sm text-muted">Last updated 3 days ago</p>

<!-- Long-form content -->
<article class="prose">
  <h2>Introduction</h2>
  <p>This design system is LLM-readable…</p>
  <ul>
    <li>Consistent tokens</li>
    <li>Structured specs</li>
  </ul>
</article>
```

---

## Cross-references

- `specs/foundations/typography.md` — full token scale reference
- `specs/tokens/token-reference.md` — master token map
- `card.css` — `.card-title` and `.card-subtitle` use typography tokens directly
