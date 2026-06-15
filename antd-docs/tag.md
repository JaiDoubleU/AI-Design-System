# Tag

**Library:** Ant Design v5  
**Category:** Data Display  
**Docs:** https://ant.design/components/tag

---

## Overview

Used for marking and categorization.

### When to use

- It can be used to tag by dimension or property.

- When categorizing.

---

## Import

```js
import { Tag } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

### Tag

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), string> | - |  | 6.0.0 |
| closeIcon | Custom close icon. 5.7.0: close button will be hidden when setting to `null` or `false` | ReactNode | false | 4.4.0 | 5.14.0 |
| color | Color of the Tag | string | `default` when `variant="solid"` | `solid` default color: 6.4.0 | × |
| disabled | Whether the tag is disabled | boolean | false | 6.0.0 | × |
| href | The address to jump when clicking, when this property is specified, the `tag` component will be rendered as an `<a>` tag | string | - | 6.0.0 | × |
| icon | Set the icon of tag | ReactNode | - |  | × |
| onClose | Callback executed when tag is closed (can be prevented by `e.preventDefault()`) | (e: React.MouseEvent

---

## AI Design System token mapping

When using this component with the AI Design System adapter, these
`--ds-*` hooks drive the component's appearance:

```
--ds-bg-muted, --ds-border, --ds-text-subtle
```

Adapter file: `lib-adapters/ant-design.css`  
Adapter spec: `specs/adapters/ant-design.md`

---

## Notes

- Full Ant Design Tag docs: https://ant.design/components/tag
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
