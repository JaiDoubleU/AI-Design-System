---
component: scroll-area
source: https://ui.shadcn.com/docs/components/scroll-area
radix-doc: https://www.radix-ui.com/docs/primitives/components/scroll-area
radix-api: https://www.radix-ui.com/docs/primitives/components/scroll-area#api-reference
---

# Scroll Area

## Overview

Augments native scroll functionality for custom, cross-browser styling.

## Import

```tsx
import { ScrollArea, ScrollBar } from "@/components/ui/scroll-area"
```

## Installation

```bash
npx shadcn@latest add scroll-area
```

## Usage

```tsx
<ScrollArea className="h-[200px] w-[350px] rounded-md border p-4">
  Your scrollable content here.
</ScrollArea>
```

## Composition

```
ScrollArea
└── ScrollBar
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Examples

### Horizontal

Use `ScrollBar` with `orientation="horizontal"` for horizontal scrolling.

## Accessibility

### ARIA Roles

Custom scrollable viewport with styled scrollbar tracks. Scrollbar: `role="scrollbar"`, `aria-orientation`, `aria-valuenow`, `aria-valuemin`, `aria-valuemax`, `aria-controls`.

### Keyboard Navigation

Standard browser scroll keyboard interactions (Arrow keys, PageUp/Down, Home/End) work within the viewport.

### ARIA Attributes

The scrollbar thumb is interactive and announces position to assistive technology.

### Screen Reader Notes

Built on Radix ScrollArea. Provides cross-browser consistent scroll styling while maintaining native scroll behavior.

## Tailwind Tokens

**CSS variables used:**

- `--border`
- `--muted`

**Key Tailwind classes:**

- `relative`
- `overflow-hidden`

Scrollbar thumb and track use `--border` color variants.

## Notes

- Full API reference: [https://www.radix-ui.com/docs/primitives/components/scroll-area](https://www.radix-ui.com/docs/primitives/components/scroll-area)
- Radix API reference: [https://www.radix-ui.com/docs/primitives/components/scroll-area#api-reference](https://www.radix-ui.com/docs/primitives/components/scroll-area#api-reference)
