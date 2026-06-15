# Divider

**Library:** Ant Design v5  
**Category:**   
**Docs:** https://ant.design/components/divider

---

## Overview

A divider line separates different content.

### When to use

- Divide sections of an article.
- Divide inline text and links such as the operation column of table.

---

## Import

```js
import { Divider } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| children | The wrapped title | ReactNode | - |  | × |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), string> | - |  | 6.0.0 |
| dashed | Whether line is dashed | boolean | false |  | × |
| orientation | Whether line is horizontal or vertical | `horizontal` \| `vertical` | `horizontal` | - | × |
| ~~orientationMargin~~ | The margin-left/right between the title and its closest border, while the `titlePlacement` should not be `center`, If a numeric value of type `string` is provided without a unit, it is assumed to be in pixels (px) by default. | string \| number | - |  | × |
| plain | Divider text show as plain style | boolean | false | 4.2.0 | × |
| styles | Customize inline style for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), CSSProperties> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), CSSProperties> | - |  | 6.0.0 |
| size | The size of divider. Only valid for horizontal layout | `small` \| `medium` \| `large` | - | 5.25.0 | × |
| titlePlacement | The position of title inside divider | `start` \| `end` \| `center` | `center` | - | × |
| ~~type~~ | The direction type of divider | `horizontal` \| `vertical` | `horizontal` | - | × |
| variant | Whether line is dashed, dotted or solid | `dashed` \| `dotted` \| `solid` | solid | 5.20.0 | × |
| vertical | Orientation, Simultaneously configure with `orientation` and prioritize `orientation` | boolean | false | - | × |

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

- Full Ant Design Divider docs: https://ant.design/components/divider
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
