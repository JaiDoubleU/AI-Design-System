# Skeleton

**Library:** Ant Design v5  
**Category:** Feedback  
**Docs:** https://ant.design/components/skeleton

---

## Overview

Provide a placeholder while you wait for content to load, or to visualize content that doesn't exist yet.

### When to use

- When a resource needs long time to load.
- When the component contains lots of information, such as List or Card.
- Only works when loading data for the first time.
- Could be replaced by Spin in any situation, but can provide a better user experience.

---

## Import

```js
import { Skeleton } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

### Common API

<embed src="./shared/sharedProps.en-US.md"></embed>

### Skeleton

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| active | Show animation effect | boolean | false |  | × |
| avatar | Show avatar placeholder | boolean \| [SkeletonAvatar](#skeletonavatar) | false |  | × |
| loading | Display the skeleton when true | boolean | - |  | × |
| paragraph | Show paragraph placeholder | boolean \| [SkeletonParagraphProps](#skeletonparagraphprops) | true |  | × |
| round | Show paragraph and title radius when true | boolean | false |  | × |
| title | Show title placeholder | boolean \| [SkeletonTitleProps](#skeletontitleprops) | true |  | × |

#### SkeletonTitleProps

| Property | Description            | Type             | Default |
| -------- | ---------------------- | ---------------- | ------- |
| width    | Set the width of title | number \| string | -       |

#### SkeletonParagraphProps

| Property | Description | Type | Default |
| --- | --- | --- | --- |
| rows | Set the row count of paragraph | number | - |
| width | Set the width of paragraph. When width is an Array, it can set the width of each row. Otherwise only set the last row width | number \| string \| Array&lt;number \| string> | - |

### Skeleton.Avatar

| Property | Description | Type | Default |
| --- | --- | --- | --- |
| active | Show animation effect, only valid when used avatar independently | boolean | false |
| shape | Set the shape of avatar | `circle` \| `square` | `circle` |
| size | Set the size of avatar | number \| `large` \| `medium` \| `small` | `medium` |

### Skeleton.Button

| Property | Description | Type | Default | Version |
| --- | --- | --- | --- | --- |
| active | Show animation effect | boolean | false |  |
| block | Option to fit button width to its parent width | boolean | false | 4.17.0 |
| shape | Set the shape of button | `circle` \| `round` \| `square` \| `default` | - |  |
| size | Set the size of button | `large` \| `medium` \| `small` | `medium` |  |

### Skeleton.Input

| Property | Description           | Type                           | Default  |
| -------- | --------------------- | ------------------------------ | -------- |
| active   | Show animation effect | boolean                        | false    |
| size     | Set the size of input | `large` \| `medium` \| `small` | `medium` |

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

- Full Ant Design Skeleton docs: https://ant.design/components/skeleton
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
