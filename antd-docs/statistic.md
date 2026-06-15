# Statistic

**Library:** Ant Design v5  
**Category:** Data Display  
**Docs:** https://ant.design/components/statistic

---

## Overview

Display statistic number.

### When to use

- When want to highlight some data.
- When want to display statistic data with description.

---

## Import

```js
import { Statistic } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

#### Statistic

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| classNames | Customize class for each semantic structure inside the Statistic component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props }) => Record<[SemanticDOM](#semantic-dom), string> | - |  | 6.0.0 |
| decimalSeparator | The decimal separator | string | `.` |  | × |
| formatter | Customize value display logic | (value) => ReactNode | - |  | × |
| groupSeparator | Group separator | string | `,` |  | × |
| loading | Loading status of Statistic | boolean | false | 4.8.0 | × |
| precision | The precision of input value | number | - |  | × |
| prefix | The prefix node of value | ReactNode | - |  | × |
| styles | Customize inline style for each semantic structure inside the Statistic component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), CSSProperties> \| (info: { props }) => Record<[SemanticDOM](#semantic-dom), CSSProperties> | - |  | 6.0.0 |
| suffix | The suffix node of value | ReactNode | - |  | × |
| title | Display title | ReactNode | - |  | × |
| value | Display value | string \| number | - |  | × |
| ~~valueStyle~~ | Set value section style, please use `styles.content` instead | CSSProperties | - |  | × |

#### Statistic.Countdown 

<!-- prettier-ignore -->
| Property | Description | Type | Default | Version |
| --- | --- | --- | --- | --- |
| format | Format as [dayjs](https://day.js.org/) | string | `HH:mm:ss` |  |
| prefix | The prefix node of value | ReactNode | - |  |
| suffix | The suffix node of value | ReactNode | - |  |
| title | Display title | ReactNode | - |  |
| value | Set target countdown time | number | - |  |
| valueStyle | Set value section style | CSSProperties | - |  |
| onFinish | Trigger when time's up | () => void | - |  |
| onChange | Trigger when time's changing | (value: number) => void | - | 4.16.0 |

#### Statistic.Timer 

| Property | Description | Type | Default | Version |
| --- | --- | --- | --- | --- |
| type | Timer direction, count down or count up | `countdown` \| `countup` | - |  |
| format | Format as [dayjs](https://day.js.org/) | string | `HH:mm:ss` |  |
| prefix | The prefix node of value | ReactNode | - |  |
| suffix | The suffix node of value | ReactNode | - |  |
| title | Display title | ReactNode | - |  |
| value | Target time for `countdown`, or start time for `countup` (timestamp in ms) | number | - |  |
| valueStyle | Set value section style | CSSProperties | - |  |
| onFinish | Trigger when time's up, only called when type is `countdown` | () => void | - |  |
| onChange | Trigger when time's changing | (value: number) => void | - |  |

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

- Full Ant Design Statistic docs: https://ant.design/components/statistic
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
