# InputNumber

**Library:** Ant Design v5  
**Category:** Data Entry  
**Docs:** https://ant.design/components/input-number

---

## Overview

Enter a number within certain range with the mouse or keyboard.

### When to use

When a numeric value needs to be provided.

---

## Import

```js
import { InputNumber } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| ~~addonAfter~~ | The label text displayed after (on the right side of) the input field, please use Space.Compact instead | ReactNode | - | 4.17.0 | × |
| ~~addonBefore~~ | The label text displayed before (on the left side of) the input field, please use Space.Compact instead | ReactNode | - | 4.17.0 | × |
| changeOnBlur | Trigger `onChange` when blur. e.g. reset value in range by blur | boolean | true | 5.11.0 | × |
| changeOnWheel | Allows control with mouse wheel | boolean | - | 5.14.0 | × |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), string> | - | 6.0.0 | 6.0.0 |
| controls | Whether to show `+-` controls, or set custom arrow icons | boolean \| { upIcon?: React.ReactNode; downIcon?: React.ReactNode; } | - |  | × |
| decimalSeparator | Decimal separator | string | - | - | × |
| placeholder | Placeholder | string | - |  | × |
| defaultValue | The initial value | number | - | - | × |
| disabled | If the input is disabled | boolean | false | - | × |
| formatter | Specifies the format of the value presented | function(value: number \| string, info: { userTyping: boolean, input: string }): string | - |  | × |
| keyboard | If keyboard behavior is enabled | boolean | true |  | × |
| max | The max value | number | [Number.MAX_SAFE_INTEGER](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER) | - | × |
| min | The min value | number | [Number.MIN_SAFE_INTEGER](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MIN_SAFE_INTEGER) | - | × |
| parser | Specifies the value extracted from formatter | function(string): number | - | - | × |
| precision | The precision of input value. Will use `formatter` when config of `formatter` | number | - | - | × |
| readOnly | If the input is readonly | boolean | false | - | × |
| status | Set validation status | 'error' \| 'warning' | - |  | × |
| styles | Customize inline style for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), CSSProperties> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), CSSProperties> | - | 6.0.0 | 6.0.0 |
| prefix | The prefix icon for the Input | ReactNode | - |  | × |
| suffix | The suffix icon for the Input | ReactNode | - | 5.20.0 | × |
| size | The height of input box | `large` \| `medium` \| `small` | - | - | × |
| step | The number to which the current value is increased or decreased. It can be an integer or decimal | number \| string | 1 | - | × |
| stringMode | Set value as string to support high precision decimals. Will return string value by `onChange` | boolean | false | 4.13.0 | × |
| mode | Show input or spinner | `'input' \| 'spinner'` | `'input'` |  | × |
| value | The current value of the component | number | - | - | × |
| variant | Variants of Input | `outlined` \| `borderless` \| `filled` \| `underlined` | `outlined` | 5.13.0 \| `underlined`: 5.24.0 | 5.19.0 |
| onChange | The callback triggered when the value is changed | function(value: number \| string \| null) | - | - | × |
| onPressEnter | The callback function that is triggered when Enter key is pressed | function(e) | - | - | × |
| onStep | The callback function that is triggered when click up or down buttons / Keyboard / Wheel | (value: number, info: { offset: number, type: 'up' \| 'down', emitter: 'handler' \| 'keydown' \| 'wheel' }) => void | - |  | × |
| ~~bordered~~ | Whether has border style, please use `variant` instead | boolean | true | - | × |

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

- Full Ant Design InputNumber docs: https://ant.design/components/input-number
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
