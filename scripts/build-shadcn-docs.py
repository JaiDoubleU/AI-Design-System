#!/usr/bin/env python3
"""
build-shadcn-docs.py
Fetches shadcn/ui v4 component MDX files from GitHub and generates
structured AI-readable .md documentation files.
"""

import re
import os
import sys
import time
import subprocess
import textwrap

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "shadcn-docs")
BASE_RAW = "https://raw.githubusercontent.com/shadcn-ui/ui/main/apps/v4/content/docs/components/radix"

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Maps component slug → AI DS CSS file relative to project root.
DS_CSS_FILE_MAP = {
    "button":        "src/components/button.css",
    "card":          "src/components/card.css",
    "input":         "src/components/input.css",
    "select":        "src/components/input.css",
    "checkbox":      "src/components/input.css",
    "radio-group":   "src/components/input.css",
    "textarea":      "src/components/input.css",
    "native-select": "src/components/input.css",
    "badge":         "src/components/badge.css",
    "alert":         "src/components/alert.css",
    "toast":         "src/components/alert.css",
    "sonner":        "src/components/alert.css",
    "typography":    "src/base/typography.css",
}

# Maps --ds-* adapter hooks to Layer 2 (--color-*, --shadow-*, etc.) equivalents.
DS_TO_LAYER2 = {
    '--ds-text':               '--color-text',
    '--ds-text-subtle':        '--color-text-subtle',
    '--ds-text-muted':         '--color-text-muted',
    '--ds-text-inverse':       '--color-text-inverse',
    '--ds-text-danger':        '--color-text-danger',
    '--ds-text-success':       '--color-text-success',
    '--ds-text-warning':       '--color-text-warning',
    '--ds-text-info':          '--color-text-info',
    '--ds-bg':                 '--color-bg',
    '--ds-bg-subtle':          '--color-bg-subtle',
    '--ds-bg-muted':           '--color-bg-muted',
    '--ds-bg-emphasis':        '--color-bg-emphasis',
    '--ds-bg-success':         '--color-bg-success',
    '--ds-bg-warning':         '--color-bg-warning',
    '--ds-bg-danger':          '--color-bg-danger',
    '--ds-bg-info':            '--color-bg-info',
    '--ds-interactive':        '--color-interactive',
    '--ds-interactive-hover':  '--color-interactive-hover',
    '--ds-interactive-active': '--color-interactive-active',
    '--ds-interactive-muted':  '--color-interactive-muted',
    '--ds-interactive-fg':     '--color-interactive-fg',
    '--ds-interactive-danger': '--color-interactive-danger',
    '--ds-border':             '--color-border',
    '--ds-border-subtle':      '--color-border-subtle',
    '--ds-border-emphasis':    '--color-border-emphasis',
    '--ds-border-focus':       '--color-border-focus',
    '--ds-border-success':     '--color-border-success',
    '--ds-border-danger':      '--color-border-danger',
    '--ds-radius-sm':          '--radius-sm',
    '--ds-radius-md':          '--radius-md',
    '--ds-radius-lg':          '--radius-lg',
    '--ds-radius-xl':          '--radius-xl',
    '--ds-radius-full':        '--radius-full',
    '--ds-shadow-sm':          '--shadow-sm',
    '--ds-shadow-md':          '--shadow-md',
    '--ds-shadow-lg':          '--shadow-lg',
    '--ds-font-sans':          '--font-sans',
    '--ds-font-mono':          '--font-mono',
    '--ds-font-serif':         '--font-serif',
}

# Maps --ds-* hooks to (css-property, context-comment) for snippet generation.
DS_TOKEN_CSS_PROP = {
    '--ds-text':               ('color',            ''),
    '--ds-text-subtle':        ('color',            'muted text'),
    '--ds-text-muted':         ('color',            'very muted text'),
    '--ds-text-inverse':       ('color',            'text on dark bg'),
    '--ds-text-danger':        ('color',            'error text'),
    '--ds-text-success':       ('color',            'success text'),
    '--ds-text-warning':       ('color',            'warning text'),
    '--ds-text-info':          ('color',            'info text'),
    '--ds-bg':                 ('background-color', ''),
    '--ds-bg-subtle':          ('background-color', 'subtle surface'),
    '--ds-bg-muted':           ('background-color', 'muted surface'),
    '--ds-bg-emphasis':        ('background-color', 'inverted surface'),
    '--ds-bg-success':         ('background-color', 'success tint'),
    '--ds-bg-warning':         ('background-color', 'warning tint'),
    '--ds-bg-danger':          ('background-color', 'danger tint'),
    '--ds-bg-info':            ('background-color', 'info tint'),
    '--ds-interactive':        ('background-color', 'primary action'),
    '--ds-interactive-hover':  ('background-color', ':hover state'),
    '--ds-interactive-active': ('background-color', ':active state'),
    '--ds-interactive-muted':  ('background-color', 'subtle tint'),
    '--ds-interactive-fg':     ('color',            'text on interactive bg'),
    '--ds-interactive-danger': ('background-color', 'danger action'),
    '--ds-border':             ('border-color',     ''),
    '--ds-border-subtle':      ('border-color',     'subtle border'),
    '--ds-border-emphasis':    ('border-color',     'emphasis border'),
    '--ds-border-focus':       ('outline-color',    'focus ring'),
    '--ds-border-success':     ('border-color',     'success state'),
    '--ds-border-danger':      ('border-color',     'error state'),
    '--ds-radius-sm':          ('border-radius',    'small'),
    '--ds-radius-md':          ('border-radius',    ''),
    '--ds-radius-lg':          ('border-radius',    'large'),
    '--ds-radius-xl':          ('border-radius',    'extra large'),
    '--ds-shadow-sm':          ('box-shadow',       'small elevation'),
    '--ds-shadow-md':          ('box-shadow',       'medium elevation'),
    '--ds-shadow-lg':          ('box-shadow',       'large elevation'),
}

DS_TOKEN_MAP = {
    "button":       "--ds-interactive, --ds-interactive-hover, --ds-interactive-fg",
    "card":         "--ds-bg, --ds-border, --ds-shadow-sm",
    "input":        "--ds-border, --ds-border-focus, --ds-text, --ds-bg",
    "select":       "--ds-border, --ds-border-focus, --ds-interactive",
    "checkbox":     "--ds-interactive, --ds-border",
    "radio-group":  "--ds-interactive, --ds-border",
    "badge":        "--ds-interactive, --ds-bg-muted, --ds-text-subtle",
    "alert":        "--ds-bg, --ds-border, --ds-text",
    "toast":        "--ds-bg-emphasis, --ds-text-inverse, --ds-shadow-lg",
    "sonner":       "--ds-bg-emphasis, --ds-text-inverse, --ds-shadow-lg",
    "dialog":       "--ds-bg, --ds-shadow-lg",
    "drawer":       "--ds-bg, --ds-shadow-lg",
    "sheet":        "--ds-bg, --ds-shadow-lg",
    "tabs":         "--ds-interactive, --ds-border",
    "tooltip":      "--ds-bg-emphasis, --ds-text-inverse",
    "popover":      "--ds-bg, --ds-border, --ds-shadow-md",
    "separator":    "--ds-border",
    "avatar":       "--ds-bg-muted, --ds-text-muted",
    "progress":     "--ds-interactive, --ds-bg-muted",
    "slider":       "--ds-interactive",
    "switch":       "--ds-interactive, --ds-bg-muted",
    "textarea":     "--ds-border, --ds-border-focus, --ds-text, --ds-bg",
    "table":        "--ds-border, --ds-bg-subtle, --ds-text",
    "typography":   "--ds-text, --ds-text-subtle",
    "skeleton":     "--ds-bg-muted",
    "accordion":    "--ds-border, --ds-text",
    "dropdown-menu":"--ds-bg, --ds-border, --ds-shadow-md",
    "context-menu": "--ds-bg, --ds-border, --ds-shadow-md",
    "menubar":      "--ds-bg, --ds-border",
    "navigation-menu": "--ds-bg, --ds-border, --ds-shadow-md",
    "calendar":     "--ds-interactive, --ds-border, --ds-bg",
    "kbd":          "--ds-bg-muted, --ds-border, --ds-text-muted",
    "hover-card":   "--ds-bg, --ds-border, --ds-shadow-md",
    "command":      "--ds-bg, --ds-border, --ds-shadow-md",
}


def read_ds_css(slug):
    """Return (css_content, relative_path) for this slug's AI DS CSS file, or (None, None)."""
    rel_path = DS_CSS_FILE_MAP.get(slug)
    if not rel_path:
        return None, None
    full_path = os.path.join(ROOT_DIR, rel_path)
    if not os.path.exists(full_path):
        return None, None
    try:
        with open(full_path, encoding='utf-8') as f:
            return f.read(), rel_path
    except OSError:
        return None, None


def make_css_section(slug, ds_tok_str, library_name, adapter_file):
    """Return a list of markdown lines for the '## AI Design System CSS' section."""
    css_content, css_path = read_ds_css(slug)
    parts = ["", "---", "", "## AI Design System CSS", ""]

    if css_content:
        parts += [
            f"Component classes from `{css_path}` — apply alongside the {library_name} component:",
            "",
            "```css",
            css_content.strip(),
            "```",
        ]
    else:
        snippet_lines = []
        if ds_tok_str and ds_tok_str != "—" and "{" not in ds_tok_str:
            raw_tokens = [t.strip() for t in re.split(r'[,;]', ds_tok_str)]
            seen_props = {}
            for tok in raw_tokens:
                m = re.match(r'(--ds-[a-z0-9-]+)', tok)
                if not m:
                    continue
                ds_var = m.group(1)
                layer2_var = DS_TO_LAYER2.get(ds_var)
                prop_info  = DS_TOKEN_CSS_PROP.get(ds_var)
                if not layer2_var or not prop_info:
                    continue
                css_prop, note = prop_info
                if css_prop not in seen_props:
                    seen_props[css_prop] = (layer2_var, ds_var, note)

            if seen_props:
                snippet_lines.append(f"/* Override {slug} appearance via AI Design System tokens */")
                snippet_lines.append(".your-selector {")
                for css_prop, (layer2_var, ds_var, note) in seen_props.items():
                    padded  = f"  {css_prop}:".ljust(24)
                    rhs     = f"var({layer2_var});"
                    comment = f"  /* {ds_var}{' — ' + note if note else ''} */"
                    snippet_lines.append(f"{padded}{rhs}{comment}")
                snippet_lines.append("}")

        if snippet_lines:
            parts += [
                f"No dedicated AI DS component file for `{slug}`. CSS override using the relevant Layer 2 tokens:",
                "",
                "```css",
                "\n".join(snippet_lines),
                "```",
            ]
        else:
            parts += [
                "Use `--color-*`, `--spacing-*`, and `--text-*` tokens for custom CSS overrides.",
                "See `specs/tokens/token-reference.md` for the full token reference.",
            ]

    parts += [
        "",
        f"Adapter: `{adapter_file}`  ",
        "Token reference: `specs/tokens/token-reference.md`",
    ]
    return parts


