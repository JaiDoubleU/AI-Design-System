---
component: alert
source: https://ui.shadcn.com/docs/components/alert
---

# Alert

## Overview

Displays a callout for user attention.

## Import

```tsx
import {
  Alert,
  AlertAction,
  AlertDescription,
  AlertTitle,
} from "@/components/ui/alert"
```

## Installation

```bash
npx shadcn@latest add alert
```

## Usage

```tsx
<Alert>
  <InfoIcon />
  <AlertTitle>Heads up!</AlertTitle>
  <AlertDescription>
    You can add components and dependencies to your app using the cli.
  </AlertDescription>
  <AlertAction>
    <Button variant="outline">Enable</Button>
  </AlertAction>
</Alert>
```

## Composition

```
Alert
├── Icon
├── AlertTitle
├── AlertDescription
└── AlertAction
```

## Props & Variants

### Alert

The `Alert` component displays a callout for user attention.

| Prop      | Type                         | Default     |
| --------- | ---------------------------- | ----------- |
| `variant` | `"default" \| "destructive"` | `"default"` |

### AlertTitle

The `AlertTitle` component displays the title of the alert.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### AlertDescription

The `AlertDescription` component displays the description or content of the alert.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### AlertAction

The `AlertAction` component displays an action element (like a button) positioned absolutely in the top-right corner of the alert.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

## Examples

### Basic

A basic alert with an icon, title and description.

### Destructive

Use `variant="destructive"` to create a destructive alert.

### Action

Use `AlertAction` to add a button or other action element to the alert.

### Custom Colors

You can customize the alert colors by adding custom classes such as `bg-amber-50 dark:bg-amber-950` to the `Alert` component.

## Accessibility

### ARIA Roles

Root renders a `<div>`. For urgent announcements add `role="alert"` (live region); for non-urgent use `role="status"`.

### Keyboard Navigation

No keyboard interaction — alert is passive content.

### ARIA Attributes

`aria-live="assertive"` (or `polite`) when used as a live region.

### Screen Reader Notes

The `AlertTitle` and `AlertDescription` sub-components provide semantic structure.

## Tailwind Tokens

**CSS variables used:**

- `--background`
- `--foreground`
- `--border`
- `--destructive`
- `--destructive-foreground`
- `--radius`

**Key Tailwind classes:**

- `relative`
- `rounded-lg`
- `border`
- `p-4`
- `bg-background`
- `text-foreground`
- `text-destructive`

`variant="destructive"` uses `--destructive` color tokens.

## Notes

