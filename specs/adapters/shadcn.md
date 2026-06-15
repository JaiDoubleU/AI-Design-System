# shadcn/ui Adapter

**File:** `lib-adapters/shadcn.css`  
**Target library:** shadcn/ui v4 (Radix UI primitives + Tailwind CSS)  
**CSS variable prefix:** bare names (`--primary`, `--background`, `--foreground` …)

---

## Prerequisites

shadcn/ui requires a `globals.css` (or equivalent) that defines its CSS
variables on `:root`. The adapter reads those bare variables and maps them
to `--ds-*` hooks. The variables are resolved at runtime by the browser's
cascade, not baked in at build time.

Minimum required shadcn variables:

```css
:root {
  --background: 0 0% 100%;
  --foreground: 222.2 84% 4.9%;
  --primary: 221.2 83.2% 53.3%;
  --primary-foreground: 210 40% 98%;
  --muted: 210 40% 96.1%;
  --muted-foreground: 215.4 16.3% 46.9%;
  --border: 214.3 31.8% 91.4%;
  --ring: 221.2 83.2% 53.3%;
  --destructive: 0 84.2% 60.2%;
  --radius: 0.5rem;
}
```

---

## Setup

### CSS entry point

```css
/* 1. shadcn/ui globals */
@import '@/styles/globals.css';

/* 2. Adapter — maps --foreground → --ds-text etc. */
@import 'ai-design-system/lib-adapters/shadcn.css';

/* 3. AI DS tokens — resolves --ds-* or falls back to --prim-* */
@import 'ai-design-system/tokens.css';

/* 4. AI DS component CSS (optional — if using AI DS components) */
@import 'ai-design-system/src/components/button.css';
```

### JavaScript (runtime, for dynamic theme switching)

```js
import { applyAdapter } from 'ai-design-system/lib-adapters';

// Call after shadcn globals are loaded on :root
applyAdapter('shadcn');
```

---

## Token mapping

| `--ds-*` | shadcn source | Notes |
|---|---|---|
| `--ds-text` | `--foreground` | |
| `--ds-text-subtle` | `--muted-foreground` | |
| `--ds-text-muted` | `--muted-foreground` | Same as subtle |
| `--ds-text-inverse` | `--primary-foreground` | |
| `--ds-text-danger` | `--destructive` | shadcn uses HSL channels |
| `--ds-bg` | `--background` | |
| `--ds-bg-subtle` | `--muted` | |
| `--ds-bg-muted` | `--muted` | |
| `--ds-interactive` | `hsl(var(--primary))` | Wrapped in hsl() |
| `--ds-interactive-hover` | `hsl(var(--primary) / 0.9)` | 10% lighter |
| `--ds-interactive-fg` | `--primary-foreground` | |
| `--ds-interactive-danger` | `hsl(var(--destructive))` | |
| `--ds-border` | `--border` | |
| `--ds-border-focus` | `--ring` | |
| `--ds-radius-lg` | `--radius` | shadcn's base radius |
| `--ds-radius-sm` | `calc(var(--radius) - 4px)` | |
| `--ds-radius-xl` | `calc(var(--radius) + 4px)` | |
| `--ds-font-sans` | `--font-sans` | Falls back to system stack |
| `--ds-font-mono` | `--font-mono` | |

---

## Component equivalents

| AI DS concept | shadcn component | Import |
|---|---|---|
| `.btn` | `<Button>` | `import { Button } from '@/components/ui/button'` |
| `.input` | `<Input>` | `import { Input } from '@/components/ui/input'` |
| `.card` | `<Card>` | `import { Card, CardHeader, … } from '@/components/ui/card'` |
| `.badge` | `<Badge>` | `import { Badge } from '@/components/ui/badge'` |
| `.alert` | `<Alert>` | `import { Alert, AlertTitle, AlertDescription } from '@/components/ui/alert'` |
| `.alert-toast` | `<Sonner>` | `import { Toaster } from '@/components/ui/sonner'` |

Full map: `lib-adapters/component-map.js`

---

## Dark mode

shadcn/ui uses a `.dark` class on `<html>`. The adapter variables inherit
automatically because they reference bare `--foreground` etc., which shadcn
redefines under `.dark { … }` in its globals. No extra adapter config needed.

---

## Known gaps

| AI DS token | shadcn equivalent | Status |
|---|---|---|
| `--ds-text-success` | Not defined | Adapter uses `hsl(var(--success, 142 76% 36%))` as a fallback |
| `--ds-text-warning` | Not defined | Adapter uses `hsl(var(--warning, 38 92% 40%))` as a fallback |
| `--ds-bg-success/warning/info/danger` | Not defined | Alpha-blended from semantic colors |

You can override these gaps by adding to your globals:

```css
:root {
  --success: 142 76% 36%;
  --warning: 38 92% 50%;
}
```
