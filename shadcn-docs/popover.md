---
component: popover
source: https://ui.shadcn.com/docs/components/popover
radix-doc: https://www.radix-ui.com/docs/primitives/components/popover
radix-api: https://www.radix-ui.com/docs/primitives/components/popover#api-reference
---

# Popover

## Overview

Displays rich content in a portal, triggered by a button.

## Import

```tsx
import {
  Popover,
  PopoverContent,
  PopoverDescription,
  PopoverHeader,
  PopoverTitle,
  PopoverTrigger,
} from "@/components/ui/popover"
```

## Installation

```bash
npx shadcn@latest add popover
```

## Usage

```tsx
<Popover>
  <PopoverTrigger asChild>
    <Button variant="outline">Open Popover</Button>
  </PopoverTrigger>
  <PopoverContent>
    <PopoverHeader>
      <PopoverTitle>Title</PopoverTitle>
      <PopoverDescription>Description text here.</PopoverDescription>
    </PopoverHeader>
  </PopoverContent>
</Popover>
```

## Composition

```
Popover
├── PopoverTrigger
└── PopoverContent
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Examples

### Basic

A simple popover with a header, title, and description.

### Align

Use the `align` prop on `PopoverContent` to control the horizontal alignment.

### With Form

A popover with form fields inside.

## Accessibility

### ARIA Roles

`role="dialog"` on the content panel (Radix Popover); trigger has `aria-haspopup="dialog"` and `aria-expanded`.

### Keyboard Navigation

| Key | Action |
|-----|--------|
| Enter / Space | Open popover |
| Tab | Move focus into / through popover content |
| Escape | Close popover |

### ARIA Attributes

`aria-labelledby` if popover has a visible title. Focus moves into the popover on open and returns to trigger on close.

### Screen Reader Notes

Unlike Dialog, Popover does not trap focus — Tab can leave the popover. Use Dialog for content requiring full focus trap.

## Tailwind Tokens

**CSS variables used:**

- `--popover`
- `--popover-foreground`
- `--border`
- `--radius`

**Key Tailwind classes:**

- `z-50`
- `rounded-md`
- `border`
- `bg-popover`
- `p-4`
- `text-popover-foreground`
- `shadow-md`

`--popover` and `--popover-foreground` are distinct from `--background`/`--foreground` to allow independent theming.

## Notes

- Full API reference: [https://www.radix-ui.com/docs/primitives/components/popover](https://www.radix-ui.com/docs/primitives/components/popover)
- Radix API reference: [https://www.radix-ui.com/docs/primitives/components/popover#api-reference](https://www.radix-ui.com/docs/primitives/components/popover#api-reference)
