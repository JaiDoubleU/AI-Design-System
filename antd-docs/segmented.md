# Segmented

**Library:** Ant Design v5  
**Category:** Data Display  
**Docs:** https://ant.design/components/segmented

---

## Overview

Display multiple options and allow users to select a single option.

### When to use

- When displaying multiple options and user can select a single option;
- When switching the selected option, the content of the associated area changes.

---

## Import

```js
import { Segmented } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

> This component is available since `antd@4.20.0`

### Segmented

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| block | Option to fit width to its parent\'s width | boolean | false |  | × |
| classNames | Customize class for each semantic structure inside the Segmented component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props }) => Record<[SemanticDOM](#semantic-dom), string> | - |  | 6.0.0 |
| defaultValue | Default selected value | string \| number | Value of first item in `options` |  | × |
| disabled | Disable all segments | boolean | false |  | × |
| onChange | The callback function that is triggered when the state changes | function(value: string \| number) |  |  | × |
| options | Set children optional | string\[] \| number\[] \| SegmentedItemType\[] | [] |  | × |
| orientation | Orientation | `horizontal` \| `vertical` | `horizontal` |  | × |
| size | The size of the Segmented. | `large` \| `medium` \| `small` | `medium` |  | × |
| styles | Customize inline style for each semantic structure inside the Segmented component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), CSSProperties> \| (info: { props }) => Record<[SemanticDOM](#semantic-dom), CSSProperties> | - |  | 6.0.0 |
| vertical | Orientation. Simultaneously existing with `orientation`, `orientation` takes priority | boolean | `false` | 5.21.0 | × |
| value | Currently selected value | string \| number |  |  | × |
| shape | shape of Segmented | `default` \| `round` | `default` | 5.24.0 | × |
| name | The `name` property of all `input[type="radio"]` children. if not set, it will fallback to a randomly generated name | string |  | 5.23.0 | × |

### SegmentedItemType

| Property | Description | Type | Default | Version |
| --- | --- | --- | --- | --- |
| disabled | Disabled state of segmented item | boolean | false |  |
| className | The additional css class | string | - |  |
| icon | Display icon for Segmented item | ReactNode | - |  |
| label | Display text for Segmented item | ReactNode | - |  |
| tooltip | tooltip for Segmented item | string \| [TooltipProps](../tooltip/index.en-US.md#api) | - |  |
| value | Value for Segmented item | string \| number | - |  |

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

- Full Ant Design Segmented docs: https://ant.design/components/segmented
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
