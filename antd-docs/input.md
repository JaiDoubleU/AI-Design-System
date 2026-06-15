# Input

**Library:** Ant Design v5  
**Category:** Data Entry  
**Docs:** https://ant.design/components/input

---

## Overview

Through mouse or keyboard input content, it is the most basic form field wrapper.

### When to use

- A user input in a form field is needed.
- A search input is required.

---

## Import

```js
import { Input } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

### Input

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| ~~addonAfter~~ | The label text displayed after (on the right side of) the input field, please use Space.Compact instead | ReactNode | - |  | × |
| ~~addonBefore~~ | The label text displayed before (on the left side of) the input field, please use Space.Compact instead | ReactNode | - |  | × |
| allowClear | If allow to remove input content with clear icon | boolean \| { clearIcon: ReactNode, disabled?: boolean } | - | disabled: 6.4.0 | 5.15.0 |
| ~~bordered~~ | Whether has border style, please use `variant` instead | boolean | true | 4.5.0 | × |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-input), string> \| (info: { props })=> Record<[SemanticDOM](#semantic-input), string> | - | 5.4.0 | 5.7.0 |
| count | Character count config | [CountConfig](#countconfig) | - | 5.10.0 | × |
| defaultValue | The initial input content | string | - |  | × |
| disabled | Whether the input is disabled | boolean | false | - | × |
| id | The ID for input | string | - |  | × |
| maxLength | The maximum number of characters in Input | number | - |  | × |
| prefix | The prefix icon for the Input | ReactNode | - |  | × |
| showCount | Whether to show character count | boolean \| { formatter: (info: { value: string, count: number, maxLength?: number }) => ReactNode } | false | 4.18.0 info.value: 4.23.0 | × |
| status | Set validation status | 'error' \| 'warning' | - | 4.19.0 | × |
| styles | Customize inline style for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-input), CSSProperties> \| (info: { props })=> Record<[SemanticDOM](#semantic-input), CSSProperties> | - | 5.4.0 | 5.7.0 |
| size | The size of the input box. Note: in the context of a form, the `medium` size is used | `large` \| `medium` \| `small` | - |  | × |
| suffix | The suffix icon for the Input | ReactNode | - |  | × |
| type | The type of input, see: [MDN](https://developer.mozilla.org/docs/Web/HTML/Element/input#Form_%3Cinput%3E_types)( use `Input.TextArea` instead of `type="textarea"`) | string | `text` |  | × |
| value | The input content value | string | - |  | × |
| variant | Variants of Input | `outlined` \| `borderless` \| `filled` \| `underlined` | `outlined` | 5.13.0 \| `underlined`: 5.24.0 | 5.19.0 |
| onChange | Callback when user input | function(e) | - |  | × |
| onPressEnter | The callback function that is triggered when Enter key is pressed | function(e) | - |  | × |
| onClear | Callback when click the clear button | () => void | - | 5.20.0 | × |

> When `Input` is used in a `Form.Item` context, if the `Form.Item` has the `id` props defined then `value`, `defaultValue`, and `id` props of `Input` are automatically set.

The rest of the props of Input are exactly the same as the original [input](https://react.dev/reference/react-dom/components/input).

#### CountConfig

```tsx
interface CountConfig {
  // Max character count. Different from the native `maxLength`, it will be marked warning but not truncated
  max?: number;
  // Custom character count, for example, the standard emoji length is greater than 1, you can customize the counting strategy to change it to 1
  strategy?: (value: string) => number;
  // Same as `showCount`
  show?: boolean | ((args: { value: string; count: number; maxLength?: number }) => ReactNode);
  // Custom clipping logic when the number of characters exceeds `count.max`, no clipping when not configured
  exceedFormatter?: (value: string, config: { max: number }) => string;
}
```

### Input.TextArea

Same as Input, and more:

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| autoSize | Height auto size feature, can be set to true \| false or an object { minRows: 2, maxRows: 6 } | boolean \| object | false |  | × |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-textarea), string> \| (info: { props }) => Record<[SemanticDOM](#semantic-textarea), string> | - | 5.4.0 | 5.15.0 |
| styles | Customize inline style for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-textarea), CSSProperties> \| (info: { props }) => Record<[SemanticDOM](#semantic-textarea), CSSProperties> | - | 5.4.0 | 5.15.0 |

The rest of the props of `Input.TextArea` are the same as the original [textarea](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea).

### Input.Search

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-search), string> \| (info: { props }) => Record<[SemanticDOM](#semantic-search), string> | - | 6.0.0 | 6.0.0 |
| enterButton | false displays the default button color, true uses the primary color, or you can provide a custom button. Conflicts with addonAfter. | ReactNode | false |  | × |
| loading | Search box with loading | boolean | false |  | × |
| onSearch | The callback function triggered when you click on the search-icon, the clear-icon or press the Enter key | function(value, event, { source: "input" \| "clear" }) | - |  | × |
| styles | Customize inline style for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-search), CSSProperties> \| (info: { props }) => Record<[SemanticDOM](#semantic-search), CSSProperties> | - | 6.0.0 | 6.0.0 |
| searchIcon | Customize the search icon | ReactNode | - | 6.4.0 | 6.4.0 |

Supports all props of `Input`.

### Input.Password

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| classNames | Semantic DOM class | Record<[SemanticDOM](#semantic-password), string> | - | 5.4.0 | 6.4.0 |
| iconRender | Custom toggle button | (visible) => ReactNode | (visible) => (visible ? &lt;EyeOutlined /> : &lt;EyeInvisibleOutlined />) | 4.3.0 | 6.4.0 |
| styles | Semantic DOM style | Record<[SemanticDOM](#semantic-password), CSSProperties> | - | 5.4.0 | 6.4.0 |
| visibilityToggle | Whether show toggle button or control password visible | boolean \| [VisibilityToggle](#visibilitytoggle) | true |  | × |

### Input.OTP

Added in `5.16.0`.

> Notes for developers
>
> When the `mask` prop is string, we recommend receiving a single character or a single emoji. If multiple characters or multiple emoji are passed, a warning will be thrown.

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| autoComplete | The autocomplete attribute for input elements, e.g. `one-time-code` for OTP autofill | string | - | 6.3.0 | × |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-otp), string> \| (info: { props }) => Record<[SemanticDOM](#semantic-otp), string> | - | 6.0.0 | 6.0.0 |
| defaultValue | Default value | string | - |  | × |
| disabled | Whether the input is disabled | boolean | false |  | × |
| formatter | Format display, blank fields will be filled with ` ` | (value: string) => string | - |  | × |
| separator | render the separator after the input box of the specified index | ReactNode \|((i: number) => ReactNode) | - | 5.24.0 | × |
| styles | Customize inline style for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-otp), CSSProperties> \| (info: { props }) => Record<[SemanticDOM](#semantic-otp), CSSProperties> | - | 6.0.0 | 6.0.0 |
| mask | Custom display, the original value will not be modified | boolean \| string | `false` | `5.17.0` | × |
| length | The number of input elements | number | 6 |  | × |
| status | Set validation status | 'error' \| 'warning' | - |  | × |
| size | The size of the input box | `small` \| `medium` \| `large` | `medium` |  | × |
| variant | Variants of Input | `outlined` \| `borderless` \| `filled` \| `underlined` | `outlined` | `underlined`: 5.24.0 | × |
| value | The input content value | string | - |  | × |
| onChange | Trigger when all the fields are filled | (value: string) => void | - |  | × |
| onInput | Trigger when the input value changes | (value: string[]) => void | - | `5.22.0` | × |

#### VisibilityToggle

| Property | Description | Type | Default | Version |
| --- | --- | --- | --- | --- |
| visible | Whether the password is show or hide | boolean | false | 4.24.0 |
| onVisibleChange | Callback executed when visibility of the password is changed | (visible) => void | - | 4.24.0 |

#### Input Methods

| Name | Description | Parameters | Version |
| --- | --- | --- | --- |
| blur | Remove focus | - |  |
| focus | Get focus | (option?: { preventScroll?: boolean, cursor?: 'start' \| 'end' \| 'all' }) | option - 4.10.0 |

---

## AI Design System token mapping

When using this component with the AI Design System adapter, these
`--ds-*` hooks drive the component's appearance:

```
--ds-border, --ds-border-focus, --ds-text, --ds-bg
```

Adapter file: `lib-adapters/ant-design.css`  
Adapter spec: `specs/adapters/ant-design.md`

---

## Notes

- Full Ant Design Input docs: https://ant.design/components/input
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
