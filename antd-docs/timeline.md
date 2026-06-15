# Timeline

**Library:** Ant Design v5  
**Category:** Data Display  
**Docs:** https://ant.design/components/timeline

---

## Overview

Vertical display timeline.

### When to use

- When a series of information needs to be ordered by time (ascending or descending).
- When you need a timeline to make a visual connection.

---

## Import

```js
import { Timeline } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

### Timeline

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), string> | - |  | 6.0.0 |
| items | Each node of timeline | [Items](#items)[] | - |  | × |
| mode | By sending `alternate` the timeline will distribute the nodes to the left and right | `start` \| `alternate` \| `end` | `start` |  | × |
| orientation | Set the direction of the timeline | `vertical` \| `horizontal` | `vertical` |  | × |
| ~~pending~~ | Set the last ghost node's existence or its content. Use `item.loading` instead | ReactNode | false |  | × |
| ~~pendingDot~~ | Set the dot of the last ghost node when pending is true. Use `item.icon` instead | ReactNode | &lt;LoadingOutlined /&gt; |  | × |
| reverse | Whether reverse nodes or not | boolean | false |  | × |
| styles | Customize inline style for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), CSSProperties> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), CSSProperties> | - |  | 6.0.0 |
| titleSpan | Set the title span space. It is the distance to the center of the dot  | number \| string | 12 |  | × |
| variant | Config style variant | `filled` \| `outlined` | `outlined` |  | × |

### Items

Node of timeline.

| Property | Description | Type | Default |
| --- | --- | --- | --- |
| color | Set the circle's color to `blue`, `red`, `green`, `gray` or other custom colors | string | `blue` |
| content | Set the content | ReactNode | - |
| ~~children~~ | Set the content. Please use `content` instead | ReactNode | - |
| ~~dot~~ | Customize timeline dot. Please use `icon` instead | ReactNode | - |
| icon | Customize node icon | ReactNode | - |
| ~~label~~ | Set the label. Please use `title` instead | ReactNode | - |
| loading | Set loading state | boolean | false |
| placement | Customize node placement | `start` \| `end` | - |
| ~~position~~ | Customize node position. Please use `placement` instead | `start` \| `end` | - |
| title | Set the title | ReactNode | - |

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

- Full Ant Design Timeline docs: https://ant.design/components/timeline
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
