# Material UI (MUI) Adapter

**File:** `lib-adapters/material-ui.css`  
**Target library:** Material UI v6 (also v5 with CssVarsProvider)  
**CSS variable prefix:** `--mui-*`

---

## Prerequisites

MUI v6 requires CSS Variables Mode to emit `--mui-*` variables. Without it,
MUI uses JS-only theming and the CSS adapter cannot read its values.

### MUI v6

```jsx
import { ThemeProvider, createTheme } from '@mui/material/styles';

const theme = createTheme({ cssVariables: true });

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <YourApp />
    </ThemeProvider>
  );
}
```

### MUI v5 (experimental)

```jsx
import { Experimental_CssVarsProvider as CssVarsProvider } from '@mui/material/styles';

function App() {
  return (
    <CssVarsProvider>
      <YourApp />
    </CssVarsProvider>
  );
}
```

---

## Setup

### CSS entry point

```css
/* 1. MUI baseline resets (if using CssBaseline, this is injected by MUI itself) */

/* 2. Adapter */
@import 'ai-design-system/lib-adapters/material-ui.css';

/* 3. AI DS tokens */
@import 'ai-design-system/tokens.css';
```

Because MUI injects styles via JS (emotion/styled-components), you may need
to apply the adapter at runtime instead:

### JavaScript (runtime — recommended for MUI)

```js
import { applyAdapter } from 'ai-design-system/lib-adapters';

// Call inside a useEffect after ThemeProvider has mounted
useEffect(() => {
  applyAdapter('materialUI');
}, []);
```

---

## Token mapping

| `--ds-*` | `--mui-*` source | Notes |
|---|---|---|
| `--ds-text` | `--mui-palette-text-primary` | |
| `--ds-text-subtle` | `--mui-palette-text-secondary` | |
| `--ds-text-muted` | `--mui-palette-text-disabled` | |
| `--ds-text-inverse` | `--mui-palette-primary-contrastText` | |
| `--ds-text-danger` | `--mui-palette-error-main` | |
| `--ds-text-success` | `--mui-palette-success-main` | |
| `--ds-text-warning` | `--mui-palette-warning-main` | |
| `--ds-text-info` | `--mui-palette-info-main` | |
| `--ds-bg` | `--mui-palette-background-default` | |
| `--ds-bg-subtle` | `--mui-palette-background-paper` | |
| `--ds-bg-muted` | `--mui-palette-action-hover` | |
| `--ds-bg-success` | `--mui-palette-success-light` | Falls back to `rgb(237 247 237)` |
| `--ds-bg-warning` | `--mui-palette-warning-light` | Falls back to `rgb(255 244 229)` |
| `--ds-bg-danger` | `--mui-palette-error-light` | Falls back to `rgb(253 237 237)` |
| `--ds-bg-info` | `--mui-palette-info-light` | Falls back to `rgb(229 246 253)` |
| `--ds-interactive` | `--mui-palette-primary-main` | |
| `--ds-interactive-hover` | `--mui-palette-primary-dark` | |
| `--ds-interactive-active` | `--mui-palette-primary-dark` | |
| `--ds-interactive-muted` | `--mui-palette-primary-light` | |
| `--ds-interactive-fg` | `--mui-palette-primary-contrastText` | |
| `--ds-interactive-danger` | `--mui-palette-error-main` | |
| `--ds-border` | `--mui-palette-divider` | |
| `--ds-border-focus` | `--mui-palette-primary-main` | |
| `--ds-radius-sm` | `calc(var(--mui-shape-borderRadius) * 0.5px)` | MUI borderRadius is unitless |
| `--ds-radius-md` | `calc(var(--mui-shape-borderRadius) * 1px)` | Default: 4 → 4px |
| `--ds-radius-lg` | `calc(var(--mui-shape-borderRadius) * 1.5px)` | |
| `--ds-radius-xl` | `calc(var(--mui-shape-borderRadius) * 2px)` | |
| `--ds-font-sans` | `--mui-font-family` | Falls back to Roboto stack |
| `--ds-font-mono` | _(hardcoded)_ | `'Roboto Mono', ui-monospace, monospace` |
| `--ds-shadow-sm` | `--mui-shadows-1` | |
| `--ds-shadow-md` | `--mui-shadows-3` | |
| `--ds-shadow-lg` | `--mui-shadows-8` | |

---

## Component equivalents

| AI DS concept | MUI component | Import |
|---|---|---|
| `.btn` | `<Button>` | `import Button from '@mui/material/Button'` |
| `.btn-primary` | `<Button variant="contained">` | |
| `.btn-secondary` | `<Button variant="outlined">` | |
| `.btn-ghost` | `<Button variant="text">` | |
| `.btn-danger` | `<Button color="error">` | |
| `.input` | `<TextField>` | `import TextField from '@mui/material/TextField'` |
| `.select` | `<Select>` | `import Select from '@mui/material/Select'` |
| `.checkbox` | `<Checkbox>` | `import Checkbox from '@mui/material/Checkbox'` |
| `.radio` | `<Radio>` | `import Radio from '@mui/material/Radio'` |
| `.card` | `<Card>` | `import Card from '@mui/material/Card'` |
| `.badge` (label) | `<Chip>` | `import Chip from '@mui/material/Chip'` |
| `.badge` (count) | `<Badge>` | `import Badge from '@mui/material/Badge'` |
| `.alert` | `<Alert>` | `import Alert from '@mui/material/Alert'` |
| `.alert-toast` | `<Snackbar>` | `import Snackbar from '@mui/material/Snackbar'` |

---

## Dark mode

```jsx
const theme = createTheme({
  cssVariables: true,
  colorSchemes: {
    light: true,
    dark: true,
  },
});

// Toggle with:
const { setColorScheme } = useColorScheme();
setColorScheme('dark');
```

MUI rewrites `--mui-palette-*` variables on the root element when the
colour scheme changes. The adapter variables update automatically.

---

## Custom palette

```jsx
const theme = createTheme({
  cssVariables: true,
  palette: {
    primary: { main: '#6366f1' },
    background: { default: '#0a0a0a', paper: '#141414' },
  },
});
```

`--mui-palette-primary-main` will be `#6366f1`, flowing through the adapter
into `--ds-interactive`.
