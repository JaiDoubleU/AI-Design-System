---
component: button-group
source: https://ui.shadcn.com/docs/components/button-group
---

# Button Group

## Overview

A container that groups related buttons together with consistent styling.

## Import

```tsx
import {
  ButtonGroup,
  ButtonGroupSeparator,
  ButtonGroupText,
} from "@/components/ui/button-group"
```

## Installation

```bash
npx shadcn@latest add button-group
```

## Usage

```tsx
<ButtonGroup>
  <Button>Button 1</Button>
  <Button>Button 2</Button>
</ButtonGroup>
```

## Composition

```
ButtonGroup
├── Button or Input
├── ButtonGroupSeparator
└── ButtonGroupText
```

## Props & Variants

### ButtonGroup

The `ButtonGroup` component is a container that groups related buttons together with consistent styling.

| Prop          | Type                         | Default        |
| ------------- | ---------------------------- | -------------- |
| `orientation` | `"horizontal" \| "vertical"` | `"horizontal"` |

### ButtonGroupSeparator

The `ButtonGroupSeparator` component visually divides buttons within a group.

| Prop          | Type                         | Default      |
| ------------- | ---------------------------- | ------------ |
| `orientation` | `"horizontal" \| "vertical"` | `"vertical"` |

### ButtonGroupText

Use this component to display text within a button group.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

## Examples

### Orientation

Set the `orientation` prop to change the button group layout.

### Size

Control the size of buttons using the `size` prop on individual buttons.

### Nested

Nest `<ButtonGroup>` components to create button groups with spacing.

### Separator

The `ButtonGroupSeparator` component visually divides buttons within a group.
Buttons with variant `outline` do not need a separator since they have a border. For other variants, a separator is recommended to improve the visual hierarchy.

### Split

Create a split button group by adding two buttons separated by a `ButtonGroupSeparator`.

### Input

Wrap an `Input` component with buttons.

### Input Group

Wrap an `InputGroup` component to create complex input layouts.

### Dropdown Menu

Create a split button group with a `DropdownMenu` component.

### Select

Pair with a `Select` component.

### Popover

Use with a `Popover` component.

## Accessibility

### ARIA Roles

Container renders with `role="group"` and an `aria-label` describing the group.

### Keyboard Navigation

Each child Button follows standard button keyboard interaction.

### ARIA Attributes

`aria-label` on the group describes the collective purpose.

### Screen Reader Notes

Use `orientation="vertical"` for stacked groups. Adjacent buttons share border styling automatically.

## Tailwind Tokens

**CSS variables used:**

- `--border`
- `--input`
- `--muted`

**Key Tailwind classes:**

- `flex`
- `items-center`
- `gap-0`
- `has-[button]:rounded-lg`

Adjacent button borders collapse. Group handles border-radius on first/last children.

## Notes

