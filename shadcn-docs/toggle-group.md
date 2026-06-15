---
component: toggle-group
source: https://ui.shadcn.com/docs/components/toggle-group
radix-doc: https://www.radix-ui.com/docs/primitives/components/toggle-group
radix-api: https://www.radix-ui.com/docs/primitives/components/toggle-group#api-reference
---

# Toggle Group

## Overview

A set of two-state buttons that can be toggled on or off.

## Import

```tsx
import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group"
```

## Installation

```bash
npx shadcn@latest add toggle-group
```

## Usage

```tsx
<ToggleGroup type="single">
  <ToggleGroupItem value="a">A</ToggleGroupItem>
  <ToggleGroupItem value="b">B</ToggleGroupItem>
  <ToggleGroupItem value="c">C</ToggleGroupItem>
</ToggleGroup>
```

## Composition

```
ToggleGroup
├── ToggleGroupItem
└── ToggleGroupItem
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Examples

### Outline

Use `variant="outline"` for an outline style.

### Size

Use the `size` prop to change the size of the toggle group.

### Spacing

Use `spacing` to add spacing between toggle group items.

### Vertical

Use `orientation="vertical"` for vertical toggle groups.

### Disabled

### Custom

A custom toggle group example.

## Accessibility

### ARIA Roles

`role="group"` with `aria-label` on the group container. Each toggle: `role="radio"` (single) or `role="checkbox"` (multiple) — or `role="button"` with `aria-pressed`.

### Keyboard Navigation

| Key | Action |
|-----|--------|
| ArrowRight / ArrowLeft | Navigate toggles (single type, roving tabindex) |
| Space | Activate / deactivate toggle (multiple type) |
| Enter | Activate toggle |

### ARIA Attributes

`aria-label` on the group describing the group's purpose.

### Screen Reader Notes

Use `type="single"` for exclusive selection and `type="multiple"` for multi-select.

## Tailwind Tokens

**CSS variables used:**

- `--accent`
- `--accent-foreground`
- `--muted`
- `--border`
- `--radius`

**Key Tailwind classes:**

- `flex`
- `items-center`
- `justify-center`
- `gap-1`

Pressed toggle within the group uses same `--accent` token as Toggle.

## Notes

- Full API reference: [https://www.radix-ui.com/docs/primitives/components/toggle-group](https://www.radix-ui.com/docs/primitives/components/toggle-group)
- Radix API reference: [https://www.radix-ui.com/docs/primitives/components/toggle-group#api-reference](https://www.radix-ui.com/docs/primitives/components/toggle-group#api-reference)

### Changelog

### 2026-05-17 Default Spacing

Changed the default `spacing` from `0` to `2` so toggle groups render with space between items by default. Use `spacing={0}` for connected items.
