---
component: combobox
source: https://ui.shadcn.com/docs/components/combobox
radix-doc: https://base-ui.com/react/components/combobox
radix-api: https://base-ui.com/react/components/combobox#api-reference
---

# Combobox

## Overview

Autocomplete input with a list of suggestions.

## Import

```tsx
import {
  Combobox,
  ComboboxContent,
  ComboboxEmpty,
  ComboboxInput,
  ComboboxItem,
  ComboboxList,
} from "@/components/ui/combobox"
```

## Installation

```bash
npx shadcn@latest add combobox
```

## Usage

```tsx
const frameworks = ["Next.js", "SvelteKit", "Nuxt.js", "Remix", "Astro"]

export function ExampleCombobox() {
  return (
    <Combobox items={frameworks}>
      <ComboboxInput placeholder="Select a framework" />
      <ComboboxContent>
        <ComboboxEmpty>No items found.</ComboboxEmpty>
        <ComboboxList>
          {(item) => (
            <ComboboxItem key={item} value={item}>
              {item}
            </ComboboxItem>
          )}
        </ComboboxList>
      </ComboboxContent>
    </Combobox>
  )
}
```

## Composition

```
Combobox
├── ComboboxInput
└── ComboboxContent
    ├── ComboboxEmpty
    └── ComboboxList
        ├── ComboboxItem
        └── ComboboxItem
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Examples

### Basic

A simple combobox with a list of frameworks.

### Multiple

A combobox with multiple selection using `multiple` and `ComboboxChips`.

### Clear Button

Use the `showClear` prop to show a clear button.

### Groups

Use `ComboboxGroup` and `ComboboxSeparator` to group items.

### Custom Items

You can render a custom component inside `ComboboxItem`.

### Invalid

Use the `aria-invalid` prop to make the combobox invalid.

### Disabled

Use the `disabled` prop to disable the combobox.

### Auto Highlight

Use the `autoHighlight` prop to automatically highlight the first item on filter.

### Popup

You can trigger the combobox from a button or any other component by using the `render` prop. Move the `ComboboxInput` inside the `ComboboxContent`.

### Input Group

You can add an addon to the combobox by using the `InputGroupAddon` component inside the `ComboboxInput`.

## Accessibility

### ARIA Roles

Input: `role="combobox"`, `aria-expanded`, `aria-autocomplete="list"`, `aria-controls` → listbox id. Listbox: `role="listbox"`. Options: `role="option"`, `aria-selected`.

### Keyboard Navigation

| Key | Action |
|-----|--------|
| ArrowDown | Open list / move to next option |
| ArrowUp | Move to previous option |
| Enter | Select focused option |
| Escape | Close list / clear selection |
| Home | Move to first option |
| End | Move to last option |
| Any character | Filter list |

### ARIA Attributes

`aria-labelledby` links input to its label; `aria-activedescendant` tracks focused option in listbox.

### Screen Reader Notes

Built on top of the Command component. Follows the [ARIA Combobox](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/) pattern.

## Tailwind Tokens

**CSS variables used:**

- `--background`
- `--foreground`
- `--border`
- `--accent`
- `--accent-foreground`
- `--muted`
- `--muted-foreground`
- `--ring`
- `--radius`

Composed of Popover + Command. Inherits tokens from both components.

## Notes

- Full API reference: [https://base-ui.com/react/components/combobox](https://base-ui.com/react/components/combobox)
- Radix API reference: [https://base-ui.com/react/components/combobox#api-reference](https://base-ui.com/react/components/combobox#api-reference)
