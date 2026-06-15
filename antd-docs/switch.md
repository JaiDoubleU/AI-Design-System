# Switch

**Library:** Ant Design v5  
**Category:** Data Entry  
**Docs:** https://ant.design/components/switch

---

## Overview

Used to toggle between two states.

### When to use

- If you need to represent the switching between two states or on-off state.
- The difference between `Switch` and `Checkbox` is that `Switch` will trigger a state change directly when you toggle it, while `Checkbox` is generally used for state marking, which should work in conjunction with submit operation.

---

## Import

```js
import { Switch } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| checked | Determine whether the Switch is checked | boolean | false |  | × |
| checkedChildren | The content to be shown when the state is checked | ReactNode | - |  | × |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), string> | - |  | 6.0.0 |
| defaultChecked | Whether to set the initial state | boolean | false |  | × |
| defaultValue | Alias for `defaultChecked` | boolean | - | 5.12.0 | × |
| disabled | Disable switch | boolean | false |  | × |
| loading | Loading state of switch | boolean | false |  | × |
| size | The size of the Switch, options: `medium` `small` | string | `medium` |  | × |
| styles | Customize inline style for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), CSSProperties> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), CSSProperties> | - |  | 6.0.0 |
| unCheckedChildren | The content to be shown when the state is unchecked | ReactNode | - |  | × |
| value | Alias for `checked` | boolean | - | 5.12.0 | × |
| onChange | Trigger when the checked state is changing | function(checked: boolean, event: Event) | - |  | × |
| onClick | Trigger when clicked | function(checked: boolean, event: Event) | - |  | × |

---

## AI Design System token mapping

When using this component with the AI Design System adapter, these
`--ds-*` hooks drive the component's appearance:

```
--ds-interactive, --ds-bg-muted
```

Adapter file: `lib-adapters/ant-design.css`  
Adapter spec: `specs/adapters/ant-design.md`

---

## Notes

- Full Ant Design Switch docs: https://ant.design/components/switch
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
