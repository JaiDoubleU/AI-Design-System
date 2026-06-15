# Collapse

**Library:** Ant Design v5  
**Category:** Data Display  
**Docs:** https://ant.design/components/collapse

---

## Overview

A content area which can be collapsed and expanded.

### When to use

- Can be used to group or hide complex regions to keep the page clean.
- `Accordion` is a special kind of `Collapse`, which allows only one panel to be expanded at a time.

---

## Import

```js
import { Collapse } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

### Collapse

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| accordion | If true, Collapse renders as Accordion | boolean | false |  | × |
| activeKey | Key of the active panel | string\[] \| string <br/> number\[] \| number | No default value. In [accordion mode](#collapse-demo-accordion), it's the key of the first panel |  | × |
| bordered | Toggles rendering of the border around the collapse block | boolean | true |  | × |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), string> | - |  | 6.0.0 |
| collapsible | Specify how to trigger Collapse. Either by clicking icon or by clicking any area in header or disable collapse functionality itself | `header` \| `icon` \| `disabled` | - | 4.9.0 | × |
| defaultActiveKey | Key of the initial active panel | string\[] \| string <br/> number\[] \| number | - |  | × |
| ~~destroyInactivePanel~~ | Destroy Inactive Panel | boolean | false |  | × |
| destroyOnHidden | Destroy Inactive Panel | boolean | false | 5.25.0 | × |
| expandIcon | Customize the collapse expand icon | (panelProps) => ReactNode | - |  | 5.15.0 |
| expandIconPlacement | Set expand icon placement | `start` \| `end` | `start` | - | × |
| ~~expandIconPosition~~ | Set expand icon position, Please use `expandIconPlacement` instead | `start` \| `end` | - | 4.21.0 | × |
| ghost | Make the collapse borderless and its background transparent | boolean | false | 4.4.0 | × |
| size | Set the size of collapse | `large` \| `medium` \| `small` | `medium` | 5.2.0 | × |
| styles | Customize inline style for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), CSSProperties> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), CSSProperties> | - |  | 6.0.0 |
| onChange | Callback function executed when active panel is changed | function | - |  | × |
| items | collapse items content | [ItemType](#itemtype) | - | 5.6.0 | × |

### ItemType

| Property | Description | Type | Default | Version |
| --- | --- | --- | --- | --- |
| classNames | Semantic structure className | [`Record<header \| body, string>`](#semantic-dom) | - | 5.21.0 |
| collapsible | Specify whether the panel be collapsible or the trigger area of collapsible | `header` \| `icon` \| `disabled` | - |  |
| children | Body area content | ReactNode | - |  |
| extra | The extra element in the corner | ReactNode | - |  |
| forceRender | Forced render of content on panel, instead of lazy rendering after clicking on header | boolean | false |  |
| key | Unique key identifying the panel from among its siblings | string \| number | - |  |
| label | Title of the panel | ReactNode | - | - |
| showArrow | If false, panel will not show arrow icon. If false, collapsible can't be set as icon | boolean | true |  |
| styles | Semantic DOM style | [`Record<header \| body, CSSProperties>`](#semantic-dom) | - | 5.21.0 |

### Collapse.Panel

<!-- prettier-ignore -->
:::warning{title=Deprecated}
When using version >= 5.6.0, we prefer to configuring the panel by `items`.
:::

| Property | Description | Type | Default | Version |
| --- | --- | --- | --- | --- |
| collapsible | Specify whether the panel be collapsible or the trigger area of collapsible | `header` \| `icon` \| `disabled` | - | 4.9.0 (icon: 4.24.0) |
| extra | The extra element in the corner | ReactNode | - |  |
| forceRender | Forced render of content on panel, instead of lazy rendering after clicking on header | boolean | false |  |
| header | Title of the panel | ReactNode | - |  |
| key | Unique key identifying the panel from among its siblings | string \| number | - |  |
| showArrow | If false, panel will not show arrow icon. If false, collapsible can't be set as icon | boolean | true |  |

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

- Full Ant Design Collapse docs: https://ant.design/components/collapse
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