# ─── Component list ───────────────────────────────────────────────────────────

COMPONENTS = [
    "accordion", "alert", "alert-dialog", "aspect-ratio", "avatar",
    "badge", "breadcrumb", "button", "button-group", "calendar",
    "card", "carousel", "chart", "checkbox", "collapsible", "combobox",
    "command", "context-menu", "data-table", "date-picker", "dialog",
    "direction", "drawer", "dropdown-menu", "empty", "field",
    "hover-card", "input", "input-group", "input-otp", "item", "kbd",
    "label", "menubar", "native-select", "navigation-menu", "pagination",
    "popover", "progress", "radio-group", "resizable", "scroll-area",
    "select", "separator", "sheet", "sidebar", "skeleton", "slider",
    "sonner", "spinner", "switch", "table", "tabs", "textarea",
    "toast", "toggle", "toggle-group", "tooltip", "typography",
]

# ─── Accessibility knowledge base ────────────────────────────────────────────

A11Y = {
    "accordion": {
        "roles": "Trigger uses native `<button>`. Panel gets `role=\"region\"` with `aria-labelledby` pointing to the trigger.",
        "keyboard": (
            "| Key | Action |\n"
            "|-----|--------|\n"
            "| Enter / Space | Toggle panel open/closed |\n"
            "| Tab | Move focus to next focusable element |\n"
            "| Shift+Tab | Move focus to previous focusable element |\n"
            "| ArrowDown | Move focus to next trigger (vertical orientation) |\n"
            "| ArrowUp | Move focus to previous trigger |\n"
            "| Home | Move focus to first trigger |\n"
            "| End | Move focus to last trigger |"
        ),
        "aria": "`aria-expanded` on trigger; `aria-controls` → panel `id`; `aria-labelledby` on panel → trigger `id`.",
        "notes": "Follows the [WAI-ARIA Accordion](https://www.w3.org/WAI/ARIA/apg/patterns/accordion/) design pattern.",
    },
    "alert": {
        "roles": "Root renders a `<div>`. For urgent announcements add `role=\"alert\"` (live region); for non-urgent use `role=\"status\"`.",
        "keyboard": "No keyboard interaction — alert is passive content.",
        "aria": "`aria-live=\"assertive\"` (or `polite`) when used as a live region.",
        "notes": "The `AlertTitle` and `AlertDescription` sub-components provide semantic structure.",
    },
    "alert-dialog": {
        "roles": "`role=\"alertdialog\"` on the dialog container; `aria-modal=\"true\"` to confine AT to the dialog.",
        "keyboard": (
            "| Key | Action |\n"
            "|-----|--------|\n"
            "| Tab | Cycle focus through interactive elements inside the dialog |\n"
            "| Shift+Tab | Cycle focus backwards |\n"
            "| Enter | Confirm action |\n"
            "| Escape | Close dialog (cancel) |"
        ),
        "aria": "`aria-labelledby` → `AlertDialogTitle` id; `aria-describedby` → `AlertDialogDescription` id.",
        "notes": "Focus is trapped inside the dialog while open. Focus returns to the trigger on close. Unlike `Dialog`, pressing Escape does **not** close the alert dialog by default — the user must click an action button.",
    },
    "aspect-ratio": {
        "roles": "No ARIA roles — purely a layout utility.",
        "keyboard": "Not interactive.",
        "aria": "None.",
        "notes": "Wrap meaningful media (images, videos) in a `<figure>` with a `<figcaption>` for screen reader context.",
    },
    "avatar": {
        "roles": "Uses an `<img>` element internally. The fallback renders text.",
        "keyboard": "Not interactive unless wrapped in a button.",
        "aria": "Add `alt` text to the image via the `src` when meaningful. Set `alt=\"\"` (empty string) for decorative avatars.",
        "notes": "The `AvatarFallback` is shown while the image loads or if it fails. Ensure text initials are surrounded by a visually hidden label when the avatar represents a person.",
    },
    "badge": {
        "roles": "Renders as a `<div>` (or `<span>` depending on usage). No implicit ARIA role.",
        "keyboard": "Not interactive unless `asChild` is used with an anchor or button.",
        "aria": "Add `aria-label` when badge content alone is insufficient for context (e.g., a numeric count).",
        "notes": "Use the `asChild` prop to render a `<Link>` styled as a badge for navigation.",
    },
    "breadcrumb": {
        "roles": "Wraps in `<nav aria-label=\"breadcrumb\">`. Items in `<ol>` list. Current page item uses `aria-current=\"page\"`.",
        "keyboard": (
            "| Key | Action |\n"
            "|-----|--------|\n"
            "| Tab | Move focus to each link |\n"
            "| Enter | Follow the link |"
        ),
        "aria": "`aria-label=\"breadcrumb\"` on `<nav>`; `aria-current=\"page\"` on last breadcrumb item.",
        "notes": "Separators (chevrons, slashes) should be hidden with `aria-hidden=\"true\"`. Collapsed breadcrumbs (ellipsis) should expose an expand control.",
    },
    "button": {
        "roles": "Renders a native `<button>` element. When `asChild` is used the role is inherited from the child element.",
        "keyboard": (
            "| Key | Action |\n"
            "|-----|--------|\n"
            "| Enter | Activate button |\n"
            "| Space | Activate button |"
        ),
        "aria": "`aria-disabled=\"true\"` when logically disabled but still focusable. `aria-busy=\"true\"` for loading states.",
        "notes": "Tailwind v4 sets `cursor: default` on buttons; add `cursor: pointer` via global CSS if needed. Use `variant=\"ghost\"` or `variant=\"link\"` for low-emphasis actions.",
    },
    "button-group": {
        "roles": "Container renders with `role=\"group\"` and an `aria-label` describing the group.",
        "keyboard": "Each child Button follows standard button keyboard interaction.",
        "aria": "`aria-label` on the group describes the collective purpose.",
        "notes": "Use `orientation=\"vertical\"` for stacked groups. Adjacent buttons share border styling automatically.",
    },
    "calendar": {
        "roles": "`role=\"grid\"` on the calendar table; `role=\"gridcell\"` on each day; `role=\"button\"` on selectable days.",
        "keyboard": (
            "| Key | Action |\n"
            "|-----|--------|\n"
            "| ArrowLeft/Right | Move one day backward/forward |\n"
            "| ArrowUp/Down | Move one week backward/forward |\n"
            "| PageUp/PageDown | Move one month backward/forward |\n"
            "| Shift+PageUp/PageDown | Move one year backward/forward |\n"
            "| Home | Move to start of week |\n"
            "| End | Move to end of week |\n"
            "| Enter / Space | Select focused day |\n"
            "| Escape | Close calendar (if in a popover) |"
        ),
        "aria": "`aria-label` on the grid; `aria-selected` on selected day(s); `aria-disabled` on unavailable days.",
        "notes": "Built on `react-day-picker`. Supports single, multiple, and range selection modes.",
    },
    "card": {
        "roles": "No implicit ARIA role — renders a `<div>`. For article-like content use a semantic `<article>` element via `asChild`.",
        "keyboard": "Not interactive by default. Interactive cards should add `tabindex=\"0\"`, `role=\"button\"` or `role=\"link\"`, and appropriate keyboard handlers.",
        "aria": "None by default. `aria-labelledby` can point to the `CardTitle` id when the card represents a named region.",
        "notes": "For purely decorative or layout cards no ARIA is needed.",
    },
    "carousel": {
        "roles": "`role=\"region\"` with `aria-label` (e.g. \"Product gallery\") on the carousel root; `aria-roledescription=\"carousel\"`. Each slide: `role=\"group\"`, `aria-roledescription=\"slide\"`, `aria-label=\"n of N\"`.",
        "keyboard": (
            "| Key | Action |\n"
            "|-----|--------|\n"
            "| Tab | Move to previous/next button or slide content |\n"
            "| Enter / Space | Activate previous or next button |"
        ),
        "aria": "Previous/Next buttons: `aria-label=\"Previous slide\"` / `aria-label=\"Next slide\"`. Add a live region `aria-live=\"polite\"` to announce slide changes.",
        "notes": "Auto-playing carousels should pause on focus or hover. Always provide pause/play controls.",
    },
    "chart": {
        "roles": "Wraps recharts. The SVG should carry `role=\"img\"` with `aria-label` describing the chart data.",
        "keyboard": "Not keyboard interactive by default.",
        "aria": "`aria-label` or `aria-labelledby` on the chart container. For complex charts provide a data table alternative.",
        "notes": "Consider adding a visually hidden `<table>` version of the chart data for screen readers.",
    },
    "checkbox": {
        "roles": "`role=\"checkbox\"` (provided by Radix Checkbox). `aria-checked`: `true`, `false`, or `mixed`.",
        "keyboard": (
            "| Key | Action |\n"
            "|-----|--------|\n"
            "| Space | Toggle checked state |\n"
            "| Tab | Move focus to next focusable element |"
        ),
        "aria": "`aria-checked` (managed by Radix); `aria-required`; `aria-invalid`; associate with a `<Label>` via `htmlFor` / `id` pair.",
        "notes": "Use `checked` (controlled) or `defaultChecked` (uncontrolled). `indeterminate` prop sets `aria-checked=\"mixed\"`.",
    },
    "collapsible": {
        "roles": "Trigger: native `<button>` with `aria-expanded`; Content: hidden/shown via CSS.",
        "keyboard": (
            "| Key | Action |\n"
            "|-----|--------|\n"
            "| Enter / Space | Toggle open/closed |\n"
            "| Tab | Move focus through interactive elements inside |"
        ),
        "aria": "`aria-expanded` on trigger; `aria-controls` → content id; content uses `hidden` attribute when collapsed.",
        "notes": "Unlike Accordion, Collapsible manages a single disclosure. No roving tabindex.",
    },
    "combobox": {
        "roles": "Input: `role=\"combobox\"`, `aria-expanded`, `aria-autocomplete=\"list\"`, `aria-controls` → listbox id. Listbox: `role=\"listbox\"`. Options: `role=\"option\"`, `aria-selected`.",
        "keyboard": (
            "| Key | Action |\n"
            "|-----|--------|\n"
            "| ArrowDown | Open list / move to next option |\n"
            "| ArrowUp | Move to previous option |\n"
            "| Enter | Select focused option |\n"
            "| Escape | Close list / clear selection |\n"
            "| Home | Move to first option |\n"
            "| End | Move to last option |\n"
            "| Any character | Filter list |"
        ),
        "aria": "`aria-labelledby` links input to its label; `aria-activedescendant` tracks focused option in listbox.",
        "notes": "Built on top of the Command component. Follows the [ARIA Combobox](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/) pattern.",
    },
    "command": {
        "roles": "`role=\"dialog\"` (if modal); inner input `role=\"searchbox\"` or `role=\"combobox\"`; results list `role=\"listbox\"`; items `role=\"option\"`.",
        "keyboard": (
            "| Key | Action |\n"
            "|-----|--------|\n"
            "| ArrowDown / ArrowUp | Navigate list items |\n"
            "| Enter | Select highlighted item |\n"
            "| Escape | Close dialog / clear input |\n"
            "| Any character | Filter items |"
        ),
        "aria": "`aria-label` on the dialog; `aria-activedescendant` on the input pointing to highlighted item.",
        "notes": "Built on `cmdk`. Renders an accessible command palette / search interface.",
    },
    "context-menu": {
        "roles": "Menu: `role=\"menu\"`; items: `role=\"menuitem\"`, `role=\"menuitemcheckbox\"`, `role=\"menuitemradio\"`. Triggered by right-click (no ARIA trigger role needed on the trigger element itself).",
        "keyboard": (
            "| Key | Action |\n"
            "|-----|--------|\n"
            "| ArrowDown / ArrowUp | Move between menu items |\n"
            "| ArrowRight | Open submenu |\n"
            "| ArrowLeft | Close submenu / return to parent |\n"
            "| Enter / Space | Activate item |\n"
            "| Escape | Close menu |\n"
            "| Home / End | Move to first / last item |"
        ),
        "aria": "Sub-menus: trigger has `aria-haspopup=\"menu\"` and `aria-expanded`. Menu items with sub-menus: `aria-haspopup=\"menu\"`.",
        "notes": "Also accessible via keyboard: focus the trigger element and press Shift+F10 or the application key to open the context menu.",
    },
    "data-table": {
        "roles": "`role=\"table\"` (or native `<table>`); `role=\"rowgroup\"`, `role=\"row\"`, `role=\"columnheader\"`, `role=\"cell\"`.",
        "keyboard": (
            "| Key | Action |\n"
            "|-----|--------|\n"
            "| Tab | Navigate interactive cells and controls |\n"
            "| Enter / Space | Activate row checkbox or sort header |"
        ),
        "aria": "Sortable columns: `aria-sort=\"ascending\"` / `\"descending\"` / `\"none\"`. Selected rows: `aria-selected=\"true\"`.",
        "notes": "Built on TanStack Table. For complex grids consider `role=\"grid\"` with roving tabindex for cell navigation.",
    },
    "date-picker": {
        "roles": "Composed of `Popover` + `Calendar`. Trigger: `role=\"button\"`. Calendar: `role=\"grid\"`. See Calendar and Popover accessibility.",
        "keyboard": "See Calendar and Popover keyboard navigation.",
        "aria": "`aria-label` on the popover trigger (e.g., \"Pick a date\"). `aria-haspopup=\"dialog\"` on trigger.",
        "notes": "Date picker is a composition pattern, not a standalone component. Combines Popover for the flyout and Calendar for selection.",
    },
    "dialog": {
        "roles": "`role=\"dialog\"` on the dialog panel; `aria-modal=\"true\"` to tell AT to ignore background content.",
        "keyboard": (
            "| Key | Action |\n"
            "|-----|--------|\n"
            "| Escape | Close dialog |\n"
            "| Tab | Cycle focus through interactive elements inside |\n"
            "| Shift+Tab | Cycle focus backwards |"
        ),
        "aria": "`aria-labelledby` → `DialogTitle` id; `aria-describedby` → `DialogDescription` id.",
        "notes": "Focus is trapped inside the dialog while open. Focus returns to the trigger element on close. Overlay click closes the dialog by default.",
    },
    "direction": {
        "roles": "Wraps content with a `dir` attribute (`ltr` or `rtl`) at the provider level.",
        "keyboard": "No keyboard interaction. Configures directionality for all child Radix components.",
        "aria": "`dir=\"rtl\"` / `dir=\"ltr\"` on the container.",
        "notes": "Integrates with Radix DirectionProvider to flip geometric props (e.g., start/end) for RTL layouts.",
    },
    "drawer": {
        "roles": "`role=\"dialog\"`, `aria-modal=\"true\"` — same semantics as Dialog but with a slide-in animation.",
        "keyboard": (
            "| Key | Action |\n"
            "|-----|--------|\n"
            "| Escape | Close drawer |\n"
            "| Tab | Cycle focus inside |\n"
            "| Shift+Tab | Cycle backwards |"
        ),
        "aria": "`aria-labelledby` → `DrawerTitle` id; `aria-describedby` → `DrawerDescription` id.",
        "notes": "Built on `vaul`. Supports swipe-to-close on touch devices. Focus trap and return on close.",
    },
    "dropdown-menu": {
        "roles": "Trigger: `aria-haspopup=\"menu\"`, `aria-expanded`. Menu: `role=\"menu\"`. Items: `role=\"menuitem\"`, `role=\"menuitemcheckbox\"`, `role=\"menuitemradio\"`.",
        "keyboard": (
            "| Key | Action |\n"
            "|-----|--------|\n"
            "| Enter / Space / ArrowDown | Open menu |\n"
            "| ArrowDown / ArrowUp | Navigate menu items |\n"
            "| ArrowRight | Open submenu |\n"
            "| ArrowLeft / Escape | Close submenu / menu |\n"
            "| Enter / Space | Activate item |\n"
            "| Home / End | Move to first / last item |"
        ),
        "aria": "Groups: `role=\"group\"` with `aria-label`. Separators: `role=\"separator\"`. Checked items: `aria-checked=\"true\"`.",
        "notes": "Built on Radix DropdownMenu. Follows the [WAI-ARIA Menu Button](https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/) pattern.",
    },
    "empty": {
        "roles": "No implicit ARIA role — a layout component for empty states.",
        "keyboard": "Not interactive.",
        "aria": "If the empty state is a response to user action, wrap in `role=\"status\"` with an appropriate `aria-label`.",
        "notes": "Typically pairs with an illustration, heading, description, and a call-to-action button.",
    },
    "field": {
        "roles": "A form field wrapper that associates a label, input, and hint/error messages.",
        "keyboard": "Focus follows standard input keyboard behavior.",
        "aria": "`aria-describedby` on the input pointing to the hint/error message id. `aria-invalid=\"true\"` on the input when there is an error.",
        "notes": "Use `FieldLabel`, `FieldControl`, `FieldDescription`, and `FieldMessage` sub-components for a fully accessible form field.",
    },
    "hover-card": {
        "roles": "Content: `role=\"dialog\"` (Radix treats it as a non-modal dialog-like surface).",
        "keyboard": "Opens on hover (pointer) or focus. Keyboard users can access via Tab to trigger focus.",
        "aria": "`aria-haspopup` on trigger. Content is announced when it appears.",
        "notes": "Hover Card content should not be the only way to access important information since it requires pointer hover.",
    },
    "input": {
        "roles": "Native `<input>` element — role is derived from `type` (e.g., `textbox`, `search`).",
        "keyboard": "Standard browser keyboard interaction for text inputs.",
        "aria": "`aria-invalid` (error state); `aria-required`; `aria-disabled`; `aria-describedby` → hint/error id. Associate with `<label>` via `id` / `htmlFor`.",
        "notes": "Always pair with a visible `<Label>` component. Use `aria-label` only when a visible label cannot be provided.",
    },
    "input-group": {
        "roles": "Wraps an input with prefix/suffix addons. No implicit ARIA role on the group.",
        "keyboard": "Standard input and button keyboard interaction.",
        "aria": "Addons that are buttons should have `aria-label`. Prefix/suffix text can be associated via `aria-describedby`.",
        "notes": "For icon-only addons always include a visually hidden text or `aria-label`.",
    },
    "input-otp": {
        "roles": "Renders a series of single-character inputs grouped as one logical OTP field. Uses a hidden actual `<input>` for value management.",
        "keyboard": (
            "| Key | Action |\n"
            "|-----|--------|\n"
            "| Any digit (0-9) | Enter digit and advance focus |\n"
            "| Backspace | Delete current digit and move back |\n"
            "| ArrowLeft / ArrowRight | Move between slots |\n"
            "| Ctrl+V / Cmd+V | Paste entire code |"
        ),
        "aria": "`aria-label` on the input group (e.g., \"One-time passcode\"). Individual slots are decorative.",
        "notes": "Built on `input-otp`. Screen readers announce the hidden input value; the slots are `aria-hidden`.",
    },
    "item": {
        "roles": "Generic list item component. Role depends on context (e.g., `role=\"listitem\"` inside a list).",
        "keyboard": "Varies by context.",
        "aria": "Depends on parent container and usage.",
        "notes": "Used as a building block inside Command, Select, and Dropdown components.",
    },
    "kbd": {
        "roles": "Renders a `<kbd>` HTML element — semantically represents a keyboard key.",
        "keyboard": "Not interactive.",
        "aria": "Screen readers announce `<kbd>` content as keyboard text. No additional ARIA needed.",
        "notes": "Can be nested: `<kbd><kbd>Ctrl</kbd>+<kbd>K</kbd></kbd>` for chord shortcuts.",
    },
    "label": {
        "roles": "Renders a `<label>` element.",
        "keyboard": "Clicking a label moves focus to its associated control.",
        "aria": "Associate with a form control via `htmlFor` matching the control's `id`. Or wrap the control inside the label.",
        "notes": "Radix Label prevents text selection on double-click, improving UX for checkboxes and radio buttons.",
    },
    "menubar": {
        "roles": "`role=\"menubar\"` on the root; `role=\"menu\"` on each sub-menu; `role=\"menuitem\"`, `role=\"menuitemcheckbox\"`, `role=\"menuitemradio\"` on items.",
        "keyboard": (
            "| Key | Action |\n"
            "|-----|--------|\n"
            "| Tab / Shift+Tab | Move focus to/from menubar |\n"
            "| ArrowRight / ArrowLeft | Move between top-level menu triggers |\n"
            "| ArrowDown / Enter / Space | Open sub-menu |\n"
            "| ArrowUp | Close sub-menu |\n"
            "| Escape | Close sub-menu and return focus |\n"
            "| Home / End | Move to first / last item in menu |"
        ),
        "aria": "Follows the [WAI-ARIA Menu](https://www.w3.org/WAI/ARIA/apg/patterns/menubar/) design pattern.",
        "notes": "Top-level triggers have `aria-haspopup=\"menu\"` and `aria-expanded`.",
    },
    "native-select": {
        "roles": "Native `<select>` element — inherits browser listbox semantics.",
        "keyboard": "Standard browser keyboard interaction (Space/Enter to open, Arrow keys to navigate, Enter to select).",
        "aria": "Associate with `<label>` via `htmlFor` / `id`. `aria-invalid` for errors. `aria-required` for required fields.",
        "notes": "Unlike the custom Select component, NativeSelect uses the browser's native select UI, which is fully accessible by default and preferred on mobile.",
    },
    "navigation-menu": {
        "roles": "Root: `<nav>` with `aria-label`. Triggers: `role=\"button\"`, `aria-haspopup=\"true\"`, `aria-expanded`. Content: `role=\"group\"`.",
        "keyboard": (
            "| Key | Action |\n"
            "|-----|--------|\n"
            "| Tab | Move focus through menu items |\n"
            "| Enter / Space | Open sub-menu or activate link |\n"
            "| Escape | Close open sub-menu |\n"
            "| ArrowDown / ArrowUp | Navigate within an open sub-menu |"
        ),
        "aria": "Built on Radix NavigationMenu. Follows the [Disclosure Navigation Menu](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/examples/disclosure-navigation/) pattern.",
        "notes": "Use `aria-label` on `NavigationMenuList` to differentiate multiple nav regions on a page.",
    },
    "pagination": {
        "roles": "Wraps in `<nav aria-label=\"pagination\">`. Previous/Next and page number links are `<a>` elements.",
        "keyboard": (
            "| Key | Action |\n"
            "|-----|--------|\n"
            "| Tab | Move between page links |\n"
            "| Enter | Navigate to the link's target page |"
        ),
        "aria": "`aria-current=\"page\"` on the active page link. `aria-label=\"Go to page N\"` on individual page links. `aria-disabled` on unavailable links (e.g., Previous on first page).",
        "notes": "Screen readers announce the nav landmark and aria-label. Ellipsis items (`PaginationEllipsis`) should be `aria-hidden`.",
    },
    "popover": {
        "roles": "`role=\"dialog\"` on the content panel (Radix Popover); trigger has `aria-haspopup=\"dialog\"` and `aria-expanded`.",
        "keyboard": (
            "| Key | Action |\n"
            "|-----|--------|\n"
            "| Enter / Space | Open popover |\n"
            "| Tab | Move focus into / through popover content |\n"
            "| Escape | Close popover |"
        ),
        "aria": "`aria-labelledby` if popover has a visible title. Focus moves into the popover on open and returns to trigger on close.",
        "notes": "Unlike Dialog, Popover does not trap focus — Tab can leave the popover. Use Dialog for content requiring full focus trap.",
    },
    "progress": {
        "roles": "`role=\"progressbar\"`.",
        "keyboard": "Not interactive.",
        "aria": "`aria-valuenow` (current value); `aria-valuemin` (default `0`); `aria-valuemax` (default `100`); `aria-label` or `aria-labelledby` for the label; `aria-valuetext` for human-readable value (e.g., \"Loading 42%\").",
        "notes": "Set `aria-valuetext` when a raw number is not sufficient context (e.g., \"Step 2 of 5\").",
    },
    "radio-group": {
        "roles": "`role=\"radiogroup\"` on the group; `role=\"radio\"` on each item; `aria-checked=\"true\"` on selected item.",
        "keyboard": (
            "| Key | Action |\n"
            "|-----|--------|\n"
            "| Tab | Move focus into the group |\n"
            "| ArrowDown / ArrowRight | Move to next radio (and select) |\n"
            "| ArrowUp / ArrowLeft | Move to previous radio (and select) |\n"
            "| Space | Select focused radio |"
        ),
        "aria": "`aria-labelledby` on the group pointing to the group label id.",
        "notes": "Only one radio in the group is in the tab sequence at a time (roving tabindex). Follows [WAI-ARIA Radio Group](https://www.w3.org/WAI/ARIA/apg/patterns/radio/) pattern.",
    },
    "resizable": {
        "roles": "Handle: `role=\"separator\"`, `aria-orientation` (`\"horizontal\"` or `\"vertical\"`), `aria-valuenow`, `aria-valuemin`, `aria-valuemax`, `aria-valuetext`.",
        "keyboard": (
            "| Key | Action |\n"
            "|-----|--------|\n"
            "| ArrowLeft/Right | Adjust horizontal panel size |\n"
            "| ArrowUp/Down | Adjust vertical panel size |\n"
            "| Home | Collapse or go to minimum size |\n"
            "| End | Expand or go to maximum size |"
        ),
        "aria": "`aria-label` on the handle (e.g., \"Resize panel\").",
        "notes": "Built on `react-resizable-panels`. Keyboard resizing follows the [WAI-ARIA Window Splitter](https://www.w3.org/WAI/ARIA/apg/patterns/windowsplitter/) pattern.",
    },
    "scroll-area": {
        "roles": "Custom scrollable viewport with styled scrollbar tracks. Scrollbar: `role=\"scrollbar\"`, `aria-orientation`, `aria-valuenow`, `aria-valuemin`, `aria-valuemax`, `aria-controls`.",
        "keyboard": "Standard browser scroll keyboard interactions (Arrow keys, PageUp/Down, Home/End) work within the viewport.",
        "aria": "The scrollbar thumb is interactive and announces position to assistive technology.",
        "notes": "Built on Radix ScrollArea. Provides cross-browser consistent scroll styling while maintaining native scroll behavior.",
    },
    "select": {
        "roles": "Trigger: `role=\"combobox\"`, `aria-haspopup=\"listbox\"`, `aria-expanded`. Content: `role=\"listbox\"`. Items: `role=\"option\"`, `aria-selected`.",
        "keyboard": (
            "| Key | Action |\n"
            "|-----|--------|\n"
            "| Space | Open select |\n"
            "| ArrowDown / ArrowUp | Navigate options |\n"
            "| Enter | Select focused option |\n"
            "| Escape | Close without selecting |\n"
            "| Home / End | Move to first / last option |\n"
            "| Any character | Jump to option starting with that character |"
        ),
        "aria": "`aria-labelledby` on the trigger pointing to the label. `aria-activedescendant` tracks the focused option.",
        "notes": "Follows the [ARIA Listbox](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/) pattern.",
    },
    "separator": {
        "roles": "`role=\"separator\"` with `aria-orientation` (`\"horizontal\"` or `\"vertical\"`). Use `role=\"presentation\"` for decorative separators.",
        "keyboard": "Not interactive.",
        "aria": "Decorative separators should have `aria-hidden=\"true\"`.",
        "notes": "Use `decorative` prop (when available) or `aria-hidden` to hide purely visual separators from screen readers.",
    },
    "sheet": {
        "roles": "`role=\"dialog\"`, `aria-modal=\"true\"` — a Dialog variant that slides in from a side.",
        "keyboard": (
            "| Key | Action |\n"
            "|-----|--------|\n"
            "| Escape | Close sheet |\n"
            "| Tab | Cycle focus inside |\n"
            "| Shift+Tab | Cycle focus backwards |"
        ),
        "aria": "`aria-labelledby` → `SheetTitle` id; `aria-describedby` → `SheetDescription` id.",
        "notes": "Focus is trapped inside while open. Focus returns to the trigger on close. Supports `side` prop (`top`, `bottom`, `left`, `right`).",
    },
    "sidebar": {
        "roles": "Renders a `<nav>` (or `<aside>`) landmark depending on role. Toggle button has `aria-expanded` and `aria-controls` → sidebar id.",
        "keyboard": (
            "| Key | Action |\n"
            "|-----|--------|\n"
            "| Tab | Move focus through sidebar links and controls |\n"
            "| Escape | Close sidebar (when open as an overlay) |"
        ),
        "aria": "`aria-label` on the nav element. `aria-hidden=\"true\"` on the collapsed sidebar icon bar if only decorative icons are shown.",
        "notes": "Supports collapsible, icon-only, and floating variants. Use keyboard shortcut `Ctrl+B` (configurable) to toggle.",
    },
    "skeleton": {
        "roles": "No implicit ARIA role on skeleton elements.",
        "keyboard": "Not interactive.",
        "aria": "Wrap the skeleton region in `role=\"status\"` with `aria-label=\"Loading…\"` and `aria-busy=\"true\"`. Remove `aria-busy` when loading is complete.",
        "notes": "Skeleton components are purely visual loading placeholders. Announce loading state via a live region, not the skeleton itself.",
    },
    "slider": {
        "roles": "`role=\"slider\"` on the thumb.",
        "keyboard": (
            "| Key | Action |\n"
            "|-----|--------|\n"
            "| ArrowRight / ArrowUp | Increase value by one step |\n"
            "| ArrowLeft / ArrowDown | Decrease value by one step |\n"
            "| PageUp | Increase value by a large step |\n"
            "| PageDown | Decrease value by a large step |\n"
            "| Home | Set to minimum value |\n"
            "| End | Set to maximum value |"
        ),
        "aria": "`aria-valuenow`; `aria-valuemin`; `aria-valuemax`; `aria-label` or `aria-labelledby`; `aria-valuetext` for human-readable value.",
        "notes": "Follows the [WAI-ARIA Slider](https://www.w3.org/WAI/ARIA/apg/patterns/slider/) pattern. Range sliders have two thumbs, each with their own `aria-*` props.",
    },
    "sonner": {
        "roles": "Toast region: `role=\"region\"`, `aria-label=\"Notifications\"`, `aria-live=\"polite\"`, `aria-atomic=\"false\"`.",
        "keyboard": (
            "| Key | Action |\n"
            "|-----|--------|\n"
            "| Tab | Focus toast |\n"
            "| Escape | Dismiss focused toast |"
        ),
        "aria": "Individual toasts use `role=\"status\"` (informational) or `role=\"alert\"` (urgent). Action buttons inside are keyboard focusable.",
        "notes": "Built on the `sonner` library. Toasts are announced by screen readers without stealing focus. Toasts with actions should have sufficient display time.",
    },
    "spinner": {
        "roles": "`role=\"status\"` or simply render as `aria-hidden=\"true\"` alongside a visible loading label.",
        "keyboard": "Not interactive.",
        "aria": "`aria-label=\"Loading…\"` when spinner is the only loading indicator. Otherwise `aria-hidden=\"true\"` and use a separate live region.",
        "notes": "For button loading states: add `aria-busy=\"true\"` to the button and render a `<Spinner data-icon=\"inline-start\"/>` inside.",
    },
    "switch": {
        "roles": "`role=\"switch\"`, `aria-checked=\"true\"` / `\"false\"`.",
        "keyboard": (
            "| Key | Action |\n"
            "|-----|--------|\n"
            "| Space | Toggle on/off |\n"
            "| Enter | Toggle on/off (when used in a form) |"
        ),
        "aria": "Associate with a `<Label>` via `htmlFor` / `id`. `aria-required`; `aria-disabled`.",
        "notes": "Follows the [WAI-ARIA Switch](https://www.w3.org/WAI/ARIA/apg/patterns/switch/) pattern. Semantically different from Checkbox: Switch represents binary on/off, Checkbox represents checked/unchecked selection.",
    },
    "table": {
        "roles": "Uses native HTML table elements: `<table>`, `<thead>`, `<tbody>`, `<tfoot>`, `<tr>`, `<th>`, `<td>`, `<caption>`.",
        "keyboard": "Not interactive by default. Interactive cells (checkboxes, buttons) are keyboard focusable per their own role.",
        "aria": "`scope=\"col\"` / `scope=\"row\"` on `<th>`. Add `<caption>` or `aria-label` / `aria-labelledby` to describe the table. Sortable headers: `aria-sort`.",
        "notes": "Use the DataTable component for tables with sorting, filtering, and pagination. Prefer native HTML table elements over ARIA table roles.",
    },
    "tabs": {
        "roles": "TabsList: `role=\"tablist\"`. Tab: `role=\"tab\"`, `aria-selected`, `aria-controls` → panel id. TabsContent: `role=\"tabpanel\"`, `aria-labelledby` → tab id.",
        "keyboard": (
            "| Key | Action |\n"
            "|-----|--------|\n"
            "| ArrowRight / ArrowLeft | Move to next / previous tab |\n"
            "| Home | Move to first tab |\n"
            "| End | Move to last tab |\n"
            "| Space / Enter | Activate tab (if not auto-activated) |\n"
            "| Tab | Move focus into the tab panel |"
        ),
        "aria": "Follows the [WAI-ARIA Tabs](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/) pattern. Supports both `activationMode=\"automatic\"` and `manual`.",
        "notes": "Only the active tab is in the tab sequence; inactive tabs use arrow keys (roving tabindex).",
    },
    "textarea": {
        "roles": "Native `<textarea>` element — `role=\"textbox\"` with `aria-multiline=\"true\"`.",
        "keyboard": "Standard browser keyboard interaction for multiline text areas.",
        "aria": "`aria-invalid`, `aria-required`, `aria-disabled`, `aria-describedby` → hint/error id. Associate with `<label>` via `htmlFor` / `id`.",
        "notes": "Always pair with a visible `<Label>`. Use `resize` CSS property to control resizing behavior.",
    },
    "toast": {
        "roles": "Toast region: `role=\"region\"`, `aria-live`. Individual toast: `role=\"alert\"` (urgent) or `role=\"status\"` (informational).",
        "keyboard": (
            "| Key | Action |\n"
            "|-----|--------|\n"
            "| Tab | Focus toast and action |\n"
            "| Escape / close button | Dismiss toast |"
        ),
        "aria": "`aria-live=\"assertive\"` for destructive / urgent toasts; `aria-live=\"polite\"` for informational. `aria-atomic=\"true\"` when the entire toast should be re-read on update.",
        "notes": "Legacy toast component — prefer `Sonner` for new projects. Toasts should not require interaction to dismiss if content is important.",
    },
    "toggle": {
        "roles": "`role=\"button\"`, `aria-pressed=\"true\"` / `\"false\"` (or `\"mixed\"`).",
        "keyboard": (
            "| Key | Action |\n"
            "|-----|--------|\n"
            "| Enter / Space | Toggle pressed state |"
        ),
        "aria": "`aria-pressed` to communicate toggle state. `aria-label` when button label does not clearly describe the action.",
        "notes": "Follows the [WAI-ARIA Toggle Button](https://www.w3.org/WAI/ARIA/apg/patterns/button/) pattern.",
    },
    "toggle-group": {
        "roles": "`role=\"group\"` with `aria-label` on the group container. Each toggle: `role=\"radio\"` (single) or `role=\"checkbox\"` (multiple) — or `role=\"button\"` with `aria-pressed`.",
        "keyboard": (
            "| Key | Action |\n"
            "|-----|--------|\n"
            "| ArrowRight / ArrowLeft | Navigate toggles (single type, roving tabindex) |\n"
            "| Space | Activate / deactivate toggle (multiple type) |\n"
            "| Enter | Activate toggle |"
        ),
        "aria": "`aria-label` on the group describing the group's purpose.",
        "notes": "Use `type=\"single\"` for exclusive selection and `type=\"multiple\"` for multi-select.",
    },
    "tooltip": {
        "roles": "Tooltip content: `role=\"tooltip\"`. Trigger references it via `aria-describedby`.",
        "keyboard": (
            "| Key | Action |\n"
            "|-----|--------|\n"
            "| Tab | Focus trigger (tooltip appears) |\n"
            "| Escape | Dismiss tooltip |"
        ),
        "aria": "`aria-describedby` on the trigger pointing to the tooltip id. Tooltip content is supplemental — the trigger must be independently understandable.",
        "notes": "Tooltip text should supplement, not replace, visible labels. Avoid putting interactive content (links, buttons) inside a tooltip.",
    },
    "typography": {
        "roles": "Applies semantic HTML elements: `<h1>`–`<h6>`, `<p>`, `<blockquote>`, `<ul>`, `<ol>`, `<li>`, `<code>`, `<pre>`, `<table>`.",
        "keyboard": "Standard browser behavior for interactive elements within prose.",
        "aria": "Semantic HTML provides implicit ARIA roles. Ensure heading hierarchy is logical (h1 → h2 → h3).",
        "notes": "The `prose` class (Tailwind Typography plugin) or the shadcn/ui typography utilities apply consistent typography to any block of HTML content.",
    },
}

