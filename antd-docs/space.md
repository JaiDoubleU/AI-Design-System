# Space

**Library:** Ant Design v5  
**Category:** Layout  
**Docs:** https://ant.design/components/space

---

## Overview

Set components spacing.

### When to use

- Avoid components clinging together and set a unified space.
- Use Space.Compact when child form components are compactly connected and the border is collapsed (After version `antd@4.24.0` Supported).

### Difference with Flex component

- Space is used to set the spacing between inline elements. It will add a wrapper element for each child element for inline alignment. Suitable for equidistant arrangement of multiple child elements in rows and columns.
- Flex is used to set the layout of block-level elements. It does not add a wrapper element. Suitable for layout of child elements in vertical or horizontal direction, and provides more flexibility and control.

---

## Import

```js
import { Space } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

### Space

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| align | Align items | `start` \| `end` \|`center` \|`baseline` | - | 4.2.0 | × |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props: SpaceProps })=> Record<[SemanticDOM](#semantic-dom), string> | - |  | 5.6.0 |
| ~~direction~~ | The space direction | `vertical` \| `horizontal` | `horizontal` | 4.1.0 | × |
| orientation | The space direction | `vertical` \| `horizontal` | `horizontal` |  | × |
| size | The space size | [Size](#size) \| [Size\[\]](#size) | `small` | 4.1.0 \| Array: 4.9.0 | 5.6.0 |
| ~~split~~ | Set split, please use `separator` instead | ReactNode | - | 4.7.0 | × |
| separator | Set separator | ReactNode | - | - | × |
| styles | Customize inline style for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), CSSProperties> \| (info: { props: SpaceProps })=> Record<[SemanticDOM](#semantic-dom), CSSProperties> | - |  | 5.6.0 |
| vertical | Orientation, Simultaneously configure with `orientation` and prioritize `orientation` | boolean | false | - | × |
| wrap | Auto wrap line, when `horizontal` effective | boolean | false | 4.9.0 | × |

### Size

`'small' | 'middle' | 'large' | number`

### Space.Compact

Use Space.Compact when child form components are compactly connected and the border is collapsed. The supported components are：

- Button
- AutoComplete
- Cascader
- DatePicker
- Input/Input.Search
- InputNumber
- Select
- TimePicker
- TreeSelect

| Property | Description | Type | Default | Version |
| --- | --- | --- | --- | --- |
| block | Option to fit width to its parent\'s width | boolean | false | 4.24.0 |
| ~~direction~~ | Set direction of layout | `vertical` \| `horizontal` | `horizontal` | 4.24.0 |
| orientation | Set direction of layout | `vertical` \| `horizontal` | `horizontal` |  |
| vertical | Orientation, Simultaneously configure with `orientation` and prioritize `orientation` | boolean | false | - |
| size | Set child component size | `large` \| `medium` \| `small` | `medium` | 4.24.0 |

### Space.Addon

> This component is available since `antd@5.29.0`.

Used to create custom cells in compact layouts.

| Property | Description    | Type      | Default | Version |
| -------- | -------------- | --------- | ------- | ------- |
| children | Custom content | ReactNode | -       | 5.29.0  |

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

- Full Ant Design Space docs: https://ant.design/components/space
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
