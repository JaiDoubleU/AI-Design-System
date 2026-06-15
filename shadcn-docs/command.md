---
component: command
source: https://ui.shadcn.com/docs/components/command
radix-doc: https://github.com/dip/cmdk
---

# Command

## Overview

Command menu for search and quick actions.

## Import

```tsx
import {
  Command,
  CommandDialog,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
  CommandList,
  CommandSeparator,
  CommandShortcut,
} from "@/components/ui/command"
```

## Installation

```bash
npx shadcn@latest add command
```

## Usage

```tsx
<Command className="max-w-sm rounded-lg border">
  <CommandInput placeholder="Type a command or search..." />
  <CommandList>
    <CommandEmpty>No results found.</CommandEmpty>
    <CommandGroup heading="Suggestions">
      <CommandItem>Calendar</CommandItem>
      <CommandItem>Search Emoji</CommandItem>
      <CommandItem>Calculator</CommandItem>
    </CommandGroup>
    <CommandSeparator />
    <CommandGroup heading="Settings">
      <CommandItem>Profile</CommandItem>
      <CommandItem>Billing</CommandItem>
      <CommandItem>Settings</CommandItem>
    </CommandGroup>
  </CommandList>
</Command>
```

## Composition

```
Command
├── CommandInput
└── CommandList
    ├── CommandEmpty
    ├── CommandGroup
    │   ├── CommandItem
    │   └── CommandItem
    ├── CommandSeparator
    └── CommandGroup
        ├── CommandItem
        └── CommandItem
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Examples

### Basic

A simple command menu in a dialog.

### Shortcuts

### Groups

A command menu with groups, icons and separators.

### Scrollable

Scrollable command menu with multiple items.

## Accessibility

### ARIA Roles

`role="dialog"` (if modal); inner input `role="searchbox"` or `role="combobox"`; results list `role="listbox"`; items `role="option"`.

### Keyboard Navigation

| Key | Action |
|-----|--------|
| ArrowDown / ArrowUp | Navigate list items |
| Enter | Select highlighted item |
| Escape | Close dialog / clear input |
| Any character | Filter items |

### ARIA Attributes

`aria-label` on the dialog; `aria-activedescendant` on the input pointing to highlighted item.

### Screen Reader Notes

Built on `cmdk`. Renders an accessible command palette / search interface.

## Tailwind Tokens

**CSS variables used:**

- `--background`
- `--foreground`
- `--border`
- `--accent`
- `--accent-foreground`
- `--muted`
- `--muted-foreground`
- `--popover`
- `--popover-foreground`
- `--radius`

**Key Tailwind classes:**

- `flex`
- `h-full`
- `w-full`
- `flex-col`
- `overflow-hidden`
- `rounded-md`
- `bg-popover`
- `text-popover-foreground`

Built on `cmdk`. Active item: `--accent` background.

## Notes

- Full API reference: [https://github.com/dip/cmdk](https://github.com/dip/cmdk)
