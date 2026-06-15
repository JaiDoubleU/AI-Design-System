---
component: resizable
source: https://ui.shadcn.com/docs/components/resizable
radix-doc: https://github.com/bvaughn/react-resizable-panels
radix-api: https://github.com/bvaughn/react-resizable-panels/tree/main/packages/react-resizable-panels
---

# Resizable

## Overview

Accessible resizable panel groups and layouts with keyboard support.

## Import

```tsx
import {
  ResizableHandle,
  ResizablePanel,
  ResizablePanelGroup,
} from "@/components/ui/resizable"
```

## Installation

```bash
npx shadcn@latest add resizable
```

## Usage

```tsx
<ResizablePanelGroup orientation="horizontal">
  <ResizablePanel>One</ResizablePanel>
  <ResizableHandle />
  <ResizablePanel>Two</ResizablePanel>
</ResizablePanelGroup>
```

## Composition

```
ResizablePanelGroup
├── ResizablePanel
├── ResizableHandle
└── ResizablePanel
```

## Props & Variants

*API reference available at the Radix UI docs link above.*

## Examples

### Vertical

Use `orientation="vertical"` for vertical resizing.

### Handle

Use the `withHandle` prop on `ResizableHandle` to show a visible handle.

## Accessibility

### ARIA Roles

Handle: `role="separator"`, `aria-orientation` (`"horizontal"` or `"vertical"`), `aria-valuenow`, `aria-valuemin`, `aria-valuemax`, `aria-valuetext`.

### Keyboard Navigation

| Key | Action |
|-----|--------|
| ArrowLeft/Right | Adjust horizontal panel size |
| ArrowUp/Down | Adjust vertical panel size |
| Home | Collapse or go to minimum size |
| End | Expand or go to maximum size |

### ARIA Attributes

`aria-label` on the handle (e.g., "Resize panel").

### Screen Reader Notes

Built on `react-resizable-panels`. Keyboard resizing follows the [WAI-ARIA Window Splitter](https://www.w3.org/WAI/ARIA/apg/patterns/windowsplitter/) pattern.

## Tailwind Tokens

**CSS variables used:**

- `--border`
- `--muted`

**Key Tailwind classes:**

- `flex`
- `h-full`
- `w-full`
- `items-center`
- `justify-center`

Handle uses `--border` color. Grip icon uses `--muted-foreground`.

## Notes

- Full API reference: [https://github.com/bvaughn/react-resizable-panels](https://github.com/bvaughn/react-resizable-panels)
- Radix API reference: [https://github.com/bvaughn/react-resizable-panels/tree/main/packages/react-resizable-panels](https://github.com/bvaughn/react-resizable-panels/tree/main/packages/react-resizable-panels)

### Changelog

### 2025-02-02 `react-resizable-panels` v4

Updated to `react-resizable-panels` v4. See the [v4.0.0 release notes](https://github.com/bvaughn/react-resizable-panels/releases/tag/4.0.0) for full details.

If you're using `react-resizable-panels` primitives directly, note the following changes:

| v3                           | v4                      |
| ---------------------------- | ----------------------- |
| `PanelGroup`                 | `Group`                 |
| `PanelResizeHandle`          | `Separator`             |
| `direction` prop             | `orientation` prop      |
| `defaultSize={50}`           | `defaultSize="50%"`     |
| `onLayout`                   | `onLayoutChange`        |
| `ImperativePanelHandle`      | `PanelImperativeHandle` |
| `ref` prop on Panel          | `panelRef` prop         |
| `data-panel-group-direction` | `aria-orientation`      |

<Callout>
  The shadcn/ui wrapper components (`ResizablePanelGroup`, `ResizablePanel`,
  `ResizableHandle`) remain unchanged.
