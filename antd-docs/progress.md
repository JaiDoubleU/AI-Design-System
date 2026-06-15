# Progress

**Library:** Ant Design v5  
**Category:** Feedback  
**Docs:** https://ant.design/components/progress

---

## Overview

Display the current progress of the operation.

### When to use

If it will take a long time to complete an operation, you can use `Progress` to show the current progress and status.

- When an operation will interrupt the current interface, or it needs to run in the background for more than 2 seconds.
- When you need to display the completion percentage of an operation.

---

## Import

```js
import { Progress } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

Properties that shared by all types.

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), string> | - | 6.0.0 | 6.0.0 |
| format | The template function of the content | function(percent, successPercent) | (percent) => percent + `%` | - | × |
| percent | To set the completion percentage | number | 0 | - | × |
| railColor | The color of unfilled part | string | - | - | × |
| showInfo | Whether to display the progress value and the status icon | boolean | true | - | × |
| status | To set the status of the Progress, options: `success` `exception` `normal` `active`(line only) | string | - | - | × |
| strokeColor | The color of progress bar | string | - | - | × |
| strokeLinecap | To set the style of the progress linecap | `round` \| `butt` \| `square`, see [stroke-linecap](https://developer.mozilla.org/docs/Web/SVG/Attribute/stroke-linecap) | `round` | - | × |
| styles | Customize inline style for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), CSSProperties> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), CSSProperties> | - | 6.0.0 | 6.0.0 |
| success | Configs of successfully progress bar | { percent: number, strokeColor: string } | - | - | × |
| ~~trailColor~~ | The color of unfilled part. Please use `railColor` instead | string | - | - | × |
| type | To set the type, options: `line` `circle` `dashboard` | string | `line` | - | × |
| size | Progress size | number \| \[number \| string, number] \| { width: number, height: number } \| "small" \| "medium" | "medium" | 5.3.0, Object: 5.18.0 | × |

### `type="line"`

| Property | Description | Type | Default | Version |
| --- | --- | --- | --- | --- |
| steps | The total step count | number | - | - |
| rounding | The function to round the value | (step: number) => number | Math.round | 5.24.0 |
| strokeColor | The color of progress bar, render `linear-gradient` when passing an object, could accept `string[]` when has `steps`. | string \| string[] \| { from: string; to: string; direction: string } | - | 4.21.0: `string[]` |
| percentPosition | Progress value position, passed in object, `align` indicates the horizontal position of the value, `type` indicates whether the value is inside or outside the progress bar | { align: string; type: string } | { align: \"end\", type: \"outer\" } | 5.18.0 |

### `type="circle"`

| Property | Description | Type | Default | Version |
| --- | --- | --- | --- | --- |
| steps | The total step count. When passing an object, `count` refers to the number of steps, and `gap` refers to the distance between them. When passing a number, the default value for `gap` is 2. | number \| { count: number, gap: number } | - | 5.16.0 |
| strokeColor | The color of circular progress, render gradient when passing an object | string \| { number%: string } | - | - |
| strokeWidth | To set the width of the circular progress, unit: percentage of the canvas width | number | 6 | - |

### `type="dashboard"`

| Property | Description | Type | Default | Version |
| --- | --- | --- | --- | --- |
| steps | The total step count. When passing an object, `count` refers to the number of steps, and `gap` refers to the distance between them. When passing a number, the default value for `gap` is 2. | number \| { count: number, gap: number } | - | 5.16.0 |
| gapDegree | The gap degree of half circle, 0 ~ 295 | number | 75 | - |
| gapPlacement | The gap placement, options: `top` `bottom` `start` `end` | string | `bottom` | - |
| ~~gapPosition~~ | The gap position, options: `top` `bottom` `left` `right`, please use `gapPlacement` instead | string | `bottom` | - |
| strokeWidth | To set the width of the dashboard progress, unit: percentage of the canvas width | number | 6 | - |

---

## AI Design System token mapping

When using this component with the AI Design System adapter, these
`--ds-*` hooks drive the component's appearance:

```
--ds-interactive, --ds-text-success, --ds-text-danger
```

Adapter file: `lib-adapters/ant-design.css`  
Adapter spec: `specs/adapters/ant-design.md`

---

## Notes

- Full Ant Design Progress docs: https://ant.design/components/progress
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
