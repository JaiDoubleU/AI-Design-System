---
component: tooltip
source: https://ui.shadcn.com/docs/components/tooltip
radix-doc: https://www.radix-ui.com/docs/primitives/components/tooltip
radix-api: https://www.radix-ui.com/docs/primitives/components/tooltip#api-reference
---

# Tooltip

## Overview

A popup that displays information related to an element when the element receives keyboard focus or the mouse hovers over it.

## Import

```tsx
import {
  Tooltip,
  TooltipContent,
  TooltipTrigger,
} from "@/components/ui/tooltip"
```

## Installation

```bash
npx shadcn@latest add tooltip
```

## Usage

```tsx
<Tooltip>
  <TooltipTrigger>Hover</TooltipTrigger>
  <TooltipContent>
    <p>Add to library</p>
  </TooltipContent>
</Tooltip>
```

## Composition

```
Tooltip
├── TooltipTrigger
└── TooltipContent
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Examples

### Side

Use the `side` prop to change the position of the tooltip.

### With Keyboard Shortcut

### Disabled Button

Show a tooltip on a disabled button by wrapping it with a span.

## Accessibility

### ARIA Roles

Tooltip content: `role="tooltip"`. Trigger references it via `aria-describedby`.

### Keyboard Navigation

| Key | Action |
|-----|--------|
| Tab | Focus trigger (tooltip appears) |
| Escape | Dismiss tooltip |

### ARIA Attributes

`aria-describedby` on the trigger pointing to the tooltip id. Tooltip content is supplemental — the trigger must be independently understandable.

### Screen Reader Notes

Tooltip text should supplement, not replace, visible labels. Avoid putting interactive content (links, buttons) inside a tooltip.

## Tailwind Tokens

**CSS variables used:**

- `--popover`
- `--popover-foreground`
- `--border`
- `--radius`

**Key Tailwind classes:**

- `z-50`
- `overflow-hidden`
- `rounded-md`
- `border`
- `bg-popover`
- `px-3`
- `py-1.5`
- `text-xs`
- `text-popover-foreground`
- `shadow-md`

Uses `--popover` tokens. Animation via `data-[state=*]` Tailwind variants.

## Notes

- Full API reference: [https://www.radix-ui.com/docs/primitives/components/tooltip](https://www.radix-ui.com/docs/primitives/components/tooltip)
- Radix API reference: [https://www.radix-ui.com/docs/primitives/components/tooltip#api-reference](https://www.radix-ui.com/docs/primitives/components/tooltip#api-reference)
