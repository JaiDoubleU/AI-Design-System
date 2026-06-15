# Spin

**Library:** Ant Design v5  
**Category:** Feedback  
**Docs:** https://ant.design/components/spin

---

## Overview

Used for the loading status of a page or a block.

### When to use

When part of the page is waiting for asynchronous data or during a rendering process, an appropriate loading animation can effectively alleviate users' inquietude.

---

## Import

```js
import { Spin } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props }) => Record<[SemanticDOM](#semantic-dom), string> | - |  | 6.0.0 |
| delay | Specifies a delay in milliseconds for loading state (prevent flush) | number (milliseconds) | - |  | × |
| description | Customize description content | ReactNode | - | 6.3.0 | × |
| fullscreen | Display a backdrop with the `Spin` component | boolean | false | 5.11.0 | × |
| indicator | React node of the spinning indicator | ReactNode | - |  | 5.20.0 |
| percent | The progress percentage, when set to `auto`, it will be an indeterminate progress | number \| 'auto' | - | 5.18.0 | × |
| size | The size of Spin, options: `small`, `medium` and `large` | string | `medium` |  | × |
| spinning | Whether Spin is visible | boolean | true |  | × |
| styles | Customize inline style for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), CSSProperties> \| (info: { props }) => Record<[SemanticDOM](#semantic-dom), CSSProperties> | - |  | 6.0.0 |
| ~~tip~~ | Customize description content when Spin has children. Deprecated, use `description` instead | ReactNode | - |  | × |
| ~~wrapperClassName~~ | The className of wrapper when Spin has children. Deprecated, use `classNames.root` instead | string | - |  | × |

### Static Method

- `Spin.setDefaultIndicator(indicator: ReactNode)`

  You can define default spin element globally.

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

- Full Ant Design Spin docs: https://ant.design/components/spin
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
