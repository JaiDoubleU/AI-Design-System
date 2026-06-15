---
component: skeleton
source: https://ui.shadcn.com/docs/components/skeleton
---

# Skeleton

## Overview

Use to show a placeholder while content is loading.

## Import

```tsx
import { Skeleton } from "@/components/ui/skeleton"
```

## Installation

```bash
npx shadcn@latest add skeleton
```

## Usage

```tsx
<Skeleton className="h-[20px] w-[100px] rounded-full" />
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Examples

### Avatar

### Card

### Text

### Form

### Table

## Accessibility

### ARIA Roles

No implicit ARIA role on skeleton elements.

### Keyboard Navigation

Not interactive.

### ARIA Attributes

Wrap the skeleton region in `role="status"` with `aria-label="Loading…"` and `aria-busy="true"`. Remove `aria-busy` when loading is complete.

### Screen Reader Notes

Skeleton components are purely visual loading placeholders. Announce loading state via a live region, not the skeleton itself.

## Tailwind Tokens

**CSS variables used:**

- `--muted`

**Key Tailwind classes:**

- `animate-pulse`
- `rounded-md`
- `bg-muted`

Uses `animate-pulse` Tailwind animation. Background: `--muted`.

## Notes

