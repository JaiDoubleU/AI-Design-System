---
component: toggle
source: https://ui.shadcn.com/docs/components/toggle
radix-doc: https://www.radix-ui.com/docs/primitives/components/toggle
radix-api: https://www.radix-ui.com/docs/primitives/components/toggle#api-reference
---

# Toggle

## Overview

A two-state button that can be either on or off.

## Import

```tsx
import { Toggle } from "@/components/ui/toggle"
```

## Installation

```bash
npx shadcn@latest add toggle
```

## Usage

```tsx
<Toggle>Toggle</Toggle>
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Examples

### Outline

Use `variant="outline"` for an outline style.

### With Text

### Size

Use the `size` prop to change the size of the toggle.

### Disabled

## Accessibility

### ARIA Roles

`role="button"`, `aria-pressed="true"` / `"false"` (or `"mixed"`).

### Keyboard Navigation

| Key | Action |
|-----|--------|
| Enter / Space | Toggle pressed state |

### ARIA Attributes

`aria-pressed` to communicate toggle state. `aria-label` when button label does not clearly describe the action.

### Screen Reader Notes

Follows the [WAI-ARIA Toggle Button](https://www.w3.org/WAI/ARIA/apg/patterns/button/) pattern.

## Tailwind Tokens

**CSS variables used:**

- `--accent`
- `--accent-foreground`
- `--muted`
- `--muted-foreground`
- `--ring`
- `--border`
- `--radius`

**Key Tailwind classes:**

- `inline-flex`
- `items-center`
- `justify-center`
- `rounded-md`
- `text-sm`
- `font-medium`
- `ring-offset-background`
- `transition-colors`
- `hover:bg-muted`
- `hover:text-muted-foreground`
- `focus-visible:ring-3`

Pressed state: `data-[state=on]` → `--accent` background.

## Notes

- Full API reference: [https://www.radix-ui.com/docs/primitives/components/toggle](https://www.radix-ui.com/docs/primitives/components/toggle)
- Radix API reference: [https://www.radix-ui.com/docs/primitives/components/toggle#api-reference](https://www.radix-ui.com/docs/primitives/components/toggle#api-reference)
