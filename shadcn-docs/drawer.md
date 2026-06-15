---
component: drawer
source: https://ui.shadcn.com/docs/components/drawer
radix-doc: https://vaul.emilkowal.ski/getting-started
---

# Drawer

## Overview

A drawer component for React.

## Import

```tsx
import {
  Drawer,
  DrawerClose,
  DrawerContent,
  DrawerDescription,
  DrawerFooter,
  DrawerHeader,
  DrawerTitle,
  DrawerTrigger,
} from "@/components/ui/drawer"
```

## Installation

```bash
npx shadcn@latest add drawer
```

## Usage

```tsx
<Drawer>
  <DrawerTrigger>Open</DrawerTrigger>
  <DrawerContent>
    <DrawerHeader>
      <DrawerTitle>Are you absolutely sure?</DrawerTitle>
      <DrawerDescription>This action cannot be undone.</DrawerDescription>
    </DrawerHeader>
    <DrawerFooter>
      <Button>Submit</Button>
      <DrawerClose>
        <Button variant="outline">Cancel</Button>
      </DrawerClose>
    </DrawerFooter>
  </DrawerContent>
</Drawer>
```

## Composition

```
Drawer
├── DrawerTrigger
└── DrawerContent
    ├── DrawerHeader
    │   ├── DrawerTitle
    │   └── DrawerDescription
    └── DrawerFooter
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Examples

### Scrollable Content

Keep actions visible while the content scrolls.

### Sides

Use the `direction` prop to set the side of the drawer. Available options are `top`, `right`, `bottom`, and `left`.

### Responsive Dialog

You can combine the `Dialog` and `Drawer` components to create a responsive dialog. This renders a `Dialog` component on desktop and a `Drawer` on mobile.

## Accessibility

### ARIA Roles

`role="dialog"`, `aria-modal="true"` — same semantics as Dialog but with a slide-in animation.

### Keyboard Navigation

| Key | Action |
|-----|--------|
| Escape | Close drawer |
| Tab | Cycle focus inside |
| Shift+Tab | Cycle backwards |

### ARIA Attributes

`aria-labelledby` → `DrawerTitle` id; `aria-describedby` → `DrawerDescription` id.

### Screen Reader Notes

Built on `vaul`. Supports swipe-to-close on touch devices. Focus trap and return on close.

## Tailwind Tokens

**CSS variables used:**

- `--background`
- `--foreground`
- `--border`
- `--muted`
- `--muted-foreground`
- `--radius`

**Key Tailwind classes:**

- `fixed`
- `inset-x-0`
- `bottom-0`
- `z-50`
- `mt-24`
- `flex`
- `h-auto`
- `flex-col`
- `rounded-t-[10px]`
- `border`
- `bg-background`

Built on `vaul`. Handle bar uses `--muted` background.

## Notes

- Full API reference: [https://vaul.emilkowal.ski/getting-started](https://vaul.emilkowal.ski/getting-started)
