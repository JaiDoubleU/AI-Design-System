# App

**Library:** Ant Design v5  
**Category:** Other  
**Docs:** https://ant.design/components/app

---

## Overview

Application wrapper for some global usages.

### When to use

- Provide reset styles based on `.ant-app` element.
- You could use static methods of `message/notification/Modal` from `useApp` without writing `contextHolder` manually.

---

## Import

```js
import { App } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

> This component is available since `antd@5.1.0`.

### App

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| component | Config render element, if `false` will not create DOM node | ComponentType \| false | div | 5.11.0 | × |
| message | Global config for Message | [MessageConfig](/components/message/#messageconfig) | - | 5.3.0 | × |
| notification | Global config for Notification | [NotificationConfig](/components/notification/#notificationconfig) | - | 5.3.0 | × |

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

- Full Ant Design App docs: https://ant.design/components/app
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
