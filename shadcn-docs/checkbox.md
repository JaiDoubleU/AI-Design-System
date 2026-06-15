---
component: checkbox
source: https://ui.shadcn.com/docs/components/checkbox
radix-doc: https://www.radix-ui.com/docs/primitives/components/checkbox
radix-api: https://www.radix-ui.com/docs/primitives/components/checkbox#api-reference
---

# Checkbox

## Overview

A control that allows the user to toggle between checked and not checked.

## Import

```tsx
import { Checkbox } from "@/components/ui/checkbox"
```

## Installation

```bash
npx shadcn@latest add checkbox
```

## Usage

```tsx
<Checkbox />
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Examples

### Basic

Pair the checkbox with `Field` and `FieldLabel` for proper layout and labeling.

### Description

Use `FieldContent` and `FieldDescription` for helper text.

### Disabled

Use the `disabled` prop to prevent interaction and add the `data-disabled` attribute to the `<Field>` component for disabled styles.

### Group

Use multiple fields to create a checkbox list.

### Table

## Accessibility

### ARIA Roles

`role="checkbox"` (provided by Radix Checkbox). `aria-checked`: `true`, `false`, or `mixed`.

### Keyboard Navigation

| Key | Action |
|-----|--------|
| Space | Toggle checked state |
| Tab | Move focus to next focusable element |

### ARIA Attributes

`aria-checked` (managed by Radix); `aria-required`; `aria-invalid`; associate with a `<Label>` via `htmlFor` / `id` pair.

### Screen Reader Notes

Use `checked` (controlled) or `defaultChecked` (uncontrolled). `indeterminate` prop sets `aria-checked="mixed"`.

## Tailwind Tokens

**CSS variables used:**

- `--primary`
- `--primary-foreground`
- `--border`
- `--ring`
- `--radius`

**Key Tailwind classes:**

- `h-4`
- `w-4`
- `shrink-0`
- `rounded-sm`
- `border`
- `border-primary`
- `focus-visible:ring-3`
- `disabled:opacity-50`

Checked state: `--primary` background with a checkmark icon in `--primary-foreground`.

## Notes

- Full API reference: [https://www.radix-ui.com/docs/primitives/components/checkbox](https://www.radix-ui.com/docs/primitives/components/checkbox)
- Radix API reference: [https://www.radix-ui.com/docs/primitives/components/checkbox#api-reference](https://www.radix-ui.com/docs/primitives/components/checkbox#api-reference)
