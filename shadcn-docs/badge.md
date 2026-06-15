---
component: badge
source: https://ui.shadcn.com/docs/components/badge
---

# Badge

## Overview

Displays a badge or a component that looks like a badge.

## Import

```tsx
import { Badge } from "@/components/ui/badge"
```

## Installation

```bash
npx shadcn@latest add badge
```

## Usage

```tsx
<Badge variant="default | outline | secondary | destructive">Badge</Badge>
```

## Props & Variants

### Badge

The `Badge` component displays a badge or a component that looks like a badge.

| Prop        | Type                                                                          | Default     |
| ----------- | ----------------------------------------------------------------------------- | ----------- |
| `variant`   | `"default" \| "secondary" \| "destructive" \| "outline" \| "ghost" \| "link"` | `"default"` |
| `className` | `string`                                                                      | -           |

## Examples

### Variants

Use the `variant` prop to change the variant of the badge.

### With Icon

You can render an icon inside the badge. Use `data-icon="inline-start"` to render the icon on the left and `data-icon="inline-end"` to render the icon on the right.

### With Spinner

You can render a spinner inside the badge. Remember to add the `data-icon="inline-start"` or `data-icon="inline-end"` prop to the spinner.

### Link

Use the `asChild` prop to render a link as a badge.

### Custom Colors

You can customize the colors of a badge by adding custom classes such as `bg-green-50 dark:bg-green-800` to the `Badge` component.

## Accessibility

### ARIA Roles

Renders as a `<div>` (or `<span>` depending on usage). No implicit ARIA role.

### Keyboard Navigation

Not interactive unless `asChild` is used with an anchor or button.

### ARIA Attributes

Add `aria-label` when badge content alone is insufficient for context (e.g., a numeric count).

### Screen Reader Notes

Use the `asChild` prop to render a `<Link>` styled as a badge for navigation.

## Tailwind Tokens

**CSS variables used:**

- `--primary`
- `--primary-foreground`
- `--secondary`
- `--secondary-foreground`
- `--destructive`
- `--destructive-foreground`
- `--border`
- `--radius`

**Key Tailwind classes:**

- `inline-flex`
- `items-center`
- `rounded-md`
- `border`
- `px-2.5`
- `py-0.5`
- `text-xs`
- `font-semibold`
- `transition-colors`

Variants: `default` (--primary), `secondary`, `destructive`, `outline`.

## Notes

