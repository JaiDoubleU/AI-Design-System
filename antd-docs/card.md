# Card

**Library:** Ant Design v5  
**Category:** Data Display  
**Docs:** https://ant.design/components/card

---

## Overview

A container for displaying information.

### When to use

A card can be used to display content related to a single subject. The content can consist of multiple elements of varying types and sizes.

---

## Import

```js
import { Card } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

```jsx

```

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| actions | The action list, shows at the bottom of the Card | Array&lt;ReactNode> | - |  | × |
| activeTabKey | Current TabPane's key | string | - |  | × |
| ~~bordered~~ | Toggles rendering of the border around the card, please use `variant` instead | boolean | true |  | × |
| ~~bodyStyle~~ | Style of card body, please use `styles.body` instead | CSSProperties | - | - | × |
| variant | Variants of Card | `outlined` \| `borderless` | `outlined` | 5.24.0 | 5.24.0 |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), string> | - |  | 5.14.0 |
| cover | Card cover | ReactNode | - |  | × |
| defaultActiveTabKey | Initial active TabPane's key, if `activeTabKey` is not set | string | `The key of first tab` |  | × |
| extra | Content to render in the top-right corner of the card | ReactNode | - |  | × |
| hoverable | Lift up when hovering card | boolean | false |  | × |
| ~~headStyle~~ | Style of card head, please use `styles.header` instead | CSSProperties | - | - | × |
| loading | Shows a loading indicator while the contents of the card are being fetched | boolean | false |  | × |
| size | Size of card | `medium` \| `small` | `medium` |  | × |
| tabBarExtraContent | Extra content in tab bar | ReactNode | - |  | × |
| tabList | List of TabPane's head | [TabItemType](/components/tabs#tabitemtype)[] | - |  | × |
| tabProps | [Tabs](/components/tabs/#tabs) | - | - |  | × |
| title | Card title | ReactNode | - |  | × |
| type | Card style type, can be set to `inner` or not set | string | - |  | × |
| styles | Customize inline style for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), CSSProperties> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), CSSProperties> | - |  | 5.14.0 |
| onTabChange | Callback when tab is switched | (key) => void | - |  | × |

### Card.Grid

| Property  | Description                     | Type    | Default | Version |
| --------- | ------------------------------- | ------- | ------- | ------- |
| hoverable | Lift up when hovering card grid | boolean | true    |         |

### Card.Meta

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| avatar | Avatar or icon | ReactNode | - |  | × |
| description | Description content | ReactNode | - |  | × |
| title | Title content | ReactNode | - |  | × |

---

## AI Design System token mapping

When using this component with the AI Design System adapter, these
`--ds-*` hooks drive the component's appearance:

```
--ds-bg, --ds-border, --ds-shadow-sm
```

Adapter file: `lib-adapters/ant-design.css`  
Adapter spec: `specs/adapters/ant-design.md`

---

## Notes

- Full Ant Design Card docs: https://ant.design/components/card
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
