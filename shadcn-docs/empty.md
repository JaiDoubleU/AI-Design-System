---
component: empty
source: https://ui.shadcn.com/docs/components/empty
---

# Empty

## Overview

Use the Empty component to display an empty state.

## Import

```tsx
import {
  Empty,
  EmptyContent,
  EmptyDescription,
  EmptyHeader,
  EmptyMedia,
  EmptyTitle,
} from "@/components/ui/empty"
```

## Installation

```bash
npx shadcn@latest add empty
```

## Usage

```tsx
<Empty>
  <EmptyHeader>
    <EmptyMedia variant="icon">
      <Icon />
    </EmptyMedia>
    <EmptyTitle>No data</EmptyTitle>
    <EmptyDescription>No data found</EmptyDescription>
  </EmptyHeader>
  <EmptyContent>
    <Button>Add data</Button>
  </EmptyContent>
</Empty>
```

## Composition

```
Empty
├── EmptyHeader
│   ├── EmptyMedia
│   ├── EmptyTitle
│   └── EmptyDescription
└── EmptyContent
```

## Props & Variants

### Empty

The main component of the empty state. Wraps the `EmptyHeader` and `EmptyContent` components.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` |         |

### EmptyHeader

The `EmptyHeader` component wraps the empty media, title, and description.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` |         |

### EmptyMedia

Use the `EmptyMedia` component to display the media of the empty state such as an icon or an image. You can also use it to display other components such as an avatar.

| Prop        | Type                  | Default   |
| ----------- | --------------------- | --------- |
| `variant`   | `"default" \| "icon"` | `default` |
| `className` | `string`              |           |

### EmptyTitle

Use the `EmptyTitle` component to display the title of the empty state.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` |         |

### EmptyDescription

Use the `EmptyDescription` component to display the description of the empty state.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` |         |

### EmptyContent

Use the `EmptyContent` component to display the content of the empty state such as a button, input or a link.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` |         |

## Examples

### Outline

Use the `border` utility class to create an outline empty state.

### Background

Use the `bg-*` and `bg-gradient-*` utilities to add a background to the empty state.

### Avatar

Use the `EmptyMedia` component to display an avatar in the empty state.

### Avatar Group

Use the `EmptyMedia` component to display an avatar group in the empty state.

### InputGroup

You can add an `InputGroup` component to the `EmptyContent` component.

## Accessibility

### ARIA Roles

No implicit ARIA role — a layout component for empty states.

### Keyboard Navigation

Not interactive.

### ARIA Attributes

If the empty state is a response to user action, wrap in `role="status"` with an appropriate `aria-label`.

### Screen Reader Notes

Typically pairs with an illustration, heading, description, and a call-to-action button.

## Tailwind Tokens

**CSS variables used:**

- `--muted-foreground`
- `--foreground`

**Key Tailwind classes:**

- `flex`
- `flex-col`
- `items-center`
- `justify-center`
- `gap-4`
- `text-center`

Minimal layout component. Icon, heading, description, and action CTA are composed manually.

## Notes

