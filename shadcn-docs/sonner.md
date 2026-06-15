---
component: sonner
source: https://ui.shadcn.com/docs/components/sonner
radix-doc: https://sonner.emilkowal.ski
---

# Sonner

## Overview

An opinionated toast component for React.

## Import

```tsx
import { toast } from "sonner"
```

## Installation

```bash
npx shadcn@latest add sonner
```

## Usage

```tsx
toast("Event has been created.")
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Examples

### Types

### Description

### Position

Use the `position` prop to change the position of the toast.

## Accessibility

### ARIA Roles

Toast region: `role="region"`, `aria-label="Notifications"`, `aria-live="polite"`, `aria-atomic="false"`.

### Keyboard Navigation

| Key | Action |
|-----|--------|
| Tab | Focus toast |
| Escape | Dismiss focused toast |

### ARIA Attributes

Individual toasts use `role="status"` (informational) or `role="alert"` (urgent). Action buttons inside are keyboard focusable.

### Screen Reader Notes

Built on the `sonner` library. Toasts are announced by screen readers without stealing focus. Toasts with actions should have sufficient display time.

## Tailwind Tokens

**CSS variables used:**

- `--normal-bg`
- `--normal-text`
- `--normal-border`
- `--success-bg`
- `--success-text`
- `--success-border`
- `--error-bg`
- `--error-text`
- `--error-border`

**Key Tailwind classes:**

- `toaster`
- `group`

Sonner uses its own CSS variable set; override via `toastOptions.classNames` or theme variables.

## Notes

- Full API reference: [https://sonner.emilkowal.ski](https://sonner.emilkowal.ski)
