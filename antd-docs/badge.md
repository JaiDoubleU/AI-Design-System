# Badge

**Library:** Ant Design v5  
**Category:** Data Display  
**Docs:** https://ant.design/components/badge

---

## Overview

Small numerical value or status descriptor for UI elements.

### When to use

Badge normally appears in proximity to notifications or user avatars with eye-catching appeal, typically displaying unread messages count.

---

## Import

```js
import { Badge } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

### Badge

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| color | Customize Badge dot color | string | - |  | × |
| count | Number to show in badge | ReactNode | - |  | × |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), string> | - |  | 5.7.0 |
| dot | Whether to display a red dot instead of `count` | boolean | false |  | × |
| offset | Set offset of the badge dot | \[number, number] | - |  | × |
| overflowCount | Max count to show | number | 99 |  | × |
| showZero | Whether to show badge when `count` is zero | boolean | false |  | × |
| size | If `count` is set, `size` sets the size of badge | `medium` \| `small` | - | - | × |
| status | Set Badge as a status dot | `success` \| `processing` \| `default` \| `error` \| `warning` | - |  | × |
| styles | Customize inline style for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), CSSProperties> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), CSSProperties> | - |  | 5.7.0 |
| text | If `status` is set, `text` sets the display text of the status `dot` | ReactNode | - |  | × |
| title | Text to show when hovering over the badge | string | - |  | × |

### Badge.Ribbon

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), string> | - |  | 6.0.0 |
| color | Customize Ribbon color | string | - |  | × |
| placement | The placement of the Ribbon, `start` and `end` follow text direction (RTL or LTR) | `start` \| `end` | `end` |  | × |
| styles | Customize inline style for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), CSSProperties> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), CSSProperties> | - |  | 6.0.0 |
| text | Content inside the Ribbon | ReactNode | - |  | × |

---

## AI Design System token mapping

When using this component with the AI Design System adapter, these
`--ds-*` hooks drive the component's appearance:

```
--ds-interactive, --ds-text-danger (count)
```

Adapter file: `lib-adapters/ant-design.css`  
Adapter spec: `specs/adapters/ant-design.md`

---

## Notes

- Full Ant Design Badge docs: https://ant.design/components/badge
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
