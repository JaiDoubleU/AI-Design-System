/**
 * Cross-library component equivalence map.
 *
 * Each key is the canonical AI Design System concept.
 * Values describe the closest equivalent in each supported library.
 *
 * Use getComponentMap() from index.js for a filtered / typed view.
 */

export const COMPONENT_MAP = {
  button: {
    description: 'Clickable element that triggers an action',
    designSystem: {
      class: '.btn',
      variants: ['btn-primary', 'btn-secondary', 'btn-ghost', 'btn-danger'],
      sizes: ['btn-sm', 'btn-lg', 'btn-xl', 'btn-icon'],
      file: 'src/components/button.css',
    },
    shadcn: {
      component: 'Button',
      import: "import { Button } from '@/components/ui/button'",
      variants: ['default', 'secondary', 'ghost', 'destructive', 'outline', 'link'],
      sizes: ['default', 'sm', 'lg', 'icon'],
      docs: 'https://ui.shadcn.com/docs/components/button',
    },
    antDesign: {
      component: 'Button',
      import: "import { Button } from 'antd'",
      variants: ['primary', 'default', 'dashed', 'text', 'link'],
      danger: 'danger prop',
      sizes: ['large', 'middle', 'small'],
      docs: 'https://ant.design/components/button',
    },
    materialUI: {
      component: 'Button',
      import: "import Button from '@mui/material/Button'",
      variants: ['contained', 'outlined', 'text'],
      colors: ['primary', 'secondary', 'error', 'warning', 'success', 'info'],
      sizes: ['large', 'medium', 'small'],
      docs: 'https://mui.com/material-ui/react-button/',
    },
  },

  input: {
    description: 'Text field for user input',
    designSystem: {
      class: '.input',
      wrapper: '.field',
      label: '.field-label',
      error: '.field-error-msg',
      file: 'src/components/input.css',
    },
    shadcn: {
      component: 'Input',
      import: "import { Input } from '@/components/ui/input'",
      related: ['Label', 'FormField', 'FormItem', 'FormMessage'],
      docs: 'https://ui.shadcn.com/docs/components/input',
    },
    antDesign: {
      component: 'Input',
      import: "import { Input } from 'antd'",
      related: ['Form', 'Form.Item'],
      variants: ['Input', 'Input.TextArea', 'Input.Password', 'Input.Search'],
      docs: 'https://ant.design/components/input',
    },
    materialUI: {
      component: 'TextField',
      import: "import TextField from '@mui/material/TextField'",
      variants: ['outlined', 'filled', 'standard'],
      related: ['FormControl', 'FormHelperText', 'InputLabel'],
      docs: 'https://mui.com/material-ui/react-text-field/',
    },
  },

  select: {
    description: 'Dropdown for selecting from a list of options',
    designSystem: {
      class: '.select',
      file: 'src/components/input.css',
    },
    shadcn: {
      component: 'Select',
      import: "import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select'",
      docs: 'https://ui.shadcn.com/docs/components/select',
    },
    antDesign: {
      component: 'Select',
      import: "import { Select } from 'antd'",
      docs: 'https://ant.design/components/select',
    },
    materialUI: {
      component: 'Select',
      import: "import Select from '@mui/material/Select'",
      related: ['FormControl', 'InputLabel', 'MenuItem'],
      docs: 'https://mui.com/material-ui/react-select/',
    },
  },

  checkbox: {
    description: 'Boolean toggle, standalone or in a group',
    designSystem: {
      class: '.checkbox',
      file: 'src/components/input.css',
    },
    shadcn: {
      component: 'Checkbox',
      import: "import { Checkbox } from '@/components/ui/checkbox'",
      docs: 'https://ui.shadcn.com/docs/components/checkbox',
    },
    antDesign: {
      component: 'Checkbox',
      import: "import { Checkbox } from 'antd'",
      docs: 'https://ant.design/components/checkbox',
    },
    materialUI: {
      component: 'Checkbox',
      import: "import Checkbox from '@mui/material/Checkbox'",
      docs: 'https://mui.com/material-ui/react-checkbox/',
    },
  },

  radio: {
    description: 'Single selection from a group of options',
    designSystem: {
      class: '.radio',
      file: 'src/components/input.css',
    },
    shadcn: {
      component: 'RadioGroup',
      import: "import { RadioGroup, RadioGroupItem } from '@/components/ui/radio-group'",
      docs: 'https://ui.shadcn.com/docs/components/radio-group',
    },
    antDesign: {
      component: 'Radio',
      import: "import { Radio } from 'antd'",
      related: ['Radio.Group'],
      docs: 'https://ant.design/components/radio',
    },
    materialUI: {
      component: 'Radio',
      import: "import Radio from '@mui/material/Radio'",
      related: ['RadioGroup', 'FormControlLabel'],
      docs: 'https://mui.com/material-ui/react-radio-button/',
    },
  },

  card: {
    description: 'Container grouping related content into a visual unit',
    designSystem: {
      class: '.card',
      variants: ['card-elevated', 'card-flat', 'card-ghost', 'card-interactive'],
      parts: ['card-header', 'card-body', 'card-footer', 'card-title', 'card-subtitle', 'card-media'],
      file: 'src/components/card.css',
    },
    shadcn: {
      component: 'Card',
      import: "import { Card, CardHeader, CardFooter, CardTitle, CardDescription, CardContent } from '@/components/ui/card'",
      docs: 'https://ui.shadcn.com/docs/components/card',
    },
    antDesign: {
      component: 'Card',
      import: "import { Card } from 'antd'",
      docs: 'https://ant.design/components/card',
    },
    materialUI: {
      component: 'Card',
      import: "import Card from '@mui/material/Card'",
      related: ['CardContent', 'CardHeader', 'CardMedia', 'CardActions'],
      docs: 'https://mui.com/material-ui/react-card/',
    },
  },

  badge: {
    description: 'Short status label or count indicator',
    designSystem: {
      class: '.badge',
      variants: ['badge-default', 'badge-primary', 'badge-success', 'badge-danger', 'badge-warning', 'badge-info'],
      file: 'src/components/badge.css',
    },
    shadcn: {
      component: 'Badge',
      import: "import { Badge } from '@/components/ui/badge'",
      variants: ['default', 'secondary', 'outline', 'destructive'],
      docs: 'https://ui.shadcn.com/docs/components/badge',
    },
    antDesign: {
      component: 'Badge',
      import: "import { Badge, Tag } from 'antd'",
      note: 'Badge for count overlays; Tag for label badges',
      docs: 'https://ant.design/components/badge',
    },
    materialUI: {
      component: 'Chip',
      import: "import Chip from '@mui/material/Chip'",
      related: ['Badge'],
      note: 'Chip for labels; Badge for count overlays',
      docs: 'https://mui.com/material-ui/react-chip/',
    },
  },

  alert: {
    description: 'Contextual feedback message for user actions or system events',
    designSystem: {
      class: '.alert',
      variants: ['alert-info', 'alert-success', 'alert-warning', 'alert-danger', 'alert-neutral'],
      file: 'src/components/alert.css',
    },
    shadcn: {
      component: 'Alert',
      import: "import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert'",
      variants: ['default', 'destructive'],
      docs: 'https://ui.shadcn.com/docs/components/alert',
    },
    antDesign: {
      component: 'Alert',
      import: "import { Alert } from 'antd'",
      variants: ['success', 'info', 'warning', 'error'],
      docs: 'https://ant.design/components/alert',
    },
    materialUI: {
      component: 'Alert',
      import: "import Alert from '@mui/material/Alert'",
      variants: ['filled', 'outlined', 'standard'],
      severity: ['error', 'warning', 'info', 'success'],
      docs: 'https://mui.com/material-ui/react-alert/',
    },
  },

  dialog: {
    description: 'Modal overlay for focused interactions or confirmations',
    designSystem: {
      note: 'Not yet in the base CSS system; use a library component with ds-* token overrides',
    },
    shadcn: {
      component: 'Dialog',
      import: "import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle, DialogTrigger } from '@/components/ui/dialog'",
      docs: 'https://ui.shadcn.com/docs/components/dialog',
    },
    antDesign: {
      component: 'Modal',
      import: "import { Modal } from 'antd'",
      docs: 'https://ant.design/components/modal',
    },
    materialUI: {
      component: 'Dialog',
      import: "import Dialog from '@mui/material/Dialog'",
      related: ['DialogTitle', 'DialogContent', 'DialogContentText', 'DialogActions'],
      docs: 'https://mui.com/material-ui/react-dialog/',
    },
  },

  tooltip: {
    description: 'Short contextual text shown on hover/focus',
    designSystem: {
      note: 'Not in the base CSS system; use a library component',
    },
    shadcn: {
      component: 'Tooltip',
      import: "import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from '@/components/ui/tooltip'",
      docs: 'https://ui.shadcn.com/docs/components/tooltip',
    },
    antDesign: {
      component: 'Tooltip',
      import: "import { Tooltip } from 'antd'",
      docs: 'https://ant.design/components/tooltip',
    },
    materialUI: {
      component: 'Tooltip',
      import: "import Tooltip from '@mui/material/Tooltip'",
      docs: 'https://mui.com/material-ui/react-tooltip/',
    },
  },

  table: {
    description: 'Structured data display with rows and columns',
    designSystem: {
      note: 'Use semantic <table> elements with typography and spacing tokens',
    },
    shadcn: {
      component: 'Table',
      import: "import { Table, TableBody, TableCaption, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table'",
      docs: 'https://ui.shadcn.com/docs/components/table',
    },
    antDesign: {
      component: 'Table',
      import: "import { Table } from 'antd'",
      docs: 'https://ant.design/components/table',
    },
    materialUI: {
      component: 'Table',
      import: "import Table from '@mui/material/Table'",
      related: ['TableBody', 'TableCell', 'TableContainer', 'TableHead', 'TableRow'],
      docs: 'https://mui.com/material-ui/react-table/',
    },
  },

  tabs: {
    description: 'Switches between related content panels',
    designSystem: {
      note: 'Not in the base CSS system; use a library component',
    },
    shadcn: {
      component: 'Tabs',
      import: "import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs'",
      docs: 'https://ui.shadcn.com/docs/components/tabs',
    },
    antDesign: {
      component: 'Tabs',
      import: "import { Tabs } from 'antd'",
      docs: 'https://ant.design/components/tabs',
    },
    materialUI: {
      component: 'Tabs',
      import: "import Tabs from '@mui/material/Tabs'",
      related: ['Tab', 'TabPanel'],
      docs: 'https://mui.com/material-ui/react-tabs/',
    },
  },

  toast: {
    description: 'Transient notification that auto-dismisses',
    designSystem: {
      class: '.alert-toast',
      container: '.toast-region',
      file: 'src/components/alert.css',
    },
    shadcn: {
      component: 'Sonner (Toast)',
      import: "import { Toaster } from '@/components/ui/sonner'",
      note: 'shadcn v4 recommends Sonner; older versions used its own toast',
      docs: 'https://ui.shadcn.com/docs/components/sonner',
    },
    antDesign: {
      component: 'message / notification',
      import: "import { message, notification } from 'antd'",
      docs: 'https://ant.design/components/message',
    },
    materialUI: {
      component: 'Snackbar',
      import: "import Snackbar from '@mui/material/Snackbar'",
      docs: 'https://mui.com/material-ui/react-snackbar/',
    },
  },
};

/**
 * Returns equivalence info for a single component concept.
 *
 * @param {string} concept - e.g. 'button', 'card', 'alert'
 * @param {string} [library] - 'shadcn' | 'antDesign' | 'materialUI'
 * @returns {object|null}
 */
export function getComponentInfo(concept, library) {
  const entry = COMPONENT_MAP[concept];
  if (!entry) return null;
  if (library) {
    return { description: entry.description, designSystem: entry.designSystem, [library]: entry[library] };
  }
  return entry;
}

/**
 * Returns all concepts that have an equivalent in the given library.
 *
 * @param {string} library - 'shadcn' | 'antDesign' | 'materialUI'
 * @returns {string[]}
 */
export function getConceptsForLibrary(library) {
  return Object.keys(COMPONENT_MAP).filter(key => COMPONENT_MAP[key][library]);
}
