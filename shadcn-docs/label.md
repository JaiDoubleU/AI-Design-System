---
component: label
source: https://ui.shadcn.com/docs/components/label
radix-doc: https://www.radix-ui.com/docs/primitives/components/label
radix-api: https://www.radix-ui.com/docs/primitives/components/label#api-reference
---

# Label

## Overview

Renders an accessible label associated with controls.

## Import

```tsx
import { Label } from "@/components/ui/label"
```

## Installation

```bash
npx shadcn@latest add label
```

## Usage

```tsx
<Label htmlFor="email">Your email address</Label>
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Accessibility

### ARIA Roles

Renders a `<label>` element.

### Keyboard Navigation

Clicking a label moves focus to its associated control.

### ARIA Attributes

Associate with a form control via `htmlFor` matching the control's `id`. Or wrap the control inside the label.

### Screen Reader Notes

Radix Label prevents text selection on double-click, improving UX for checkboxes and radio buttons.

## Tailwind Tokens

**CSS variables used:**

- `--foreground`
- `--muted-foreground`

**Key Tailwind classes:**

- `text-sm`
- `font-medium`
- `leading-none`
- `peer-disabled:cursor-not-allowed`
- `peer-disabled:opacity-70`

Uses Tailwind `peer-*` variants to style based on adjacent disabled input state.

## Notes

- Full API reference: [https://www.radix-ui.com/docs/primitives/components/label](https://www.radix-ui.com/docs/primitives/components/label)
- Radix API reference: [https://www.radix-ui.com/docs/primitives/components/label#api-reference](https://www.radix-ui.com/docs/primitives/components/label#api-reference)
