---
component: select
source: https://ui.shadcn.com/docs/components/select
radix-doc: https://www.radix-ui.com/docs/primitives/components/select
radix-api: https://www.radix-ui.com/docs/primitives/components/select#api-reference
---

# Select

## Overview

Displays a list of options for the user to pick from—triggered by a button.

## Import

```tsx
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"
```

## Installation

```bash
npx shadcn@latest add select
```

## Usage

```tsx
<Select>
  <SelectTrigger className="w-[180px]">
    <SelectValue placeholder="Theme" />
  </SelectTrigger>
  <SelectContent>
    <SelectGroup>
      <SelectItem value="light">Light</SelectItem>
      <SelectItem value="dark">Dark</SelectItem>
      <SelectItem value="system">System</SelectItem>
    </SelectGroup>
  </SelectContent>
</Select>
```

## Composition

```
Select
├── SelectTrigger
│   └── SelectValue
└── SelectContent
    ├── SelectGroup
    │   ├── SelectLabel
    │   ├── SelectItem
    │   └── SelectItem
    ├── SelectSeparator
    └── SelectGroup
        ├── SelectLabel
        ├── SelectItem
        └── SelectItem
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Examples

### Align Item With Trigger

Use the `position` prop on `SelectContent` to control alignment. When `position="item-aligned"` (default), the popup positions so the selected item appears over the trigger. When `position="popper"`, the popup aligns to the trigger edge.

### Groups

Use `SelectGroup`, `SelectLabel`, and `SelectSeparator` to organize items.

### Scrollable

A select with many items that scrolls.

### Disabled

### Invalid

Add the `data-invalid` attribute to the `Field` component and the `aria-invalid` attribute to the `SelectTrigger` component to show an error state.
```tsx showLineNumbers /data-invalid/ /aria-invalid/
```

## Accessibility

### ARIA Roles

Trigger: `role="combobox"`, `aria-haspopup="listbox"`, `aria-expanded`. Content: `role="listbox"`. Items: `role="option"`, `aria-selected`.

### Keyboard Navigation

| Key | Action |
|-----|--------|
| Space | Open select |
| ArrowDown / ArrowUp | Navigate options |
| Enter | Select focused option |
| Escape | Close without selecting |
| Home / End | Move to first / last option |
| Any character | Jump to option starting with that character |

### ARIA Attributes

`aria-labelledby` on the trigger pointing to the label. `aria-activedescendant` tracks the focused option.

### Screen Reader Notes

Follows the [ARIA Listbox](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/) pattern.

## Tailwind Tokens

**CSS variables used:**

- `--background`
- `--foreground`
- `--border`
- `--input`
- `--ring`
- `--radius`
- `--popover`
- `--popover-foreground`
- `--accent`
- `--accent-foreground`
- `--muted-foreground`

**Key Tailwind classes:**

- `flex`
- `h-8`
- `w-full`
- `items-center`
- `justify-between`
- `rounded-lg`
- `border`
- `border-input`
- `bg-background`
- `px-3`
- `py-2`
- `text-sm`

Trigger: inherits Input tokens. Content: inherits Popover tokens.

## Notes

- Full API reference: [https://www.radix-ui.com/docs/primitives/components/select](https://www.radix-ui.com/docs/primitives/components/select)
- Radix API reference: [https://www.radix-ui.com/docs/primitives/components/select#api-reference](https://www.radix-ui.com/docs/primitives/components/select#api-reference)
