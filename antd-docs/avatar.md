# Avatar

**Library:** Ant Design v5  
**Category:**   
**Docs:** https://ant.design/components/avatar

---

## Overview

Used to represent users or things, supporting the display of images, icons, or characters.

---

## Import

```js
import { Avatar } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

### Avatar

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| alt | This attribute defines the alternative text describing the image | string | - |  | × |
| gap | Letter type unit distance between left and right sides | number | 4 | 4.3.0 | × |
| icon | Custom icon type for an icon avatar | ReactNode | - |  | × |
| shape | The shape of avatar | `circle` \| `square` | `circle` |  | × |
| size | The size of the avatar | number \| `large` \| `medium` \| `small` \| { xs: number, sm: number, ...} | `medium` | 4.7.0 | × |
| src | The address of the image for an image avatar or image element | string \| ReactNode | - | ReactNode: 4.8.0 | × |
| srcSet | A list of sources to use for different screen resolutions | string | - |  | × |
| draggable | Whether the picture is allowed to be dragged | boolean \| `'true'` \| `'false'` | true |  | × |
| crossOrigin | CORS settings attributes | `'anonymous'` \| `'use-credentials'` \| `''` | - | 4.17.0 | × |
| onError | Handler when img load error, return false to prevent default fallback behavior | () => boolean | - |  | × |

> Tip: You can set `icon` or `children` as the fallback for image load error, with the priority of `icon` > `children`

### Avatar.Group 

| Property | Description | Type | Default | Version |
| --- | --- | --- | --- | --- |
| max | Set maximum display related configurations | `{ count?: number; style?: CSSProperties; popover?: PopoverProps }` | - | 5.18.0 |
| ~~maxCount~~ | Deprecated, please use `max={{ count: number }}` | number | - |  |
| ~~maxPopoverPlacement~~ | Deprecated, please use `max={{ popover: PopoverProps }}` | `top` \| `bottom` | `top` |  |
| ~~maxPopoverTrigger~~ | Deprecated, please use `max={{ popover: PopoverProps }}` | `hover` \| `focus` \| `click` | `hover` |  |
| ~~maxStyle~~ | Deprecated, please use `max={{ style: CSSProperties }}` | CSSProperties | - |  |
| size | The size of the avatar | number \| `large` \| `medium` \| `small` \| { xs: number, sm: number, ...} | `medium` | 4.8.0 |
| shape | The shape of the avatar | `circle` \| `square` | `circle` | 5.8.0 |

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

- Full Ant Design Avatar docs: https://ant.design/components/avatar
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
