# Popconfirm

**Library:** Ant Design v5  
**Category:** Feedback  
**Docs:** https://ant.design/components/popconfirm

---

## Overview

Pop up a bubble confirmation box for an action.

### When to use

A simple and compact dialog used for asking for user confirmation.

The difference with the `confirm` modal dialog is that it's more lightweight than the static popped full-screen confirm modal.

---

## Import

```js
import { Popconfirm } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| cancelButtonProps | The cancel button props | [ButtonProps](/components/button/#api) | - |  | × |
| cancelText | The text of the Cancel button | string | `Cancel` |  | × |
| disabled | Whether show popconfirm when click its childrenNode | boolean | false |  | × |
| icon | Customize icon of confirmation | ReactNode | &lt;ExclamationCircleFilled /> |  | × |
| okButtonProps | The ok button props | [ButtonProps](/components/button/#api) | - |  | × |
| okText | The text of the Confirm button | string | `OK` |  | × |
| okType | Button `type` of the Confirm button | string | `primary` |  | × |
| showCancel | Show cancel button | boolean | true | 4.18.0 | × |
| title | The title of the confirmation box | ReactNode \| () => ReactNode | - |  | × |
| description | The description of the confirmation box title | ReactNode \| () => ReactNode | - | 5.1.0 | × |
| onCancel | A callback of cancel | function(e) | - |  | × |
| onConfirm | A callback of confirmation | function(e) | - |  | × |
| onPopupClick | A callback of popup click | function(e) | - | 5.5.0 | × |

<!-- Common API -->

<embed src="../tooltip/shared/sharedProps.en-US.md"></embed>

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

- Full Ant Design Popconfirm docs: https://ant.design/components/popconfirm
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
