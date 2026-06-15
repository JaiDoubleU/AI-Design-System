# Carousel

**Library:** Ant Design v5  
**Category:** Data Display  
**Docs:** https://ant.design/components/carousel

---

## Overview

A set of carousel areas.

### When to use

- When there is a group of content on the same level.
- When there is insufficient content space, it can be used to save space in the form of a revolving door.
- Commonly used for a group of pictures/cards.

---

## Import

```js
import { Carousel } from 'antd';
```

---

## Props / API

Common props ref：[Common props](/docs/react/common-props)

| Property | Description | Type | Default | Version | [Global Config](/components/config-provider#component-config) |
| --- | --- | --- | --- | --- | --- |
| arrows | Whether to show switch arrows | boolean | false | 5.17.0 | × |
| autoplay | Whether to scroll automatically, you can specify `autoplay={{ dotDuration: true }}` to display the progress bar | boolean \| { dotDuration?: boolean } | false | dotDuration: 5.24.0 | × |
| autoplaySpeed | Delay between each auto scroll (in milliseconds) | number | 3000 |  | × |
| adaptiveHeight | Adjust the slide's height automatically | boolean | false |  | × |
| dotPlacement | The position of the dots, which can be one of `top` `bottom` `start` `end` | string | `bottom` |  | × |
| ~~dotPosition~~ | The position of the dots, which can be one of `top` `bottom` `left` `right` `start` `end`, Please use `dotPlacement` instead | string | `bottom` |  | × |
| dots | Whether to show the dots at the bottom of the gallery, `object` for `dotsClass` | boolean \| { className?: string } | true |  | × |
| draggable | Enable scrollable via dragging on desktop | boolean | false |  | × |
| fade | Whether to use fade transition | boolean | false |  | × |
| infinite | Infinitely wrap around contents | boolean | true |  | × |
| speed | Animation speed in milliseconds | number | 500 |  | × |
| easing | Transition interpolation function name | string | `linear` |  | × |
| effect | Transition effect | `scrollx` \| `fade` | `scrollx` |  | × |
| afterChange | Callback function called after the current index changes | (current: number) => void | - |  | × |
| beforeChange | Callback function called before the current index changes | (current: number, next: number) => void | - |  | × |
| waitForAnimate | Whether to wait for the animation when switching | boolean | false |  | × |

Find more APIs in react-slick [documentation](https://react-slick.neostack.com/docs/api).

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

- Full Ant Design Carousel docs: https://ant.design/components/carousel
- Props are subject to change across Ant Design patch versions.
- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.
