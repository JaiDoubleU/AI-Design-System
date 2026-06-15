---
component: input-group
source: https://ui.shadcn.com/docs/components/input-group
---

# Input Group

## Overview

Add addons, buttons, and helper content to inputs.

## Import

```tsx
import {
  InputGroup,
  InputGroupAddon,
  InputGroupButton,
  InputGroupInput,
  InputGroupText,
  InputGroupTextarea,
} from "@/components/ui/input-group"
```

## Installation

```bash
npx shadcn@latest add input-group
```

## Usage

```tsx
<InputGroup>
  <InputGroupInput placeholder="Search..." />
  <InputGroupAddon>
    <SearchIcon />
  </InputGroupAddon>
</InputGroup>
```

## Composition

```
InputGroup
├── InputGroupInput or InputGroupTextarea
├── InputGroupAddon
├── InputGroupButton
└── InputGroupText
```

## Props & Variants

### InputGroup

The main component that wraps inputs and addons.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` |         |

### InputGroupAddon

Displays icons, text, buttons, or other content alongside inputs. For proper focus navigation, the `InputGroupAddon` component should be placed after the input. Set the `align` prop to position the addon.

| Prop        | Type                                                             | Default          |
| ----------- | ---------------------------------------------------------------- | ---------------- |
| `align`     | `"inline-start" \| "inline-end" \| "block-start" \| "block-end"` | `"inline-start"` |
| `className` | `string`                                                         |                  |

### InputGroupButton

Displays buttons within input groups.

| Prop        | Type                                                                          | Default   |
| ----------- | ----------------------------------------------------------------------------- | --------- |
| `size`      | `"xs" \| "icon-xs" \| "sm" \| "icon-sm"`                                      | `"xs"`    |
| `variant`   | `"default" \| "destructive" \| "outline" \| "secondary" \| "ghost" \| "link"` | `"ghost"` |
| `className` | `string`                                                                      |           |

### InputGroupInput

Replacement for `<Input />` when building input groups. This component has the input group styles pre-applied and uses the unified `data-slot="input-group-control"` for focus state handling.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` |         |

### InputGroupTextarea

Replacement for `<Textarea />` when building input groups. This component has the textarea group styles pre-applied and uses the unified `data-slot="input-group-control"` for focus state handling.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` |         |

## Examples

### Icon

### Text

### Button

### Kbd

### Dropdown

### Spinner

### Textarea

### Custom Input

Add the `data-slot="input-group-control"` attribute to your custom input for automatic focus state handling.
Here's an example of a custom resizable textarea from a third-party library.

## Accessibility

### ARIA Roles

Wraps an input with prefix/suffix addons. No implicit ARIA role on the group.

### Keyboard Navigation

Standard input and button keyboard interaction.

### ARIA Attributes

Addons that are buttons should have `aria-label`. Prefix/suffix text can be associated via `aria-describedby`.

### Screen Reader Notes

For icon-only addons always include a visually hidden text or `aria-label`.

## Tailwind Tokens

**CSS variables used:**

- `--background`
- `--border`
- `--input`
- `--muted`
- `--foreground`
- `--radius`

**Key Tailwind classes:**

- `flex`
- `items-center`
- `rounded-lg`
- `border`
- `bg-background`

Addon elements use `--muted` background.

## Notes


### Changelog

### 2025-10-06 `InputGroup`

Add the `min-w-0` class to the `InputGroup` component. See [diff](https://github.com/shadcn-ui/ui/pull/8341/files#diff-0e2ee95d0050ca4c5d82339df86c54e14a6739dc4638fdda0eec8f73aebc2da9).
