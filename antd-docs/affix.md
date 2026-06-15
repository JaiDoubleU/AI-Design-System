# Affix

**Library:** Ant Design v5  
**Category:**   
**Docs:** https://ant.design/components/affix

---

## Overview

Stick an element to the viewport.

### When to use

On longer web pages, it's helpful to stick component into the viewport. This is common for menus and actions.

Please note that Affix should not cover other content on the page, especially when the size of the viewport is small.

> Notes for developers
>
> After version `5.10.0`, we rewrite Affix use FC, Some methods of obtaining `ref` and calling internal instance methods will be invalid.

---

## Import

```js
import { Affix } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| offsetBottom | Offset from the bottom of the viewport (in pixels) | number | - |  | × |
| offsetTop | Offset from the top of the viewport (in pixels) | number | 0 |  | × |
| target | Specifies the scrollable area DOM node | () => Window \| HTMLElement \| null | () => window |  | × |
| onChange | Callback for when Affix state is changed | (affixed?: boolean) => void | - |  | × |

**Note:** Children of `Affix` must not have the property `position: absolute`, but you can set `position: absolute` on `Affix` itself:

```jsx

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

- Full Ant Design Affix docs: https://ant.design/components/affix
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
