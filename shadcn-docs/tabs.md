---
component: tabs
source: https://ui.shadcn.com/docs/components/tabs
radix-doc: https://www.radix-ui.com/docs/primitives/components/tabs
radix-api: https://www.radix-ui.com/docs/primitives/components/tabs#api-reference
---

# Tabs

## Overview

A set of layered sections of content—known as tab panels—that are displayed one at a time.

## Import

```tsx
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
```

## Installation

```bash
npx shadcn@latest add tabs
```

## Usage

```tsx
<Tabs defaultValue="account" className="w-[400px]">
  <TabsList>
    <TabsTrigger value="account">Account</TabsTrigger>
    <TabsTrigger value="password">Password</TabsTrigger>
  </TabsList>
  <TabsContent value="account">Make changes to your account here.</TabsContent>
  <TabsContent value="password">Change your password here.</TabsContent>
</Tabs>
```

## Composition

```
Tabs
├── TabsList
│   ├── TabsTrigger
│   └── TabsTrigger
├── TabsContent
└── TabsContent
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Examples

### Line

Use the `variant="line"` prop on `TabsList` for a line style.

### Vertical

Use `orientation="vertical"` for vertical tabs.

### Disabled

### Icons

## Accessibility

### ARIA Roles

TabsList: `role="tablist"`. Tab: `role="tab"`, `aria-selected`, `aria-controls` → panel id. TabsContent: `role="tabpanel"`, `aria-labelledby` → tab id.

### Keyboard Navigation

| Key | Action |
|-----|--------|
| ArrowRight / ArrowLeft | Move to next / previous tab |
| Home | Move to first tab |
| End | Move to last tab |
| Space / Enter | Activate tab (if not auto-activated) |
| Tab | Move focus into the tab panel |

### ARIA Attributes

Follows the [WAI-ARIA Tabs](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/) pattern. Supports both `activationMode="automatic"` and `manual`.

### Screen Reader Notes

Only the active tab is in the tab sequence; inactive tabs use arrow keys (roving tabindex).

## Tailwind Tokens

**CSS variables used:**

- `--background`
- `--foreground`
- `--muted`
- `--muted-foreground`
- `--border`
- `--radius`

**Key Tailwind classes:**

- `inline-flex`
- `h-9`
- `items-center`
- `justify-center`
- `rounded-lg`
- `bg-muted`
- `p-1`
- `text-muted-foreground`

Active tab: `--background` with shadow. Tab content: `mt-2` below the tab list.

## Notes

- Full API reference: [https://www.radix-ui.com/docs/primitives/components/tabs](https://www.radix-ui.com/docs/primitives/components/tabs)
- Radix API reference: [https://www.radix-ui.com/docs/primitives/components/tabs#api-reference](https://www.radix-ui.com/docs/primitives/components/tabs#api-reference)
