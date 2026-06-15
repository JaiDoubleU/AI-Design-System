---
component: menubar
source: https://ui.shadcn.com/docs/components/menubar
radix-doc: https://www.radix-ui.com/docs/primitives/components/menubar
radix-api: https://www.radix-ui.com/docs/primitives/components/menubar#api-reference
---

# Menubar

## Overview

A visually persistent menu common in desktop applications that provides quick access to a consistent set of commands.

## Import

```tsx
import {
  Menubar,
  MenubarContent,
  MenubarGroup,
  MenubarItem,
  MenubarMenu,
  MenubarSeparator,
  MenubarShortcut,
  MenubarTrigger,
} from "@/components/ui/menubar"
```

## Installation

```bash
npx shadcn@latest add menubar
```

## Usage

```tsx
<Menubar>
  <MenubarMenu>
    <MenubarTrigger>File</MenubarTrigger>
    <MenubarContent>
      <MenubarGroup>
        <MenubarItem>
          New Tab <MenubarShortcut>⌘T</MenubarShortcut>
        </MenubarItem>
        <MenubarItem>New Window</MenubarItem>
      </MenubarGroup>
      <MenubarSeparator />
      <MenubarGroup>
        <MenubarItem>Share</MenubarItem>
        <MenubarItem>Print</MenubarItem>
      </MenubarGroup>
    </MenubarContent>
  </MenubarMenu>
</Menubar>
```

## Composition

```
Menubar
├── MenubarMenu
│   ├── MenubarTrigger
│   └── MenubarContent
│       ├── MenubarGroup
│       │   ├── MenubarLabel
│       │   ├── MenubarItem
│       │   └── MenubarItem
│       ├── MenubarSeparator
│       ├── MenubarGroup
│       │   ├── MenubarLabel
│       │   ├── MenubarCheckboxItem
│       │   └── MenubarCheckboxItem
│       ├── MenubarSeparator
│       ├── MenubarGroup
│       │   ├── MenubarLabel
│       │   └── MenubarRadioGroup
│       │       ├── MenubarRadioItem
│       │       └── MenubarRadioItem
│       └── MenubarSub
│           ├── MenubarSubTrigger
│           └── MenubarSubContent
│               └── MenubarGroup
│                   ├── MenubarLabel
│                   ├── MenubarItem
│                   └── MenubarItem
└── MenubarMenu
    ├── MenubarTrigger
    └── MenubarContent
        └── MenubarGroup
            ├── MenubarLabel
            ├── MenubarItem
            └── MenubarItem
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Examples

### Checkbox

Use `MenubarCheckboxItem` for toggleable options.

### Radio

Use `MenubarRadioGroup` and `MenubarRadioItem` for single-select options.

### Submenu

Use `MenubarSub`, `MenubarSubTrigger`, and `MenubarSubContent` for nested menus.

### With Icons

## Accessibility

### ARIA Roles

`role="menubar"` on the root; `role="menu"` on each sub-menu; `role="menuitem"`, `role="menuitemcheckbox"`, `role="menuitemradio"` on items.

### Keyboard Navigation

| Key | Action |
|-----|--------|
| Tab / Shift+Tab | Move focus to/from menubar |
| ArrowRight / ArrowLeft | Move between top-level menu triggers |
| ArrowDown / Enter / Space | Open sub-menu |
| ArrowUp | Close sub-menu |
| Escape | Close sub-menu and return focus |
| Home / End | Move to first / last item in menu |

### ARIA Attributes

Follows the [WAI-ARIA Menu](https://www.w3.org/WAI/ARIA/apg/patterns/menubar/) design pattern.

### Screen Reader Notes

Top-level triggers have `aria-haspopup="menu"` and `aria-expanded`.

## Tailwind Tokens

**CSS variables used:**

- `--background`
- `--foreground`
- `--accent`
- `--accent-foreground`
- `--border`
- `--popover`
- `--popover-foreground`
- `--muted`
- `--radius`

**Key Tailwind classes:**

- `flex`
- `h-9`
- `items-center`
- `gap-1`
- `rounded-md`
- `border`
- `bg-background`
- `p-1`
- `shadow-sm`

Top-level trigger active/open state uses `--accent` background.

## Notes

- Full API reference: [https://www.radix-ui.com/docs/primitives/components/menubar](https://www.radix-ui.com/docs/primitives/components/menubar)
- Radix API reference: [https://www.radix-ui.com/docs/primitives/components/menubar#api-reference](https://www.radix-ui.com/docs/primitives/components/menubar#api-reference)
