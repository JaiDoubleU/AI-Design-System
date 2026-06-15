# Image

**Library:** Ant Design v5  
**Category:** Data Display  
**Docs:** https://ant.design/components/image

---

## Overview

Preview-able image.

### When to use

- When you need to display pictures.
- Display when loading a large image or fault tolerant handling when loading fail.

---

## Import

```js
import { Image } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

### Image

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| alt | Image description | string | - |  | × |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), string> | - |  | 6.0.0 |
| fallback | Fallback URL when load fails | string | - |  | 5.28.0 |
| height | Image height | string \| number | - |  | × |
| placeholder | Loading placeholder, supports ReactNode or config object | [PlaceholderType](#placeholdertype) | - |  | × |
| preview | Preview configuration; set to false to disable | boolean \| [PreviewType](#previewtype) | true |  | `preview.closeIcon`: 5.14.0, `preview.mask`: 6.0.0, `preview.mask.closable`: 6.4.0 |
| src | Image URL | string | - |  | × |
| styles | Customize inline style for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), CSSProperties> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), CSSProperties> | - |  | 6.0.0 |
| width | Image width | string \| number | - |  | × |
| onError | Callback when loading error occurs | (event: Event) => void | - |  | × |

Other Property ref [&lt;img>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#Attributes)

### PlaceholderType

| Property | Description | Type | Default | Version |
| --- | --- | --- | --- | --- |
| progress | Progress config, set to `true` to show gradient animation, set `{ percent: number }` to show progress, `render` for custom rendering | boolean \| [ImageProgressConfig](#imageprogressconfig) | - |  |

### ImageProgressConfig

| Property | Description | Type | Default | Version |
| --- | --- | --- | --- | --- |
| percent | Progress value | number | - |  |
| render | Custom rendering, receives default progress UI and percentage | (progress: React.ReactNode, percent: number) => React.ReactNode | - |  |

### PreviewType

| Property | Description | Type | Default | Version |
| --- | --- | --- | --- | --- |
| actionsRender | Custom toolbar render | (originalNode: React.ReactElement, info: ToolbarRenderInfoType) => React.ReactNode | - |  |
| closeIcon | Custom close icon | React.ReactNode | - |  |
| cover | Custom preview mask | React.ReactNode \| [CoverConfig](#coverconfig) | - | CoverConfig support after v6.0 |
| focusTrap | Whether to trap focus within the preview when open | boolean | true | 6.4.0 |
| ~~destroyOnClose~~ | Destroy child elements on preview close (removed, no longer supported) | boolean | false |  |
| ~~forceRender~~ | Force render preview image (removed, no longer supported) | boolean | - |  |
| getContainer | Specify container for preview mounting; still full screen; false mounts at current location | string \| HTMLElement \| (() => HTMLElement) \| false | - |  |
| imageRender | Custom preview content | (originalNode: React.ReactElement, info: { transform: [TransformType](#transformtype), image: [ImgInfo](#imginfo) }) => React.ReactNode | - |  |
| mask | preview mask effect | boolean \| { enabled?: boolean, blur?: boolean, closable?: boolean } | true | mask.closable: 6.4.0 |
| ~~maskClassName~~ | Thumbnail mask class name; please use 'classNames.cover' instead | string | - |  |
| maxScale | Maximum zoom scale | number | 50 |  |
| minScale | Minimum zoom scale | number | 1 |  |
| movable | Whether the preview image can be dragged when it is larger than the viewport | boolean | true |  |
| open | Whether to display preview | boolean | - |  |
| rootClassName | Root DOM class name for preview; applies to both image and preview wrapper | string | - |  |
| scaleStep | Each step's zoom multiplier is 1 + scaleStep | number | 0.5 |  |
| src | Custom preview src | string | - |  |
| styles | Custom semantic structure styles | Record<[SemanticDOM](#semantic-dom), CSSProperties> | - |  |
| ~~toolbarRender~~ | Custom toolbar; please use 'actionsRender' instead | (originalNode: React.ReactElement, info: Omit

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

- Full Ant Design Image docs: https://ant.design/components/image
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
