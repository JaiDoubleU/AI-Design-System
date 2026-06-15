# ConfigProvider

**Library:** Ant Design v5  
**Category:** Other  
**Docs:** https://ant.design/components/config-provider

---

## Overview

Provide a uniform configuration support for components.

### When to use

This component provides a configuration to all React components underneath itself via the [context API](https://react.dev/learn/passing-data-deeply-with-context). In the render tree all components will have access to the provided config.

---

## Import

```js
import { ConfigProvider } from 'antd';
```

---

## Props / API

| Property | Description | Type | Default | Version |
| --- | --- | --- | --- | --- |
| componentDisabled | Config antd component `disabled` | boolean | - | 4.21.0 |
| componentSize | Config antd component size | `small` \| `medium` \| `large` | - |  |
| csp | Set [Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) config | { nonce: string } | - |  |
| direction | Set direction of layout. See [demo](#config-provider-demo-direction) | `ltr` \| `rtl` | `ltr` |  |
| getPopupContainer | To set the container of the popup element. The default is to create a `div` element in `body` | `(trigger?: HTMLElement) => HTMLElement \| ShadowRoot` | () => document.body |  |
| getTargetContainer | Config Affix, Anchor scroll target container | `() => HTMLElement \| Window \| ShadowRoot` | () => window | 4.2.0 |
| iconPrefixCls | Set icon prefix className | string | `anticon` | 4.11.0 |
| locale | Language package setting, you can find the packages in [antd/locale](https://unpkg.com/antd/locale/) | object | - |  |
| popupMatchSelectWidth | Determine whether the dropdown menu and the select input are the same width. Default set `min-width` same as input. Will ignore when value less than select width. `false` will disable virtual scroll | boolean \| number | - | 5.5.0 |
| popupOverflow | Select like component popup logic. Can set to show in viewport or follow window scroll | 'viewport' \| 'scroll'  | 'viewport' | 5.5.0 |
| prefixCls | Set prefix className | string | `ant` |  |
| renderEmpty | Set empty content of components. Ref [Empty](/components/empty/) | function(componentName: string): ReactNode | - |  |
| theme | Set theme, ref [Customize Theme](/docs/react/customize-theme) | [Theme](/docs/react/customize-theme#theme) | - | 5.0.0 |
| variant | Set variant of data entry components | `outlined` \| `filled` \| `borderless` | - | 5.19.0 |
| virtual | Disable virtual scroll when set to `false` | boolean | - | 4.3.0 |
| warning | Config warning level, when `strict` is `false`, it will aggregate deprecated information into a single message | { strict: boolean } | - | 5.10.0 |
| ~~autoInsertSpaceInButton~~ | Button auto spacing config, please use `button={{ autoInsertSpace: boolean }}` instead | boolean | - | - |
| ~~dropdownMatchSelectWidth~~ | Determine whether the dropdown menu and the select input are the same width, please use `popupMatchSelectWidth` instead | boolean | - | - |

### ConfigProvider.config() {#config}

Setting `Modal`, `Message`, `Notification` static config. Does not work on hooks.

```tsx
ConfigProvider.config({
  // 5.13.0+
  holderRender: (children) => (
    
  ),
});
```

### ConfigProvider.useConfig()  {#useconfig}

Get the value of the parent `Provider`, Such as `DisabledContextProvider`, `SizeContextProvider`.

```jsx
const {
  componentDisabled, // 5.3.0+
  componentSize, // 5.3.0+
} = ConfigProvider.useConfig();
```

| Property | Description | Type | Default | Version |
| --- | --- | --- | --- | --- |
| componentDisabled | antd component disabled state | boolean | - | 5.3.0 |
| componentSize | antd component size state | `small` \| `medium` \| `large` | - | 5.3.0 |

### Component Config

The following config keys set common props for corresponding components or global effects. See the related APIs for details:

- `affix`: [Affix](/components/affix#api) (supported since 6.0.0)
- `alert`: [Alert](/components/alert#api) (supported since 5.7.0)
- `anchor`: [Anchor](/components/anchor#api) (supported since 6.0.0)
- `app`: [App](/components/app#api) (supported since 6.3.0)
- `avatar`: [Avatar](/components/avatar#api) (supported since 5.7.0)
- `badge`: [Badge](/components/badge#api) (supported since 5.7.0)
- `borderBeam`: [BorderBeam](/components/border-beam#api) (supported since 6.4.0)
- `breadcrumb`: [Breadcrumb](/components/breadcrumb#api) (supported since 5.7.0)
- `button`: [Button](/components/button#api) (supported since 5.6.0)
- `card`: [Card](/components/card#api) (supported since 5.14.0)
- `cardMeta`: [Card.Meta](/components/card#cardmeta) (supported since 6.0.0)
- `calendar`: [Calendar](/components/calendar#api) (supported since 6.0.0)
- `carousel`: [Carousel](/components/carousel#api) (supported since 5.7.0)
- `cascader`: [Cascader](/components/cascader#api) (supported since 5.13.0)
- `checkbox`: [Checkbox](/components/checkbox#api) (supported since 6.0.0)
- `collapse`: [Collapse](/components/collapse#api) (supported since 5.15.0)
- `colorPicker`: [ColorPicker](/components/color-picker#api) (supported since 6.3.0)
- `datePicker`: [DatePicker](/components/date-picker#api) (supported since 5.7.0)
- `rangePicker`: [RangePicker](/components/date-picker#rangepicker) (supported since 5.11.0)
- `descriptions`: [Descriptions](/components/descriptions#api) (supported since 5.23.0)
- `divider`: [Divider](/components/divider#api) (supported since 5.10.0)
- `drawer`: [Drawer](/components/drawer#api) (supported since 5.10.0)
- `dropdown`: [Dropdown](/components/dropdown#api) (supported since 5.11.0)
- `empty`: [Empty](/components/empty#api) (supported since 5.23.0)
- `flex`: [Flex](/components/flex#api) (supported since 5.10.0)
- `floatButton`: [FloatButton](/components/float-button#api) (supported since 6.0.0)
- `floatButtonGroup`: [FloatButton.Group](/components/float-button#floatbuttongroup) (supported since 5.16.0)
- `form`: [Form](/components/form#api) (supported since 4.8.0)
- `image`: [Image](/components/image#api) (supported since 5.14.0)
- `input`: [Input](/components/input#input) (supported since 4.2.0)
- `inputNumber`: [InputNumber](/components/input-number#api) (supported since 5.19.0)
- `otp`: [Input.OTP](/components/input#inputotp) (supported since 6.0.0)
- `inputPassword`: [Input.Password](/components/input#inputpassword) (supported since 6.4.0)
- `inputSearch`: [Input.Search](/components/input#inputsearch) (supported since 6.4.0)
- `textArea`: [Input.TextArea](/components/input#inputtextarea) (supported since 5.15.0)
- `layout`: [Layout](/components/layout#api) (supported since 5.7.0)
- `list`: [List](/components/list#api) (supported since 5.7.0)
- `masonry`: [Masonry](/components/masonry#api) (supported since 6.0.0)
- `menu`: [Menu](/components/menu#api) (supported since 5.15.0)
- `mentions`: [Mentions](/components/mentions#api) (supported since 5.13.0)
- `message`: [Message](/components/message#api) (supported since 5.7.0)
- `modal`: [Modal](/components/modal#api) (supported since 5.10.0)
- `notification`: [Notification](/components/notification#api) (supported since 5.14.0)
- `pagination`: [Pagination](/components/pagination#api) (supported since 6.0.0)
- `progress`: [Progress](/components/progress#api) (supported since 5.7.0)
- `radio`: [Radio](/components/radio#api) (supported since 6.0.0)
- `rate`: [Rate](/components/rate#api) (supported since 5.7.0)
- `result`: [Result](/components/result#api) (supported since 6.0.0)
- `ribbon`: [Badge.Ribbon](/components/badge#badgeribbon) (supported since 6.0.0)
- `skeleton`: [Skeleton](/components/skeleton#api) (supported since 6.0.0)
- `segmented`: [Segmented](/components/segmented#api) (supported since 6.0.0)
- `select`: [Select](/components/select#api) (supported since 5.13.0)
- `slider`: [Slider](/components/slider#api) (supported since 5.23.0)
- `switch`: [Switch](/components/switch#api) (supported since 6.0.0)
- `space`: [Space](/components/space#api) (supported since 5.6.0)
- `splitter`: [Splitter](/components/splitter#api) (supported since 5.21.0)
- `spin`: [Spin](/components/spin#api) (supported since 5.20.0)
- `statistic`: [Statistic](/components/statistic#api) (supported since 6.0.0)
- `steps`: [Steps](/components/steps#api) (supported since 5.10.0)
- `table`: [Table](/components/table#api) (supported since 6.2.0)
- `tabs`: [Tabs](/components/tabs#api) (supported since 5.14.0)
- `tag`: [Tag](/components/tag#api) (supported since 5.14.0)
- `timeline`: [Timeline](/components/timeline#api) (supported since 6.0.0)
- `timePicker`: [TimePicker](/components/time-picker#api) (supported since 5.13.0)
- `tour`: [Tour](/components/tour#api) (supported since 5.14.0)
- `tooltip`: [Tooltip](/components/tooltip#api) (supported since 6.1.0)
- `popover`: [Popover](/components/popover#api) (supported since 5.23.0)
- `popconfirm`: [Popconfirm](/components/popconfirm#api) (supported since 5.23.0)
- `qrcode`: [QRCode](/components/qr-code#api) (supported since 6.0.0)
- `transfer`: [Transfer](/components/transfer#api) (supported since 5.7.0)
- `tree`: [Tree](/components/tree#api) (supported since 6.0.0)
- `treeSelect`: [TreeSelect](/components/tree-select#api) (supported since 5.19.0)
- `typography`: [Typography](/components/typography#api) (supported since 6.4.0)
- `upload`: [Upload](/components/upload#api) (supported since 5.27.0)
- `watermark`: [Watermark](/components/watermark#api) (supported since 6.0.0)
- `wave`: [WaveConfig](#waveconfig) (supported since 5.8.0)

### WaveConfig

| Property | Description | Type | Default | Version |
| --- | --- | --- | --- | --- |
| disabled | Whether to disable wave effect | boolean | false |  |
| showEffect | Customized wave effect | (node: HTMLElement, info: { className, token, component }) => void | - |  |
| triggerType | The event that triggers wave effect | `click` \| `pointerdown` \| `pointerup` \| `mousedown` \| `mouseup` | `click` | 6.4.0 |

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

- Full Ant Design ConfigProvider docs: https://ant.design/components/config-provider
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
