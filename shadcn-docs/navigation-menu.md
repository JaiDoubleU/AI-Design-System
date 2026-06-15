---
component: navigation-menu
source: https://ui.shadcn.com/docs/components/navigation-menu
radix-doc: https://www.radix-ui.com/docs/primitives/components/navigation-menu
radix-api: https://www.radix-ui.com/docs/primitives/components/navigation-menu#api-reference
---

# Navigation Menu

## Overview

A collection of links for navigating websites.

## Import

```tsx
import {
  NavigationMenu,
  NavigationMenuContent,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  NavigationMenuTrigger,
} from "@/components/ui/navigation-menu"
```

## Installation

```bash
npx shadcn@latest add navigation-menu
```

## Usage

```tsx
<NavigationMenu>
  <NavigationMenuList>
    <NavigationMenuItem>
      <NavigationMenuTrigger>Item One</NavigationMenuTrigger>
      <NavigationMenuContent>
        <NavigationMenuLink>Link</NavigationMenuLink>
      </NavigationMenuContent>
    </NavigationMenuItem>
  </NavigationMenuList>
</NavigationMenu>
```

## Composition

```
NavigationMenu
├── NavigationMenuList
│   ├── NavigationMenuItem
│   │   ├── NavigationMenuTrigger
│   │   └── NavigationMenuContent
│   │       ├── NavigationMenuLink
│   │       └── NavigationMenuLink
│   └── NavigationMenuItem
│       └── NavigationMenuLink
└── NavigationMenuIndicator
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Accessibility

### ARIA Roles

Root: `<nav>` with `aria-label`. Triggers: `role="button"`, `aria-haspopup="true"`, `aria-expanded`. Content: `role="group"`.

### Keyboard Navigation

| Key | Action |
|-----|--------|
| Tab | Move focus through menu items |
| Enter / Space | Open sub-menu or activate link |
| Escape | Close open sub-menu |
| ArrowDown / ArrowUp | Navigate within an open sub-menu |

### ARIA Attributes

Built on Radix NavigationMenu. Follows the [Disclosure Navigation Menu](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/examples/disclosure-navigation/) pattern.

### Screen Reader Notes

Use `aria-label` on `NavigationMenuList` to differentiate multiple nav regions on a page.

## Tailwind Tokens

**CSS variables used:**

- `--background`
- `--foreground`
- `--accent`
- `--accent-foreground`
- `--border`
- `--popover`
- `--popover-foreground`
- `--radius`

**Key Tailwind classes:**

- `relative`
- `flex`
- `max-w-max`
- `flex-1`
- `items-center`
- `justify-center`

Viewport content uses `--popover` token. Trigger hover: `--accent`.

## Notes

- Full API reference: [https://www.radix-ui.com/docs/primitives/components/navigation-menu](https://www.radix-ui.com/docs/primitives/components/navigation-menu)
- Radix API reference: [https://www.radix-ui.com/docs/primitives/components/navigation-menu#api-reference](https://www.radix-ui.com/docs/primitives/components/navigation-menu#api-reference)
