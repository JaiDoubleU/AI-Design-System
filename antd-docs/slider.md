# Slider

**Library:** Ant Design v5  
**Category:** Data Entry  
**Docs:** https://ant.design/components/slider

---

## Overview

A Slider component for displaying current value and intervals in range.

### When to use

Used to input a value within a specified range.

---

## Import

```js
import { Slider } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), string> | - |  | 5.23.0 |
| defaultValue | The default value of the slider. When `range` is false, use number, otherwise, use \[number, number] | number \| \[number, number] | 0 \| \[0, 0] |  | × |
| disabled | If true, the slider will not be interactive | boolean | false |  | × |
| keyboard | Support using keyboard to move handlers | boolean | true | 5.2.0+ | × |
| dots | Whether the thumb can only be dragged to tick marks | boolean | false |  | × |
| included | Takes effect when `marks` is not null. True means containment and false means coordinative | boolean | true |  | × |
| marks | Tick marks of Slider. The type of key must be `number`, and must be in closed interval \[min, max]. Each mark can declare its own style | object | { number: ReactNode } \| { number: { style: CSSProperties, label: ReactNode } } |  | × |
| max | The maximum value the slider can slide to | number | 100 |  | × |
| min | The minimum value the slider can slide to | number | 0 |  | × |
| orientation | Orientation | `horizontal` \| `vertical` | `horizontal` |  | × |
| range | Enable dual thumb mode for range selection | boolean | false |  | × |
| reverse | Reverse the component | boolean | false |  | × |
| step | The granularity the slider can step through values. Must be greater than 0, and be divisible by (max - min). When `step` is `null` and `marks` exist, valid points will only be marks, `min` and `max` | number \| null | 1 |  | × |
| styles | Customize inline style for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), CSSProperties> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), CSSProperties> | - |  | 5.23.0 |
| tooltip | The tooltip related props | [tooltip](#tooltip) | - | 4.23.0 | × |
| value | The value of slider. When `range` is false, use number, otherwise, use \[number, number] | number \| \[number, number] | - |  | × |
| vertical | If true, the slider will be vertical. Simultaneously existing with `orientation`, `orientation` takes priority | boolean | false |  | × |
| onChangeComplete | Fire when `mouseup` or `keyup` is fired | (value) => void | - |  | × |
| onChange | Callback function that is fired when the user changes the slider's value | (value) => void | - |  | × |
| ~~handleStyle~~ | Style of the slider handle, please use `styles.handle` instead | CSSProperties | - | - | × |
| ~~onAfterChange~~ | Callback fired when `mouseup` or `keyup` is fired, please use `onChangeComplete` instead | (value) => void | - | - | × |
| ~~railStyle~~ | Style of the slider rail, please use `styles.rail` instead | CSSProperties | - | - | × |
| ~~trackStyle~~ | Style of the slider track, please use `styles.track` instead | CSSProperties | - | - | × |

### range

| Property | Description | Type | Default | Version |
| --- | --- | --- | --- | --- |
| draggableTrack | Whether range track can be dragged | boolean | false | - |
| editable | Dynamic edit nodes. Cannot be used with `draggableTrack` | boolean | false | 5.20.0 |
| minCount | The minimum count of nodes | number | 0 | 5.20.0 |
| maxCount | The maximum count of nodes | number | - | 5.20.0 |

### tooltip

| Property | Description | Type | Default | Version |
| --- | --- | --- | --- | --- |
| autoAdjustOverflow | Whether to automatically adjust the popup position | boolean | true | 5.8.0 |
| open | If true, Tooltip will always be visible; if false, it will never be visible, even when dragging or hovering | boolean | - | 4.23.0 |
| placement | Set Tooltip display position. Ref [Tooltip](/components/tooltip/) | string | - | 4.23.0 |
| getPopupContainer | The DOM container of the Tooltip. The default behavior is to create a div element in the body | (triggerNode) => HTMLElement | () => document.body | 4.23.0 |
| formatter | Slider will pass its value to `formatter`, display its value in Tooltip, and hide the Tooltip when the returned value is null | value => ReactNode \| null | IDENTITY | 4.23.0 |

---

## AI Design System token mapping

When using this component with the AI Design System adapter, these
`--ds-*` hooks drive the component's appearance:

```
--ds-interactive
```

Adapter file: `lib-adapters/ant-design.css`  
Adapter spec: `specs/adapters/ant-design.md`

---

## Notes

- Full Ant Design Slider docs: https://ant.design/components/slider
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
