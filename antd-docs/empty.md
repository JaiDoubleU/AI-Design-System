# Empty

**Library:** Ant Design v5  
**Category:** Data Display  
**Docs:** https://ant.design/components/empty

---

## Overview

Empty state placeholder.

### When to use

- When there is no data provided, display for friendly tips.
- User tutorial to create something in fresh new situation.

---

## Import

```js
import { Empty } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

```jsx

</Empty>
```

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), string> | - |  | 5.23.0 |
| description | Customize description | ReactNode | - |  | × |
| image | Customize image. Will treat as image url when string provided | ReactNode | `Empty.PRESENTED_IMAGE_DEFAULT` |  | 5.27.0 |
| ~~imageStyle~~ | The style of image, please use `styles.image` instead | CSSProperties | - |  | × |
| styles | Customize inline style for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), CSSProperties> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), CSSProperties> | - |  | 5.23.0 |

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

- Full Ant Design Empty docs: https://ant.design/components/empty
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
