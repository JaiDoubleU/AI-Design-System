---
component: carousel
source: https://ui.shadcn.com/docs/components/carousel
radix-doc: https://www.embla-carousel.com/get-started/react
radix-api: https://www.embla-carousel.com/api
---

# Carousel

## Overview

A carousel with motion and swipe built using Embla.

## Import

```tsx
import {
  Carousel,
  CarouselContent,
  CarouselItem,
  CarouselNext,
  CarouselPrevious,
} from "@/components/ui/carousel"
```

## Installation

```bash
npx shadcn@latest add carousel
```

## Usage

```tsx
<Carousel>
  <CarouselContent>
    <CarouselItem>...</CarouselItem>
    <CarouselItem>...</CarouselItem>
    <CarouselItem>...</CarouselItem>
  </CarouselContent>
  <CarouselPrevious />
  <CarouselNext />
</Carousel>
```

## Composition

```
Carousel
├── CarouselContent
│   ├── CarouselItem
│   └── CarouselItem
├── CarouselPrevious
└── CarouselNext
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Examples

### Sizes

To set the size of the items, you can use the `basis` utility class on the `<CarouselItem />`.
```tsx showLineNumbers {4-6}
// 33% of the carousel width.
```
```tsx showLineNumbers {4-6}
// 50% on small screens and 33% on larger screens.
```

### Spacing

To set the spacing between the items, we use a `pl-[VALUE]` utility on the `<CarouselItem />` and a negative `-ml-[VALUE]` on the `<CarouselContent />`.
```tsx showLineNumbers /-ml-4/ /pl-4/
```
```tsx showLineNumbers /-ml-2/ /pl-2/ /md:-ml-4/ /md:pl-4/
```

### Orientation

Use the `orientation` prop to set the orientation of the carousel.
```tsx showLineNumbers /vertical | horizontal/
```

## Accessibility

### ARIA Roles

`role="region"` with `aria-label` (e.g. "Product gallery") on the carousel root; `aria-roledescription="carousel"`. Each slide: `role="group"`, `aria-roledescription="slide"`, `aria-label="n of N"`.

### Keyboard Navigation

| Key | Action |
|-----|--------|
| Tab | Move to previous/next button or slide content |
| Enter / Space | Activate previous or next button |

### ARIA Attributes

Previous/Next buttons: `aria-label="Previous slide"` / `aria-label="Next slide"`. Add a live region `aria-live="polite"` to announce slide changes.

### Screen Reader Notes

Auto-playing carousels should pause on focus or hover. Always provide pause/play controls.

## Tailwind Tokens

**CSS variables used:**

- `--background`
- `--foreground`
- `--border`
- `--radius`

**Key Tailwind classes:**

- `relative`
- `overflow-hidden`
- `flex`

Navigation buttons use Button component tokens. Slide transitions via CSS transform.

## Notes

- Full API reference: [https://www.embla-carousel.com/get-started/react](https://www.embla-carousel.com/get-started/react)
- Radix API reference: [https://www.embla-carousel.com/api](https://www.embla-carousel.com/api)
