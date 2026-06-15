# Layout

**Library:** Ant Design v5  
**Category:** Layout  
**Docs:** https://ant.design/components/layout

---

## Overview

Handling the overall layout of a page.

### When to use

The first level navigation is left aligned near a logo, and the secondary menu is right aligned.

---

## Import

```js
import { Layout } from 'antd';  // Layout.Header, Layout.Content, Layout.Sider, Layout.Footer
```

---

## Props / API

```jsx

  
    
    
  </Layout>
  
</Layout>
```

### Layout

Common props ref：[Common props](/docs/react/common-props)

The wrapper.

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| hasSider | Whether contain Sider in children, don't have to assign it normally. Useful in ssr avoid style flickering | boolean | - |  | × |

### Layout.Sider

The sidebar.

| Property | Description | Type | Default | Version |
| --- | --- | --- | --- | --- |
| breakpoint | [Breakpoints](/components/grid/#col) of the responsive layout | `xs` \| `sm` \| `md` \| `lg` \| `xl` \| `xxl` \| `xxxl` | - | xxxl: 6.3.0 |
| collapsed | To set the current status | boolean | - |  |
| collapsedWidth | Width of the collapsed sidebar, by setting to 0 a special trigger will appear | number | 80 |  |
| collapsible | Whether can be collapsed | boolean | false |  |
| defaultCollapsed | To set the initial status | boolean | false |  |
| reverseArrow | Reverse direction of arrow, for a sider that expands from the right | boolean | false |  |
| theme | Color theme of the sidebar | `light` \| `dark` | `dark` |  |
| trigger | Specify the customized trigger, set to null to hide the trigger | ReactNode | - |  |
| width | Width of the sidebar | number \| string | 200 |  |
| zeroWidthTriggerStyle | To customize the styles of the special trigger that appears when `collapsedWidth` is 0 | object | - |  |
| onBreakpoint | The callback function, executed when [breakpoints](/components/grid/#api) changed | (broken) => {} | - |  |
| onCollapse | The callback function, executed by clicking the trigger or activating the responsive layout | (collapsed, type) => {} | - |  |

#### breakpoint width

```js
{
  xs: '480px',
  sm: '576px',
  md: '768px',
  lg: '992px',
  xl: '1200px',
  xxl: '1600px',
  xxxl: '1920px',
}
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

- Full Ant Design Layout docs: https://ant.design/components/layout
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
