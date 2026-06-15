---
component: table
source: https://ui.shadcn.com/docs/components/table
---

# Table

## Overview

A responsive table component.

## Import

```tsx
import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"
```

## Installation

```bash
npx shadcn@latest add table
```

## Usage

```tsx
<Table>
  <TableCaption>A list of your recent invoices.</TableCaption>
  <TableHeader>
    <TableRow>
      <TableHead className="w-[100px]">Invoice</TableHead>
      <TableHead>Status</TableHead>
      <TableHead>Method</TableHead>
      <TableHead className="text-right">Amount</TableHead>
    </TableRow>
  </TableHeader>
  <TableBody>
    <TableRow>
      <TableCell className="font-medium">INV001</TableCell>
      <TableCell>Paid</TableCell>
      <TableCell>Credit Card</TableCell>
      <TableCell className="text-right">$250.00</TableCell>
    </TableRow>
  </TableBody>
</Table>
```

## Composition

```
Table
├── TableCaption
├── TableHeader
│   └── TableRow
│       ├── TableHead
│       ├── TableHead
│       ├── TableHead
│       └── TableHead
├── TableBody
│   ├── TableRow
│   │   ├── TableCell
│   │   ├── TableCell
│   │   ├── TableCell
│   │   └── TableCell
│   └── TableRow
│       ├── TableCell
│       ├── TableCell
│       ├── TableCell
│       └── TableCell
└── TableFooter
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Examples

### Footer

Use the `<TableFooter />` component to add a footer to the table.

### Actions

A table showing actions for each row using a `<DropdownMenu />` component.

## Accessibility

### ARIA Roles

Uses native HTML table elements: `<table>`, `<thead>`, `<tbody>`, `<tfoot>`, `<tr>`, `<th>`, `<td>`, `<caption>`.

### Keyboard Navigation

Not interactive by default. Interactive cells (checkboxes, buttons) are keyboard focusable per their own role.

### ARIA Attributes

`scope="col"` / `scope="row"` on `<th>`. Add `<caption>` or `aria-label` / `aria-labelledby` to describe the table. Sortable headers: `aria-sort`.

### Screen Reader Notes

Use the DataTable component for tables with sorting, filtering, and pagination. Prefer native HTML table elements over ARIA table roles.

## Tailwind Tokens

**CSS variables used:**

- `--border`
- `--muted`
- `--foreground`
- `--muted-foreground`

**Key Tailwind classes:**

- `w-full`
- `caption-bottom`
- `text-sm`
- `border-b`
- `text-muted-foreground`
- `bg-muted/50`

Header row uses `--muted/50` background. Borders: `--border`.

## Notes

