---
component: dropdown-menu
source: https://ui.shadcn.com/docs/components/dropdown-menu
radix-doc: https://www.radix-ui.com/docs/primitives/components/dropdown-menu
radix-api: https://www.radix-ui.com/docs/primitives/components/dropdown-menu#api-reference
---

# Dropdown Menu

## Overview

Displays a menu to the user — such as a set of actions or functions — triggered by a button.

## Import

```tsx
import { Button } from "@/components/ui/button"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuGroup,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
```

## Installation

```bash
npx shadcn@latest add dropdown-menu
```

## Usage

```tsx
<DropdownMenu>
  <DropdownMenuTrigger asChild>
    <Button variant="outline">Open</Button>
  </DropdownMenuTrigger>
  <DropdownMenuContent>
    <DropdownMenuGroup>
      <DropdownMenuLabel>My Account</DropdownMenuLabel>
      <DropdownMenuItem>Profile</DropdownMenuItem>
      <DropdownMenuItem>Billing</DropdownMenuItem>
    </DropdownMenuGroup>
    <DropdownMenuSeparator />
    <DropdownMenuGroup>
      <DropdownMenuItem>Team</DropdownMenuItem>
      <DropdownMenuItem>Subscription</DropdownMenuItem>
    </DropdownMenuGroup>
  </DropdownMenuContent>
</DropdownMenu>
```

## Composition

```
DropdownMenu
├── DropdownMenuTrigger
└── DropdownMenuContent
    ├── DropdownMenuGroup
    │   ├── DropdownMenuLabel
    │   ├── DropdownMenuItem
    │   └── DropdownMenuItem
    ├── DropdownMenuSeparator
    ├── DropdownMenuGroup
    │   ├── DropdownMenuLabel
    │   ├── DropdownMenuCheckboxItem
    │   └── DropdownMenuCheckboxItem
    ├── DropdownMenuSeparator
    ├── DropdownMenuGroup
    │   ├── DropdownMenuLabel
    │   └── DropdownMenuRadioGroup
    │       ├── DropdownMenuRadioItem
    │       └── DropdownMenuRadioItem
    └── DropdownMenuSub
        ├── DropdownMenuSubTrigger
        └── DropdownMenuSubContent
            └── DropdownMenuGroup
                ├── DropdownMenuLabel
                ├── DropdownMenuItem
                └── DropdownMenuItem
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Examples

### Basic

A basic dropdown menu with labels and separators.

### Submenu

Use `DropdownMenuSub` to nest secondary actions.

### Shortcuts

Add `DropdownMenuShortcut` to show keyboard hints.

### Icons

Combine icons with labels for quick scanning.

### Checkboxes

Use `DropdownMenuCheckboxItem` for toggles.

### Checkboxes Icons

Add icons to checkbox items.

### Radio Group

Use `DropdownMenuRadioGroup` for exclusive choices.

### Radio Icons

Show radio options with icons.

### Destructive

Use `variant="destructive"` for irreversible actions.

### Avatar

An account switcher dropdown triggered by an avatar.

### Complex

A richer example combining groups, icons, and submenus.

## Accessibility

### ARIA Roles

Trigger: `aria-haspopup="menu"`, `aria-expanded`. Menu: `role="menu"`. Items: `role="menuitem"`, `role="menuitemcheckbox"`, `role="menuitemradio"`.

### Keyboard Navigation

| Key | Action |
|-----|--------|
| Enter / Space / ArrowDown | Open menu |
| ArrowDown / ArrowUp | Navigate menu items |
| ArrowRight | Open submenu |
| ArrowLeft / Escape | Close submenu / menu |
| Enter / Space | Activate item |
| Home / End | Move to first / last item |

### ARIA Attributes

Groups: `role="group"` with `aria-label`. Separators: `role="separator"`. Checked items: `aria-checked="true"`.

### Screen Reader Notes

Built on Radix DropdownMenu. Follows the [WAI-ARIA Menu Button](https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/) pattern.

## Tailwind Tokens

**CSS variables used:**

- `--popover`
- `--popover-foreground`
- `--accent`
- `--accent-foreground`
- `--border`
- `--muted`
- `--muted-foreground`
- `--destructive`
- `--radius`

**Key Tailwind classes:**

- `z-50`
- `min-w-[8rem]`
- `rounded-md`
- `border`
- `bg-popover`
- `p-1`
- `shadow-md`

Shares token set with ContextMenu. Destructive items use `--destructive` color.

## Notes

- Full API reference: [https://www.radix-ui.com/docs/primitives/components/dropdown-menu](https://www.radix-ui.com/docs/primitives/components/dropdown-menu)
- Radix API reference: [https://www.radix-ui.com/docs/primitives/components/dropdown-menu#api-reference](https://www.radix-ui.com/docs/primitives/components/dropdown-menu#api-reference)