# ─── Tailwind token knowledge ─────────────────────────────────────────────────

TAILWIND_TOKENS = {
    "accordion": {
        "vars": ["--radius", "--border", "--muted", "--foreground", "--muted-foreground"],
        "classes": ["border-b", "px-4", "py-2", "font-medium", "text-sm", "text-muted-foreground", "hover:underline"],
        "notes": "Trigger underline on hover; content hidden/shown with data attributes.",
    },
    "alert": {
        "vars": ["--background", "--foreground", "--border", "--destructive", "--destructive-foreground", "--radius"],
        "classes": ["relative", "rounded-lg", "border", "p-4", "bg-background", "text-foreground", "text-destructive"],
        "notes": "`variant=\"destructive\"` uses `--destructive` color tokens.",
    },
    "alert-dialog": {
        "vars": ["--background", "--foreground", "--border", "--radius", "--destructive", "--muted"],
        "classes": ["fixed", "inset-0", "z-50", "bg-black/80", "rounded-lg", "shadow-lg", "p-6"],
        "notes": "Overlay uses `bg-black/80`. Dialog panel uses `--background`.",
    },
    "aspect-ratio": {
        "vars": [],
        "classes": ["relative", "overflow-hidden"],
        "notes": "Uses `aspect-ratio` CSS property via Radix AspectRatio. No color tokens.",
    },
    "avatar": {
        "vars": ["--muted", "--muted-foreground", "--radius"],
        "classes": ["relative", "flex", "h-10", "w-10", "shrink-0", "overflow-hidden", "rounded-full", "bg-muted", "text-muted-foreground"],
        "notes": "Fallback uses `--muted` background and `--muted-foreground` text.",
    },
    "badge": {
        "vars": ["--primary", "--primary-foreground", "--secondary", "--secondary-foreground", "--destructive", "--destructive-foreground", "--border", "--radius"],
        "classes": ["inline-flex", "items-center", "rounded-md", "border", "px-2.5", "py-0.5", "text-xs", "font-semibold", "transition-colors"],
        "notes": "Variants: `default` (--primary), `secondary`, `destructive`, `outline`.",
    },
    "breadcrumb": {
        "vars": ["--foreground", "--muted-foreground", "--border"],
        "classes": ["flex", "flex-wrap", "items-center", "gap-1.5", "text-sm", "text-muted-foreground"],
        "notes": "Current page item uses `text-foreground font-normal`. Separator is `aria-hidden`.",
    },
    "button": {
        "vars": ["--primary", "--primary-foreground", "--secondary", "--secondary-foreground", "--destructive", "--muted", "--foreground", "--border", "--ring", "--radius", "--radius-md"],
        "classes": ["inline-flex", "items-center", "justify-center", "whitespace-nowrap", "rounded-lg", "text-sm", "font-medium", "transition-all", "focus-visible:ring-3", "disabled:opacity-50"],
        "notes": "Variant styles from Nova CSS: `cn-button-variant-*`. Size styles: `cn-button-size-*`.",
    },
    "button-group": {
        "vars": ["--border", "--input", "--muted"],
        "classes": ["flex", "items-center", "gap-0", "has-[button]:rounded-lg"],
        "notes": "Adjacent button borders collapse. Group handles border-radius on first/last children.",
    },
    "calendar": {
        "vars": ["--background", "--foreground", "--accent", "--accent-foreground", "--primary", "--primary-foreground", "--muted", "--muted-foreground", "--border", "--radius"],
        "classes": ["p-3", "rounded-md", "border", "bg-background"],
        "notes": "Selected day: `--primary` background. Today: `--accent`. Disabled: `--muted-foreground`.",
    },
    "card": {
        "vars": ["--card", "--card-foreground", "--border", "--radius", "--card-spacing"],
        "classes": ["rounded-xl", "bg-card", "text-card-foreground", "ring-1", "ring-foreground/10", "flex", "flex-col", "overflow-hidden"],
        "notes": "`--card-spacing` CSS variable controls internal spacing. Default `--spacing(4)`, small `--spacing(3)`.",
    },
    "carousel": {
        "vars": ["--background", "--foreground", "--border", "--radius"],
        "classes": ["relative", "overflow-hidden", "flex"],
        "notes": "Navigation buttons use Button component tokens. Slide transitions via CSS transform.",
    },
    "chart": {
        "vars": ["--chart-1", "--chart-2", "--chart-3", "--chart-4", "--chart-5", "--background", "--foreground", "--border", "--muted"],
        "classes": ["[&_.recharts-cartesian-grid-line[stroke]]:stroke-border", "[&_.recharts-curve.recharts-tooltip-cursor]:stroke-border"],
        "notes": "Chart colors use `--chart-1` through `--chart-5` CSS variables defined in `globals.css`.",
    },
    "checkbox": {
        "vars": ["--primary", "--primary-foreground", "--border", "--ring", "--radius"],
        "classes": ["h-4", "w-4", "shrink-0", "rounded-sm", "border", "border-primary", "focus-visible:ring-3", "disabled:opacity-50"],
        "notes": "Checked state: `--primary` background with a checkmark icon in `--primary-foreground`.",
    },
    "collapsible": {
        "vars": [],
        "classes": [],
        "notes": "Headless component — bring your own styles. Content is hidden/shown via data-state attributes.",
    },
    "combobox": {
        "vars": ["--background", "--foreground", "--border", "--accent", "--accent-foreground", "--muted", "--muted-foreground", "--ring", "--radius"],
        "classes": [],
        "notes": "Composed of Popover + Command. Inherits tokens from both components.",
    },
    "command": {
        "vars": ["--background", "--foreground", "--border", "--accent", "--accent-foreground", "--muted", "--muted-foreground", "--popover", "--popover-foreground", "--radius"],
        "classes": ["flex", "h-full", "w-full", "flex-col", "overflow-hidden", "rounded-md", "bg-popover", "text-popover-foreground"],
        "notes": "Built on `cmdk`. Active item: `--accent` background.",
    },
    "context-menu": {
        "vars": ["--popover", "--popover-foreground", "--accent", "--accent-foreground", "--border", "--muted", "--muted-foreground", "--radius"],
        "classes": ["z-50", "min-w-[8rem]", "rounded-md", "border", "bg-popover", "p-1", "shadow-md"],
        "notes": "Shares token set with DropdownMenu. Active item: `--accent`.",
    },
    "data-table": {
        "vars": ["--border", "--background", "--muted", "--muted-foreground", "--foreground", "--accent"],
        "classes": [],
        "notes": "Built on TanStack Table + shadcn/ui Table component. Inherits Table token set.",
    },
    "date-picker": {
        "vars": [],
        "classes": [],
        "notes": "Composed of Popover + Calendar. Inherits tokens from both components.",
    },
    "dialog": {
        "vars": ["--background", "--foreground", "--border", "--radius", "--muted-foreground"],
        "classes": ["fixed", "inset-0", "z-50", "bg-black/80", "grid", "place-items-center", "rounded-lg", "shadow-lg", "p-6", "gap-4"],
        "notes": "Overlay: `bg-black/80`. Panel: `--background`.",
    },
    "direction": {
        "vars": [],
        "classes": [],
        "notes": "Utility context provider — no visual tokens.",
    },
    "drawer": {
        "vars": ["--background", "--foreground", "--border", "--muted", "--muted-foreground", "--radius"],
        "classes": ["fixed", "inset-x-0", "bottom-0", "z-50", "mt-24", "flex", "h-auto", "flex-col", "rounded-t-[10px]", "border", "bg-background"],
        "notes": "Built on `vaul`. Handle bar uses `--muted` background.",
    },
    "dropdown-menu": {
        "vars": ["--popover", "--popover-foreground", "--accent", "--accent-foreground", "--border", "--muted", "--muted-foreground", "--destructive", "--radius"],
        "classes": ["z-50", "min-w-[8rem]", "rounded-md", "border", "bg-popover", "p-1", "shadow-md"],
        "notes": "Shares token set with ContextMenu. Destructive items use `--destructive` color.",
    },
    "empty": {
        "vars": ["--muted-foreground", "--foreground"],
        "classes": ["flex", "flex-col", "items-center", "justify-center", "gap-4", "text-center"],
        "notes": "Minimal layout component. Icon, heading, description, and action CTA are composed manually.",
    },
    "field": {
        "vars": ["--foreground", "--muted-foreground", "--destructive", "--border"],
        "classes": ["flex", "flex-col", "gap-2"],
        "notes": "Pairs with Label, Input, and error/hint text. Error state uses `--destructive` color.",
    },
    "hover-card": {
        "vars": ["--popover", "--popover-foreground", "--border", "--radius"],
        "classes": ["z-50", "rounded-md", "border", "bg-popover", "p-4", "shadow-md"],
        "notes": "Same visual token set as Popover but without focus trap.",
    },
    "input": {
        "vars": ["--background", "--foreground", "--border", "--input", "--ring", "--radius", "--muted-foreground"],
        "classes": ["flex", "h-8", "w-full", "rounded-lg", "border", "border-input", "bg-background", "px-3", "py-1", "text-sm", "placeholder:text-muted-foreground", "focus-visible:ring-3", "disabled:opacity-50"],
        "notes": "`--input` token sets the default border color. Focus ring uses `--ring`.",
    },
    "input-group": {
        "vars": ["--background", "--border", "--input", "--muted", "--foreground", "--radius"],
        "classes": ["flex", "items-center", "rounded-lg", "border", "bg-background"],
        "notes": "Addon elements use `--muted` background.",
    },
    "input-otp": {
        "vars": ["--border", "--ring", "--background", "--foreground", "--radius"],
        "classes": ["flex", "items-center", "gap-2", "has-[:disabled]:opacity-50"],
        "notes": "Built on `input-otp`. Individual slot uses `--border` and `--ring` for focus.",
    },
    "item": {
        "vars": ["--accent", "--accent-foreground", "--foreground", "--muted-foreground"],
        "classes": ["relative", "flex", "cursor-default", "select-none", "items-center", "rounded-sm", "px-2", "py-1.5", "text-sm"],
        "notes": "Used as a building block — inherits parent context tokens.",
    },
    "kbd": {
        "vars": ["--muted", "--muted-foreground", "--border", "--radius"],
        "classes": ["pointer-events-none", "inline-flex", "h-5", "items-center", "gap-1", "rounded", "border", "bg-muted", "px-1.5", "font-mono", "text-[10px]", "font-medium", "text-muted-foreground"],
        "notes": "`--muted` background with `--muted-foreground` text and `--border` outline.",
    },
    "label": {
        "vars": ["--foreground", "--muted-foreground"],
        "classes": ["text-sm", "font-medium", "leading-none", "peer-disabled:cursor-not-allowed", "peer-disabled:opacity-70"],
        "notes": "Uses Tailwind `peer-*` variants to style based on adjacent disabled input state.",
    },
    "menubar": {
        "vars": ["--background", "--foreground", "--accent", "--accent-foreground", "--border", "--popover", "--popover-foreground", "--muted", "--radius"],
        "classes": ["flex", "h-9", "items-center", "gap-1", "rounded-md", "border", "bg-background", "p-1", "shadow-sm"],
        "notes": "Top-level trigger active/open state uses `--accent` background.",
    },
    "native-select": {
        "vars": ["--background", "--foreground", "--border", "--input", "--ring", "--radius", "--muted-foreground"],
        "classes": ["h-8", "w-full", "rounded-lg", "border", "border-input", "bg-background", "text-sm", "focus:ring-3"],
        "notes": "Uses native browser `<select>` UI. Styles are applied via CSS but browser controls appearance.",
    },
    "navigation-menu": {
        "vars": ["--background", "--foreground", "--accent", "--accent-foreground", "--border", "--popover", "--popover-foreground", "--radius"],
        "classes": ["relative", "flex", "max-w-max", "flex-1", "items-center", "justify-center"],
        "notes": "Viewport content uses `--popover` token. Trigger hover: `--accent`.",
    },
    "pagination": {
        "vars": ["--border", "--accent", "--accent-foreground", "--background", "--foreground", "--radius"],
        "classes": ["flex", "flex-row", "items-center", "gap-1"],
        "notes": "Active page button uses `--border` emphasis variant. Disabled arrow buttons use `--muted`.",
    },
    "popover": {
        "vars": ["--popover", "--popover-foreground", "--border", "--radius"],
        "classes": ["z-50", "rounded-md", "border", "bg-popover", "p-4", "text-popover-foreground", "shadow-md"],
        "notes": "`--popover` and `--popover-foreground` are distinct from `--background`/`--foreground` to allow independent theming.",
    },
    "progress": {
        "vars": ["--primary", "--muted"],
        "classes": ["relative", "h-2", "w-full", "overflow-hidden", "rounded-full", "bg-muted"],
        "notes": "Track: `--muted`. Fill indicator: `--primary`. Use `className` to override track or fill color.",
    },
    "radio-group": {
        "vars": ["--primary", "--border", "--ring", "--foreground"],
        "classes": ["aspect-square", "h-4", "w-4", "rounded-full", "border", "border-primary", "text-primary", "focus:ring-3", "disabled:opacity-50"],
        "notes": "Selected state fills inner circle with `--primary` color.",
    },
    "resizable": {
        "vars": ["--border", "--muted"],
        "classes": ["flex", "h-full", "w-full", "items-center", "justify-center"],
        "notes": "Handle uses `--border` color. Grip icon uses `--muted-foreground`.",
    },
    "scroll-area": {
        "vars": ["--border", "--muted"],
        "classes": ["relative", "overflow-hidden"],
        "notes": "Scrollbar thumb and track use `--border` color variants.",
    },
    "select": {
        "vars": ["--background", "--foreground", "--border", "--input", "--ring", "--radius", "--popover", "--popover-foreground", "--accent", "--accent-foreground", "--muted-foreground"],
        "classes": ["flex", "h-8", "w-full", "items-center", "justify-between", "rounded-lg", "border", "border-input", "bg-background", "px-3", "py-2", "text-sm"],
        "notes": "Trigger: inherits Input tokens. Content: inherits Popover tokens.",
    },
    "separator": {
        "vars": ["--border"],
        "classes": ["shrink-0", "bg-border"],
        "notes": "Renders as `h-[1px] w-full` (horizontal) or `h-full w-[1px]` (vertical). Color: `--border`.",
    },
    "sheet": {
        "vars": ["--background", "--foreground", "--border", "--muted-foreground", "--radius"],
        "classes": ["fixed", "inset-y-0", "z-50", "flex", "h-full", "flex-col", "border-l", "bg-background", "p-6", "shadow-lg"],
        "notes": "Overlay: `bg-black/80`. Panel tokens same as Dialog.",
    },
    "sidebar": {
        "vars": ["--sidebar-background", "--sidebar-foreground", "--sidebar-primary", "--sidebar-primary-foreground", "--sidebar-accent", "--sidebar-accent-foreground", "--sidebar-border", "--sidebar-ring"],
        "classes": ["flex", "h-full", "min-h-svh", "flex-col", "bg-sidebar"],
        "notes": "Sidebar has its own dedicated CSS variable set (`--sidebar-*`) for independent theming.",
    },
    "skeleton": {
        "vars": ["--muted"],
        "classes": ["animate-pulse", "rounded-md", "bg-muted"],
        "notes": "Uses `animate-pulse` Tailwind animation. Background: `--muted`.",
    },
    "slider": {
        "vars": ["--primary", "--primary-foreground", "--muted", "--ring", "--radius"],
        "classes": ["relative", "flex", "w-full", "touch-none", "select-none", "items-center"],
        "notes": "Track: `--muted`. Range fill: `--primary`. Thumb: `--primary` with `--ring` focus.",
    },
    "sonner": {
        "vars": ["--normal-bg", "--normal-text", "--normal-border", "--success-bg", "--success-text", "--success-border", "--error-bg", "--error-text", "--error-border"],
        "classes": ["toaster", "group"],
        "notes": "Sonner uses its own CSS variable set; override via `toastOptions.classNames` or theme variables.",
    },
    "spinner": {
        "vars": ["--foreground", "--muted-foreground"],
        "classes": ["animate-spin", "text-muted-foreground"],
        "notes": "SVG with `animate-spin`. Color inherits from `currentColor` (set via `className`).",
    },
    "switch": {
        "vars": ["--primary", "--input", "--background", "--ring", "--radius"],
        "classes": ["peer", "inline-flex", "h-5", "w-9", "shrink-0", "cursor-pointer", "items-center", "rounded-full", "border-2", "border-transparent", "transition-colors", "focus-visible:ring-3"],
        "notes": "Track off: `--input`. Track on: `--primary`. Thumb: `--background`.",
    },
    "table": {
        "vars": ["--border", "--muted", "--foreground", "--muted-foreground"],
        "classes": ["w-full", "caption-bottom", "text-sm", "border-b", "text-muted-foreground", "bg-muted/50"],
        "notes": "Header row uses `--muted/50` background. Borders: `--border`.",
    },
    "tabs": {
        "vars": ["--background", "--foreground", "--muted", "--muted-foreground", "--border", "--radius"],
        "classes": ["inline-flex", "h-9", "items-center", "justify-center", "rounded-lg", "bg-muted", "p-1", "text-muted-foreground"],
        "notes": "Active tab: `--background` with shadow. Tab content: `mt-2` below the tab list.",
    },
    "textarea": {
        "vars": ["--background", "--foreground", "--border", "--input", "--ring", "--radius", "--muted-foreground"],
        "classes": ["flex", "min-h-16", "w-full", "rounded-lg", "border", "border-input", "bg-background", "px-3", "py-2", "text-sm", "placeholder:text-muted-foreground", "focus-visible:ring-3", "disabled:opacity-50"],
        "notes": "Same token set as Input. Default `min-h-16`; use CSS `resize` to control resizing.",
    },
    "toast": {
        "vars": ["--background", "--foreground", "--border", "--destructive", "--destructive-foreground", "--radius", "--muted", "--muted-foreground"],
        "classes": ["group", "pointer-events-auto", "relative", "flex", "w-full", "items-center", "justify-between", "space-x-4", "rounded-md", "border", "p-6", "pr-8", "shadow-lg"],
        "notes": "Legacy component. Destructive variant uses `--destructive` tokens. Prefer Sonner.",
    },
    "toggle": {
        "vars": ["--accent", "--accent-foreground", "--muted", "--muted-foreground", "--ring", "--border", "--radius"],
        "classes": ["inline-flex", "items-center", "justify-center", "rounded-md", "text-sm", "font-medium", "ring-offset-background", "transition-colors", "hover:bg-muted", "hover:text-muted-foreground", "focus-visible:ring-3"],
        "notes": "Pressed state: `data-[state=on]` → `--accent` background.",
    },
    "toggle-group": {
        "vars": ["--accent", "--accent-foreground", "--muted", "--border", "--radius"],
        "classes": ["flex", "items-center", "justify-center", "gap-1"],
        "notes": "Pressed toggle within the group uses same `--accent` token as Toggle.",
    },
    "tooltip": {
        "vars": ["--popover", "--popover-foreground", "--border", "--radius"],
        "classes": ["z-50", "overflow-hidden", "rounded-md", "border", "bg-popover", "px-3", "py-1.5", "text-xs", "text-popover-foreground", "shadow-md"],
        "notes": "Uses `--popover` tokens. Animation via `data-[state=*]` Tailwind variants.",
    },
    "typography": {
        "vars": ["--foreground", "--muted-foreground", "--border", "--background"],
        "classes": ["prose", "prose-neutral", "dark:prose-invert"],
        "notes": "Uses Tailwind Typography plugin classes. Headings, paragraphs, lists inherit from the `prose` class.",
    },
}

