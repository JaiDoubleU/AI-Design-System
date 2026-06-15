# Alert

**Library:** Ant Design v5  
**Category:**   
**Docs:** https://ant.design/components/alert

---

## Overview

Display warning messages that require attention.

### When to use

- When you need to show alert messages to users.
- When you need a persistent static container which is closable by user actions.

---

## Import

```js
import { Alert } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| action | The action of Alert | ReactNode | - |  | × |
| ~~afterClose~~ | Called when close animation is finished, please use `closable.afterClose` instead | () => void | - |  | × |
| banner | Whether to show as banner | boolean | false |  | × |
| variant | Variant of Alert style | `outlined` \| `filled` | `outlined` | 6.4.0 | 6.4.0 |
| classNames | Customize class for each semantic structure inside the component. Supports object or function | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props }) => Record<[SemanticDOM](#semantic-dom), string> | - |  | 6.0.0 |
| closable | The config of closable | boolean \| [ClosableType](#closabletype) & React.AriaAttributes | `false` |  | 5.15.0 |
| closeIcon | (Only supports global configuration) Custom close icon | ReactNode | - | × | 5.14.0 |
| description | Additional content of Alert | ReactNode | - |  | × |
| errorIcon | (Only supports global configuration) Custom error icon in Alert icon | ReactNode | - | × | 6.2.0 |
| icon | Custom icon, effective when `showIcon` is true | ReactNode | - |  | × |
| infoIcon | (Only supports global configuration) Custom info icon in Alert icon | ReactNode | - | × | 6.2.0 |
| ~~message~~ | Content of Alert, please use `title` instead | ReactNode | - |  | × |
| ~~onClose~~ | Callback when Alert is closed, please use `closable.onClose` instead | (e: MouseEvent) => void | - |  | × |
| ~~closeIcon~~ | Custom close icon, please use `closable.closeIcon` instead | ReactNode | - | - | × |
| ~~closeText~~ | Close text to show, please use `closable.closeIcon` instead | ReactNode | - | - | × |
| showIcon | Whether to show icon | boolean | false, in `banner` mode default is true |  | × |
| styles | Customize inline style for each semantic structure inside the component. Supports object or function | Record<[SemanticDOM](#semantic-dom), CSSProperties> \| (info: { props }) => Record<[SemanticDOM](#semantic-dom), CSSProperties> | - |  | 6.0.0 |
| successIcon | (Only supports global configuration) Custom success icon in Alert icon | ReactNode | - | × | 6.2.0 |
| title | Content of Alert | ReactNode | - |  | × |
| type | Type of Alert styles, options: `success`, `info`, `warning`, `error` | string | `info`, in `banner` mode default is `warning` |  | × |
| warningIcon | (Only supports global configuration) Custom warning icon in Alert icon | ReactNode | - | × | 6.2.0 |

### ClosableType

| Property | Description | Type | Default | Version |
| --- | --- | --- | --- | --- |
| afterClose | Called when close animation is finished | function | - | - |
| closeIcon | Custom close icon | ReactNode | - | - |
| onClose | Callback when Alert is closed | (e: MouseEvent) => void | - | - |

### Alert.ErrorBoundary

| Property | Description | Type | Default | Version |
| --- | --- | --- | --- | --- |
| description | Custom error description to show | ReactNode | {{ error stack }} |  |
| ~~message~~ | Custom error message to show, please use `title` instead | ReactNode | {{ error }} |  |
| title | Custom error title to show | ReactNode | {{ error }} |  |

---

## AI Design System token mapping

When using this component with the AI Design System adapter, these
`--ds-*` hooks drive the component's appearance:

```
--ds-bg-{variant}, --ds-border-{variant}, --ds-text-{variant}
```

Adapter file: `lib-adapters/ant-design.css`  
Adapter spec: `specs/adapters/ant-design.md`

---

## Notes

- Full Ant Design Alert docs: https://ant.design/components/alert
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
