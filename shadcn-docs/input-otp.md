---
component: input-otp
source: https://ui.shadcn.com/docs/components/input-otp
radix-doc: https://input-otp.rodz.dev
---

# Input OTP

## Overview

Accessible one-time password component with copy-paste functionality.

## Import

```tsx
import {
  InputOTP,
  InputOTPGroup,
  InputOTPSeparator,
  InputOTPSlot,
} from "@/components/ui/input-otp"
```

## Installation

```bash
npx shadcn@latest add input-otp
```

## Usage

```tsx
<InputOTP maxLength={6}>
  <InputOTPGroup>
    <InputOTPSlot index={0} />
    <InputOTPSlot index={1} />
    <InputOTPSlot index={2} />
  </InputOTPGroup>
  <InputOTPSeparator />
  <InputOTPGroup>
    <InputOTPSlot index={3} />
    <InputOTPSlot index={4} />
    <InputOTPSlot index={5} />
  </InputOTPGroup>
</InputOTP>
```

## Composition

```
InputOTP
├── InputOTPGroup
│   ├── InputOTPSlot
│   ├── InputOTPSlot
│   └── InputOTPSlot
├── InputOTPSeparator
├── InputOTPGroup
│   ├── InputOTPSlot
│   ├── InputOTPSlot
│   └── InputOTPSlot
├── InputOTPSeparator
└── InputOTPGroup
    ├── InputOTPSlot
    └── InputOTPSlot
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Examples

### Separator

Use the `<InputOTPSeparator />` component to add a separator between input groups.

### Disabled

Use the `disabled` prop to disable the input.

### Controlled

Use the `value` and `onChange` props to control the input value.

### Invalid

Use `aria-invalid` on the slots to show an error state.

### Four Digits

A common pattern for PIN codes. This uses the `pattern={REGEXP_ONLY_DIGITS}` prop.

### Alphanumeric

Use `REGEXP_ONLY_DIGITS_AND_CHARS` to accept both letters and numbers.

### Form

## Accessibility

### ARIA Roles

Renders a series of single-character inputs grouped as one logical OTP field. Uses a hidden actual `<input>` for value management.

### Keyboard Navigation

| Key | Action |
|-----|--------|
| Any digit (0-9) | Enter digit and advance focus |
| Backspace | Delete current digit and move back |
| ArrowLeft / ArrowRight | Move between slots |
| Ctrl+V / Cmd+V | Paste entire code |

### ARIA Attributes

`aria-label` on the input group (e.g., "One-time passcode"). Individual slots are decorative.

### Screen Reader Notes

Built on `input-otp`. Screen readers announce the hidden input value; the slots are `aria-hidden`.

## Tailwind Tokens

**CSS variables used:**

- `--border`
- `--ring`
- `--background`
- `--foreground`
- `--radius`

**Key Tailwind classes:**

- `flex`
- `items-center`
- `gap-2`
- `has-[:disabled]:opacity-50`

Built on `input-otp`. Individual slot uses `--border` and `--ring` for focus.

## Notes

- Full API reference: [https://input-otp.rodz.dev](https://input-otp.rodz.dev)
