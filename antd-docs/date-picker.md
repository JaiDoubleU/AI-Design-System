# DatePicker

**Library:** Ant Design v5  
**Category:** Data Entry  
**Docs:** https://ant.design/components/date-picker

---

## Overview

To select or input a date.

### When to use

By clicking the input box, you can select a date from a popup calendar.

---

## Import

```js
import { DatePicker } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

There are five kinds of picker:

- DatePicker
- DatePicker\[picker="month"]
- DatePicker\[picker="week"]
- DatePicker\[picker="year"]
- DatePicker\[picker="quarter"] (Added in 4.1.0)
- RangePicker

### Localization

The default locale is en-US, if you need to use other languages, recommend to use internationalized components provided by us at the entrance. Look at: [ConfigProvider](https://ant.design/components/config-provider/).

If there are special needs (only modifying single component language), Please use the property: locale. Example: [default](https://github.com/ant-design/ant-design/blob/master/components/date-picker/locale/example.json).

```jsx
// The default locale is en-US, if you want to use other locale, just set locale in entry file globally.
// Make sure you import the relevant dayjs file as well, otherwise the locale won't change for all texts (e.g. range picker months)
import locale from 'antd/locale/zh_CN';
import dayjs from 'dayjs';

import 'dayjs/locale/zh-cn';

dayjs.locale('zh-cn');

;
```

<!-- prettier-ignore -->
:::warning
When use with Next.js App Router, make sure to add `'use client'` before import locale file of dayjs. It's because all components of Ant Design only works in client, importing locale in RSC will not work.
:::

### Common API

The following APIs are shared by DatePicker, RangePicker.

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| allowClear | Customize clear button | boolean \| { clearIcon?: ReactNode } | true | 5.8.0: Support object type | 6.4.0 |
| ~~bordered~~ | Whether has border style, please use `variant` instead | boolean | true | - | × |
| className | The picker className | string | - |  | DatePicker: 5.7.0, RangePicker: 5.11.0 |
| classNames | Customize class for each semantic structure inside the component. Supports object or function. | Record<[SemanticDOM](#semantic-dom), string> \| (info: { props })=> Record<[SemanticDOM](#semantic-dom), string> | - |  | DatePicker: 5.25.0, RangePicker: 5.25.0 |
| dateRender | Custom rendering function for date cells, >= 5.4.0 use `cellRender` instead. | function(currentDate: dayjs, today: dayjs) => React.ReactNode | - | < 5.4.0 | × |
| cellRender | Custom rendering function for picker cells | (current: dayjs, info: { originNode: React.ReactElement,today: DateType, range?: 'start' \| 'end', type: PanelMode, locale?: Locale, subType?: 'hour' \| 'minute' \| 'second' \| 'meridiem' }) => React.ReactNode | - | 5.4.0 | × |
| components | Custom panels | Record

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

- Full Ant Design DatePicker docs: https://ant.design/components/date-picker
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
