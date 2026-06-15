---
component: kbd
source: https://ui.shadcn.com/docs/components/kbd
---

# Kbd

## Overview

Used to display textual user input from keyboard.

## Import

```tsx
import { Kbd } from "@/components/ui/kbd"
```

## Installation

```bash
npx shadcn@latest add kbd
```

## Usage

```tsx
<Kbd>Ctrl</Kbd>
```

## Composition

```
Kbd
KbdGroup
├── Kbd
└── Kbd
```

## Props & Variants

### Kbd

Use the `Kbd` component to display a keyboard key.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | ``      |

### KbdGroup

Use the `KbdGroup` component to group `Kbd` components together.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | ``      |

## Examples

### Group

Use the `KbdGroup` component to group keyboard keys together.

### Button

Use the `Kbd` component inside a `Button` component to display a keyboard key inside a button.

### Tooltip

You can use the `Kbd` component inside a `Tooltip` component to display a tooltip with a keyboard key.

### Input Group

You can use the `Kbd` component inside a `InputGroupAddon` component to display a keyboard key inside an input group.

## Accessibility

### ARIA Roles

Renders a `<kbd>` HTML element — semantically represents a keyboard key.

### Keyboard Navigation

Not interactive.

### ARIA Attributes

Screen readers announce `<kbd>` content as keyboard text. No additional ARIA needed.

### Screen Reader Notes

Can be nested: `<kbd><kbd>Ctrl</kbd>+<kbd>K</kbd></kbd>` for chord shortcuts.

## Tailwind Tokens

**CSS variables used:**

- `--muted`
- `--muted-foreground`
- `--border`
- `--radius`

**Key Tailwind classes:**

- `pointer-events-none`
- `inline-flex`
- `h-5`
- `items-center`
- `gap-1`
- `rounded`
- `border`
- `bg-muted`
- `px-1.5`
- `font-mono`
- `text-[10px]`
- `font-medium`
- `text-muted-foreground`

`--muted` background with `--muted-foreground` text and `--border` outline.

## Notes

