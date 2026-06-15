---
component: button
source: https://ui.shadcn.com/docs/components/button
---

# Button

## Overview

Displays a button or a component that looks like a button.

## Import

```tsx
import { Button } from "@/components/ui/button"
```

## Installation

```bash
npx shadcn@latest add button
```

## Usage

```tsx
<Button variant="outline">Button</Button>
```

## Props & Variants

### Button

The `Button` component is a wrapper around the `button` element that adds a variety of styles and functionality.

| Prop      | Type                                                                                 | Default     |
| --------- | ------------------------------------------------------------------------------------ | ----------- |
| `variant` | `"default" \| "outline" \| "ghost" \| "destructive" \| "secondary" \| "link"`        | `"default"` |
| `size`    | `"default" \| "xs" \| "sm" \| "lg" \| "icon" \| "icon-xs" \| "icon-sm" \| "icon-lg"` | `"default"` |
| `asChild` | `boolean`                                                                            | `false`     |

## Examples

### Size

Use the `size` prop to change the size of the button.

### Default

### Outline

### Secondary

### Ghost

### Destructive

### Link

### Icon

### With Icon

Remember to add the `data-icon="inline-start"` or `data-icon="inline-end"` attribute to the icon for the correct spacing.

### Rounded

Use the `rounded-full` class to make the button rounded.

### Spinner

Render a `<Spinner />` component inside the button to show a loading state. Remember to add the `data-icon="inline-start"` or `data-icon="inline-end"` attribute to the spinner for the correct spacing.

### Button Group

To create a button group, use the `ButtonGroup` component. See the [Button Group](/docs/components/radix/button-group) documentation for more details.

### As Child

You can use the `asChild` prop on `<Button />` to make another component look like a button. Here's an example of a link that looks like a button.

## Accessibility

### ARIA Roles

Renders a native `<button>` element. When `asChild` is used the role is inherited from the child element.

### Keyboard Navigation

| Key | Action |
|-----|--------|
| Enter | Activate button |
| Space | Activate button |

### ARIA Attributes

`aria-disabled="true"` when logically disabled but still focusable. `aria-busy="true"` for loading states.

### Screen Reader Notes

Tailwind v4 sets `cursor: default` on buttons; add `cursor: pointer` via global CSS if needed. Use `variant="ghost"` or `variant="link"` for low-emphasis actions.

## Tailwind Tokens

**CSS variables used:**

- `--primary`
- `--primary-foreground`
- `--secondary`
- `--secondary-foreground`
- `--destructive`
- `--muted`
- `--foreground`
- `--border`
- `--ring`
- `--radius`
- `--radius-md`

**Key Tailwind classes:**

- `inline-flex`
- `items-center`
- `justify-center`
- `whitespace-nowrap`
- `rounded-lg`
- `text-sm`
- `font-medium`
- `transition-all`
- `focus-visible:ring-3`
- `disabled:opacity-50`

Variant styles from Nova CSS: `cn-button-variant-*`. Size styles: `cn-button-size-*`.

## Notes

