---
component: textarea
source: https://ui.shadcn.com/docs/components/textarea
---

# Textarea

## Overview

Displays a form textarea or a component that looks like a textarea.

## Import

```tsx
import { Textarea } from "@/components/ui/textarea"
```

## Installation

```bash
npx shadcn@latest add textarea
```

## Usage

```tsx
<Textarea />
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Examples

### Field

Use `Field`, `FieldLabel`, and `FieldDescription` to create a textarea with a label and description.

### Disabled

Use the `disabled` prop to disable the textarea. To style the disabled state, add the `data-disabled` attribute to the `Field` component.

### Invalid

Use the `aria-invalid` prop to mark the textarea as invalid. To style the invalid state, add the `data-invalid` attribute to the `Field` component.

### Button

Pair with `Button` to create a textarea with a submit button.

## Accessibility

### ARIA Roles

Native `<textarea>` element — `role="textbox"` with `aria-multiline="true"`.

### Keyboard Navigation

Standard browser keyboard interaction for multiline text areas.

### ARIA Attributes

`aria-invalid`, `aria-required`, `aria-disabled`, `aria-describedby` → hint/error id. Associate with `<label>` via `htmlFor` / `id`.

### Screen Reader Notes

Always pair with a visible `<Label>`. Use `resize` CSS property to control resizing behavior.

## Tailwind Tokens

**CSS variables used:**

- `--background`
- `--foreground`
- `--border`
- `--input`
- `--ring`
- `--radius`
- `--muted-foreground`

**Key Tailwind classes:**

- `flex`
- `min-h-16`
- `w-full`
- `rounded-lg`
- `border`
- `border-input`
- `bg-background`
- `px-3`
- `py-2`
- `text-sm`
- `placeholder:text-muted-foreground`
- `focus-visible:ring-3`
- `disabled:opacity-50`

Same token set as Input. Default `min-h-16`; use CSS `resize` to control resizing.

## Notes

