# Tour

**Library:** Ant Design v5  
**Category:** Data Display  
**Docs:** https://ant.design/components/tour

---

## Overview

A popup component for guiding users through a product.

### When to use

Use when you want to guide users through a product.

---

## Import

```js
import { Tour } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

### Tour

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| arrow | Whether to show the arrow, including the configuration whether to point to the center of the element | `boolean` \| `{ pointAtCenter: boolean }` | `true` |  | × |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), string> | - |  | 6.0.0 |
| closeIcon | Customize close icon | `React.ReactNode` | `true` | 5.9.0 | 5.14.0 |
| disabledInteraction | Disable interaction on highlighted area. | `boolean` | `false` | 5.13.0 | × |
| gap | Control the radius of the highlighted area and the offset between highlighted area and the element. | `{ offset?: number \| [number, number]; radius?: number }` | `{ offset?: 6 ; radius?: 2 }` | 5.0.0 (array type `offset`: 5.9.0) | × |
| keyboard | Whether to enable keyboard shortcuts | boolean | true | 6.2.0 | × |
| placement | Position of the guide card relative to the target element | `center` \| `left` \| `leftTop` \| `leftBottom` \| `right` \| `rightTop` \| `rightBottom` \| `top` \| `topLeft` \| `topRight` \| `bottom` \| `bottomLeft` \| `bottomRight` | `bottom` |  | × |
| onClose | Callback function on shutdown | `Function` | - |  | × |
| onFinish | Callback when the tour is finished | `Function` | - |  | × |
| mask | Whether to enable masking, change mask style and fill color by pass custom props | `boolean \| { style?: React.CSSProperties; color?: string; }` | `true` |  | × |
| type | Type, affects the background color and text color | `default` \| `primary` | `default` |  | × |
| open | Open tour | `boolean` | - |  | × |
| onChange | Callback when the step changes. Current is the previous step | `(current: number) => void` | - |  | × |
| current | What is the current step | `number` | - |  | × |
| scrollIntoViewOptions | support pass custom scrollIntoView options | `boolean \| ScrollIntoViewOptions` | `true` | 5.2.0 | × |
| styles | Customize inline style for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), CSSProperties> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), CSSProperties> | - |  | 6.0.0 |
| indicatorsRender | custom indicator | `(current: number, total: number) => ReactNode` | - | 5.2.0 | × |
| actionsRender | custom action | `(originNode: ReactNode, info: { current: number, total: number }) => ReactNode` | - | 5.25.0 | × |
| zIndex | Tour's zIndex | number | 1001 | 5.3.0 | × |
| getPopupContainer | Set the rendering node of Tour floating layer | `(node: HTMLElement) => HTMLElement` | body | 5.12.0 | × |

### TourStep

| Property | Description | Type | Default | Version |
| --- | --- | --- | --- | --- |
| target | Get the element the guide card points to. Empty makes it show in center of screen | `() => HTMLElement` \| `HTMLElement` | - |  |
| arrow | Whether to show the arrow, including the configuration whether to point to the center of the element | `boolean` \| `{ pointAtCenter: boolean}` | `true` |  |
| closeIcon | Customize close icon | `React.ReactNode` | `true` | 5.9.0 |
| cover | Displayed pictures or videos | `ReactNode` | - |  |
| title | title | `ReactNode` | - |  |
| description | description | `ReactNode` | - |  |
| placement | Position of the guide card relative to the target element | `center` \| `left` \| `leftTop` \| `leftBottom` \| `right` \| `rightTop` \| `rightBottom` \| `top` \| `topLeft` \| `topRight` \| `bottom` \| `bottomLeft` \| `bottomRight` | `bottom` |  |
| onClose | Callback function on shutdown | `Function` | - |  |
| mask | Whether to enable masking, change mask style and fill color by pass custom props, the default follows the `mask` property of Tour | `boolean \| { style?: React.CSSProperties; color?: string; }` | `true` |  |
| type | Type, affects the background color and text color | `default` \| `primary` | `default` |  |
| nextButtonProps | Properties of the Next button | `{ children: ReactNode; onClick: Function }` | - |  |
| prevButtonProps | Properties of the previous button | `{ children: ReactNode; onClick: Function }` | - |  |
| scrollIntoViewOptions | support pass custom scrollIntoView options, the default follows the `scrollIntoViewOptions` property of Tour | `boolean \| ScrollIntoViewOptions` | `true` | 5.2.0 |

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

- Full Ant Design Tour docs: https://ant.design/components/tour
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
