---
component: typography
source: https://ui.shadcn.com/docs/components/typography
---

# Typography

## Overview

Styles for headings, paragraphs, lists, etc.

## Import

```tsx
import { Typography } from "@/components/ui/typography"
```

## Installation

```bash
npx shadcn@latest add typography
```

## Usage

```tsx
<Typography />
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Accessibility

### ARIA Roles

Applies semantic HTML elements: `<h1>`–`<h6>`, `<p>`, `<blockquote>`, `<ul>`, `<ol>`, `<li>`, `<code>`, `<pre>`, `<table>`.

### Keyboard Navigation

Standard browser behavior for interactive elements within prose.

### ARIA Attributes

Semantic HTML provides implicit ARIA roles. Ensure heading hierarchy is logical (h1 → h2 → h3).

### Screen Reader Notes

The `prose` class (Tailwind Typography plugin) or the shadcn/ui typography utilities apply consistent typography to any block of HTML content.

## Tailwind Tokens

**CSS variables used:**

- `--foreground`
- `--muted-foreground`
- `--border`
- `--background`

**Key Tailwind classes:**

- `prose`
- `prose-neutral`
- `dark:prose-invert`

Uses Tailwind Typography plugin classes. Headings, paragraphs, lists inherit from the `prose` class.

## Notes

