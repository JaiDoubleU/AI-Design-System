---
component: slider
source: https://ui.shadcn.com/docs/components/slider
radix-doc: https://www.radix-ui.com/docs/primitives/components/slider
radix-api: https://www.radix-ui.com/docs/primitives/components/slider#api-reference
---

# Slider

## Overview

An input where the user selects a value from within a given range.

## Import

```tsx
import { Slider } from "@/components/ui/slider"
```

## Installation

```bash
npx shadcn@latest add slider
```

## Usage

```tsx
<Slider defaultValue={[33]} max={100} step={1} />
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Examples

### Range

Use an array with two values for a range slider.

### Multiple Thumbs

Use an array with multiple values for multiple thumbs.

### Vertical

Use `orientation="vertical"` for a vertical slider.

### Controlled

### Disabled

Use the `disabled` prop to disable the slider.

## Accessibility

### ARIA Roles

`role="slider"` on the thumb.

### Keyboard Navigation

| Key | Action |
|-----|--------|
| ArrowRight / ArrowUp | Increase value by one step |
| ArrowLeft / ArrowDown | Decrease value by one step |
| PageUp | Increase value by a large step |
| PageDown | Decrease value by a large step |
| Home | Set to minimum value |
| End | Set to maximum value |

### ARIA Attributes

`aria-valuenow`; `aria-valuemin`; `aria-valuemax`; `aria-label` or `aria-labelledby`; `aria-valuetext` for human-readable value.

### Screen Reader Notes

Follows the [WAI-ARIA Slider](https://www.w3.org/WAI/ARIA/apg/patterns/slider/) pattern. Range sliders have two thumbs, each with their own `aria-*` props.

## Tailwind Tokens

**CSS variables used:**

- `--primary`
- `--primary-foreground`
- `--muted`
- `--ring`
- `--radius`

**Key Tailwind classes:**

- `relative`
- `flex`
- `w-full`
- `touch-none`
- `select-none`
- `items-center`

Track: `--muted`. Range fill: `--primary`. Thumb: `--primary` with `--ring` focus.

## Notes

- Full API reference: [https://www.radix-ui.com/docs/primitives/components/slider](https://www.radix-ui.com/docs/primitives/components/slider)
- Radix API reference: [https://www.radix-ui.com/docs/primitives/components/slider#api-reference](https://www.radix-ui.com/docs/primitives/components/slider#api-reference)
