# QRCode

**Library:** Ant Design v5  
**Category:**   
**Docs:** https://ant.design/components/qr-code

---

## Overview

Components that can convert text into QR codes, and support custom color and logo.

### When to use

Used when the text needs to be converted into a QR Code.

---

## Import

```js
import { QRCode } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

> This component is available since `antd@5.1.0`

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| :-- | :-- | :-- | :-- | :-- | --- |
| value | scanned text | `string \| string[]` | - | `string[]`: 5.28.0 | × |
| type | render type | `canvas \| svg` | `canvas` | 5.6.0 | × |
| icon | include image url (only image link are supported) | string | - | - | × |
| size | QRCode size | number | 160 | - | × |
| iconSize | include image size | number \| { width: number; height: number } | 40 | 5.19.0 | × |
| color | QRCode Color | string | `#000` | - | × |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), string> | - | 6.0.0 | 6.0.0 |
| bgColor | QRCode Background Color | string | `transparent` | 5.5.0 | × |
| marginSize | Quiet zone size (in modules). `0` means no margin | number | `0` | 6.2.0 | × |
| bordered | Whether has border style | boolean | true | - | × |
| errorLevel | Error Code Level | `'L' \| 'M' \| 'Q' \| 'H'` | `M` | - | × |
| boostLevel | If enabled, the Error Correction Level of the result may be higher than the specified Error Correction Level | `boolean` | true | 5.28.0 | × |
| status | QRCode status | `active \| expired \| loading \| scanned` | `active` | scanned: 5.13.0 | × |
| statusRender | custom status render | (info: [StatusRenderInfo](/components/qr-code#statusrenderinfo)) => React.ReactNode | - | 5.20.0 | × |
| styles | Customize inline style for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), CSSProperties> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), CSSProperties> | - | 6.0.0 | 6.0.0 |

### StatusRenderInfo

```typescript
type StatusRenderInfo = {
  status: QRStatus;
  locale: Locale['QRCode'];
  onRefresh?: () => void;
};
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

- Full Ant Design QRCode docs: https://ant.design/components/qr-code
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
