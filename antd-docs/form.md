# Form

**Library:** Ant Design v5  
**Category:** Data Entry  
**Docs:** https://ant.design/components/form

---

## Overview

High-performance form component with data domain management. Includes data entry, validation, and corresponding styles.

### When to use

Common props ref：[Common props](/docs/react/common-props)

### Form

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), string> | - |  | 6.0.0 |
| colon | Configure the default value of `colon` for Form.Item. Indicates whether the colon after the label is displayed (only effective when prop layout is horizontal) | boolean | true |  | 4.18.0 |
| disabled | Set form component disable, only available for antd components | boolean | false | 4.21.0 | × |
| component | Set the Form rendering element. Do not create a DOM node for `false` | ComponentType \| false | form |  | × |
| fields | Control of form fields through state management (such as redux). Not recommended for non-strong demand. View [example](#form-demo-global-state) | [FieldData](#fielddata)\[] | - |  | × |
| form | Form control instance created by `Form.useForm()`. Automatically created when not provided | [FormInstance](#forminstance) | - |  | × |
| feedbackIcons | Can be passed custom icons while `Form.Item` element has `hasFeedback` | [FeedbackIcons](#feedbackicons) | - | 5.9.0 | × |
| initialValues | Set value by Form initialization or reset | object | - |  | × |
| labelAlign | The text align of label of all items | `left` \| `right` | `right` |  | 6.4.0 |
| labelWrap | whether label can be wrap | boolean | false | 4.18.0 | × |
| labelCol | Label layout, like `;
```

## Form.Item

Form field component for data bidirectional binding, validation, layout, and so on.

---

## Import

```js
import { Form, Form.Item } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

### Form

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), string> | - |  | 6.0.0 |
| colon | Configure the default value of `colon` for Form.Item. Indicates whether the colon after the label is displayed (only effective when prop layout is horizontal) | boolean | true |  | 4.18.0 |
| disabled | Set form component disable, only available for antd components | boolean | false | 4.21.0 | × |
| component | Set the Form rendering element. Do not create a DOM node for `false` | ComponentType \| false | form |  | × |
| fields | Control of form fields through state management (such as redux). Not recommended for non-strong demand. View [example](#form-demo-global-state) | [FieldData](#fielddata)\[] | - |  | × |
| form | Form control instance created by `Form.useForm()`. Automatically created when not provided | [FormInstance](#forminstance) | - |  | × |
| feedbackIcons | Can be passed custom icons while `Form.Item` element has `hasFeedback` | [FeedbackIcons](#feedbackicons) | - | 5.9.0 | × |
| initialValues | Set value by Form initialization or reset | object | - |  | × |
| labelAlign | The text align of label of all items | `left` \| `right` | `right` |  | 6.4.0 |
| labelWrap | whether label can be wrap | boolean | false | 4.18.0 | × |
| labelCol | Label layout, like `;
```

---

## AI Design System token mapping

When using this component with the AI Design System adapter, these
`--ds-*` hooks drive the component's appearance:

```
--ds-text-danger (errors), --ds-border-focus (active fields)
```

Adapter file: `lib-adapters/ant-design.css`  
Adapter spec: `specs/adapters/ant-design.md`

---

## Notes

- Full Ant Design Form docs: https://ant.design/components/form
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
