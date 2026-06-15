# Steps

**Library:** Ant Design v5  
**Category:** Navigation  
**Docs:** https://ant.design/components/steps

---

## Overview

A navigation bar that guides users through the steps of a task.

### When to use

When a given task is complicated or has a certain sequence in the series of subtasks, we can decompose it into several steps to make things easier.

---

## Import

```js
import { Steps } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

### Steps

The whole of the step bar.

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), string> | - |  | 6.0.0 |
| current | To set the current step, counting from 0. You can overwrite this state by using `status` of `Step` | number | 0 |  | × |
| ~~direction~~ | To specify the direction of the step bar, `horizontal` or `vertical` | string | `horizontal` |  | × |
| iconRender | Custom render icon, please use `items.icon` first | (oriNode, info: { index, active, item }) => ReactNode | - |  | × |
| initial | Set the initial step, counting from 0 | number | 0 |  | × |
| ~~labelPlacement~~ | Place title and content with `horizontal` or `vertical` direction | string | `horizontal` |  | × |
| orientation | To specify the orientation of the step bar, `horizontal` or `vertical` | string | `horizontal` |  | × |
| percent | Progress circle percentage of current step in `process` status (only works on basic Steps) | number | - | 4.5.0 | × |
| ~~progressDot~~ | Steps with progress dot style, customize the progress dot by setting it to a function. Please use `type="dot"` instead. `titlePlacement` will be `vertical` | boolean \| (iconDot, { index, status, title, content }) => ReactNode | false |  | × |
| responsive | Change to vertical direction when screen width smaller than `532px` | boolean | true |  | × |
| size | To specify the size of the step bar, `medium` and `small` are currently supported | string | `medium` |  | × |
| status | To specify the status of current step, can be set to one of the following values: `wait` `process` `finish` `error` | string | `process` |  | × |
| styles | Customize inline style for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), CSSProperties> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), CSSProperties> | - |  | 6.0.0 |
| titlePlacement | Place title and content with `horizontal` or `vertical` direction | string | `horizontal` |  | × |
| type | Type of steps, can be set to one of the following values: `default` `dot` `inline` `navigation` `panel` | string | `default` |  | × |
| variant | Config style variant | `filled` \| `outlined` | `filled` |  | × |
| onChange | Trigger when Step is changed | (current) => void | - |  | × |
| items | StepItem content | [StepItem](#stepitem) | [] | 4.24.0 | × |

### StepItem

A single step in the step bar.

| Property | Description | Type | Default | Version |
| --- | --- | --- | --- | --- |
| content | Description of the step, optional property | ReactNode | - |  |
| ~~description~~ | Description of the step, optional property | ReactNode | - |  |
| disabled | Disable click | boolean | false |  |
| icon | Icon of the step, optional property | ReactNode | - |  |
| status | To specify the status. It will be automatically set by `current` of `Steps` if not configured. Optional values are: `wait` `process` `finish` `error` | string | `wait` |  |
| subTitle | Subtitle of the step | ReactNode | - |  |
| title | Title of the step | ReactNode | - |  |

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

- Full Ant Design Steps docs: https://ant.design/components/steps
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
