---
component: native-select
source: https://ui.shadcn.com/docs/components/native-select
---

# Native Select

## Overview

A styled native HTML select element with consistent design system integration.

## Import

```tsx
import {
  NativeSelect,
  NativeSelectOptGroup,
  NativeSelectOption,
} from "@/components/ui/native-select"
```

## Installation

```bash
npx shadcn@latest add native-select
```

## Usage

```tsx
<NativeSelect>
  <NativeSelectOption value="">Select a fruit</NativeSelectOption>
  <NativeSelectOption value="apple">Apple</NativeSelectOption>
  <NativeSelectOption value="banana">Banana</NativeSelectOption>
  <NativeSelectOption value="blueberry">Blueberry</NativeSelectOption>
  <NativeSelectOption value="pineapple">Pineapple</NativeSelectOption>
</NativeSelect>
```

## Composition

```
NativeSelect
├── NativeSelectOption
├── NativeSelectOption
├── NativeSelectOption
└── NativeSelectOption
```

## Props & Variants

### NativeSelect

The main select component that wraps the native HTML select element. ```tsx ```

### NativeSelectOption

Represents an individual option within the select.

| Prop       | Type      | Default |
| ---------- | --------- | ------- |
| `value`    | `string`  |         |
| `disabled` | `boolean` | `false` |

### NativeSelectOptGroup

Groups related options together for better organization.

| Prop       | Type      | Default |
| ---------- | --------- | ------- |
| `label`    | `string`  |         |
| `disabled` | `boolean` | `false` |

## Examples

### Groups

Use `NativeSelectOptGroup` to organize options into categories.

### Disabled

Add the `disabled` prop to the `NativeSelect` component to disable the select.

### Invalid

Use `aria-invalid` to show validation errors and the `data-invalid` attribute to the `Field` component for styling.

## Accessibility

### ARIA Roles

Native `<select>` element — inherits browser listbox semantics.

### Keyboard Navigation

Standard browser keyboard interaction (Space/Enter to open, Arrow keys to navigate, Enter to select).

### ARIA Attributes

Associate with `<label>` via `htmlFor` / `id`. `aria-invalid` for errors. `aria-required` for required fields.

### Screen Reader Notes

Unlike the custom Select component, NativeSelect uses the browser's native select UI, which is fully accessible by default and preferred on mobile.

## Tailwind Tokens

**CSS variables used:**

- `--background`
- `--foreground`
- `--border`
- `--input`
- `--ring`
- `--radius`
- `--muted-foreground`

**Key Tailwind classes:**

- `h-8`
- `w-full`
- `rounded-lg`
- `border`
- `border-input`
- `bg-background`
- `text-sm`
- `focus:ring-3`

Uses native browser `<select>` UI. Styles are applied via CSS but browser controls appearance.

## Notes

