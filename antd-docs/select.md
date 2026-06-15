# Select

**Library:** Ant Design v5  
**Category:** Data Entry  
**Docs:** https://ant.design/components/select

---

## Overview

A dropdown menu for displaying choices.

### When to use

- A dropdown menu for displaying choices - an elegant alternative to the native `<select>` element.
- Utilizing [Radio](/components/radio/) is recommended when there are fewer total options (less than 5).
- You probably need [AutoComplete](/components/auto-complete/) if you're looking for an input box that can be typed or selected.

---

## Import

```js
import { Select } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

### Select props

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| allowClear | Customize clear icon | boolean \| { clearIcon?: ReactNode } | false | 5.8.0: Support object type | 6.4.0 |
| ~~autoClearSearchValue~~ | Whether the current search will be cleared on selecting an item. Only applies when `mode` is set to `multiple` or `tags` | boolean | true |  | × |
| ~~bordered~~ | Whether has border style, please use `variant` instead | boolean | true | - | × |
| classNames | Customize class for each semantic structure inside the Select component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), string> | - |  | 5.25.0 |
| defaultActiveFirstOption | Whether active first option by default | boolean | true |  | × |
| defaultOpen | Initial open state of dropdown | boolean | - |  | × |
| defaultValue | Initial selected option | string \| string\[] \| <br />number \| number\[] \| <br />LabeledValue \| LabeledValue\[] | - |  | × |
| disabled | Whether disabled select | boolean | false |  | × |
| ~~dropdownClassName~~ | The className of dropdown menu, please use `classNames.popup.root` instead | string | - | - | × |
| ~~dropdownMatchSelectWidth~~ | Determine whether the popup menu and the select input are the same width, please use `popupMatchSelectWidth` instead | boolean \| number | true | - | × |
| ~~popupClassName~~ | The className of dropdown menu, use `classNames.popup.root` instead | string | - | 4.23.0 | × |
| popupMatchSelectWidth | Determine whether the popup menu and the select input are the same width. Default set `min-width` same as input. Will ignore when value less than select width. `false` will disable virtual scroll | boolean \| number | true | 5.5.0 | × |
| ~~dropdownRender~~ | Customize dropdown content, use `popupRender` instead | (originNode: ReactNode) => ReactNode | - |  | × |
| popupRender | Customize dropdown content | (originNode: ReactNode) => ReactNode | - | 5.25.0 | × |
| ~~dropdownStyle~~ | The style of dropdown menu, use `styles.popup.root` instead | CSSProperties | - |  | × |
| fieldNames | Customize node label, value, options，groupLabel field name | object | { label: `label`, value: `value`, options: `options`, groupLabel: `label` } | 4.17.0 (`groupLabel` added in 5.6.0) | × |
| ~~filterOption~~ | If true, filter options by input, if function, filter options against it. The function will receive two arguments, `inputValue` and `option`, if the function returns `true`, the option will be included in the filtered set; Otherwise, it will be excluded | boolean \| function(inputValue, option) | true |  | × |
| ~~filterSort~~ | Sort function for search options sorting, see [Array.sort](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)'s compareFunction | (optionA: Option, optionB: Option, info: { searchValue: string }) => number | - | `searchValue`: 5.19.0 | × |
| getPopupContainer | Parent Node which the selector should be rendered to. Default to `body`. When position issues happen, try to modify it into scrollable content and position it relative. [Example](https://codesandbox.io/s/4j168r7jw0) | function(triggerNode) | () => document.body |  | × |
| labelInValue | Whether to embed label in value, turn the format of value from `string` to { value: string, label: ReactNode } | boolean | false |  | × |
| listHeight | Config popup height | number | 256 |  | × |
| loading | Indicate loading state | boolean | false |  | × |
| loadingIcon | Customize the loading icon | ReactNode | `` | 6.4.0 | 6.4.0 |
| maxCount | The max number of items can be selected, only applies when `mode` is `multiple` or `tags` | number | - | 5.13.0 | × |
| maxTagCount | Max tag count to show. `responsive` will cost render performance | number \| `responsive` | - | responsive: 4.10 | × |
| maxTagPlaceholder | Placeholder for not showing tags | ReactNode \| function(omittedValues) | - |  | × |
| maxTagTextLength | Max tag text length to show | number | - |  | × |
| menuItemSelectedIcon | The custom menuItemSelected icon with multiple options | ReactNode | `` |  | 6.4.0 |
| mode | Set mode of Select | `multiple` \| `tags` | - |  | × |
| notFoundContent | Specify content to show when no result matches | ReactNode | `Not Found` |  | × |
| open | Controlled open state of dropdown | boolean | - |  | × |
| ~~optionFilterProp~~ | Deprecated, see `showSearch.optionFilterProp` |  |  |  | × |
| optionLabelProp | Which prop value of option will render as content of select. [Example](https://codesandbox.io/s/antd-reproduction-template-tk678) | string | `children` |  | × |
| options | Select options. Will get better perf than jsx definition | { label, value }\[] | - |  | × |
| optionRender | Customize the rendering dropdown options | (option: FlattenOptionData\

---

## AI Design System token mapping

When using this component with the AI Design System adapter, these
`--ds-*` hooks drive the component's appearance:

```
--ds-border, --ds-border-focus, --ds-interactive
```

Adapter file: `lib-adapters/ant-design.css`  
Adapter spec: `specs/adapters/ant-design.md`

---

## Notes

- Full Ant Design Select docs: https://ant.design/components/select
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
