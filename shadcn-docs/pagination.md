---
component: pagination
source: https://ui.shadcn.com/docs/components/pagination
---

# Pagination

## Overview

Pagination with page navigation, next and previous links.

## Import

```tsx
import {
  Pagination,
  PaginationContent,
  PaginationEllipsis,
  PaginationItem,
  PaginationLink,
  PaginationNext,
  PaginationPrevious,
} from "@/components/ui/pagination"
```

## Installation

```bash
npx shadcn@latest add pagination
```

## Usage

```tsx
<Pagination>
  <PaginationContent>
    <PaginationItem>
      <PaginationPrevious href="#" />
    </PaginationItem>
    <PaginationItem>
      <PaginationLink href="#">1</PaginationLink>
    </PaginationItem>
    <PaginationItem>
      <PaginationLink href="#" isActive>
        2
      </PaginationLink>
    </PaginationItem>
    <PaginationItem>
      <PaginationLink href="#">3</PaginationLink>
    </PaginationItem>
    <PaginationItem>
      <PaginationEllipsis />
    </PaginationItem>
    <PaginationItem>
      <PaginationNext href="#" />
    </PaginationItem>
  </PaginationContent>
</Pagination>
```

## Composition

```
Pagination
└── PaginationContent
    ├── PaginationItem
    │   └── PaginationPrevious
    ├── PaginationItem
    │   └── PaginationLink
    ├── PaginationItem
    │   └── PaginationEllipsis
    └── PaginationItem
        └── PaginationNext
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Examples

### Simple

A simple pagination with only page numbers.

### Icons Only

Use just the previous and next buttons without page numbers. This is useful for data tables with a rows per page selector.

## Accessibility

### ARIA Roles

Wraps in `<nav aria-label="pagination">`. Previous/Next and page number links are `<a>` elements.

### Keyboard Navigation

| Key | Action |
|-----|--------|
| Tab | Move between page links |
| Enter | Navigate to the link's target page |

### ARIA Attributes

`aria-current="page"` on the active page link. `aria-label="Go to page N"` on individual page links. `aria-disabled` on unavailable links (e.g., Previous on first page).

### Screen Reader Notes

Screen readers announce the nav landmark and aria-label. Ellipsis items (`PaginationEllipsis`) should be `aria-hidden`.

## Tailwind Tokens

**CSS variables used:**

- `--border`
- `--accent`
- `--accent-foreground`
- `--background`
- `--foreground`
- `--radius`

**Key Tailwind classes:**

- `flex`
- `flex-row`
- `items-center`
- `gap-1`

Active page button uses `--border` emphasis variant. Disabled arrow buttons use `--muted`.

## Notes


### Changelog

### RTL Support

If you're upgrading from a previous version of the `Pagination` component, you'll need to apply the following updates to add the `text` prop:

```diff
  function PaginationPrevious({
    className,
+   text = "Previous",
    ...props
- }: React.ComponentProps<typeof PaginationLink>) {
+ }: React.ComponentProps<typeof PaginationLink> & { text?: string }) {
    return (
      <PaginationLink
        aria-label="Go to previous page"
        {...props}
      >
        <ChevronLeftIcon />
        <span className="cn-pagination-previous-text hidden sm:block">
-         Previous
+         {text}
    )
  }
```

```diff
  function PaginationNext({
    className,
+   text = "Next",
    ...props
- }: React.ComponentProps<typeof PaginationLink>) {
+ }: React.ComponentProps<typeof PaginationLink> & { text?: string }) {
    return (
      <PaginationLink
        aria-label="Go to next page"
        {...props}
      >
-       <span className="cn-pagination-next-text hidden sm:block">Next</span>
+       <span className="cn-pagination-next-text hidden sm:block">{text}</span>
        <ChevronRightIcon />
    )
  }
```
