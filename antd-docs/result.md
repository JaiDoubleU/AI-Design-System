# Result

**Library:** Ant Design v5  
**Category:** Feedback  
**Docs:** https://ant.design/components/result

---

## Overview

Used to feedback the processing results of a series of operations.

### When to use

Use when important operations need to inform the user to process the results and the feedback is more complicated.

---

## Import

```js
import { Result } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| classNames | Customize class for each semantic structure inside the component. Supports object or function | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props }) => Record<[SemanticDOM](#semantic-dom), string> | - | 6.0.0 | 6.0.0 |
| extra | Operating area | ReactNode | - |  | × |
| icon | Custom back icon | ReactNode | - |  | × |
| status | Result status, decide icons and colors | `success` \| `error` \| `info` \| `warning` \| `404` \| `403` \| `500` | `info` |  | × |
| styles | Customize inline style for each semantic structure inside the component. Supports object or function | Record<[SemanticDOM](#semantic-dom), CSSProperties> \| (info: { props }) => Record<[SemanticDOM](#semantic-dom), CSSProperties> | - | 6.0.0 | 6.0.0 |
| subTitle | The subTitle | ReactNode | - |  | × |
| title | The title | ReactNode | - |  | × |

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

- Full Ant Design Result docs: https://ant.design/components/result
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