# ─── MDX fetcher ──────────────────────────────────────────────────────────────

def fetch_mdx(slug):
    url = f"{BASE_RAW}/{slug}.mdx"
    result = subprocess.run(
        ["curl", "-s", "--max-time", "20", url],
        capture_output=True, text=True
    )
    content = result.stdout.strip()
    if content.startswith("404:") or not content:
        return None
    return content

# ─── MDX parser ───────────────────────────────────────────────────────────────

def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip()
    return fm

def get_section(text, heading):
    """Extract content between ## heading and next ## heading."""
    pattern = rf"## {re.escape(heading)}\n(.*?)(?=\n## |\Z)"
    m = re.search(pattern, text, re.DOTALL)
    return m.group(1).strip() if m else ""

def get_sections(text):
    """Return dict of all ## sections."""
    parts = re.split(r"\n## ", text)
    sections = {}
    for part in parts[1:]:
        nl = part.index("\n") if "\n" in part else len(part)
        heading = part[:nl].strip()
        body = part[nl:].strip()
        sections[heading] = body
    return sections

def extract_code_blocks(text, lang=""):
    """Return all code block contents for a given lang."""
    pattern = rf"```{re.escape(lang)}[\w ]*\n(.*?)```"
    return re.findall(pattern, text, re.DOTALL)

