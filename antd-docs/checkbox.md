# Checkbox

**Library:** Ant Design v5  
**Category:** Data Entry  
**Docs:** https://ant.design/components/checkbox

---

## Overview

Collect user's choices.

### When to use

- Used for selecting multiple values from several options.
- If you use only one checkbox, it is the same as using Switch to toggle between two states. The difference is that Switch will trigger the state change directly, but Checkbox just marks the state as changed and this needs to be submitted.

---

## Import

```js
import { Checkbox } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

#### Checkbox

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| checked | Specifies whether the checkbox is selected | boolean | false |  | × |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), string> | - |  | 6.0.0 |
| defaultChecked | Specifies the initial state: whether or not the checkbox is selected | boolean | false |  | × |
| disabled | If disable checkbox | boolean | false |  | × |
| indeterminate | The indeterminate checked state of checkbox | boolean | false |  | × |
| onChange | The callback function that is triggered when the state changes | (e: CheckboxChangeEvent) => void | - |  | × |
| onBlur | Called when leaving the component | function() | - |  | × |
| onFocus | Called when entering the component | function() | - |  | × |
| styles | Customize inline style for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), CSSProperties> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), CSSProperties> | - |  | 6.0.0 |

#### Checkbox.Group

| Property | Description | Type | Default | Version |
| --- | --- | --- | --- | --- |
| defaultValue | Default selected value | (string \| number)\[] | \[] |  |
| disabled | If disable all checkboxes | boolean | false |  |
| name | The `name` property of all `input[type="checkbox"]` children | string | - |  |
| options | Specifies options | string\[] \| number\[] \| Option\[] | \[] |  |
| value | Used for setting the currently selected value | (string \| number \| boolean)\[] | \[] |  |
| title | title of the option | `string` | - |  |
| className | className of the option | `string` | - | 5.25.0 |
| style | styles of the option | `React.CSSProperties` | - |  |
| onChange | The callback function that is triggered when the state changes | (checkedValue: T[]) => void | - |  |

##### Option

```typescript
interface Option {
  label: string;
  value: string;
  disabled?: boolean;
}
```

### Methods

#### Checkbox

| Name          | Description                          | Version |
| ------------- | ------------------------------------ | ------- |
| blur()        | Remove focus                         |         |
| focus()       | Get focus                            |         |
| nativeElement | Returns the DOM node of the Checkbox | 5.17.3  |

---

## AI Design System token mapping

When using this component with the AI Design System adapter, these
`--ds-*` hooks drive the component's appearance:

```
--ds-interactive, --ds-border
```

Adapter file: `lib-adapters/ant-design.css`  
Adapter spec: `specs/adapters/ant-design.md`

---

## Notes

- Full Ant Design Checkbox docs: https://ant.design/components/checkbox
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
