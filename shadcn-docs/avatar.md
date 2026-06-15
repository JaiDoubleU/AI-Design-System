---
component: avatar
source: https://ui.shadcn.com/docs/components/avatar
radix-doc: https://www.radix-ui.com/primitives/docs/components/avatar
radix-api: https://www.radix-ui.com/primitives/docs/components/avatar#api-reference
---

# Avatar

## Overview

An image element with a fallback for representing the user.

## Import

```tsx
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
```

## Installation

```bash
npx shadcn@latest add avatar
```

## Usage

```tsx
<Avatar>
  <AvatarImage src="https://github.com/shadcn.png" />
  <AvatarFallback>CN</AvatarFallback>
</Avatar>
```

## Composition

```
Avatar
├── AvatarImage
├── AvatarFallback
└── AvatarBadge
```

## Props & Variants

### Avatar

The `Avatar` component is the root component that wraps the avatar image and fallback.

| Prop        | Type                        | Default     |
| ----------- | --------------------------- | ----------- |
| `size`      | `"default" \| "sm" \| "lg"` | `"default"` |
| `className` | `string`                    | -           |

### AvatarImage

The `AvatarImage` component displays the avatar image. It accepts all Radix UI Avatar Image props.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `src`       | `string` | -       |
| `alt`       | `string` | -       |
| `className` | `string` | -       |

### AvatarFallback

The `AvatarFallback` component displays a fallback when the image fails to load. It accepts all Radix UI Avatar Fallback props.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### AvatarBadge

The `AvatarBadge` component displays a badge indicator on the avatar, typically positioned at the bottom right.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### AvatarGroup

The `AvatarGroup` component displays a group of avatars with overlapping styling.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### AvatarGroupCount

The `AvatarGroupCount` component displays a count indicator in an avatar group, typically showing the number of additional avatars.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

## Examples

### Basic

A basic avatar component with an image and a fallback.

### Badge

Use the `AvatarBadge` component to add a badge to the avatar. The badge is positioned at the bottom right of the avatar.
Use the `className` prop to add custom styles to the badge such as custom colors, sizes, etc.
```tsx showLineNumbers
```

### Badge with Icon

You can also use an icon inside `<AvatarBadge>`.

### Avatar Group

Use the `AvatarGroup` component to add a group of avatars.

### Avatar Group Count

Use `<AvatarGroupCount>` to add a count to the group.

### Avatar Group with Icon

You can also use an icon inside `<AvatarGroupCount>`.

### Sizes

Use the `size` prop to change the size of the avatar.

### Dropdown

You can use the `Avatar` component as a trigger for a dropdown menu.

## Accessibility

### ARIA Roles

Uses an `<img>` element internally. The fallback renders text.

### Keyboard Navigation

Not interactive unless wrapped in a button.

### ARIA Attributes

Add `alt` text to the image via the `src` when meaningful. Set `alt=""` (empty string) for decorative avatars.

### Screen Reader Notes

The `AvatarFallback` is shown while the image loads or if it fails. Ensure text initials are surrounded by a visually hidden label when the avatar represents a person.

## Tailwind Tokens

**CSS variables used:**

- `--muted`
- `--muted-foreground`
- `--radius`

**Key Tailwind classes:**

- `relative`
- `flex`
- `h-10`
- `w-10`
- `shrink-0`
- `overflow-hidden`
- `rounded-full`
- `bg-muted`
- `text-muted-foreground`

Fallback uses `--muted` background and `--muted-foreground` text.

## Notes

- Full API reference: [https://www.radix-ui.com/primitives/docs/components/avatar](https://www.radix-ui.com/primitives/docs/components/avatar)
- Radix API reference: [https://www.radix-ui.com/primitives/docs/components/avatar#api-reference](https://www.radix-ui.com/primitives/docs/components/avatar#api-reference)
