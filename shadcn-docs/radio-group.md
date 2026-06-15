---
component: radio-group
source: https://ui.shadcn.com/docs/components/radio-group
radix-doc: https://www.radix-ui.com/docs/primitives/components/radio-group
radix-api: https://www.radix-ui.com/docs/primitives/components/radio-group#api-reference
---

# Radio Group

## Overview

A set of checkable buttons—known as radio buttons—where no more than one of the buttons can be checked at a time.

## Import

```tsx
import { Label } from "@/components/ui/label"
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group"
```

## Installation

```bash
npx shadcn@latest add radio-group
```

## Usage

```tsx
<RadioGroup defaultValue="option-one">
  <div className="flex items-center gap-3">
    <RadioGroupItem value="option-one" id="option-one" />
    <Label htmlFor="option-one">Option One</Label>
  </div>
  <div className="flex items-center gap-3">
    <RadioGroupItem value="option-two" id="option-two" />
    <Label htmlFor="option-two">Option Two</Label>
  </div>
</RadioGroup>
```

## Composition

```
RadioGroup
├── RadioGroupItem
└── RadioGroupItem
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Examples

### Description

Radio group items with a description using the `Field` component.

### Choice Card

Use `FieldLabel` to wrap the entire `Field` for a clickable card-style selection.

### Fieldset

Use `FieldSet` and `FieldLegend` to group radio items with a label and description.

### Disabled

Use the `disabled` prop on `RadioGroupItem` to disable individual items.

### Invalid

Use `aria-invalid` on `RadioGroupItem` and `data-invalid` on `Field` to show validation errors.

## Accessibility

### ARIA Roles

`role="radiogroup"` on the group; `role="radio"` on each item; `aria-checked="true"` on selected item.

### Keyboard Navigation

| Key | Action |
|-----|--------|
| Tab | Move focus into the group |
| ArrowDown / ArrowRight | Move to next radio (and select) |
| ArrowUp / ArrowLeft | Move to previous radio (and select) |
| Space | Select focused radio |

### ARIA Attributes

`aria-labelledby` on the group pointing to the group label id.

### Screen Reader Notes

Only one radio in the group is in the tab sequence at a time (roving tabindex). Follows [WAI-ARIA Radio Group](https://www.w3.org/WAI/ARIA/apg/patterns/radio/) pattern.

## Tailwind Tokens

**CSS variables used:**

- `--primary`
- `--border`
- `--ring`
- `--foreground`

**Key Tailwind classes:**

- `aspect-square`
- `h-4`
- `w-4`
- `rounded-full`
- `border`
- `border-primary`
- `text-primary`
- `focus:ring-3`
- `disabled:opacity-50`

Selected state fills inner circle with `--primary` color.

## Notes

- Full API reference: [https://www.radix-ui.com/docs/primitives/components/radio-group](https://www.radix-ui.com/docs/primitives/components/radio-group)
- Radix API reference: [https://www.radix-ui.com/docs/primitives/components/radio-group#api-reference](https://www.radix-ui.com/docs/primitives/components/radio-group#api-reference)
