# Dropdown

**Library:** Ant Design v5  
**Category:** Navigation  
**Docs:** https://ant.design/components/dropdown

---

## Overview

A dropdown list.

### When to use

When there are more than a few options to choose from, you can wrap them in a `Dropdown`. By hovering or clicking on the trigger, a dropdown menu will appear, which allows you to choose an option and execute the relevant action.

---

## Import

```js
import { Dropdown } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

### Dropdown

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| arrow | Whether the dropdown arrow should be visible | boolean \| { pointAtCenter: boolean } | false |  | × |
| autoAdjustOverflow | Whether to adjust dropdown placement automatically when dropdown is off screen | boolean | true | 5.2.0 | × |
| classNames | Customize class for each semantic structure inside the Dropdown component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props }) => Record<[SemanticDOM](#semantic-dom), string> | - |  | 6.0.0 |
| disabled | Whether the dropdown menu is disabled | boolean | - |  | × |
| ~~destroyPopupOnHide~~ | Whether destroy dropdown when hidden, use `destroyOnHidden` instead | boolean | false |  | × |
| destroyOnHidden | Whether destroy dropdown when hidden | boolean | false | 5.25.0 | × |
| ~~dropdownRender~~ | Customize dropdown content, use `popupRender` instead | (menus: ReactNode) => ReactNode | - | 4.24.0 | × |
| popupRender | Customize popup content | (menus: ReactNode) => ReactNode | - | 5.25.0 | × |
| getPopupContainer | To set the container of the dropdown menu. The default is to create a div element in body, but you can reset it to the scrolling area and make a relative reposition. [Example on CodePen](https://codepen.io/afc163/pen/zEjNOy?editors=0010) | (triggerNode: HTMLElement) => HTMLElement | () => document.body |  | × |
| menu | The menu props | [MenuProps](/components/menu/#api) | - |  | × |
| ~~overlayClassName~~ | The class name of the dropdown root element, please use `classNames.root` instead | string | - |  | × |
| ~~overlayStyle~~ | The style of the dropdown root element, please use `styles.root` instead | CSSProperties | - |  | × |
| placement | Placement of popup menu: `bottom` `bottomLeft` `bottomRight` `top` `topLeft` `topRight` | string | `bottomLeft` |  | × |
| styles | Customize inline style for each semantic structure inside the Dropdown component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), CSSProperties> \| (info: { props }) => Record<[SemanticDOM](#semantic-dom), CSSProperties> | - |  | 6.0.0 |
| trigger | The trigger mode which executes the dropdown action. Note that hover can't be used on touchscreens | Array&lt;`click`\|`hover`\|`contextMenu`> | \[`hover`] |  | × |
| open | Whether the dropdown menu is currently open | boolean | - |  | × |
| onOpenChange | Called when the open state is changed. Not trigger when hidden by click item | (open: boolean, info: { source: 'trigger' \| 'menu' }) => void | - | `info.source`: 5.11.0 | × |

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

- Full Ant Design Dropdown docs: https://ant.design/components/dropdown
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
