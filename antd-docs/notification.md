# Notification

**Library:** Ant Design v5  
**Category:** Feedback  
**Docs:** https://ant.design/components/notification

---

## Overview

Prompt notification message globally.

### When to use

To display a notification message at any of the four corners of the viewport. Typically it can be used in the following cases:

- A notification with complex content.
- A notification providing a feedback based on the user interaction. Or it may show some details about upcoming steps the user may have to follow.
- A notification that is pushed by the application.

---

## Import

```js
import { notification } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

- `notification.success(config)`
- `notification.error(config)`
- `notification.info(config)`
- `notification.warning(config)`
- `notification.open(config)`
- `notification.destroy(key?: String)`

The properties of config are as follows:

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| actions | Customized button group | ReactNode | - | 5.24.0 | × |
| ~~btn~~ | Customized close button group, please use `actions` instead | ReactNode | - | - | × |
| className | Customized CSS class | string | - | - | 5.7.0 |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), string> | - |  | 6.0.0 |
| closable | Whether to show the close button | boolean \| [ClosableType](#closabletype) | true | - | × |
| closeIcon | Custom close icon | ReactNode | true | 5.7.0: close button will be hidden when setting to null or false | 5.14.0 |
| description | The content of notification box (required) | ReactNode | - | - | × |
| duration | Time in seconds before Notification is closed. When set to `0` or `false`, it will never be closed automatically | number \| false | 4.5 | - | × |
| showProgress | Show progress bar for auto-closing notification | boolean |  | 5.18.0 | × |
| pauseOnHover | keep the timer running or not on hover | boolean | true | 5.18.0 | × |
| icon | Customized icon | ReactNode | - | - | × |
| key | The unique identifier of the Notification | string | - | - | × |
| title | The title of notification box | ReactNode | - | 6.0.0 | × |
| ~~message~~ | The title of notification box (deprecated), please use `title` instead | ReactNode | - | - | × |
| placement | Position of Notification, can be one of `top` \| `topLeft` \| `topRight` \| `bottom` \| `bottomLeft` \| `bottomRight` | string | `topRight` | - | × |
| role | The semantics of notification content recognized by screen readers. The default value is `alert`. When set as the default value, the screen reader will promptly interrupt any ongoing content reading and prioritize the notification content for immediate attention. | `alert \| status` | `alert` | 5.6.0 | × |
| style | Customized inline style | [CSSProperties](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/e434515761b36830c3e58a970abf5186f005adac/types/react/index.d.ts#L794) | - | - | 5.7.0 |
| styles | Customize inline style for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), CSSProperties> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), CSSProperties> | - |  | 6.0.0 |
| onClick | Specify a function that will be called when the notification is clicked | function | - | - | × |
| onClose | Trigger when notification closed | function | - | - | × |
| props | An object that can contain `data-*`, `aria-*`, or `role` props, to be put on the notification `div`. This currently only allows `data-testid` instead of `data-*` in TypeScript. See https://github.com/microsoft/TypeScript/issues/28960. | Object | - | - | × |

- `notification.useNotification(config)`

The properties of config are as follows:

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| bottom | Distance from the bottom of the viewport, when `placement` is `bottom` `bottomRight` or `bottomLeft` (unit: pixels) | number | 24 |  | × |
| closeIcon | Custom close icon | ReactNode | true | 5.7.0: close button will be hidden when setting to null or false | 5.14.0 |
| getContainer | Return the mount node for Notification | () => HTMLNode | () => document.body |  | × |
| placement | Position of Notification, can be one of `top` \| `topLeft` \| `topRight` \| `bottom` \| `bottomLeft` \| `bottomRight` | string | `topRight` |  | × |
| showProgress | Show progress bar for auto-closing notification | boolean |  | 5.18.0 | × |
| pauseOnHover | keep the timer running or not on hover | boolean | true | 5.18.0 | × |
| rtl | Whether to enable RTL mode | boolean | false |  | × |
| stack | Notifications will be stacked when amount is over threshold | boolean \| `{ threshold: number }` | `{ threshold: 3 }` | 5.10.0 | × |
| top | Distance from the top of the viewport, when `placement` is `top` `topRight` or `topLeft` (unit: pixels) | number | 24 |  | × |
| maxCount | Max Notification show, drop oldest if exceed limit | number | - | 4.17.0 | × |

`notification` also provides a global `config()` method that can be used for specifying the default options. Once this method is used, all the notification boxes will take into account these globally defined options when displaying.

### ClosableType

| Property  | Description                     | Type      | Default   | Version |
| --------- | ------------------------------- | --------- | --------- | ------- |
| closeIcon | Custom close icon               | ReactNode | undefined | -       |
| onClose   | Trigger when notification close | Function  | undefined | -       |

### Global configuration

`notification.config(options)`

> When you use `ConfigProvider` for global configuration, the system will automatically start RTL mode by default.(4.3.0+)
>
> When you want to use it alone, you can start the RTL mode through the following settings.

#### notification.config

```js
notification.config({
  placement: 'bottomRight',
  bottom: 50,
  duration: 3,
  rtl: true,
});
```

| Property | Description | Type | Default | Version |
| --- | --- | --- | --- | --- |
| bottom | Distance from the bottom of the viewport, when `placement` is `bottom` `bottomRight` or `bottomLeft` (unit: pixels) | number | 24 |  |
| closeIcon | Custom close icon | ReactNode | true | 5.7.0: close button will be hidden when setting to null or false |
| duration | Time in seconds before Notification is closed. When set to 0 or null, it will never be closed automatically | number | 4.5 |  |
| getContainer | Return the mount node for Notification, but still display at fullScreen | () => HTMLNode | () => document.body |  |
| placement | Position of Notification, can be one of `top` `topLeft` `topRight` `bottom` `bottomLeft` `bottomRight` | string | `topRight` |  |
| showProgress | Show progress bar for auto-closing notification | boolean |  | 5.18.0 |
| pauseOnHover | keep the timer running or not on hover | boolean | true | 5.18.0 |
| rtl | Whether to enable RTL mode | boolean | false |  |
| top | Distance from the top of the viewport, when `placement` is `top` `topRight` or `topLeft` (unit: pixels) | number | 24 |  |
| maxCount | Max Notification show, drop oldest if exceed limit | number | - | 4.17.0 |

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

- Full Ant Design Notification docs: https://ant.design/components/notification
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
