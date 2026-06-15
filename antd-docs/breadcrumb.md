# Breadcrumb

**Library:** Ant Design v5  
**Category:** Navigation  
**Docs:** https://ant.design/components/breadcrumb

---

## Overview

Display the current location within a hierarchy. And allow going back to states higher up in the hierarchy.

### When to use

- When the system has more than two layers in a hierarchy.
- When you need to inform the user of where they are.
- When the user may need to navigate back to a higher level.

---

## Import

```js
import { Breadcrumb } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

### Breadcrumb

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), string> | - | 6.0.0 | 6.0.0 |
| dropdownIcon | Custom dropdown icon | ReactNode | `` | 6.2.0 | 6.2.0 |
| items | The routing stack information of router (>=5.3.0 recommended, use `Breadcrumb.Item` children for older versions) | [ItemType\[\]](#itemtype) | - | 5.3.0 | × |
| itemRender | Custom item renderer, work with react-router, see [example](#use-with-browserhistory) | (route, params, routes, paths) => ReactNode | - |  | × |
| params | Routing parameters | object | - |  | × |
| separator | Custom separator | ReactNode | `/` |  | 6.0.0 |
| styles | Customize inline style for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), CSSProperties> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), CSSProperties> | - | 6.0.0 | 6.0.0 |

### ItemType

> type ItemType = Omit<[RouteItemType](#routeitemtype), 'title' | 'path'> | [SeparatorType](#separatortype)

### RouteItemType

| Property | Description | Type | Default | Version |
| --- | --- | --- | --- | --- |
| className | The additional css class | string | - |  |
| dropdownProps | The dropdown props | [Dropdown](/components/dropdown) | - |  |
| href | Target of hyperlink. Can not work with `path` | string | - |  |
| path | Connected path. Each path will connect with prev one. Can not work with `href` | string | - |  |
| menu | The menu props | [MenuProps](/components/menu/#api) | - | 4.24.0 |
| onClick | Set the handler to handle click event | (e:MouseEvent) => void | - |  |
| title | item name | ReactNode | - | 5.3.0 |

### SeparatorType

```ts
const item = {
  type: 'separator', // Must have
  separator: '/',
};
```

| Property  | Description       | Type        | Default | Version |
| --------- | ----------------- | ----------- | ------- | ------- |
| type      | Mark as separator | `separator` |         | 5.3.0   |
| separator | Custom separator  | ReactNode   | `/`     | 5.3.0   |

### Use with browserHistory

The link of Breadcrumb item targets `#` by default, you can use `itemRender` to make a `browserHistory` Link.

```jsx
import { Link } from 'react-router';

const items = [
  {
    path: '/index',
    title: 'home',
  },
  {
    path: '/first',
    title: 'first',
    children: [
      {
        path: '/general',
        title: 'General',
      },
      {
        path: '/layout',
        title: 'Layout',
      },
      {
        path: '/navigation',
        title: 'Navigation',
      },
    ],
  },
  {
    path: '/second',
    title: 'second',
  },
];

function itemRender(currentRoute, params, items, paths) {
  const isLast = currentRoute?.path === items[items.length - 1]?.path;

  return isLast ? (
    <span>{currentRoute.title}</span>
  ) : (
    
  );
}

return ;
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

- Full Ant Design Breadcrumb docs: https://ant.design/components/breadcrumb
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
