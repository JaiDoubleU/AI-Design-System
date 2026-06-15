---
component: toast
source: https://ui.shadcn.com/docs/components/toast
---

# Toast

## Overview

A succinct message that is displayed temporarily.

## Import

```tsx
import { Toast } from "@/components/ui/toast"
```

## Installation

```bash
npx shadcn@latest add toast
```

## Usage

```tsx
<Toast />
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Accessibility

### ARIA Roles

Toast region: `role="region"`, `aria-live`. Individual toast: `role="alert"` (urgent) or `role="status"` (informational).

### Keyboard Navigation

| Key | Action |
|-----|--------|
| Tab | Focus toast and action |
| Escape / close button | Dismiss toast |

### ARIA Attributes

`aria-live="assertive"` for destructive / urgent toasts; `aria-live="polite"` for informational. `aria-atomic="true"` when the entire toast should be re-read on update.

### Screen Reader Notes

Legacy toast component — prefer `Sonner` for new projects. Toasts should not require interaction to dismiss if content is important.

## Tailwind Tokens

**CSS variables used:**

- `--background`
- `--foreground`
- `--border`
- `--destructive`
- `--destructive-foreground`
- `--radius`
- `--muted`
- `--muted-foreground`

**Key Tailwind classes:**

- `group`
- `pointer-events-auto`
- `relative`
- `flex`
- `w-full`
- `items-center`
- `justify-between`
- `space-x-4`
- `rounded-md`
- `border`
- `p-6`
- `pr-8`
- `shadow-lg`

Legacy component. Destructive variant uses `--destructive` tokens. Prefer Sonner.

## Notes

