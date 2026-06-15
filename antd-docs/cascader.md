# Cascader

**Library:** Ant Design v5  
**Category:** Data Entry  
**Docs:** https://ant.design/components/cascader

---

## Overview

Cascade selection box.

### When to use

- When you need to select from a set of associated data set. Such as province/city/district, company level, things classification.
- When selecting from a large data set, with multi-stage classifications separated for easy selection.
- Chooses cascade items in one float layer for better user experience.

---

## Import

```js
import { Cascader } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

```jsx

```

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| allowClear | Show clear button | boolean \| { clearIcon?: ReactNode } | true | 5.8.0: Support object type | `clearIcon`: 6.4.0 |
| ~~autoClearSearchValue~~ | Whether the current search will be cleared on selecting an item. Only applies when `multiple` is `true` | boolean | true | 5.9.0 | × |
| ~~bordered~~ | Whether has border style, please use `variant` instead | boolean | true | - | × |
| changeOnSelect | Change value on each selection if set to true, see above demo for details | boolean | false |  | × |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), string> | - |  | 5.25.0 |
| defaultOpen | Initial visible of cascader popup | boolean | - |  | × |
| defaultValue | Initial selected value | string\[] \| number\[] | \[] |  | × |
| disabled | Whether disabled select | boolean | false |  | × |
| displayRender | The render function of displaying selected options | (label, selectedOptions) => ReactNode | label => label.join(`/`) | `multiple`: 4.18.0 | × |
| tagRender | Custom render function for tags in `multiple` mode | (label: string, onClose: function, value: string) => ReactNode | - |  | × |
| ~~popupClassName~~ | The additional className of popup overlay, use `classNames.popup.root` instead | string | - | 4.23.0 | × |
| ~~dropdownClassName~~ | The additional className of popup overlay, please use `classNames.popup.root` instead | string | - | - | × |
| ~~dropdownRender~~ | Customize dropdown content, use `popupRender` instead | (menus: ReactNode) => ReactNode | - | 4.4.0 | × |
| popupRender | Customize dropdown content | (menus: ReactNode) => ReactNode | - |  | × |
| ~~dropdownStyle~~ | The style of dropdown menu, use `styles.popup.root` instead | CSSProperties | - |  | × |
| expandIcon | Customize the current item expand icon | ReactNode | - | 4.4.0 | 6.3.0 |
| expandTrigger | expand current item when click or hover, one of `click` `hover` | string | `click` |  | × |
| fieldNames | Custom field name for label and value and children | object | { label: `label`, value: `value`, children: `children` } |  | × |
| getPopupContainer | Parent Node which the selector should be rendered to. Default to `body`. When position issues happen, try to modify it into scrollable content and position it relative. [example](https://codepen.io/afc163/pen/zEjNOy?editors=0010) | function(triggerNode) | () => document.body |  | × |
| loadData | To load option lazily, and it cannot work with `showSearch` | (selectedOptions) => void | - |  | × |
| loadingIcon | Customize the loading icon | ReactNode | - |  | 6.3.0 |
| maxTagCount | Max tag count to show. `responsive` will cost render performance | number \| `responsive` | - | 4.17.0 | × |
| maxTagPlaceholder | Placeholder for not showing tags | ReactNode \| function(omittedValues) | - | 4.17.0 | × |
| maxTagTextLength | Max tag text length to show | number | - | 4.17.0 | × |
| notFoundContent | Specify content to show when no result matches | ReactNode | `Not Found` |  | × |
| open | Set visible of cascader popup | boolean | - | 4.17.0 | × |
| options | The data options of cascade | [Option](#option)\[] | - |  | × |
| placeholder | The input placeholder | string | - |  | × |
| placement | Use preset popup align config from builtinPlacements | `bottomLeft` `bottomRight` `topLeft` `topRight` | `bottomLeft` | 4.17.0 | × |
| prefix | The custom prefix | ReactNode | - | 5.22.0 | × |
| ~~showArrow~~ | Whether to show the arrow icon, please use `suffixIcon={null}` instead | boolean | true | - | × |
| showSearch | Whether show search input in single mode | boolean \| [Object](#showsearch) | false |  | `searchIcon`: 6.4.0 |
| size | The input size | `large` \| `medium` \| `small` | `medium` |  | × |
| status | Set validation status | 'error' \| 'warning' | - | 4.19.0 | × |
| styles | Customize inline style for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), CSSProperties> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), CSSProperties> | - |  | 5.25.0 |
| suffixIcon | The custom suffix icon | ReactNode | - |  | 6.4.0 |
| value | The selected value | string\[] \| number\[] | - |  | × |
| variant | Variants of selector | `outlined` \| `borderless` \| `filled` \| `underlined` | `outlined` | 5.13.0 \| `underlined`: 5.24.0 | 5.19.0 |
| onChange | Callback when finishing cascader select | (value, selectedOptions) => void | - |  | × |
| onClear | Called when clear | () => void | - | - | × |
| ~~onDropdownVisibleChange~~ | Callback when popup shown or hidden, use `onOpenChange` instead | (value) => void | - | 4.17.0 | × |
| onOpenChange | Callback when popup shown or hidden | (value) => void | - |  | × |
| ~~onPopupVisibleChange~~ | Callback when popup shown or hidden, please use `onOpenChange` instead | (value) => void | - | - | × |
| multiple | Support multiple or not | boolean | - | 4.17.0 | × |
| removeIcon | The custom remove icon | ReactNode | - |  | 6.4.0 |
| showCheckedStrategy | The way to show selected items in the box (only effective when `multiple` is `true`). `Cascader.SHOW_CHILD`: just show child treeNode. `Cascader.SHOW_PARENT`: just show parent treeNode (when all child treeNode under the parent treeNode are checked) | `Cascader.SHOW_PARENT` \| `Cascader.SHOW_CHILD` | `Cascader.SHOW_PARENT` | 4.20.0 | × |
| ~~searchValue~~ | Set search value, Need work with `showSearch` | string | - | 4.17.0 | × |
| ~~onSearch~~ | The callback function triggered when input changed | (search: string) => void | - | 4.17.0 | × |
| ~~dropdownMenuColumnStyle~~ | The style of the drop-down menu column, use `styles.popup.listItem` instead | CSSProperties | - |  | × |
| ~~popupMenuColumnStyle~~ | The style of the drop-down menu column, use `styles.popup.listItem` instead | CSSProperties | - |  | × |
| optionRender | Customize the rendering dropdown options | (option: Option) => React.ReactNode | - | 5.16.0 | × |

### showSearch

| Property | Description | Type | Default | Version |
| --- | --- | --- | --- | --- |
| autoClearSearchValue | Whether the current search will be cleared on selecting an item. Only applies when `multiple` is `true` | boolean | true | 5.9.0 |
| filter | The function will receive two arguments, inputValue and option, if the function returns true, the option will be included in the filtered set; Otherwise, it will be excluded | function(inputValue, path): boolean | - |  |
| limit | Set the count of filtered items | number \| false | 50 |  |
| matchInputWidth | Whether the width of list matches input, ([how it looks](https://github.com/ant-design/ant-design/issues/25779)) | boolean | true |  |
| render | Used to render filtered options | function(inputValue, path): ReactNode | - |  |
| sort | Used to sort filtered options | function(a, b, inputValue) | - |  |
| searchValue | Set search value, Need work with `showSearch` | string | - | 4.17.0 |
| onSearch | The callback function triggered when input changed | (search: string) => void | - | 4.17.0 |
| searchIcon | Customize the search icon | ReactNode | - | 6.3.0 |

### Option

```typescript
interface Option {
  value: string | number;
  label?: React.ReactNode;
  disabled?: boolean;
  children?: Option[];
  // Determines if this is a leaf node(effective when `loadData` is specified).
  // `false` will force trade TreeNode as a parent node.
  // Show expand icon even if the current node has no children.
  isLeaf?: boolean;
}
```

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

- Full Ant Design Cascader docs: https://ant.design/components/cascader
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
