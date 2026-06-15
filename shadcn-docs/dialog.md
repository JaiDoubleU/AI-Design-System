---
component: dialog
source: https://ui.shadcn.com/docs/components/dialog
radix-doc: https://www.radix-ui.com/docs/primitives/components/dialog
radix-api: https://www.radix-ui.com/docs/primitives/components/dialog#api-reference
---

# Dialog

## Overview

A window overlaid on either the primary window or another dialog window, rendering the content underneath inert.

## Import

```tsx
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
```

## Installation

```bash
npx shadcn@latest add dialog
```

## Usage

```tsx
<Dialog>
  <DialogTrigger>Open</DialogTrigger>
  <DialogContent>
    <DialogHeader>
      <DialogTitle>Are you absolutely sure?</DialogTitle>
      <DialogDescription>
        This action cannot be undone. This will permanently delete your account
        and remove your data from our servers.
      </DialogDescription>
    </DialogHeader>
  </DialogContent>
</Dialog>
```

## Composition

```
Dialog
├── DialogTrigger
└── DialogContent
    ├── DialogHeader
    │   ├── DialogTitle
    │   └── DialogDescription
    └── DialogFooter
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Examples

### Custom Close Button

Replace the default close control with your own button.

### No Close Button

Use `showCloseButton={false}` to hide the close button.

### Sticky Footer

Keep actions visible while the content scrolls.

### Scrollable Content

Long content can scroll while the header stays in view.

## Accessibility

### ARIA Roles

`role="dialog"` on the dialog panel; `aria-modal="true"` to tell AT to ignore background content.

### Keyboard Navigation

| Key | Action |
|-----|--------|
| Escape | Close dialog |
| Tab | Cycle focus through interactive elements inside |
| Shift+Tab | Cycle focus backwards |

### ARIA Attributes

`aria-labelledby` → `DialogTitle` id; `aria-describedby` → `DialogDescription` id.

### Screen Reader Notes

Focus is trapped inside the dialog while open. Focus returns to the trigger element on close. Overlay click closes the dialog by default.

## Tailwind Tokens

**CSS variables used:**

- `--background`
- `--foreground`
- `--border`
- `--radius`
- `--muted-foreground`

**Key Tailwind classes:**

- `fixed`
- `inset-0`
- `z-50`
- `bg-black/80`
- `grid`
- `place-items-center`
- `rounded-lg`
- `shadow-lg`
- `p-6`
- `gap-4`

Overlay: `bg-black/80`. Panel: `--background`.

## Notes

- Full API reference: [https://www.radix-ui.com/docs/primitives/components/dialog](https://www.radix-ui.com/docs/primitives/components/dialog)
- Radix API reference: [https://www.radix-ui.com/docs/primitives/components/dialog#api-reference](https://www.radix-ui.com/docs/primitives/components/dialog#api-reference)
