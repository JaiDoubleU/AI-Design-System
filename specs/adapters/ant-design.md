# Ant Design Adapter

**File:** `lib-adapters/ant-design.css`  
**Target library:** Ant Design v5  
**CSS variable prefix:** `--ant-*`

---

## Prerequisites

Ant Design v5's CSS Variables Mode must be enabled. Without it, Ant Design
uses JS-only theming and emits no `--ant-*` CSS variables for the adapter
to read.

Enable it in your root `ConfigProvider`:

```jsx
import { ConfigProvider } from 'antd';

function App() {
  return (
    <ConfigProvider theme={{ cssVar: true, hashed: false }}>
      <YourApp />
    </ConfigProvider>
  );
}
```

`hashed: false` is recommended so class names are stable and predictable.

---

## Setup

### CSS entry point

```css
/* 1. Ant Design reset */
@import 'antd/dist/reset.css';

/* 2. Adapter */
@import 'ai-design-system/lib-adapters/ant-design.css';

/* 3. AI DS tokens */
@import 'ai-design-system/tokens.css';
```

### JavaScript (runtime)

```js
import { applyAdapter } from 'ai-design-system/lib-adapters';

// Call after ConfigProvider has mounted and injected --ant-* onto :root
applyAdapter('antDesign');
```

---

## Token mapping

| `--ds-*` | `--ant-*` source | Notes |
|---|---|---|
| `--ds-text` | `--ant-color-text` | |
| `--ds-text-subtle` | `--ant-color-text-secondary` | |
| `--ds-text-muted` | `--ant-color-text-quaternary` | |
| `--ds-text-inverse` | `--ant-color-text-light-solid` | White on coloured surfaces |
| `--ds-text-danger` | `--ant-color-error-text` | |
| `--ds-text-success` | `--ant-color-success-text` | |
| `--ds-text-warning` | `--ant-color-warning-text` | |
| `--ds-text-info` | `--ant-color-info-text` | |
| `--ds-bg` | `--ant-color-bg-base` | |
| `--ds-bg-subtle` | `--ant-color-bg-layout` | |
| `--ds-bg-muted` | `--ant-color-fill-quaternary` | |
| `--ds-bg-success` | `--ant-color-success-bg` | |
| `--ds-bg-warning` | `--ant-color-warning-bg` | |
| `--ds-bg-danger` | `--ant-color-error-bg` | |
| `--ds-bg-info` | `--ant-color-info-bg` | |
| `--ds-interactive` | `--ant-color-primary` | |
| `--ds-interactive-hover` | `--ant-color-primary-hover` | |
| `--ds-interactive-active` | `--ant-color-primary-active` | |
| `--ds-interactive-muted` | `--ant-color-primary-bg` | |
| `--ds-interactive-fg` | `--ant-color-text-light-solid` | |
| `--ds-interactive-danger` | `--ant-color-error` | |
| `--ds-border` | `--ant-color-border` | |
| `--ds-border-subtle` | `--ant-color-border-secondary` | |
| `--ds-border-focus` | `--ant-color-primary-border-hover` | |
| `--ds-border-success` | `--ant-color-success-border` | |
| `--ds-border-danger` | `--ant-color-error-border` | |
| `--ds-radius-sm` | `--ant-border-radius-sm` | |
| `--ds-radius-md` | `--ant-border-radius` | |
| `--ds-radius-lg` | `--ant-border-radius-lg` | |
| `--ds-radius-xl` | `--ant-border-radius-xl` | |
| `--ds-font-sans` | `--ant-font-family` | |
| `--ds-font-mono` | `--ant-font-family-code` | |
| `--ds-shadow-sm` | `--ant-box-shadow-tertiary` | |
| `--ds-shadow-md` | `--ant-box-shadow-secondary` | |
| `--ds-shadow-lg` | `--ant-box-shadow` | |

---

## Component equivalents

| AI DS concept | Ant Design component | Import |
|---|---|---|
| `.btn` | `<Button>` | `import { Button } from 'antd'` |
| `.btn-danger` | `<Button danger>` | danger prop on Button |
| `.input` | `<Input>` | `import { Input } from 'antd'` |
| `.select` | `<Select>` | `import { Select } from 'antd'` |
| `.card` | `<Card>` | `import { Card } from 'antd'` |
| `.badge` (label) | `<Tag>` | `import { Tag } from 'antd'` |
| `.badge` (count) | `<Badge>` | `import { Badge } from 'antd'` |
| `.alert` | `<Alert>` | `import { Alert } from 'antd'` |
| `.alert-toast` | `message` / `notification` | `import { message } from 'antd'` |
| `.checkbox` | `<Checkbox>` | `import { Checkbox } from 'antd'` |
| `.radio` | `<Radio>` | `import { Radio } from 'antd'` |

---

## Dark mode

Ant Design uses `ConfigProvider` with `theme.algorithm`:

```jsx
import { ConfigProvider, theme } from 'antd';

<ConfigProvider theme={{ algorithm: theme.darkAlgorithm, cssVar: true }}>
```

When dark algorithm is active, Ant Design recomputes all `--ant-*` on `:root`.
The adapter variables update automatically — no extra steps required.

---

## Custom theme tokens

Override specific Ant Design tokens in `ConfigProvider`:

```jsx
<ConfigProvider theme={{
  cssVar: true,
  token: {
    colorPrimary: '#6366f1',
    borderRadius: 8,
    fontFamily: '"DM Sans", sans-serif',
  },
}}>
```

These flow through `--ant-color-primary`, `--ant-border-radius`, and
`--ant-font-family`, then through the adapter into `--ds-interactive`,
`--ds-radius-md`, and `--ds-font-sans`.
