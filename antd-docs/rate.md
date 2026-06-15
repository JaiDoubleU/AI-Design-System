# Rate

**Library:** Ant Design v5  
**Category:** Data Entry  
**Docs:** https://ant.design/components/rate

---

## Overview

Used for rating operation on something.

### When to use

- Show evaluation.
- A quick rating operation on something.

---

## Import

```js
import { Rate } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| allowClear | Whether to allow clear when click again | boolean | true |  | × |
| allowHalf | Whether to allow semi selection | boolean | false |  | × |
| character | The custom character of rate | ReactNode \| (RateProps) => ReactNode | &lt;StarFilled /> | function(): 4.4.0 | × |
| count | Star count | number | 5 |  | × |
| defaultValue | The default value | number | 0 |  | × |
| disabled | If read only, unable to interact | boolean | false |  | × |
| keyboard | Support keyboard operation | boolean | true | 5.18.0 | × |
| size | Star size | 'small' \| 'medium' \| 'large' | 'medium' |  | × |
| tooltips | Customize tooltip by each character | [TooltipProps](/components/tooltip#api)[] \| string\[] | - |  | × |
| value | The current value | number | - |  | × |
| onBlur | Callback when component lose focus | function() | - |  | × |
| onChange | Callback when select value | function(value: number) | - |  | × |
| onFocus | Callback when component get focus | function() | - |  | × |
| onHoverChange | Callback when hover item | function(value: number) | - |  | × |
| onKeyDown | Callback when keydown on component | function(event) | - |  | × |

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

- Full Ant Design Rate docs: https://ant.design/components/rate
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
