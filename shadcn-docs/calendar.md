---
component: calendar
source: https://ui.shadcn.com/docs/components/calendar
radix-doc: https://react-day-picker.js.org
---

# Calendar

## Overview

A calendar component that allows users to select a date or a range of dates.

## Import

```tsx
import { Calendar } from "@/components/ui/calendar"
```

## Installation

```bash
npx shadcn@latest add calendar
```

## Usage

```tsx
const [date, setDate] = React.useState<Date | undefined>(new Date())

return (
  <Calendar
    mode="single"
    selected={date}
    onSelect={setDate}
    className="rounded-lg border"
  />
)
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Examples

### Basic

A basic calendar component. We used `className="rounded-lg border"` to style the calendar.

### Range Calendar

Use the `mode="range"` prop to enable range selection.

### Month and Year Selector

Use `captionLayout="dropdown"` to show month and year dropdowns.

### Presets

### Date and Time Picker

### Booked dates

### Custom Cell Size

You can customize the size of calendar cells using the `--cell-size` CSS variable. You can also make it responsive by using breakpoint-specific values:
```tsx showLineNumbers
```
Or use fixed values:
```tsx showLineNumbers
```

### Week Numbers

Use `showWeekNumber` to show week numbers.

## Accessibility

### ARIA Roles

`role="grid"` on the calendar table; `role="gridcell"` on each day; `role="button"` on selectable days.

### Keyboard Navigation

| Key | Action |
|-----|--------|
| ArrowLeft/Right | Move one day backward/forward |
| ArrowUp/Down | Move one week backward/forward |
| PageUp/PageDown | Move one month backward/forward |
| Shift+PageUp/PageDown | Move one year backward/forward |
| Home | Move to start of week |
| End | Move to end of week |
| Enter / Space | Select focused day |
| Escape | Close calendar (if in a popover) |

### ARIA Attributes

`aria-label` on the grid; `aria-selected` on selected day(s); `aria-disabled` on unavailable days.

### Screen Reader Notes

Built on `react-day-picker`. Supports single, multiple, and range selection modes.

## Tailwind Tokens

**CSS variables used:**

- `--background`
- `--foreground`
- `--accent`
- `--accent-foreground`
- `--primary`
- `--primary-foreground`
- `--muted`
- `--muted-foreground`
- `--border`
- `--radius`

**Key Tailwind classes:**

- `p-3`
- `rounded-md`
- `border`
- `bg-background`

Selected day: `--primary` background. Today: `--accent`. Disabled: `--muted-foreground`.

## Notes

- Full API reference: [https://react-day-picker.js.org](https://react-day-picker.js.org)

### Changelog

### RTL Support

If you're upgrading from a previous version of the `Calendar` component, you'll need to apply the following updates to add locale support:

Add `Locale` to your imports from `react-day-picker`:

```diff
  import {
    DayPicker,
    getDefaultClassNames,
    type DayButton,
+   type Locale,
  } from "react-day-picker"
```

Add the `locale` prop to the component's props:

```diff
  function Calendar({
    className,
    classNames,
    showOutsideDays = true,
    captionLayout = "label",
    buttonVariant = "ghost",
+   locale,
    formatters,
    components,
    ...props
  }: React.ComponentProps<typeof DayPicker> & {
    buttonVariant?: React.ComponentProps<typeof Button>["variant"]
  }) {
```

Pass the `locale` prop to the `DayPicker` component:

```diff
    <DayPicker
+     locale={locale}
        formatMonthDropdown: (date) =>
-         date.toLocaleString("default", { month: "short" }),
+         date.toLocaleString(locale?.code, { month: "short" }),
        ...formatters,
      }}
```

Update the `CalendarDayButton` component signature and pass `locale`:

```diff
  function CalendarDayButton({
    className,
    day,
    modifiers,
+   locale,
    ...props
- }: React.ComponentProps<typeof DayButton>) {
+ }: React.ComponentProps<typeof DayButton> & { locale?: Partial<Locale> }) {
```

Use `locale?.code` in the date formatting:

```diff
    <Button
-     data-day={day.date.toLocaleDateString()}
+     data-day={day.date.toLocaleDateString(locale?.code)}
      ...
    />
```

Update the `DayButton` component usage to pass the `locale` prop:

```diff
        ...
-       DayButton: CalendarDayButton,
+       DayButton: ({ ...props }) => (
+         <CalendarDayButton locale={locale} {...props} />
+       ),
        ...
      }}
```

Replace directional classes with logical properties for better RTL support:

```diff
  // In the day classNames:
- [&:last-child[data-selected=true]_button]:rounded-r-(--cell-radius)
+ [&:last-child[data-selected=true]_button]:rounded-e-(--cell-radius)
- [&:nth-child(2)[data-selected=true]_button]:rounded-l-(--cell-radius)
+ [&:nth-child(2)[data-selected=true]_button]:rounded-s-(--cell-radius)
- [&:first-child[data-selected=true]_button]:rounded-l-(--cell-radius)
+ [&:first-child[data-selected=true]_button]:rounded-s-(--cell-radius)

  // In range_start classNames:
- rounded-l-(--cell-radius) ... after:right-0
+ rounded-s-(--cell-radius) ... after:end-0

  // In range_end classNames:
- rounded-r-(--cell-radius) ... after:left-0
+ rounded-e-(--cell-radius) ... after:start-0

  // In CalendarDayButton className:
- data-[range-end=true]:rounded-r-(--cell-radius)
+ data-[range-end=true]:rounded-e-(--cell-radius)
- data-[range-start=true]:rounded-l-(--cell-radius)
+ data-[range-start=true]:rounded-s-(--cell-radius)
```

After applying these changes, you can use the `locale` prop to provide locale-specific formatting:

```tsx
import { enUS } from "react-day-picker/locale"

;<Calendar mode="single" selected={date} onSelect={setDate} locale={enUS} />
```
