# Anchor

**Library:** Ant Design v5  
**Category:**   
**Docs:** https://ant.design/components/anchor

---

## Overview

Hyperlinks to scroll on one page.

### When to use

For displaying anchor hyperlinks on page and jumping between them.

> Notes for developers
>
> After version `4.24.0`, we rewrite Anchor use FC, Some methods of obtaining `ref` and calling internal instance methods will invalid.

---

## Import

```js
import { Anchor } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

### Anchor Props

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| affix | Fixed mode of Anchor | boolean \| Omit

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

- Full Ant Design Anchor docs: https://ant.design/components/anchor
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