def extract_first_code_block(text):
    """Return first code block regardless of lang."""
    m = re.search(r"```[\w ]*\n(.*?)```", text, re.DOTALL)
    return m.group(1).strip() if m else ""

def clean_jsx(text):
    """Strip multi-line JSX component blocks (<ComponentPreview .../>, <Step>, etc.)."""
    # Remove complete JSX elements (self-closing and multi-line) for known component tags
    # First remove self-closing single-line tags
    text = re.sub(r"<(?:ComponentPreview|ComponentSource|CodeTabs|Steps?|TabsList|TabsTrigger|TabsContent|Step)\b[^>]*/>\n?", "", text)
    # Remove multi-line JSX blocks: opening tag, attributes, close
    text = re.sub(
        r"<(?:ComponentPreview|ComponentSource|CodeTabs|Steps?|TabsList|TabsTrigger|TabsContent|Step)\b.*?(?:/>|</(?:ComponentPreview|ComponentSource|CodeTabs|Steps?|TabsList|TabsTrigger|TabsContent|Step)>)\n?",
        "", text, flags=re.DOTALL
    )
    # Remove orphan JSX attribute lines (  name="..." styleName="..." etc.)
    text = re.sub(r"^\s+\w+=[\"\{][^\n]*\n", "", text, flags=re.MULTILINE)
    # Remove closing tags on their own line
    text = re.sub(r"^\s*</\w+>\n?", "", text, flags=re.MULTILINE)
    # Collapse multiple blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text

