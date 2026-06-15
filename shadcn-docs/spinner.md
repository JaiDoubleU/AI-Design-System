---
component: spinner
source: https://ui.shadcn.com/docs/components/spinner
---

# Spinner

## Overview

An indicator that can be used to show a loading state.

## Import

```tsx
import { Spinner } from "@/components/ui/spinner"
```

## Installation

```bash
npx shadcn@latest add spinner
```

## Usage

```tsx
<Spinner />
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Examples

### Size

Use the `size-*` utility class to change the size of the spinner.

### Button

Add a spinner to a button to indicate a loading state. Place the `<Spinner />` before the label with `data-icon="inline-start"` for a start position, or after the label with `data-icon="inline-end"` for an end position.

### Badge

Add a spinner to a badge to indicate a loading state. Place the `<Spinner />` before the label with `data-icon="inline-start"` for a start position, or after the label with `data-icon="inline-end"` for an end position.

### Input Group

### Empty

## Accessibility

### ARIA Roles

`role="status"` or simply render as `aria-hidden="true"` alongside a visible loading label.

### Keyboard Navigation

Not interactive.

### ARIA Attributes

`aria-label="Loading…"` when spinner is the only loading indicator. Otherwise `aria-hidden="true"` and use a separate live region.

### Screen Reader Notes

For button loading states: add `aria-busy="true"` to the button and render a `<Spinner data-icon="inline-start"/>` inside.

## Tailwind Tokens

**CSS variables used:**

- `--foreground`
- `--muted-foreground`

**Key Tailwind classes:**

- `animate-spin`
- `text-muted-foreground`

SVG with `animate-spin`. Color inherits from `currentColor` (set via `className`).

## Notes

