---
component: item
source: https://ui.shadcn.com/docs/components/item
---

# Item

## Overview

A versatile component for displaying content with media, title, description, and actions.

## Import

```tsx
import {
  Item,
  ItemActions,
  ItemContent,
  ItemDescription,
  ItemMedia,
  ItemTitle,
} from "@/components/ui/item"
```

## Installation

```bash
npx shadcn@latest add item
```

## Usage

```tsx
<Item>
  <ItemMedia variant="icon">
    <Icon />
  </ItemMedia>
  <ItemContent>
    <ItemTitle>Title</ItemTitle>
    <ItemDescription>Description</ItemDescription>
  </ItemContent>
  <ItemActions>
    <Button>Action</Button>
  </ItemActions>
</Item>
```

## Composition

```
ItemGroup
└── Item
    ├── ItemHeader
    ├── ItemMedia
    ├── ItemContent
    │   ├── ItemTitle
    │   └── ItemDescription
    ├── ItemActions
    └── ItemFooter
```

## Props & Variants

### Item

The main component for displaying content with media, title, description, and actions.

| Prop      | Type                                | Default     |
| --------- | ----------------------------------- | ----------- |
| `variant` | `"default" \| "outline" \| "muted"` | `"default"` |
| `size`    | `"default" \| "sm" \| "xs"`         | `"default"` |
| `asChild` | `boolean`                           | `false`     |

### ItemGroup

A container that groups related items together with consistent styling. ```tsx ```

### ItemSeparator

A separator between items in a group. ```tsx ```

### ItemMedia

Use `ItemMedia` to display media content such as icons, images, or avatars.

| Prop      | Type                             | Default     |
| --------- | -------------------------------- | ----------- |
| `variant` | `"default" \| "icon" \| "image"` | `"default"` |

### ItemContent

Wraps the title and description of the item. ```tsx ```

### ItemTitle

Displays the title of the item. ```tsx ```

### ItemDescription

Displays the description of the item. ```tsx ```

### ItemActions

Container for action buttons or other interactive elements. ```tsx ```

### ItemHeader

Displays a header above the item content. ```tsx ```

### ItemFooter

Displays a footer below the item content. ```tsx ```

## Examples

### Icon

Use `ItemMedia` with `variant="icon"` to display an icon.

### Avatar

You can use `ItemMedia` with `variant="avatar"` to display an avatar.

### Image

Use `ItemMedia` with `variant="image"` to display an image.

### Group

Use `ItemGroup` to group related items together.

### Header

Use `ItemHeader` to add a header above the item content.

### Link

Use the `asChild` prop to render the item as a link. The hover and focus states will be applied to the anchor element.
```tsx showLineNumbers
```

### Dropdown

## Accessibility

### ARIA Roles

Generic list item component. Role depends on context (e.g., `role="listitem"` inside a list).

### Keyboard Navigation

Varies by context.

### ARIA Attributes

Depends on parent container and usage.

### Screen Reader Notes

Used as a building block inside Command, Select, and Dropdown components.

## Tailwind Tokens

**CSS variables used:**

- `--accent`
- `--accent-foreground`
- `--foreground`
- `--muted-foreground`

**Key Tailwind classes:**

- `relative`
- `flex`
- `cursor-default`
- `select-none`
- `items-center`
- `rounded-sm`
- `px-2`
- `py-1.5`
- `text-sm`

Used as a building block — inherits parent context tokens.

## Notes

