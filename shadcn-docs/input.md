---
component: input
source: https://ui.shadcn.com/docs/components/input
---

# Input

## Overview

A text input component for forms and user data entry with built-in styling and accessibility features.

## Import

```tsx
import { Input } from "@/components/ui/input"
```

## Installation

```bash
npx shadcn@latest add input
```

## Usage

```tsx
<Input />
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Examples

### Basic

### Field

Use `Field`, `FieldLabel`, and `FieldDescription` to create an input with a
label and description.

### Field Group

Use `FieldGroup` to show multiple `Field` blocks and to build forms.

### Disabled

Use the `disabled` prop to disable the input. To style the disabled state, add the `data-disabled` attribute to the `Field` component.

### Invalid

Use the `aria-invalid` prop to mark the input as invalid. To style the invalid state, add the `data-invalid` attribute to the `Field` component.

### File

Use the `type="file"` prop to create a file input.

### Inline

Use `Field` with `orientation="horizontal"` to create an inline input.
Pair with `Button` to create a search input with a button.

### Grid

Use a grid layout to place multiple inputs side by side.

### Required

Use the `required` attribute to indicate required inputs.

### Badge

Use `Badge` in the label to highlight a recommended field.

### Input Group

To add icons, text, or buttons inside an input, use the `InputGroup` component. See the [Input Group](/docs/components/input-group) component for more examples.

### Button Group

To add buttons to an input, use the `ButtonGroup` component. See the [Button Group](/docs/components/button-group) component for more examples.

### Form

A full form example with multiple inputs, a select, and a button.

## Accessibility

### ARIA Roles

Native `<input>` element — role is derived from `type` (e.g., `textbox`, `search`).

### Keyboard Navigation

Standard browser keyboard interaction for text inputs.

### ARIA Attributes

`aria-invalid` (error state); `aria-required`; `aria-disabled`; `aria-describedby` → hint/error id. Associate with `<label>` via `id` / `htmlFor`.

### Screen Reader Notes

Always pair with a visible `<Label>` component. Use `aria-label` only when a visible label cannot be provided.

## Tailwind Tokens

**CSS variables used:**

- `--background`
- `--foreground`
- `--border`
- `--input`
- `--ring`
- `--radius`
- `--muted-foreground`

**Key Tailwind classes:**

- `flex`
- `h-8`
- `w-full`
- `rounded-lg`
- `border`
- `border-input`
- `bg-background`
- `px-3`
- `py-1`
- `text-sm`
- `placeholder:text-muted-foreground`
- `focus-visible:ring-3`
- `disabled:opacity-50`

`--input` token sets the default border color. Focus ring uses `--ring`.

## Notes

