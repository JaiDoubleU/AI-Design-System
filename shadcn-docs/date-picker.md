---
component: date-picker
source: https://ui.shadcn.com/docs/components/date-picker
---

# Date Picker

## Overview

A date picker component with range and presets.

## Import

```tsx
import { Date Picker } from "@/components/ui/date-picker"
```

## Installation

```bash
npx shadcn@latest add date-picker
```

## Usage

```tsx
<Date Picker />
```

## Composition

```
Popover
├── PopoverTrigger
└── PopoverContent
    └── Calendar
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Examples

### Basic

A basic date picker component.

### Range Picker

A date picker component for selecting a range of dates.

### Date of Birth

A date picker component for selecting a date of birth. This component includes a dropdown caption layout for date and month selection.

### Input

A date picker component with an input field for selecting a date.

### Time Picker

A date picker component with a time input field for selecting a time.

### Natural Language Picker

This component uses the `chrono-node` library to parse natural language dates.

## Accessibility

### ARIA Roles

Composed of `Popover` + `Calendar`. Trigger: `role="button"`. Calendar: `role="grid"`. See Calendar and Popover accessibility.

### Keyboard Navigation

See Calendar and Popover keyboard navigation.

### ARIA Attributes

`aria-label` on the popover trigger (e.g., "Pick a date"). `aria-haspopup="dialog"` on trigger.

### Screen Reader Notes

Date picker is a composition pattern, not a standalone component. Combines Popover for the flyout and Calendar for selection.

## Tailwind Tokens

Composed of Popover + Calendar. Inherits tokens from both components.

## Notes

