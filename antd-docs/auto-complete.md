# AutoComplete

**Library:** Ant Design v5  
**Category:**   
**Docs:** https://ant.design/components/auto-complete

---

## Overview

Autocomplete function of input field.

### When to use

- When you need an input box instead of a selector.
- When you need input suggestions or helping text.

The differences with Select are:

- AutoComplete is an input box with text hints, and users can type freely. The keyword is aiding **input**.
- Select is selecting among given choices. The keyword is **select**.

---

## Import

```js
import { AutoComplete } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

| Property | Description | Type | Default | Version |
| --- | --- | --- | --- | --- |
| allowClear | Show clear button | boolean \| { clearIcon?: ReactNode } | false | 5.8.0: Support Object type |
| backfill | If backfill selected item the input when using keyboard | boolean | false |  |
| children | Customize input element | HTMLInputElement \| HTMLTextAreaElement \| React.ReactElement&lt;InputProps> | &lt;Input /> |  |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), string> | - |  |
| ~~dataSource~~ | Data source of autocomplete options, please use `options` instead | DataSourceItemType[] | - | - |
| defaultActiveFirstOption | Whether active first option by default | boolean | true |  |
| defaultOpen | Initial open state of dropdown | boolean | - |  |
| defaultValue | Initial selected option | string | - |  |
| disabled | Whether disabled select | boolean | false |  |
| ~~dropdownClassName~~ | The className of dropdown menu, please use `classNames.popup.root` instead | string | - | - |
| ~~dropdownMatchSelectWidth~~ | Determine whether the dropdown menu and the input are the same width, please use `popupMatchSelectWidth` instead | boolean \| number | true | - |
| ~~dropdownRender~~ | Customize dropdown content, use `popupRender` instead | (originNode: ReactNode) => ReactNode | - | 4.24.0 |
| popupRender | Customize dropdown content | (originNode: ReactNode) => ReactNode | - |  |
| ~~dropdownStyle~~ | The style of dropdown menu, use `styles.popup.root` instead | CSSProperties | - |  |
| ~~popupClassName~~ | The className of dropdown menu, use `classNames.popup.root` instead | string | - | 4.23.0 |
| popupMatchSelectWidth | Determine whether the dropdown menu and the select input are the same width. Default set `min-width` same as input. Will ignore when value less than select width. `false` will disable virtual scroll | boolean \| number | true |  |
| ~~filterOption~~ | If true, filter options by input, if function, filter options against it. The function will receive two arguments, `inputValue` and `option`, if the function returns true, the option will be included in the filtered set; Otherwise, it will be excluded | boolean \| function(inputValue, option) | true |  |
| getPopupContainer | Parent node of the dropdown. Default to body, if you encountered positioning problems during scroll, try changing to the scrollable area and position relative to it. [Example](https://codesandbox.io/s/4j168r7jw0) | function(triggerNode) | () => document.body |  |
| notFoundContent | Specify content to show when no result matches | ReactNode | - |  |
| open | Controlled open state of dropdown | boolean | - |  |
| options | Select options. Will get better perf than jsx definition | { label, value }\[] | - |  |
| placeholder | The placeholder of input | string | - |  |
| showSearch | search for configuration | true \| [Object](#showsearch) | true |  |
| status | Set validation status | 'error' \| 'warning' | - | 4.19.0 |
| size | The size of the input box | `large` \| `medium` \| `small` | - |  |
| value | Selected option | string | - |  |
| styles | Customize inline style for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), CSSProperties> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), CSSProperties> | - |  |
| variant | Variants of input | `outlined` \| `borderless` \| `filled` \| `underlined` | `outlined` | 5.13.0 |
| virtual | Disable virtual scroll when set to false | boolean | true | 4.1.0 |
| onBlur | Called when leaving the component | function() | - |  |
| onChange | Called when selecting an option or changing an input value | function(value) | - |  |
| ~~onDropdownVisibleChange~~ | Called when dropdown open, use `onOpenChange` instead | (open: boolean) => void | - |  |
| onOpenChange | Called when dropdown open | (open: boolean) => void | - |  |
| onFocus | Called when entering the component | function() | - |  |
| ~~onSearch~~ | Called when searching items | function(value) | - |  |
| onSelect | Called when a option is selected. param is option's value and option instance | function(value, option) | - |  |
| onClear | Called when clear | function | - | 4.6.0 |
| onInputKeyDown | Called when key pressed | (event: KeyboardEvent) => void | - |  |
| onPopupScroll | Called when dropdown scrolls | (event: UIEvent) => void | - |  |

### showSearch

| Property | Description | Type | Default | Version |
| --- | --- | --- | --- | --- |
| filterOption | If true, filter options by input, if function, filter options against it. The function will receive two arguments, `inputValue` and `option`, if the function returns true, the option will be included in the filtered set; Otherwise, it will be excluded | boolean \| function(inputValue, option) | true |  |
| onSearch | Called when searching items | function(value) | - |  |

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

- Full Ant Design AutoComplete docs: https://ant.design/components/auto-complete
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
