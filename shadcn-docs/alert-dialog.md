---
component: alert-dialog
source: https://ui.shadcn.com/docs/components/alert-dialog
radix-doc: https://www.radix-ui.com/primitives/docs/components/alert-dialog
radix-api: https://www.radix-ui.com/primitives/docs/components/alert-dialog#api-reference
---

# Alert Dialog

## Overview

A modal dialog that interrupts the user with important content and expects a response.

## Import

```tsx
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from "@/components/ui/alert-dialog"
```

## Installation

```bash
npx shadcn@latest add alert-dialog
```

## Usage

```tsx
<AlertDialog>
  <AlertDialogTrigger asChild>
    <Button variant="outline">Show Dialog</Button>
  </AlertDialogTrigger>
  <AlertDialogContent>
    <AlertDialogHeader>
      <AlertDialogTitle>Are you absolutely sure?</AlertDialogTitle>
      <AlertDialogDescription>
        This action cannot be undone. This will permanently delete your account
        from our servers.
      </AlertDialogDescription>
    </AlertDialogHeader>
    <AlertDialogFooter>
      <AlertDialogCancel>Cancel</AlertDialogCancel>
      <AlertDialogAction>Continue</AlertDialogAction>
    </AlertDialogFooter>
  </AlertDialogContent>
</AlertDialog>
```

## Composition

```
AlertDialog
├── AlertDialogTrigger
└── AlertDialogContent
    ├── AlertDialogHeader
    │   ├── AlertDialogMedia
    │   ├── AlertDialogTitle
    │   └── AlertDialogDescription
    └── AlertDialogFooter
        ├── AlertDialogCancel
        └── AlertDialogAction
```

## Props & Variants

### size

Use the `size` prop on the `AlertDialogContent` component to control the size of the alert dialog. It accepts the following values:

| Prop   | Type                | Default     |
| ------ | ------------------- | ----------- |
| `size` | `"default" \| "sm"` | `"default"` |

## Examples

### Basic

A basic alert dialog with a title, description, and cancel and continue buttons.

### Small

Use the `size="sm"` prop to make the alert dialog smaller.

### Media

Use the `AlertDialogMedia` component to add a media element such as an icon or image to the alert dialog.

### Small with Media

Use the `size="sm"` prop to make the alert dialog smaller and the `AlertDialogMedia` component to add a media element such as an icon or image to the alert dialog.

### Destructive

Use the `AlertDialogAction` component to add a destructive action button to the alert dialog.

## Accessibility

### ARIA Roles

`role="alertdialog"` on the dialog container; `aria-modal="true"` to confine AT to the dialog.

### Keyboard Navigation

| Key | Action |
|-----|--------|
| Tab | Cycle focus through interactive elements inside the dialog |
| Shift+Tab | Cycle focus backwards |
| Enter | Confirm action |
| Escape | Close dialog (cancel) |

### ARIA Attributes

`aria-labelledby` → `AlertDialogTitle` id; `aria-describedby` → `AlertDialogDescription` id.

### Screen Reader Notes

Focus is trapped inside the dialog while open. Focus returns to the trigger on close. Unlike `Dialog`, pressing Escape does **not** close the alert dialog by default — the user must click an action button.

## Tailwind Tokens

**CSS variables used:**

- `--background`
- `--foreground`
- `--border`
- `--radius`
- `--destructive`
- `--muted`

**Key Tailwind classes:**

- `fixed`
- `inset-0`
- `z-50`
- `bg-black/80`
- `rounded-lg`
- `shadow-lg`
- `p-6`

Overlay uses `bg-black/80`. Dialog panel uses `--background`.

## Notes

- Full API reference: [https://www.radix-ui.com/primitives/docs/components/alert-dialog](https://www.radix-ui.com/primitives/docs/components/alert-dialog)
- Radix API reference: [https://www.radix-ui.com/primitives/docs/components/alert-dialog#api-reference](https://www.radix-ui.com/primitives/docs/components/alert-dialog#api-reference)
