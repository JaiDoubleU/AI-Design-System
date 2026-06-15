---
component: progress
source: https://ui.shadcn.com/docs/components/progress
radix-doc: https://www.radix-ui.com/docs/primitives/components/progress
radix-api: https://www.radix-ui.com/docs/primitives/components/progress#api-reference
---

# Progress

## Overview

Displays an indicator showing the completion progress of a task, typically displayed as a progress bar.

## Import

```tsx
import { Progress } from "@/components/ui/progress"
```

## Installation

```bash
npx shadcn@latest add progress
```

## Usage

```tsx
<Progress value={33} />
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Examples

### Label

Use a `Field` component to add a label to the progress bar.

### Controlled

A progress bar that can be controlled by a slider.

## Accessibility

### ARIA Roles

`role="progressbar"`.

### Keyboard Navigation

Not interactive.

### ARIA Attributes

`aria-valuenow` (current value); `aria-valuemin` (default `0`); `aria-valuemax` (default `100`); `aria-label` or `aria-labelledby` for the label; `aria-valuetext` for human-readable value (e.g., "Loading 42%").

### Screen Reader Notes

Set `aria-valuetext` when a raw number is not sufficient context (e.g., "Step 2 of 5").

## Tailwind Tokens

**CSS variables used:**

- `--primary`
- `--muted`

**Key Tailwind classes:**

- `relative`
- `h-2`
- `w-full`
- `overflow-hidden`
- `rounded-full`
- `bg-muted`

Track: `--muted`. Fill indicator: `--primary`. Use `className` to override track or fill color.

## Notes

- Full API reference: [https://www.radix-ui.com/docs/primitives/components/progress](https://www.radix-ui.com/docs/primitives/components/progress)
- Radix API reference: [https://www.radix-ui.com/docs/primitives/components/progress#api-reference](https://www.radix-ui.com/docs/primitives/components/progress#api-reference)
