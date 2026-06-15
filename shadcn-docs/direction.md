---
component: direction
source: https://ui.shadcn.com/docs/components/direction
radix-doc: https://www.radix-ui.com/primitives/docs/utilities/direction-provider
radix-api: https://www.radix-ui.com/primitives/docs/utilities/direction-provider#api-reference
---

# Direction

## Overview

A provider component that sets the text direction for your application.

## Import

```tsx
import { DirectionProvider } from "@/components/ui/direction"
```

## Installation

```bash
npx shadcn@latest add direction
```

## Usage

```tsx
<html dir="rtl">
  <body>
    <DirectionProvider direction="rtl">
      {/* Your app content */}
    </DirectionProvider>
  </body>
</html>
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Accessibility

### ARIA Roles

Wraps content with a `dir` attribute (`ltr` or `rtl`) at the provider level.

### Keyboard Navigation

No keyboard interaction. Configures directionality for all child Radix components.

### ARIA Attributes

`dir="rtl"` / `dir="ltr"` on the container.

### Screen Reader Notes

Integrates with Radix DirectionProvider to flip geometric props (e.g., start/end) for RTL layouts.

## Tailwind Tokens

Utility context provider — no visual tokens.

## Notes

- Full API reference: [https://www.radix-ui.com/primitives/docs/utilities/direction-provider](https://www.radix-ui.com/primitives/docs/utilities/direction-provider)
- Radix API reference: [https://www.radix-ui.com/primitives/docs/utilities/direction-provider#api-reference](https://www.radix-ui.com/primitives/docs/utilities/direction-provider#api-reference)
