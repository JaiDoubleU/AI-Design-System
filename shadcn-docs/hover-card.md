---
component: hover-card
source: https://ui.shadcn.com/docs/components/hover-card
radix-doc: https://www.radix-ui.com/docs/primitives/components/hover-card
radix-api: https://www.radix-ui.com/docs/primitives/components/hover-card#api-reference
---

# Hover Card

## Overview

For sighted users to preview content available behind a link.

## Import

```tsx
import {
  HoverCard,
  HoverCardContent,
  HoverCardTrigger,
} from "@/components/ui/hover-card"
```

## Installation

```bash
npx shadcn@latest add hover-card
```

## Usage

```tsx
<HoverCard>
  <HoverCardTrigger>Hover</HoverCardTrigger>
  <HoverCardContent>
    The React Framework – created and maintained by @vercel.
  </HoverCardContent>
</HoverCard>
```

## Composition

```
HoverCard
├── HoverCardTrigger
└── HoverCardContent
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Examples

### Basic

### Sides

## Accessibility

### ARIA Roles

Content: `role="dialog"` (Radix treats it as a non-modal dialog-like surface).

### Keyboard Navigation

Opens on hover (pointer) or focus. Keyboard users can access via Tab to trigger focus.

### ARIA Attributes

`aria-haspopup` on trigger. Content is announced when it appears.

### Screen Reader Notes

Hover Card content should not be the only way to access important information since it requires pointer hover.

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
- `shadow-md`

Same visual token set as Popover but without focus trap.

## Notes

- Full API reference: [https://www.radix-ui.com/docs/primitives/components/hover-card](https://www.radix-ui.com/docs/primitives/components/hover-card)
- Radix API reference: [https://www.radix-ui.com/docs/primitives/components/hover-card#api-reference](https://www.radix-ui.com/docs/primitives/components/hover-card#api-reference)
