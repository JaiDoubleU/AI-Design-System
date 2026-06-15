# Typography

**Library:** Ant Design v5  
**Category:** General  
**Docs:** https://ant.design/components/typography

---

## Overview

Basic text writing, including headings, body text, lists, and more.

### When to use

- When you need to display a title or paragraph contents in Articles/Blogs/Notes.
- When you need copyable/editable/ellipsis texts.

---

## Import

```js
import { Typography } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

### Typography.Text

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| actions | Configure the operation bar | [actions](#actions) | - | 6.4.0 | × |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), string> | - | 6.4.0 | 6.4.0 |
| code | Code style | boolean | false |  | × |
| copyable | Whether to be copyable, customize it via setting an object | boolean \| [copyable](#copyable) | false |  | × |
| delete | Deleted line style | boolean | false |  | × |
| disabled | Disabled content | boolean | false |  | × |
| editable | If editable. Can control edit state when is object | boolean \| [editable](#editable) | false |  | × |
| ellipsis | Display ellipsis when text overflows, can't configure expandable, rows and onExpand by using object. Diff with Typography.Paragraph, Text do not have 100% width style which means it will fix width on the first ellipsis. If you want to have responsive ellipsis, please set width manually | boolean \| [Omit<ellipsis, 'expandable' \| 'rows' \| 'onExpand'>](#ellipsis) | false |  | × |
| italic | Italic style | boolean | false | 4.16.0 | × |
| keyboard | Keyboard style | boolean | false | 4.3.0 | × |
| mark | Marked style | boolean | false |  | × |
| strong | Bold style | boolean | false |  | × |
| styles | Customize inline style for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), CSSProperties> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), CSSProperties> | - | 6.4.0 | 6.4.0 |
| type | Content type | `secondary` \| `success` \| `warning` \| `danger` | - | success: 4.6.0 | × |
| underline | Underlined style | boolean | false |  | × |
| onClick | Set the handler to handle click event | (event) => void | - |  | × |

### Typography.Title

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| actions | Configure the operation bar | [actions](#actions) | - | 6.4.0 | × |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), string> | - | 6.4.0 | 6.4.0 |
| code | Code style | boolean | false |  | × |
| copyable | Whether to be copyable, customize it via setting an object | boolean \| [copyable](#copyable) | false |  | × |
| delete | Deleted line style | boolean | false |  | × |
| disabled | Disabled content | boolean | false |  | × |
| editable | If editable. Can control edit state when is object | boolean \| [editable](#editable) | false |  | × |
| ellipsis | Display ellipsis when text overflows, can configure rows and expandable by using object | boolean \| [ellipsis](#ellipsis) | false |  | × |
| italic | Italic style | boolean | false | 4.16.0 | × |
| level | Set content importance. Match with `h1`, `h2`, `h3`, `h4`, `h5` | number: 1, 2, 3, 4, 5 | 1 | 5: 4.6.0 | × |
| mark | Marked style | boolean | false |  | × |
| styles | Customize inline style for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), CSSProperties> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), CSSProperties> | - | 6.4.0 | 6.4.0 |
| type | Content type | `secondary` \| `success` \| `warning` \| `danger` | - | success: 4.6.0 | × |
| underline | Underlined style | boolean | false |  | × |
| onClick | Set the handler to handle click event | (event) => void | - |  | × |

### Typography.Paragraph

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| actions | Configure the operation bar | [actions](#actions) | - | 6.4.0 | × |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), string> | - | 6.4.0 | 6.4.0 |
| code | Code style | boolean | false |  | × |
| copyable | Whether to be copyable, customize it via setting an object | boolean \| [copyable](#copyable) | false |  | × |
| delete | Deleted line style | boolean | false |  | × |
| disabled | Disabled content | boolean | false |  | × |
| editable | If editable. Can control edit state when is object | boolean \| [editable](#editable) | false |  | × |
| ellipsis | Display ellipsis when text overflows, can configure rows and expandable by using object | boolean \| [ellipsis](#ellipsis) | false |  | × |
| italic | Italic style | boolean | false | 4.16.0 | × |
| mark | Marked style | boolean | false |  | × |
| strong | Bold style | boolean | false |  | × |
| styles | Customize inline style for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), CSSProperties> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), CSSProperties> | - | 6.4.0 | 6.4.0 |
| type | Content type | `secondary` \| `success` \| `warning` \| `danger` | - | success: 4.6.0 | × |
| underline | Underlined style | boolean | false |  | × |
| onClick | Set the handler to handle click event | (event) => void | - |  | × |

### actions

    {
      placement: 'start' | 'end',
    }

| Property | Description | Type | Default | Version |
| --- | --- | --- | --- | --- |
| placement | Set the operation bar placement relative to the text | `start` \| `end` | `end` | 6.4.0 |

### copyable

    {
      text: string | (() => string | Promise<string>),
      onCopy: function(event),
      icon: ReactNode,
      tooltips: false | [ReactNode, ReactNode],
      format: 'text/plain' | 'text/html',
      tabIndex: number,
    }

| Property | Description | Type | Default | Version |
| --- | --- | --- | --- | --- |
| format | The Mime Type of the text | 'text/plain' \| 'text/html' | - | 4.21.0 |
| icon | Custom copy icon: \[copyIcon, copiedIcon] | \[ReactNode, ReactNode] | - | 4.6.0 |
| tabIndex | Set tabIndex of the copy button | number | 0 | 5.17.0 |
| text | The text to copy | string | - |  |
| tooltips | Custom tooltip text, hide when it is false | \[ReactNode, ReactNode] | \[`Copy`, `Copied`] | 4.4.0 |
| onCopy | Called when copied text | function | - |  |

### editable

    {
      icon: ReactNode,
      tooltip: ReactNode,
      editing: boolean,
      maxLength: number,
      autoSize: boolean | { minRows: number, maxRows: number },
      text: string,
      onChange: function(string),
      onCancel: function,
      onStart: function,
      onEnd: function,
      triggerType: ('icon' | 'text')[],
      enterIcon: ReactNode,
      tabIndex: number,
    }

| Property | Description | Type | Default | Version |
| --- | --- | --- | --- | --- |
| autoSize | `autoSize` attribute of textarea | boolean \| { minRows: number, maxRows: number } | - | 4.4.0 |
| editing | Whether to be editable | boolean | false |  |
| enterIcon | Custom "enter" icon in the edit field (passing `null` removes the icon) | ReactNode | `` | 4.17.0 |
| icon | Custom editable icon | ReactNode | &lt;EditOutlined /> | 4.6.0 |
| maxLength | `maxLength` attribute of textarea | number | - | 4.4.0 |
| tabIndex | Set tabIndex of the edit button | number | 0 | 5.17.0 |
| text | Edit text, specify the editing content instead of using the children implicitly | string | - | 4.24.0 |
| tooltip | Custom tooltip text, hide when it is false | ReactNode | `Edit` | 4.6.0 |
| triggerType | Edit mode trigger - icon, text or both (not specifying icon as trigger hides it) | Array&lt;`icon`\|`text`> | \[`icon`] |  |
| onCancel | Called when type ESC to exit editable state | function | - |  |
| onChange | Called when input at textarea | function(value: string) | - |  |
| onEnd | Called when type ENTER to exit editable state | function | - | 4.14.0 |
| onStart | Called when enter editable state | function | - |  |

### ellipsis

```tsx
interface EllipsisConfig {
  rows: number;
  /** `collapsible` added in `5.16.0` */
  expandable: boolean | 'collapsible';
  suffix: string;
  /** render function added in `5.16.0` */
  symbol: ReactNode | ((expanded: boolean) => ReactNode);
  tooltip: ReactNode | TooltipProps;
  /** added in `5.16.0` */
  defaultExpanded: boolean;
  /** added in `5.16.0` */
  expanded: boolean;
  /** `info` added in `5.16.0` */
  onExpand: (event: MouseEvent, info: { expanded: boolean }) => void;
  onEllipsis: (ellipsis: boolean) => void;
}
```

| Property | Description | Type | Default | Version |
| --- | --- | --- | --- | --- |
| defaultExpanded | Default expand or collapse | boolean |  | 5.16.0 |
| expandable | Whether to be expandable | boolean \| 'collapsible' | - | `collapsible`: 5.16.0 |
| expanded | Expand or Collapse | boolean |  | 5.16.0 |
| rows | Max rows of content | number | - |  |
| suffix | Suffix of ellipsis content | string | - |  |
| symbol | Custom description of ellipsis | ReactNode \| ((expanded: boolean) => ReactNode) | `Expand` `Collapse` |  |
| tooltip | Show tooltip when ellipsis | ReactNode \| [TooltipProps](/components/tooltip/#api) | - | 4.11.0 |
| onEllipsis | Called when enter or leave ellipsis state | function(ellipsis) | - | 4.2.0 |
| onExpand | Called when expand content | function(event, { expanded: boolean }) | - | `info`: 5.16.0 |

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

- Full Ant Design Typography docs: https://ant.design/components/typography
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
