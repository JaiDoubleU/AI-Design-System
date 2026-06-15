# Message

**Library:** Ant Design v5  
**Category:** Feedback  
**Docs:** https://ant.design/components/message

---

## Overview

Display global messages as feedback in response to user operations.

### When to use

- To provide feedback such as success, warning, error etc.
- A message is displayed at top and center and will be dismissed automatically, as a non-interrupting light-weighted prompt.

---

## Import

```js
import { message } from 'antd';  // message.success(), message.error(), ...
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

This component provides some static methods, with usage and arguments as following:

- `message.success(content, [duration], onClose)`
- `message.error(content, [duration], onClose)`
- `message.info(content, [duration], onClose)`
- `message.warning(content, [duration], onClose)`
- `message.loading(content, [duration], onClose)`

| Property | Description | Type | Default |
| --- | --- | --- | --- |
| content | The content of the message | ReactNode \| config | - |
| duration | Time(seconds) before auto-dismiss, don't dismiss if set to 0 | number | 3 |
| onClose | Specify a function that will be called when the message is closed | function | - |

`afterClose` can be called in thenable interface:

- `message[level](content, [duration]).then(afterClose)`
- `message[level](content, [duration], onClose).then(afterClose)`

where `level` refers one static methods of `message`. The result of `then` method will be a Promise.

Supports passing parameters wrapped in an object:

- `message.open(config)`
- `message.success(config)`
- `message.error(config)`
- `message.info(config)`
- `message.warning(config)`
- `message.loading(config)`

The properties of config are as follows:

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| className | Customized CSS class | string | - | - | 5.7.0 |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), string> | - | 6.0.0 | 6.0.0 |
| content | The content of the message | ReactNode | - | - | × |
| duration | Time(seconds) before auto-dismiss, don't dismiss if set to 0 | number | 3 | - | × |
| icon | Customized Icon | ReactNode | - | - | × |
| pauseOnHover | keep the timer running or not on hover | boolean | true | - | × |
| key | The unique identifier of the Message | string \| number | - | - | × |
| style | Customized inline style | [CSSProperties](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/e434515761b36830c3e58a970abf5186f005adac/types/react/index.d.ts#L794) | - | - | 5.7.0 |
| styles | Customize inline style for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), CSSProperties> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), CSSProperties> | - | 6.0.0 | 6.0.0 |
| onClick | Specify a function that will be called when the message is clicked | function | - | - | × |
| onClose | Specify a function that will be called when the message is closed | function | - | - | × |

### Global static methods

Methods for global configuration and destruction are also provided:

- `message.config(options)`
- `message.destroy()`

> use `message.destroy(key)` to remove a message.

#### message.config

> When you use `ConfigProvider` for global configuration, the system will automatically start RTL mode by default.(4.3.0+)
>
> When you want to use it alone, you can start the RTL mode through the following settings.

```js
message.config({
  top: 100,
  duration: 2,
  maxCount: 3,
  rtl: true,
  prefixCls: 'my-message',
});
```

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| duration | Time before auto-dismiss, in seconds | number | 3 |  | × |
| getContainer | Return the mount node for Message, but still display at fullScreen | () => HTMLElement | () => document.body |  | × |
| maxCount | Max message show, drop oldest if exceed limit | number | - |  | × |
| prefixCls | The prefix className of message node | string | `ant-message` | 4.5.0 | × |
| rtl | Whether to enable RTL mode | boolean | false |  | × |
| stack | Messages will be stacked when amount is over threshold. Only the latest message is shown in the collapsed stack | boolean \| `{ threshold: number }` | false | 6.4.0 | × |
| top | Distance from top | string \| number | 8 |  | × |

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

- Full Ant Design Message docs: https://ant.design/components/message
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
