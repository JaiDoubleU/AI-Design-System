---
component: aspect-ratio
source: https://ui.shadcn.com/docs/components/aspect-ratio
radix-doc: https://www.radix-ui.com/primitives/docs/components/aspect-ratio
radix-api: https://www.radix-ui.com/primitives/docs/components/aspect-ratio#api-reference
---

# Aspect Ratio

## Overview

Displays content within a desired ratio.

## Import

```tsx
import { AspectRatio } from "@/components/ui/aspect-ratio"
```

## Installation

```bash
npx shadcn@latest add aspect-ratio
```

## Usage

```tsx
<AspectRatio ratio={16 / 9}>
  <Image src="..." alt="Image" className="rounded-md object-cover" />
</AspectRatio>
```

## Props & Variants

### AspectRatio

The `AspectRatio` component displays content within a desired ratio.

| Prop        | Type     | Default | Required |
| ----------- | -------- | ------- | -------- |
| `ratio`     | `number` | -       | Yes      |
| `className` | `string` | -       | No       |

## Examples

### Square

A square aspect ratio component using the `ratio={1 / 1}` prop. This is useful for displaying images in a square format.

### Portrait

A portrait aspect ratio component using the `ratio={9 / 16}` prop. This is useful for displaying images in a portrait format.

## Accessibility

### ARIA Roles

No ARIA roles — purely a layout utility.

### Keyboard Navigation

Not interactive.

### ARIA Attributes

None.

### Screen Reader Notes

Wrap meaningful media (images, videos) in a `<figure>` with a `<figcaption>` for screen reader context.

## Tailwind Tokens

**Key Tailwind classes:**

- `relative`
- `overflow-hidden`

Uses `aspect-ratio` CSS property via Radix AspectRatio. No color tokens.

## Notes

- Full API reference: [https://www.radix-ui.com/primitives/docs/components/aspect-ratio](https://www.radix-ui.com/primitives/docs/components/aspect-ratio)
- Radix API reference: [https://www.radix-ui.com/primitives/docs/components/aspect-ratio#api-reference](https://www.radix-ui.com/primitives/docs/components/aspect-ratio#api-reference)
