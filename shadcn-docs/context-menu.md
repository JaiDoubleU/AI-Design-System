---
component: context-menu
source: https://ui.shadcn.com/docs/components/context-menu
radix-doc: https://www.radix-ui.com/docs/primitives/components/context-menu
radix-api: https://www.radix-ui.com/docs/primitives/components/context-menu#api-reference
---

# Context Menu

## Overview

Displays a menu of actions triggered by a right click.

## Import

```tsx
import {
  ContextMenu,
  ContextMenuContent,
  ContextMenuItem,
  ContextMenuTrigger,
} from "@/components/ui/context-menu"
```

## Installation

```bash
npx shadcn@latest add context-menu
```

## Usage

```tsx
<ContextMenu>
  <ContextMenuTrigger>Right click here</ContextMenuTrigger>
  <ContextMenuContent>
    <ContextMenuItem>Profile</ContextMenuItem>
    <ContextMenuItem>Billing</ContextMenuItem>
    <ContextMenuItem>Team</ContextMenuItem>
    <ContextMenuItem>Subscription</ContextMenuItem>
  </ContextMenuContent>
</ContextMenu>
```

## Composition

```
ContextMenu
├── ContextMenuTrigger
└── ContextMenuContent
    ├── ContextMenuGroup
    │   ├── ContextMenuLabel
    │   ├── ContextMenuItem
    │   └── ContextMenuItem
    ├── ContextMenuSeparator
    ├── ContextMenuGroup
    │   ├── ContextMenuLabel
    │   ├── ContextMenuCheckboxItem
    │   └── ContextMenuCheckboxItem
    ├── ContextMenuSeparator
    ├── ContextMenuGroup
    │   ├── ContextMenuLabel
    │   └── ContextMenuRadioGroup
    │       ├── ContextMenuRadioItem
    │       └── ContextMenuRadioItem
    └── ContextMenuSub
        ├── ContextMenuSubTrigger
        └── ContextMenuSubContent
            └── ContextMenuGroup
                ├── ContextMenuItem
                └── ContextMenuItem
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Examples

### Basic

A simple context menu with a few actions.

### Submenu

Use `ContextMenuSub` to nest secondary actions.

### Shortcuts

Add `ContextMenuShortcut` to show keyboard hints.

### Groups

Group related actions and separate them with dividers.

### Icons

Combine icons with labels for quick scanning.

### Checkboxes

Use `ContextMenuCheckboxItem` for toggles.

### Radio

Use `ContextMenuRadioItem` for exclusive choices.

### Destructive

Use `variant="destructive"` to style the menu item as destructive.

## Accessibility

### ARIA Roles

Menu: `role="menu"`; items: `role="menuitem"`, `role="menuitemcheckbox"`, `role="menuitemradio"`. Triggered by right-click (no ARIA trigger role needed on the trigger element itself).

### Keyboard Navigation

| Key | Action |
|-----|--------|
| ArrowDown / ArrowUp | Move between menu items |
| ArrowRight | Open submenu |
| ArrowLeft | Close submenu / return to parent |
| Enter / Space | Activate item |
| Escape | Close menu |
| Home / End | Move to first / last item |

### ARIA Attributes

Sub-menus: trigger has `aria-haspopup="menu"` and `aria-expanded`. Menu items with sub-menus: `aria-haspopup="menu"`.

### Screen Reader Notes

Also accessible via keyboard: focus the trigger element and press Shift+F10 or the application key to open the context menu.

## Tailwind Tokens

**CSS variables used:**

- `--popover`
- `--popover-foreground`
- `--accent`
- `--accent-foreground`
- `--border`
- `--muted`
- `--muted-foreground`
- `--radius`

**Key Tailwind classes:**

- `z-50`
- `min-w-[8rem]`
- `rounded-md`
- `border`
- `bg-popover`
- `p-1`
- `shadow-md`

Shares token set with DropdownMenu. Active item: `--accent`.

## Notes

- Full API reference: [https://www.radix-ui.com/docs/primitives/components/context-menu](https://www.radix-ui.com/docs/primitives/components/context-menu)
- Radix API reference: [https://www.radix-ui.com/docs/primitives/components/context-menu#api-reference](https://www.radix-ui.com/docs/primitives/components/context-menu#api-reference)