def extract_api_tables(text):
    """Extract all markdown tables from a section."""
    tables = []
    current = []
    in_table = False
    for line in text.splitlines():
        if re.match(r"^\|", line):
            current.append(line)
            in_table = True
        else:
            if in_table and current:
                tables.append("\n".join(current))
                current = []
            in_table = False
    if current:
        tables.append("\n".join(current))
    return tables

def extract_usage_import(text):
    """Extract import statement from usage section."""
    blocks = extract_code_blocks(text, "tsx")
    for b in blocks:
        if "import" in b and "from" in b:
            return b.strip()
    return ""

def extract_usage_example(text):
    """Extract first usage example (non-import code block)."""
    blocks = extract_code_blocks(text, "tsx")
    for b in blocks:
        if "import" not in b:
            return b.strip()
    return ""

def extract_composition(text):
    """Extract composition tree from a code block."""
    blocks = extract_code_blocks(text, "text")
    if blocks:
        return blocks[0].strip()
    return ""

def extract_install_cmd(text):
    bash_blocks = extract_code_blocks(text, "bash")
    for b in bash_blocks:
        if "shadcn" in b:
            return b.strip()
    return ""

def extract_examples(text):
    """Extract named examples from ## Examples section."""
    examples = []
    cleaned = clean_jsx(text)
    for m in re.finditer(r"### ([^\n]+)\n(.*?)(?=\n### |\Z)", cleaned, re.DOTALL):
        name = m.group(1).strip()
        desc = m.group(2).strip()
        # Keep only lines that are plain text (not JSX tags or lone attributes)
        desc_lines = []
        for line in desc.splitlines():
            s = line.strip()
            if not s:
                continue
            # Skip orphaned JSX attribute-style lines
            if re.match(r'^\w+=["\{]', s):
                continue
            if s.startswith("<") or s.startswith("/>") or s == ">":
                continue
            desc_lines.append(s)
        examples.append((name, "\n".join(desc_lines)))
    return examples

