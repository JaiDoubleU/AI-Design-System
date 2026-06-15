# Typography

**Library:** Vanilla HTML/CSS/JS  
**CSS file:** `src/components/typography.css`  
**Spec:** `specs/components/typography.md`

---

## Overview

Typography utility classes. No JavaScript required. Wrap long-form content in `.prose` for automatic rhythm and spacing.

---

## Setup

### HTML — link tags

```html
<!-- In your <head> — link order matters -->
<link rel="stylesheet" href="tokens.css">
<link rel="stylesheet" href="src/base/reset.css">
<link rel="stylesheet" href="src/components/typography.css">
```

### CSS — bundler / PostCSS

```css
/* Via CSS @import (PostCSS / Vite / webpack) */
@import 'ai-design-system/tokens.css';
@import 'ai-design-system/src/base/reset.css';
@import 'ai-design-system/src/components/typography.css';
```

---

## HTML examples

### Display headings (marketing / hero)

```html
<h1 class="display-lg">Display large</h1>
<h1 class="display-md">Display medium</h1>
<h2 class="display-sm">Display small</h2>
```

### Section headings

```html
<h1 class="heading-xl">Heading XL (≈ h1)</h1>
<h2 class="heading-lg">Heading LG (≈ h2)</h2>
<h3 class="heading-md">Heading MD (≈ h3)</h3>
<h4 class="heading-sm">Heading SM (≈ h4)</h4>
<h5 class="heading-xs">HEADING XS (≈ h5/h6)</h5>
```

### Body text

```html
<p class="text-lg">Large body — introductory paragraphs</p>
<p class="text-md">Default body — general copy</p>
<p class="text-sm">Small body — supporting detail</p>
<p class="text-xs">Extra small — metadata, timestamps</p>
```

### Color modifiers

```html
<p class="text-md">Default text color</p>
<p class="text-md text-subtle">Subtle — secondary information</p>
<p class="text-md text-muted">Muted — disabled or de-emphasised</p>
<p class="text-md text-danger">Danger — errors or destructive warnings</p>
<p class="text-md text-success">Success — confirmations</p>
<p class="text-md text-warning">Warning — caution messages</p>
<p class="text-md text-info">Info — neutral hints</p>
```

### Weight modifiers

```html
<p class="text-md font-normal">Normal weight (400)</p>
<p class="text-md font-medium">Medium weight (500)</p>
<p class="text-md font-semibold">Semibold weight (600)</p>
<p class="text-md font-bold">Bold weight (700)</p>
```

### Inline code

```html
<p class="text-md">
  Install with <code class="code-inline">npm install ai-design-system</code>
  then import <code class="code-inline">tokens.css</code>.
</p>
```

### Code block

```html
<pre class="code-block"><code>import { applyAdapter } from 'ai-design-system/lib-adapters';
applyAdapter('shadcn');</code></pre>
```

### Prose (long-form content)

```html
<article class="prose">
  <h2>Getting started</h2>
  <p>The AI Design System is a token-first CSS framework. All values are
     expressed as CSS custom properties so they respond to theme changes.</p>
  <h3>Installation</h3>
  <p>Add the package and import the stylesheet that matches your setup:</p>
  <pre><code>npm install ai-design-system</code></pre>
  <ul>
    <li>Use <code>tokens.css</code> for the complete token layer.</li>
    <li>Use <code>src/components/*.css</code> for individual component styles.</li>
    <li>Use <code>lib-adapters/shadcn.css</code> to bridge shadcn/ui variables.</li>
  </ul>
  <blockquote>
    <p>All component CSS is free of raw values — every property references a
       Layer 2 token so themes propagate automatically.</p>
  </blockquote>
</article>
```

> `.prose` applies typographic rhythm to all direct-descendant block elements. Max-width is 65ch.

---

## JavaScript

_No JavaScript required for this component._

---

## Class reference

See full API table: [`specs/components/typography.md`](../specs/components/typography.md)
