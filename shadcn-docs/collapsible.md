---
component: collapsible
source: https://ui.shadcn.com/docs/components/collapsible
radix-doc: https://www.radix-ui.com/docs/primitives/components/collapsible
radix-api: https://www.radix-ui.com/docs/primitives/components/collapsible#api-reference
---

# Collapsible

## Overview

An interactive component which expands/collapses a panel.

## Import

```tsx
import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from "@/components/ui/collapsible"
```

## Installation

```bash
npx shadcn@latest add collapsible
```

## Usage

```tsx
<Collapsible>
  <CollapsibleTrigger>Can I use this in my project?</CollapsibleTrigger>
  <CollapsibleContent>
    Yes. Free to use for personal and commercial projects. No attribution
    required.
  </CollapsibleContent>
</Collapsible>
```

## Composition

```
Collapsible
├── CollapsibleTrigger
└── CollapsibleContent
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Examples

### Basic

### Settings Panel

Use a trigger button to reveal additional settings.

### File Tree

Use nested collapsibles to build a file tree.

## Accessibility

### ARIA Roles

Trigger: native `<button>` with `aria-expanded`; Content: hidden/shown via CSS.

### Keyboard Navigation

| Key | Action |
|-----|--------|
| Enter / Space | Toggle open/closed |
| Tab | Move focus through interactive elements inside |

### ARIA Attributes

`aria-expanded` on trigger; `aria-controls` → content id; content uses `hidden` attribute when collapsed.

### Screen Reader Notes

Unlike Accordion, Collapsible manages a single disclosure. No roving tabindex.

## Tailwind Tokens

Headless component — bring your own styles. Content is hidden/shown via data-state attributes.

## Notes

- Full API reference: [https://www.radix-ui.com/docs/primitives/components/collapsible](https://www.radix-ui.com/docs/primitives/components/collapsible)
- Radix API reference: [https://www.radix-ui.com/docs/primitives/components/collapsible#api-reference](https://www.radix-ui.com/docs/primitives/components/collapsible#api-reference)
