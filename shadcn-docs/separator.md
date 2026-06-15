---
component: separator
source: https://ui.shadcn.com/docs/components/separator
radix-doc: https://www.radix-ui.com/docs/primitives/components/separator
radix-api: https://www.radix-ui.com/docs/primitives/components/separator#api-reference
---

# Separator

## Overview

Visually or semantically separates content.

## Import

```tsx
import { Separator } from "@/components/ui/separator"
```

## Installation

```bash
npx shadcn@latest add separator
```

## Usage

```tsx
<Separator />
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Examples

### Vertical

Use `orientation="vertical"` for a vertical separator.

### Menu

Vertical separators between menu items with descriptions.

### List

Horizontal separators between list items.

## Accessibility

### ARIA Roles

`role="separator"` with `aria-orientation` (`"horizontal"` or `"vertical"`). Use `role="presentation"` for decorative separators.

### Keyboard Navigation

Not interactive.

### ARIA Attributes

Decorative separators should have `aria-hidden="true"`.

### Screen Reader Notes

Use `decorative` prop (when available) or `aria-hidden` to hide purely visual separators from screen readers.

## Tailwind Tokens

**CSS variables used:**

- `--border`

**Key Tailwind classes:**

- `shrink-0`
- `bg-border`

Renders as `h-[1px] w-full` (horizontal) or `h-full w-[1px]` (vertical). Color: `--border`.

## Notes

- Full API reference: [https://www.radix-ui.com/docs/primitives/components/separator](https://www.radix-ui.com/docs/primitives/components/separator)
- Radix API reference: [https://www.radix-ui.com/docs/primitives/components/separator#api-reference](https://www.radix-ui.com/docs/primitives/components/separator#api-reference)
