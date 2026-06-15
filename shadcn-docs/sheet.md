---
component: sheet
source: https://ui.shadcn.com/docs/components/sheet
radix-doc: https://www.radix-ui.com/docs/primitives/components/dialog
radix-api: https://www.radix-ui.com/docs/primitives/components/dialog#api-reference
---

# Sheet

## Overview

Extends the Dialog component to display content that complements the main content of the screen.

## Import

```tsx
import {
  Sheet,
  SheetClose,
  SheetContent,
  SheetDescription,
  SheetFooter,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "@/components/ui/sheet"
```

## Installation

```bash
npx shadcn@latest add sheet
```

## Usage

```tsx
<Sheet>
  <SheetTrigger>Open</SheetTrigger>
  <SheetContent>
    <SheetHeader>
      <SheetTitle>Are you absolutely sure?</SheetTitle>
      <SheetDescription>This action cannot be undone.</SheetDescription>
    </SheetHeader>
  </SheetContent>
</Sheet>
```

## Composition

```
Sheet
├── SheetTrigger
└── SheetContent
    ├── SheetHeader
    │   ├── SheetTitle
    │   └── SheetDescription
    └── SheetFooter
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Examples

### Side

Use the `side` prop on `SheetContent` to set the edge of the screen where the sheet appears. Values are `top`, `right`, `bottom`, or `left`.

### No Close Button

Use `showCloseButton={false}` on `SheetContent` to hide the close button.

## Accessibility

### ARIA Roles

`role="dialog"`, `aria-modal="true"` — a Dialog variant that slides in from a side.

### Keyboard Navigation

| Key | Action |
|-----|--------|
| Escape | Close sheet |
| Tab | Cycle focus inside |
| Shift+Tab | Cycle focus backwards |

### ARIA Attributes

`aria-labelledby` → `SheetTitle` id; `aria-describedby` → `SheetDescription` id.

### Screen Reader Notes

Focus is trapped inside while open. Focus returns to the trigger on close. Supports `side` prop (`top`, `bottom`, `left`, `right`).

## Tailwind Tokens

**CSS variables used:**

- `--background`
- `--foreground`
- `--border`
- `--muted-foreground`
- `--radius`

**Key Tailwind classes:**

- `fixed`
- `inset-y-0`
- `z-50`
- `flex`
- `h-full`
- `flex-col`
- `border-l`
- `bg-background`
- `p-6`
- `shadow-lg`

Overlay: `bg-black/80`. Panel tokens same as Dialog.

## Notes

- Full API reference: [https://www.radix-ui.com/docs/primitives/components/dialog](https://www.radix-ui.com/docs/primitives/components/dialog)
- Radix API reference: [https://www.radix-ui.com/docs/primitives/components/dialog#api-reference](https://www.radix-ui.com/docs/primitives/components/dialog#api-reference)
