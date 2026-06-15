# Flex

**Library:** Ant Design v5  
**Category:** Layout  
**Docs:** https://ant.design/components/flex

---

## Overview

A flex layout container for alignment.

### When to use

- Good for setting spacing between elements.
- Suitable for setting various horizontal and vertical alignments.

### Difference with Space component

- Space is used to set the spacing between inline elements. It will add a wrapper element for each child element for inline alignment. Suitable for equidistant arrangement of multiple child elements in rows and columns.
- Flex is used to set the layout of block-level elements. It does not add a wrapper element. Suitable for layout of child elements in vertical or horizontal direction, and provides more flexibility and control.

---

## Import

```js
import { Flex } from 'antd';
```

---

## Props / API

> This component is available since `antd@5.10.0`. The default behavior of Flex in horizontal mode is to align upward, In vertical mode, aligns the stretch, You can adjust this via properties.

Common props ref：[Common props](/docs/react/common-props)

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| vertical | Is direction of the flex vertical, use `flex-direction: column` | boolean | false | 5.10.0 | 5.10.0 |
| wrap | Set whether the element is displayed in a single line or in multiple lines | [flex-wrap](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-wrap) \| boolean | nowrap | boolean: 5.17.0 | × |
| justify | Sets the alignment of elements in the direction of the main axis | [justify-content](https://developer.mozilla.org/en-US/docs/Web/CSS/justify-content) | normal |  | × |
| align | Sets the alignment of elements in the direction of the cross axis | [align-items](https://developer.mozilla.org/en-US/docs/Web/CSS/align-items) | normal |  | × |
| flex | flex CSS shorthand properties | [flex](https://developer.mozilla.org/en-US/docs/Web/CSS/flex) | normal |  | × |
| gap | Sets the gap between grids | `small` \| `medium` \| `large` \| string \| number | - |  | × |
| component | custom element type | React.ComponentType | `div` |  | × |
| orientation | direction of the flex | `horizontal` \| `vertical` | `horizontal` | - | × |

---

## AI Design System token mapping

When using this component with the AI Design System adapter, these
`--ds-*` hooks drive the component's appearance:

```
—
```

Adapter file: `lib-adapters/ant-design.css`  
Adapter spec: `specs/adapters/ant-design.md`

---

## Notes

- Full Ant Design Flex docs: https://ant.design/components/flex
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