def extract_api_section(sections):
    """Find and return API reference content."""
    for key in sections:
        if "api" in key.lower() or "reference" in key.lower():
            return sections[key]
    return ""

# ─── .md generator ───────────────────────────────────────────────────────────

def make_md(slug, mdx):
    fm = parse_frontmatter(mdx)
    title = fm.get("title", slug.replace("-", " ").title())
    description = fm.get("description", "")
    radix_doc = ""
    radix_api = ""
    if "links:" in mdx:
        doc_m = re.search(r"doc:\s*(https?://\S+)", mdx)
        api_m = re.search(r"api:\s*(https?://\S+)", mdx)
        if doc_m:
            radix_doc = doc_m.group(1)
        if api_m:
            radix_api = api_m.group(1)

    sections = get_sections(mdx)

    install_cmd = extract_install_cmd(sections.get("Installation", ""))

    usage_text = sections.get("Usage", "")
    import_block = extract_usage_import(usage_text)
    usage_example = extract_usage_example(usage_text)

    composition_text = sections.get("Composition", "")
    composition = extract_composition(composition_text)

    examples_text = sections.get("Examples", "")
    examples = extract_examples(examples_text)

    api_text = extract_api_section(sections)
    api_tables = extract_api_tables(api_text)
    # Also extract sub-component descriptions from api_text
    sub_headings = re.findall(r"### ([^\n]+)\n.*?(?=\n### |\Z)", api_text, re.DOTALL)

    a11y = A11Y.get(slug, {
        "roles": "See Radix UI documentation.",
        "keyboard": "See Radix UI documentation.",
        "aria": "See Radix UI documentation.",
        "notes": "",
    })

    tokens = TAILWIND_TOKENS.get(slug, {"vars": [], "classes": [], "notes": ""})

    # ── Assemble output ────────────────────────────────────────────────────────
    lines = []

    # Frontmatter
    lines.append("---")
    lines.append(f"component: {slug}")
    lines.append(f"source: https://ui.shadcn.com/docs/components/{slug}")
    if radix_doc:
        lines.append(f"radix-doc: {radix_doc}")
    if radix_api:
        lines.append(f"radix-api: {radix_api}")
    lines.append("---")
    lines.append("")

    # Heading
    lines.append(f"# {title}")
    lines.append("")

    # Overview
    lines.append("## Overview")
    lines.append("")
    lines.append(description)
    lines.append("")

    # Import
    lines.append("## Import")
    lines.append("")
    if import_block:
        lines.append("```tsx")
        lines.append(import_block)
        lines.append("```")
    else:
        lines.append(f"```tsx")
        lines.append(f'import {{ {title} }} from "@/components/ui/{slug}"')
        lines.append("```")
    lines.append("")

    # Installation
    lines.append("## Installation")
    lines.append("")
    if install_cmd:
        lines.append("```bash")
        lines.append(install_cmd)
        lines.append("```")
    else:
        lines.append(f"```bash")
        lines.append(f"npx shadcn@latest add {slug}")
        lines.append("```")
    lines.append("")

    # Usage
    lines.append("## Usage")
    lines.append("")
    if usage_example:
        lines.append("```tsx")
        lines.append(usage_example)
        lines.append("```")
    else:
        lines.append(f"```tsx")
        lines.append(f"<{title} />")
        lines.append("```")
    lines.append("")

    # Composition
    if composition:
        lines.append("## Composition")
        lines.append("")
        lines.append("```")
        lines.append(composition)
        lines.append("```")
        lines.append("")

    # Props & Variants
    lines.append("## Props & Variants")
    lines.append("")
    if api_tables:
        # Extract sub-component names from api_text headings
        sub_comp_sections = re.findall(
            r"### ([^\n]+)\n(.*?)(?=\n### |\Z)", api_text, re.DOTALL
        )
        if sub_comp_sections:
            for comp_name, comp_body in sub_comp_sections:
                lines.append(f"### {comp_name}")
                lines.append("")
                desc_lines = []
                for ln in comp_body.splitlines():
                    if re.match(r"^\|", ln) or (desc_lines and re.match(r"^\|", desc_lines[-1])):
                        break
                    if ln.strip() and not ln.strip().startswith("<"):
                        desc_lines.append(ln.strip())
                if desc_lines:
                    lines.append(" ".join(desc_lines))
                    lines.append("")
                comp_tables = extract_api_tables(comp_body)
                for tbl in comp_tables:
                    lines.append(tbl)
                    lines.append("")
        else:
            for tbl in api_tables:
                lines.append(tbl)
                lines.append("")
    else:
        lines.append("*API reference available at the Radix UI docs link above.*")
        lines.append("")

    # Examples
    if examples:
        lines.append("## Examples")
        lines.append("")
        for name, desc in examples:
            lines.append(f"### {name}")
            lines.append("")
            if desc:
                lines.append(desc)
                lines.append("")

    # Accessibility
    lines.append("## Accessibility")
    lines.append("")
    lines.append("### ARIA Roles")
    lines.append("")
    lines.append(a11y["roles"])
    lines.append("")
    lines.append("### Keyboard Navigation")
    lines.append("")
    lines.append(a11y["keyboard"])
    lines.append("")
    lines.append("### ARIA Attributes")
    lines.append("")
    lines.append(a11y["aria"])
    lines.append("")
    if a11y.get("notes"):
        lines.append("### Screen Reader Notes")
        lines.append("")
        lines.append(a11y["notes"])
        lines.append("")

    # Tailwind Tokens
    lines.append("## Tailwind Tokens")
    lines.append("")
    if tokens["vars"]:
        lines.append("**CSS variables used:**")
        lines.append("")
        for v in tokens["vars"]:
            lines.append(f"- `{v}`")
        lines.append("")
    if tokens["classes"]:
        lines.append("**Key Tailwind classes:**")
        lines.append("")
        for c in tokens["classes"]:
            lines.append(f"- `{c}`")
        lines.append("")
    if tokens["notes"]:
        lines.append(tokens["notes"])
        lines.append("")

    # AI Design System CSS
    ds_tok_str = DS_TOKEN_MAP.get(slug, "—")
    for item in make_css_section(slug, ds_tok_str, "shadcn/ui", "lib-adapters/shadcn.css"):
        lines.append(item)
    lines.append("")

    # Notes
    lines.append("## Notes")
    lines.append("")
    if radix_doc:
        lines.append(f"- Full API reference: [{radix_doc}]({radix_doc})")
    if radix_api:
        lines.append(f"- Radix API reference: [{radix_api}]({radix_api})")

    # Changelog section if present
    changelog = sections.get("Changelog", "")
    if changelog:
        cleaned = clean_jsx(changelog).strip()
        if cleaned:
            lines.append("")
            lines.append("### Changelog")
            lines.append("")
            lines.append(cleaned)

    lines.append("")

    return "\n".join(lines)

# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    index_rows = []
    total = len(COMPONENTS)

    for i, slug in enumerate(COMPONENTS, 1):
        print(f"[{i:>2}/{total}] {slug} ...", end=" ", flush=True)

        mdx = fetch_mdx(slug)
        if mdx is None:
            print("404 — writing stub")
            stub = (
                f"---\ncomponent: {slug}\n"
                f"source: https://ui.shadcn.com/docs/components/{slug}\n"
                f"status: stub\n---\n\n"
                f"# {slug.replace('-', ' ').title()}\n\n"
                f"> Page not found or not yet available.\n"
            )
            out_path = os.path.join(OUT_DIR, f"{slug}.md")
            with open(out_path, "w") as f:
                f.write(stub)
            index_rows.append((slug, f"{slug}.md", "*(stub)*"))
            continue

        fm = parse_frontmatter(mdx)
        description = fm.get("description", "")
        md = make_md(slug, mdx)

        out_path = os.path.join(OUT_DIR, f"{slug}.md")
        with open(out_path, "w") as f:
            f.write(md)

        print(f"✓  ({len(md):,} chars)")
        index_rows.append((slug, f"{slug}.md", description))

        # polite delay to avoid hammering GitHub
        time.sleep(0.4)

    # ── INDEX.md ───────────────────────────────────────────────────────────────
    index_lines = [
        "# shadcn/ui Component Index",
        "",
        f"Generated from the [shadcn/ui v4 documentation](https://ui.shadcn.com/docs/components).",
        f"Source: `apps/v4/content/docs/components/radix/` in the [shadcn-ui/ui](https://github.com/shadcn-ui/ui) repository.",
        "",
        f"**{len(index_rows)} components documented.**",
        "",
        "| Component | File | Description |",
        "|-----------|------|-------------|",
    ]
    for slug, fname, desc in index_rows:
        index_lines.append(f"| [{slug}]({fname}) | `{fname}` | {desc} |")

    index_path = os.path.join(OUT_DIR, "INDEX.md")
    with open(index_path, "w") as f:
        f.write("\n".join(index_lines) + "\n")

    print(f"\n✅  Done. {len(index_rows)} files written to {OUT_DIR}")
    print(f"    INDEX.md written to {index_path}")

if __name__ == "__main__":
    main()
