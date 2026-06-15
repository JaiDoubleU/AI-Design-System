# Descriptions

**Library:** Ant Design v5  
**Category:** Data Display  
**Docs:** https://ant.design/components/descriptions

---

## Overview

Display multiple read-only fields in a group.

### When to use

Commonly displayed on the details page.

```tsx | pure
// works when >= 5.8.0, recommended ✅

const items: DescriptionsProps['items'] = [
  {
    key: '1',
    label: 'UserName',
    children: <p>Zhou Maomao</p>,
  },
  {
    key: '2',
    label: 'Telephone',
    children: <p>1810000000</p>,
  },
  {
    key: '3',
    label: 'Live',
    children: <p>Hangzhou, Zhejiang</p>,
  },
  {
    key: '4',
    label: 'Remark',
    children: <p>empty</p>,
  },
  {
    key: '5',
    label: 'Address',
    children: <p>No. 18, Wantang Road, Xihu District, Hangzhou, Zhejiang, China</p>,
  },
];

;

// works when <5.8.0 , deprecated when >=5.8.0 🙅🏻‍♀️

  
  
  
  
</Descriptions>;
```

---

## Import

```js
import { Descriptions } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

### Descriptions

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| bordered | Whether to display the border | boolean | false |  | × |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), string> | - |  | 5.23.0 |
| colon | Change default props `colon` value of Descriptions.Item. Indicates whether the colon after the label is displayed | boolean | true |  | × |
| column | The number of `DescriptionItems` in a row, could be an object (like `{ xs: 8, sm: 16, md: 24}`, but must have `bordered={true}`) or a number | number \| [Record

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

- Full Ant Design Descriptions docs: https://ant.design/components/descriptions
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
