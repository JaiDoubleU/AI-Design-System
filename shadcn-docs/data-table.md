---
component: data-table
source: https://ui.shadcn.com/docs/components/data-table
radix-doc: https://tanstack.com/table/v8/docs/introduction
---

# Data Table

## Overview

Powerful table and datagrids built using TanStack Table.

## Import

```tsx
import { Data Table } from "@/components/ui/data-table"
```

## Installation

```bash
npx shadcn@latest add table
```

## Usage

```tsx
<Data Table />
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Accessibility

### ARIA Roles

`role="table"` (or native `<table>`); `role="rowgroup"`, `role="row"`, `role="columnheader"`, `role="cell"`.

### Keyboard Navigation

| Key | Action |
|-----|--------|
| Tab | Navigate interactive cells and controls |
| Enter / Space | Activate row checkbox or sort header |

### ARIA Attributes

Sortable columns: `aria-sort="ascending"` / `"descending"` / `"none"`. Selected rows: `aria-selected="true"`.

### Screen Reader Notes

Built on TanStack Table. For complex grids consider `role="grid"` with roving tabindex for cell navigation.

## Tailwind Tokens

**CSS variables used:**

- `--border`
- `--background`
- `--muted`
- `--muted-foreground`
- `--foreground`
- `--accent`

Built on TanStack Table + shadcn/ui Table component. Inherits Table token set.

## Notes

- Full API reference: [https://tanstack.com/table/v8/docs/introduction](https://tanstack.com/table/v8/docs/introduction)
