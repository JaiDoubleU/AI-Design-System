---
component: breadcrumb
source: https://ui.shadcn.com/docs/components/breadcrumb
---

# Breadcrumb

## Overview

Displays the path to the current resource using a hierarchy of links.

## Import

```tsx
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"
```

## Installation

```bash
npx shadcn@latest add breadcrumb
```

## Usage

```tsx
<Breadcrumb>
  <BreadcrumbList>
    <BreadcrumbItem>
      <BreadcrumbLink href="/">Home</BreadcrumbLink>
    </BreadcrumbItem>
    <BreadcrumbSeparator />
    <BreadcrumbItem>
      <BreadcrumbLink href="/components">Components</BreadcrumbLink>
    </BreadcrumbItem>
    <BreadcrumbSeparator />
    <BreadcrumbItem>
      <BreadcrumbPage>Breadcrumb</BreadcrumbPage>
    </BreadcrumbItem>
  </BreadcrumbList>
</Breadcrumb>
```

## Composition

```
Breadcrumb
└── BreadcrumbList
    ├── BreadcrumbItem
    │   └── BreadcrumbLink
    ├── BreadcrumbSeparator
    ├── BreadcrumbItem
    │   └── BreadcrumbLink
    ├── BreadcrumbSeparator
    └── BreadcrumbItem
        └── BreadcrumbPage
```

## Props & Variants

### Breadcrumb

The `Breadcrumb` component is the root navigation element that wraps all breadcrumb components.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### BreadcrumbList

The `BreadcrumbList` component displays the ordered list of breadcrumb items.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### BreadcrumbItem

The `BreadcrumbItem` component wraps individual breadcrumb items.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### BreadcrumbLink

The `BreadcrumbLink` component displays a clickable link in the breadcrumb.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### BreadcrumbPage

The `BreadcrumbPage` component displays the current page in the breadcrumb (non-clickable).

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### BreadcrumbSeparator

The `BreadcrumbSeparator` component displays a separator between breadcrumb items. You can pass custom children to override the default separator icon.

| Prop        | Type              | Default |
| ----------- | ----------------- | ------- |
| `children`  | `React.ReactNode` | -       |
| `className` | `string`          | -       |

### BreadcrumbEllipsis

The `BreadcrumbEllipsis` component displays an ellipsis indicator for collapsed breadcrumb items.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

## Examples

### Basic

A basic breadcrumb with a home link and a components link.

### Custom separator

Use a custom component as `children` for `<BreadcrumbSeparator />` to create a custom separator.

### Dropdown

You can compose `<BreadcrumbItem />` with a `<DropdownMenu />` to create a dropdown in the breadcrumb.

### Collapsed

We provide a `<BreadcrumbEllipsis />` component to show a collapsed state when the breadcrumb is too long.

### Link component

To use a custom link component from your routing library, you can use the `asChild` prop on `<BreadcrumbLink />`.

## Accessibility

### ARIA Roles

Wraps in `<nav aria-label="breadcrumb">`. Items in `<ol>` list. Current page item uses `aria-current="page"`.

### Keyboard Navigation

| Key | Action |
|-----|--------|
| Tab | Move focus to each link |
| Enter | Follow the link |

### ARIA Attributes

`aria-label="breadcrumb"` on `<nav>`; `aria-current="page"` on last breadcrumb item.

### Screen Reader Notes

Separators (chevrons, slashes) should be hidden with `aria-hidden="true"`. Collapsed breadcrumbs (ellipsis) should expose an expand control.

## Tailwind Tokens

**CSS variables used:**

- `--foreground`
- `--muted-foreground`
- `--border`

**Key Tailwind classes:**

- `flex`
- `flex-wrap`
- `items-center`
- `gap-1.5`
- `text-sm`
- `text-muted-foreground`

Current page item uses `text-foreground font-normal`. Separator is `aria-hidden`.

## Notes

