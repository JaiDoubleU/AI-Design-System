# Pagination

**Library:** Ant Design v5  
**Category:** Navigation  
**Docs:** https://ant.design/components/pagination

---

## Overview

A long list can be divided into several pages, and only one page will be loaded at a time.

### When to use

- When it will take a long time to load/render all items.
- If you want to browse the data by navigating through pages.

---

## Import

```js
import { Pagination } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

```jsx

```

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| align | Align | start \| center \| end | - | 5.19.0 | × |
| classNames | Customize class for each semantic structure inside the component. Supports object or function | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props }) => Record<[SemanticDOM](#semantic-dom), string> | - |  | 6.0.0 |
| current | Current page number | number | - |  | × |
| defaultCurrent | Default initial page number | number | 1 |  | × |
| defaultPageSize | Default number of data items per page | number | 10 |  | × |
| disabled | Disable pagination | boolean | - |  | × |
| hideOnSinglePage | Whether to hide pager on single page | boolean | false |  | × |
| itemRender | To customize item's innerHTML | (page, type: 'page' \| 'prev' \| 'next', originalElement) => React.ReactNode | - |  | × |
| pageSize | Number of data items per page | number | - |  | × |
| pageSizeOptions | Specify the sizeChanger options | number\[] | \[`10`, `20`, `50`, `100`] |  | × |
| responsive | If `size` is not specified, `Pagination` would resize according to the width of the window | boolean | - |  | × |
| showLessItems | Show less page items | boolean | false |  | × |
| showQuickJumper | Determine whether you can jump to pages directly | boolean \| { goButton: ReactNode } | false |  | × |
| showSizeChanger | Determine whether to show `pageSize` select | boolean \| [SelectProps](/components/select#api) | - | SelectProps: 5.21.0 | 4.21.0, SelectProps: 5.21.0 |
| showTitle | Show page item's title | boolean | true |  | × |
| showTotal | To display the total number and range | function(total, range) | - |  | × |
| simple | Whether to use simple mode | boolean \| { readOnly?: boolean } | - |  | × |
| size | Component size | `large` \| `medium` \| `small` | `medium` |  | × |
| styles | Customize inline style for each semantic structure inside the component. Supports object or function | Record<[SemanticDOM](#semantic-dom), CSSProperties> \| (info: { props }) => Record<[SemanticDOM](#semantic-dom), CSSProperties> | - |  | 6.0.0 |
| total | Total number of data items | number | 0 |  | × |
| totalBoundaryShowSizeChanger | When `total` larger than it, `showSizeChanger` will be true | number | 50 |  | 6.2.0 |
| onChange | Called when the page number or `pageSize` is changed, and it takes the resulting page number and pageSize as its arguments | function(page, pageSize) | - |  | × |
| onShowSizeChange | Called when `pageSize` is changed | function(current, size) | - |  | × |

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

- Full Ant Design Pagination docs: https://ant.design/components/pagination
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
