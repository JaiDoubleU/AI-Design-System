---
component: accordion
source: https://ui.shadcn.com/docs/components/accordion
radix-doc: https://www.radix-ui.com/primitives/docs/components/accordion
radix-api: https://www.radix-ui.com/primitives/docs/components/accordion#api-reference
---

# Accordion

## Overview

A vertically stacked set of interactive headings that each reveal a section of content.

## Import

```tsx
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion"
```

## Installation

```bash
npx shadcn@latest add accordion
```

## Usage

```tsx
<Accordion type="single" collapsible defaultValue="item-1">
  <AccordionItem value="item-1">
    <AccordionTrigger>Is it accessible?</AccordionTrigger>
    <AccordionContent>
      Yes. It adheres to the WAI-ARIA design pattern.
    </AccordionContent>
  </AccordionItem>
</Accordion>
```

## Composition

```
Accordion
├── AccordionItem
│   ├── AccordionTrigger
│   └── AccordionContent
└── AccordionItem
    ├── AccordionTrigger
    └── AccordionContent
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Examples

### Basic

A basic accordion that shows one item at a time. The first item is open by default.

### Multiple

Use `type="multiple"` to allow multiple items to be open at the same time.

### Disabled

Use the `disabled` prop on `AccordionItem` to disable individual items.

### Borders

Add `border` to the `Accordion` and `border-b last:border-b-0` to the `AccordionItem` to add borders to the items.

### Card

Wrap the `Accordion` in a `Card` component.

## Accessibility

### ARIA Roles

Trigger uses native `<button>`. Panel gets `role="region"` with `aria-labelledby` pointing to the trigger.

### Keyboard Navigation

| Key | Action |
|-----|--------|
| Enter / Space | Toggle panel open/closed |
| Tab | Move focus to next focusable element |
| Shift+Tab | Move focus to previous focusable element |
| ArrowDown | Move focus to next trigger (vertical orientation) |
| ArrowUp | Move focus to previous trigger |
| Home | Move focus to first trigger |
| End | Move focus to last trigger |

### ARIA Attributes

`aria-expanded` on trigger; `aria-controls` → panel `id`; `aria-labelledby` on panel → trigger `id`.

### Screen Reader Notes

Follows the [WAI-ARIA Accordion](https://www.w3.org/WAI/ARIA/apg/patterns/accordion/) design pattern.

## Tailwind Tokens

**CSS variables used:**

- `--radius`
- `--border`
- `--muted`
- `--foreground`
- `--muted-foreground`

**Key Tailwind classes:**

- `border-b`
- `px-4`
- `py-2`
- `font-medium`
- `text-sm`
- `text-muted-foreground`
- `hover:underline`

Trigger underline on hover; content hidden/shown with data attributes.

## Notes

- Full API reference: [https://www.radix-ui.com/primitives/docs/components/accordion](https://www.radix-ui.com/primitives/docs/components/accordion)
- Radix API reference: [https://www.radix-ui.com/primitives/docs/components/accordion#api-reference](https://www.radix-ui.com/primitives/docs/components/accordion#api-reference)
