# Menu

**Library:** Ant Design v5  
**Category:** Navigation  
**Docs:** https://ant.design/components/menu

---

## Overview

A versatile menu for navigation.

### When to use

Navigation is an important part of any website, as a good navigation setup allows users to move around the site quickly and efficiently. Ant Design offers two navigation options: top and side. Top navigation provides all the categories and functions of the website. Side navigation provides the multi-level structure of the website.

More layouts with navigation: [Layout](/components/layout).

---

## Import

```js
import { Menu } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

### Menu

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props }) => Record<[SemanticDOM](#semantic-dom), string> | - |  | 6.0.0 |
| defaultOpenKeys | Array with the keys of default opened sub menus | string\[] | - |  | × |
| defaultSelectedKeys | Array with the keys of default selected menu items | string\[] | - |  | × |
| expandIcon | custom expand icon of submenu | ReactNode \| `(props: SubMenuProps & { isSubMenu: boolean }) => ReactNode` | - | 4.9.0 | 5.15.0 |
| forceSubMenuRender | Render submenu into DOM before it becomes visible | boolean | false |  | × |
| inlineCollapsed | Specifies the collapsed status when menu is inline mode | boolean | - |  | × |
| inlineIndent | Indent (in pixels) of inline menu items on each level | number | 24 |  | × |
| items | Menu item content | [ItemType\[\]](#itemtype) | - | 4.20.0 | × |
| mode | Type of menu | `vertical` \| `horizontal` \| `inline` | `vertical` |  | × |
| multiple | Allows selection of multiple items | boolean | false |  | × |
| openKeys | Array with the keys of currently opened sub-menus | string\[] | - |  | × |
| overflowedIndicator | Customized the ellipsis icon when menu is collapsed horizontally | ReactNode | `` |  | × |
| selectable | Allows selecting menu items | boolean | true |  | × |
| selectedKeys | Array with the keys of currently selected menu items | string\[] | - |  | × |
| styles | Customize inline style for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), CSSProperties> \| (info: { props }) => Record<[SemanticDOM](#semantic-dom), CSSProperties> | - |  | 6.0.0 |
| subMenuCloseDelay | Delay time to hide submenu when mouse leaves (in seconds) | number | 0.1 |  | × |
| subMenuOpenDelay | Delay time to show submenu when mouse enters, (in seconds) | number | 0 |  | × |
| tooltip | Config tooltip props for menu items in inline collapsed mode. Set to `false` to disable. | false \| TooltipProps | - | 6.3.0 | × |
| theme | Color theme of the menu | `light` \| `dark` | `light` |  | × |
| triggerSubMenuAction | Which action can trigger submenu open/close | `hover` \| `click` | `hover` |  | × |
| onClick | Called when a menu item is clicked | function({ key, keyPath, domEvent }) | - |  | × |
| onDeselect | Called when a menu item is deselected (multiple mode only) | function({ key, keyPath, selectedKeys, domEvent }) | - |  | × |
| onOpenChange | Called when sub-menus are opened or closed | function(openKeys: string\[]) | - |  | × |
| onSelect | Called when a menu item is selected | function({ key, keyPath, selectedKeys, domEvent }) | - |  | × |
| popupRender | Custom popup renderer for submenu | (node: ReactElement, props: { item: SubMenuProps; keys: string[] }) => ReactElement | - |  | × |

> More options in [@rc-component/menu](https://github.com/react-component/menu#api)

### ItemType

> type ItemType = [MenuItemType](#menuitemtype) | [SubMenuType](#submenutype) | [MenuItemGroupType](#menuitemgrouptype) | [MenuDividerType](#menudividertype);

#### MenuItemType

| Property | Description                          | Type      | Default | Version |
| -------- | ------------------------------------ | --------- | ------- | ------- |
| danger   | Display the danger style             | boolean   | false   |         |
| disabled | Whether menu item is disabled        | boolean   | false   |         |
| extra    | The extra of the menu item           | ReactNode | -       | 5.21.0  |
| icon     | The icon of the menu item            | ReactNode | -       |         |
| key      | Unique ID of the menu item           | string    | -       |         |
| label    | Menu label                           | ReactNode | -       |         |
| title    | Set display title for collapsed item | string    | -       |         |

#### SubMenuType

<!-- prettier-ignore -->
| Property | Description | Type | Default | Version |
| --- | --- | --- | --- | --- |
| children | Sub-menus or sub-menu items | [ItemType\[\]](#itemtype) | - |  |
| disabled | Whether sub-menu is disabled | boolean | false |  |
| icon | Icon of sub menu | ReactNode | - |  |
| key | Unique ID of the sub-menu | string | - |  |
| label | Menu label | ReactNode | - |  |
| popupClassName | Sub-menu class name, not working when `mode="inline"` | string | - |  |
| popupOffset | Sub-menu offset, not working when `mode="inline"` | \[number, number] | - |  |
| theme | Color theme of the SubMenu (inherits from Menu by default) | `light` \| `dark` | - |  |
| onTitleClick | Callback executed when the sub-menu title is clicked | function({ key, domEvent }) | - |  |
| popupRender | Custom popup renderer for current sub-menu | (node: ReactElement, props: { item: SubMenuProps; keys: string[] }) => ReactElement | - |  |

#### MenuItemGroupType

Define `type` as `group` to make as group:

```ts
const groupItem = {
  type: 'group', // Must have
  label: 'My Group',
  children: [],
};
```

| Property | Description            | Type                              | Default | Version |
| -------- | ---------------------- | --------------------------------- | ------- | ------- |
| children | Sub-menu items         | [MenuItemType\[\]](#menuitemtype) | -       |         |
| label    | The title of the group | ReactNode                         | -       |         |

#### MenuDividerType

Divider line in between menu items, only used in vertical popup Menu or Dropdown Menu. Need define the `type` as `divider`：

```ts
const dividerItem = {
  type: 'divider', // Must have
};
```

| Property | Description            | Type    | Default | Version |
| -------- | ---------------------- | ------- | ------- | ------- |
| dashed   | Whether line is dashed | boolean | false   |         |

---

## AI Design System token mapping

When using this component with the AI Design System adapter, these
`--ds-*` hooks drive the component's appearance:

```
--ds-interactive (selected), --ds-bg-subtle (hover)
```

Adapter file: `lib-adapters/ant-design.css`  
Adapter spec: `specs/adapters/ant-design.md`

---

## Notes

- Full Ant Design Menu docs: https://ant.design/components/menu
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
