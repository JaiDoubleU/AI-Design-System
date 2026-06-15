---
component: chart
source: https://ui.shadcn.com/docs/components/chart
---

# Chart

## Overview

Beautiful charts. Built using Recharts. Copy and paste into your apps.

## Import

```tsx
import { Chart } from "@/components/ui/chart"
```

## Installation

```bash
npx shadcn@latest add chart
```

## Usage

```tsx
<Chart />
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Accessibility

### ARIA Roles

Wraps recharts. The SVG should carry `role="img"` with `aria-label` describing the chart data.

### Keyboard Navigation

Not keyboard interactive by default.

### ARIA Attributes

`aria-label` or `aria-labelledby` on the chart container. For complex charts provide a data table alternative.

### Screen Reader Notes

Consider adding a visually hidden `<table>` version of the chart data for screen readers.

## Tailwind Tokens

**CSS variables used:**

- `--chart-1`
- `--chart-2`
- `--chart-3`
- `--chart-4`
- `--chart-5`
- `--background`
- `--foreground`
- `--border`
- `--muted`

**Key Tailwind classes:**

- `[&_.recharts-cartesian-grid-line[stroke]]:stroke-border`
- `[&_.recharts-curve.recharts-tooltip-cursor]:stroke-border`

Chart colors use `--chart-1` through `--chart-5` CSS variables defined in `globals.css`.

## Notes

