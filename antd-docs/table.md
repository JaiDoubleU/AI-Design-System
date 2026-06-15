# Table

**Library:** Ant Design v5  
**Category:** Data Display  
**Docs:** https://ant.design/components/table

---

## Overview

A table displays rows of data.

### When to use

- To display a collection of structured data.
- To sort, search, paginate, filter data.

---

## Import

```js
import { Table } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

### Table

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| bordered | Whether to show all table borders | boolean | false |  | × |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), string> | - |  | 6.0.1 |
| column | Shared props applied to columns when the same property is not defined on the column itself | Partial<[ColumnType](#column)> | - | 6.4.0 | × |
| columns | Columns of table | [ColumnsType](#column)\[] | - |  | × |
| components | Override default table elements | [TableComponents](https://github.com/react-component/table/blob/75ee0064e54a4b3215694505870c9d6c817e9e4a/src/interface.ts#L129) | - |  | × |
| dataSource | Data record array to be displayed | object\[] | - |  | × |
| expandable | Config expandable content | [expandable](#expandable) | - |  | `expandable.expandIcon`: 5.14.0 |
| footer | Table footer renderer | function(currentPageData) | - |  | × |
| getPopupContainer | The render container of dropdowns in table | (triggerNode) => HTMLElement | () => TableHtmlElement |  | × |
| loading | Loading status of table | boolean \| [Spin Props](/components/spin/#api) | false |  | × |
| locale | The i18n text including filter, sort, empty text, etc | object | [Default Value](https://github.com/ant-design/ant-design/blob/6dae4a7e18ad1ba193aedd5ab6867e1d823e2aa4/components/locale/en_US.tsx#L19-L37) |  | × |
| pagination | Config of pagination. You can ref table pagination [config](#pagination) or full [`pagination`](/components/pagination/) document, hide it by setting it to `false` | object \| `false` | - |  | × |
| rowClassName | Row's className | function(record, index): string | - |  | × |
| rowKey | Row's unique key, could be a string or function that returns a string | string \| function(record): string | `key` |  | `string`: 6.0.0, `function`: 6.1.0 |
| rowSelection | Row selection [config](#rowselection) | object | - |  | × |
| rowHoverable | Row hover | boolean | true | 5.16.0 | × |
| scroll | Whether the table can be scrollable, [config](#scroll) | object | - |  | 6.3.0 |
| showHeader | Whether to show table header | boolean | true |  | × |
| showSorterTooltip | The header show next sorter direction tooltip. It will be set as the property of Tooltip if its type is object | boolean \| [Tooltip props](/components/tooltip/#api) & `{target?: 'full-header' \| 'sorter-icon' }` | { target: 'full-header' } | 5.16.0 | × |
| size | Size of table | `large` \| `medium` \| `small` | `large` |  | × |
| sortDirections | Supported sort way, could be `ascend`, `descend` | Array | \[`ascend`, `descend`] |  | × |
| sticky | Set sticky header and scroll bar | boolean \| `{offsetHeader?: number, offsetScroll?: number, getContainer?: () => HTMLElement}` | - | 4.6.0 (getContainer: 4.7.0) | × |
| styles | Customize inline style for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), CSSProperties> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), CSSProperties> | - |  | 6.0.1 |
| summary | Summary content | (currentData) => ReactNode | - |  | × |
| tableLayout | The [table-layout](https://developer.mozilla.org/en-US/docs/Web/CSS/table-layout) attribute of table element | - \| `auto` \| `fixed` | -<hr />`fixed` when header/columns are fixed, or using `column.ellipsis` |  | × |
| title | Table title renderer | function(currentPageData) | - |  | × |
| virtual | Support virtual list | boolean | - | 5.9.0 | × |
| onChange | Callback executed when pagination, filters or sorter is changed | function(pagination, filters, sorter, extra: { currentDataSource: \[], action: `paginate` \| `sort` \| `filter` }) | - |  | × |
| onHeaderRow | Set props on per header row | function(columns, index) | - |  | × |
| onRow | Set props on per row | function(record, index) | - |  | × |
| onScroll | Triggered when the table body is scrolled. Note that only vertical scrolling will trigger the event when `virtual` | function(event) | - | 5.16.0 | × |

### Table ref

| Property | Description | Type | Version |
| --- | --- | --- | --- |
| nativeElement | The wrap element | HTMLDivElement | 5.11.0 |
| scrollTo | Trigger to scroll to target position. `key` match with record `rowKey`. When `offset` is specified, the table will scroll to align the target row to the top with the given offset and not working with `top`. Optional `align` param to control alignment: `start` align to top, `center` align to center, `end` align to bottom, `nearest` smart align (default). `center` align is not supported in virtual scrolling mode | (config: { index?: number, key?: React.Key, top?: number, offset?: number, align?: 'start' \| 'center' \| 'end' \| 'nearest' }) => void | 5.11.0 |

#### onRow usage

Same as `onRow` `onHeaderRow` `onCell` `onHeaderCell`

```jsx

  </>
);

export default Demo;
```

Here is the [CodeSandbox for TypeScript](https://codesandbox.io/s/serene-platform-0jo5t).

---

## AI Design System token mapping

When using this component with the AI Design System adapter, these
`--ds-*` hooks drive the component's appearance:

```
--ds-border, --ds-bg-subtle (stripe), --ds-interactive (sort)
```

Adapter file: `lib-adapters/ant-design.css`  
Adapter spec: `specs/adapters/ant-design.md`

---

## Notes

- Full Ant Design Table docs: https://ant.design/components/table
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
