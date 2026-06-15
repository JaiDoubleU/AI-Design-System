# ColorPicker

**Library:** Ant Design v5  
**Category:**   
**Docs:** https://ant.design/components/color-picker

---

## Overview

Used for color selection.

### When to use

Used when the user needs to make a customized color selection.

---

## Import

```js
import { ColorPicker } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

> This component is available since `antd@5.5.0`.

<!-- prettier-ignore -->
| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| :-- | :-- | :-- | :-- | :-- | --- |
| allowClear | 	Allow clearing color selected | boolean | false |  | × |
| arrow | Configuration for popup arrow | `boolean \| { pointAtCenter: boolean }` | true |  | 6.3.0 |
| children | Trigger of ColorPicker | React.ReactNode | - |  | × |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), string> | - |  | 6.0.0 |
| defaultValue | Default value of color | [ColorType](#colortype) | - |  | × |
| defaultFormat | Default format of color | `rgb` \| `hex` \| `hsb` | `hex` | 5.9.0 | × |
| disabled | Disable ColorPicker | boolean | - |  | × |
| disabledAlpha | Disable Alpha | boolean | - | 5.8.0 | × |
| disabledFormat | Disable format of color | boolean | - | 5.22.0 | × |
| ~~destroyTooltipOnHide~~ | Whether destroy dom when close | `boolean` | false | 5.7.0 | × |
| destroyOnHidden | Whether destroy dom when close | `boolean` | false | 5.25.0 | × |
| format | Format of color | `rgb` \| `hex` \| `hsb` | - |  | × |
| mode | Configure single or gradient color | `'single' \| 'gradient' \| ('single' \| 'gradient')[]` | `single` | 5.20.0 | × |
| open | Whether to show popup | boolean | - |  | × |
| presets | Preset colors | [PresetColorType](#presetcolortype) | - |  | × |
| placement | Placement of popup | The design of the [placement](/components/tooltip/#api) parameter is the same as the `Tooltips` component. | `bottomLeft` |  | × |
| panelRender | Custom Render Panel | `(panel: React.ReactNode, extra: { components: { Picker: FC; Presets: FC } }) => React.ReactNode` | - | 5.7.0 | × |
| showText | Show color text | boolean \| `(color: Color) => React.ReactNode` | - | 5.7.0 | × |
| size | Setting the trigger size | `large` \| `medium` \| `small` | `medium` | 5.7.0 | × |
| styles | Customize inline style for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), CSSProperties> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), CSSProperties> | - |  | 6.0.0 |
| trigger | ColorPicker trigger mode | `hover` \| `click` | `click` |  | × |
| value | Value of color | [ColorType](#colortype) | - |  | × |
| onChange | Callback when `value` is changed | `(value: Color, css: string) => void` | - |  | × |
| onChangeComplete | Called when color pick ends. Will not change the display color when `value` controlled by `onChangeComplete` | `(value: Color) => void` | - | 5.7.0 | × |
| onFormatChange | Callback when `format` is changed | `(format: 'hex' \| 'rgb' \| 'hsb') => void` | - |  | × |
| onOpenChange | Callback when `open` is changed | `(open: boolean) => void` | - |  | × |
| onClear | Called when clear | `() => void` | - | 5.6.0 | × |

#### ColorType

```typescript
type ColorType =
  | string
  | Color
  | {
      color: string;
      percent: number;
    }[];
```

#### PresetColorType

```typescript
type PresetColorType = {
  label: React.ReactNode;
  defaultOpen?: boolean;
  key?: React.Key;
  colors: ColorType[];
};
```

### Color

<!-- prettier-ignore -->
| Property | Description | Type | Version |
| :-- | :-- | :-- | :-- |
| toCssString | Convert to CSS support format | `() => string` | 5.20.0 |
| toHex | Convert to `hex` format characters, the return type like: `1677ff` | `() => string` | - |
| toHexString | Convert to `hex` format color string, the return type like: `#1677ff` | `() => string` | - |
| toHsb | Convert to `hsb` object  | `() => ({ h: number, s: number, b: number, a number })` | - |
| toHsbString | Convert to `hsb` format color string, the return type like: `hsb(215, 91%, 100%)` | `() => string` | - |
| toRgb | Convert to `rgb` object  | `() => ({ r: number, g: number, b: number, a number })` | - |
| toRgbString | Convert to `rgb` format color string, the return type like: `rgb(22, 119, 255)` | `() => string` | - |

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

- Full Ant Design ColorPicker docs: https://ant.design/components/color-picker
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
