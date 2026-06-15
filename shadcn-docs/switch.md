---
component: switch
source: https://ui.shadcn.com/docs/components/switch
radix-doc: https://www.radix-ui.com/docs/primitives/components/switch
radix-api: https://www.radix-ui.com/docs/primitives/components/switch#api-reference
---

# Switch

## Overview

A control that allows the user to toggle between checked and not checked.

## Import

```tsx
import { Switch } from "@/components/ui/switch"
```

## Installation

```bash
npx shadcn@latest add switch
```

## Usage

```tsx
<Switch />
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Examples

### Description

### Choice Card

Card-style selection where `FieldLabel` wraps the entire `Field` for a clickable card pattern.

### Disabled

Add the `disabled` prop to the `Switch` component to disable the switch. Add the `data-disabled` prop to the `Field` component for styling.

### Invalid

Add the `aria-invalid` prop to the `Switch` component to indicate an invalid state. Add the `data-invalid` prop to the `Field` component for styling.

### Size

Use the `size` prop to change the size of the switch.

## Accessibility

### ARIA Roles

`role="switch"`, `aria-checked="true"` / `"false"`.

### Keyboard Navigation

| Key | Action |
|-----|--------|
| Space | Toggle on/off |
| Enter | Toggle on/off (when used in a form) |

### ARIA Attributes

Associate with a `<Label>` via `htmlFor` / `id`. `aria-required`; `aria-disabled`.

### Screen Reader Notes

Follows the [WAI-ARIA Switch](https://www.w3.org/WAI/ARIA/apg/patterns/switch/) pattern. Semantically different from Checkbox: Switch represents binary on/off, Checkbox represents checked/unchecked selection.

## Tailwind Tokens

**CSS variables used:**

- `--primary`
- `--input`
- `--background`
- `--ring`
- `--radius`

**Key Tailwind classes:**

- `peer`
- `inline-flex`
- `h-5`
- `w-9`
- `shrink-0`
- `cursor-pointer`
- `items-center`
- `rounded-full`
- `border-2`
- `border-transparent`
- `transition-colors`
- `focus-visible:ring-3`

Track off: `--input`. Track on: `--primary`. Thumb: `--background`.

## Notes

- Full API reference: [https://www.radix-ui.com/docs/primitives/components/switch](https://www.radix-ui.com/docs/primitives/components/switch)
- Radix API reference: [https://www.radix-ui.com/docs/primitives/components/switch#api-reference](https://www.radix-ui.com/docs/primitives/components/switch#api-reference)
