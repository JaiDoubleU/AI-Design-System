#!/usr/bin/env python3
"""
build-mui-docs.py — Material UI v6 component documentation scraper

Fetches component docs from the MUI GitHub repository and generates structured
.md files in mui-docs/ that AI agents can use as coding context.

Output format mirrors shadcn-docs/ and antd-docs/ for a consistent agent interface.

Called by: scripts/build-docs.js
Output:    mui-docs/{component}.md + mui-docs/INDEX.md
"""

import os
import re
import time
import json
import urllib.request
import urllib.error

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

OUT_DIR  = "mui-docs"
BASE_RAW = "https://raw.githubusercontent.com/mui/material-ui/master/docs/data/material/components"
API_RAW  = "https://raw.githubusercontent.com/mui/material-ui/master/docs/data/material/api"
DELAY    = 0.4

# Maps component slug → (docs path, api slug, import path, description)
# docs path is relative to BASE_RAW
COMPONENTS = {
    # Inputs
    "autocomplete":    ("autocomplete/autocomplete.md",  "autocomplete",   "@mui/material/Autocomplete",   "Combo box with free-form and fixed options"),
    "button":          ("buttons/buttons.md",            "button",         "@mui/material/Button",         "Clickable element for triggering actions"),
    "button-group":    ("button-group/button-group.md",  "button-group",   "@mui/material/ButtonGroup",    "Groups related buttons together"),
    "checkbox":        ("checkboxes/checkboxes.md",      "checkbox",       "@mui/material/Checkbox",       "Boolean toggle, standalone or in a group"),
    "floating-action": ("floating-action-button/floating-action-button.md", "fab", "@mui/material/Fab",    "Circular button for the primary action"),
    "icon-button":     ("buttons/buttons.md",            "icon-button",    "@mui/material/IconButton",     "Compact button showing only an icon"),
    "radio":           ("radio-buttons/radio-buttons.md","radio",          "@mui/material/Radio",          "Single selection from a group"),
    "rating":          ("rating/rating.md",              "rating",         "@mui/material/Rating",         "Star rating input"),
    "select":          ("selects/selects.md",            "select",         "@mui/material/Select",         "Dropdown option selector"),
    "slider":          ("slider/slider.md",              "slider",         "@mui/material/Slider",         "Range or single value input"),
    "switch":          ("switches/switches.md",          "switch",         "@mui/material/Switch",         "Toggle between two boolean states"),
    "text-field":      ("text-fields/text-fields.md",    "text-field",     "@mui/material/TextField",      "Single or multi-line text input"),
    "toggle-button":   ("toggle-button/toggle-button.md","toggle-button",  "@mui/material/ToggleButton",   "Exclusive or multi-select button group"),
    "transfer-list":   ("transfer-list/transfer-list.md","",               "@mui/material",                "Dual-list item selection"),
    # Data display
    "avatar":          ("avatars/avatars.md",            "avatar",         "@mui/material/Avatar",         "User or entity image or initial"),
    "badge":           ("badges/badges.md",              "badge",          "@mui/material/Badge",          "Count or status indicator overlay"),
    "chip":            ("chips/chips.md",                "chip",           "@mui/material/Chip",           "Compact label with optional dismiss/icon"),
    "divider":         ("dividers/dividers.md",          "divider",        "@mui/material/Divider",        "Thin horizontal or vertical separator"),
    "icons":           ("icons/icons.md",                "",               "@mui/icons-material",          "Material Design icon library"),
    "list":            ("lists/lists.md",                "list",           "@mui/material/List",           "Uniform vertical list of items"),
    "table":           ("tables/tables.md",              "table",          "@mui/material/Table",          "Structured data with rows and columns"),
    "tooltip":         ("tooltips/tooltips.md",          "tooltip",        "@mui/material/Tooltip",        "Short hint shown on hover or focus"),
    "typography":      ("typography/typography.md",      "typography",     "@mui/material/Typography",     "Text formatting with semantic variants"),
    # Feedback
    "alert":           ("alert/alert.md",                "alert",          "@mui/material/Alert",          "Contextual feedback message"),
    "backdrop":        ("backdrop/backdrop.md",          "backdrop",       "@mui/material/Backdrop",       "Dims content behind a modal or drawer"),
    "circular-progress":("progress/progress.md",        "circular-progress","@mui/material/CircularProgress","Circular loading indicator"),
    "dialog":          ("dialogs/dialogs.md",            "dialog",         "@mui/material/Dialog",         "Modal overlay for focused interactions"),
    "drawer":          ("drawers/drawers.md",            "drawer",         "@mui/material/Drawer",         "Side panel overlay"),
    "linear-progress": ("progress/progress.md",         "linear-progress","@mui/material/LinearProgress", "Horizontal progress bar"),
    "skeleton":        ("skeleton/skeleton.md",          "skeleton",       "@mui/material/Skeleton",       "Placeholder while content loads"),
    "snackbar":        ("snackbars/snackbars.md",        "snackbar",       "@mui/material/Snackbar",       "Transient corner notification"),
    # Surfaces
    "accordion":       ("accordion/accordion.md",        "accordion",      "@mui/material/Accordion",      "Expandable/collapsible content panel"),
    "app-bar":         ("app-bar/app-bar.md",            "app-bar",        "@mui/material/AppBar",         "Top navigation bar"),
    "card":            ("cards/cards.md",                "card",           "@mui/material/Card",           "Content container with optional media"),
    "paper":           ("paper/paper.md",                "paper",          "@mui/material/Paper",          "Elevated surface container"),
    # Navigation
    "bottom-navigation":("bottom-navigation/bottom-navigation.md","bottom-navigation","@mui/material/BottomNavigation","Mobile bottom nav bar"),
    "breadcrumbs":     ("breadcrumbs/breadcrumbs.md",   "breadcrumbs",    "@mui/material/Breadcrumbs",    "Hierarchical page location trail"),
    "link":            ("links/links.md",                "link",           "@mui/material/Link",           "Styled anchor with MUI theming"),
    "menu":            ("menus/menus.md",                "menu",           "@mui/material/Menu",           "Contextual list of options"),
    "pagination":      ("pagination/pagination.md",      "pagination",     "@mui/material/Pagination",     "Page navigation control"),
    "speed-dial":      ("speed-dial/speed-dial.md",      "speed-dial",     "@mui/material/SpeedDial",      "FAB that expands into action options"),
    "stepper":         ("steppers/steppers.md",          "stepper",        "@mui/material/Stepper",        "Multi-step workflow indicator"),
    "tabs":            ("tabs/tabs.md",                  "tabs",           "@mui/material/Tabs",           "Content panels switching via tab bar"),
    # Layout
    "box":             ("box/box.md",                    "box",            "@mui/material/Box",            "Generic container with sx prop support"),
    "container":       ("container/container.md",        "container",      "@mui/material/Container",      "Centers content with max-width"),
    "grid":            ("grid/grid.md",                  "grid",           "@mui/material/Grid",           "12-column responsive grid system"),
    "stack":           ("stack/stack.md",                "stack",          "@mui/material/Stack",          "One-dimensional flex layout helper"),
    "image-list":      ("image-list/image-list.md",      "image-list",     "@mui/material/ImageList",      "Responsive grid of images"),
}

# AI Design System token hints per component
DS_TOKEN_MAP = {
    "button":           "--ds-interactive, --ds-interactive-hover, --ds-interactive-fg",
    "text-field":       "--ds-border, --ds-border-focus, --ds-text, --ds-bg",
    "select":           "--ds-border, --ds-border-focus, --ds-interactive",
    "card":             "--ds-bg, --ds-border, --ds-shadow-sm",
    "dialog":           "--ds-bg, --ds-shadow-lg",
    "drawer":           "--ds-bg, --ds-shadow-lg",
    "alert":            "--ds-bg-{variant}, --ds-border-{variant}, --ds-text-{variant}",
    "snackbar":         "--ds-bg-emphasis, --ds-text-inverse, --ds-shadow-lg",
    "chip":             "--ds-bg-muted, --ds-border, --ds-text-subtle",
    "badge":            "--ds-interactive, --ds-text-danger",
    "tooltip":          "--ds-bg-emphasis, --ds-text-inverse",
    "tabs":             "--ds-interactive (active), --ds-border",
    "linear-progress":  "--ds-interactive, --ds-bg-muted",
    "circular-progress":"--ds-interactive",
    "checkbox":         "--ds-interactive, --ds-border",
    "radio":            "--ds-interactive, --ds-border",
    "switch":           "--ds-interactive, --ds-bg-muted",
    "slider":           "--ds-interactive",
    "app-bar":          "--ds-interactive, --ds-interactive-fg",
    "accordion":        "--ds-bg, --ds-border",
    "paper":            "--ds-bg, --ds-shadow-sm",
    "table":            "--ds-border, --ds-bg-subtle (zebra), --ds-interactive (sort)",
    "menu":             "--ds-bg, --ds-shadow-md, --ds-interactive (selected)",
}

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Maps component slug → AI DS CSS file relative to project root.
DS_CSS_FILE_MAP = {
    "button":       "src/components/button.css",
    "card":         "src/components/card.css",
    "text-field":   "src/components/input.css",
    "select":       "src/components/input.css",
    "checkbox":     "src/components/input.css",
    "radio":        "src/components/input.css",
    "autocomplete": "src/components/input.css",
    "chip":         "src/components/badge.css",
    "badge":        "src/components/badge.css",
    "alert":        "src/components/alert.css",
    "snackbar":     "src/components/alert.css",
    "typography":   "src/base/typography.css",
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


# ---------------------------------------------------------------------------
# Fetch helpers
# ---------------------------------------------------------------------------

def fetch(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "ai-design-system-docs/1.0"})
        with urllib.request.urlopen(req, timeout=12) as r:
            return r.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

def strip_mdx_components(text):
    """Remove JSX/MDX-specific elements that don't render as markdown."""
    # Remove JSX component tags with content
    text = re.sub(r"<\w+[A-Z]\w*[^>]*/?>", "", text)
    # Remove closing JSX tags
    text = re.sub(r"</[A-Z]\w*>", "", text)
    # Remove import statements
    text = re.sub(r"^import .+;\s*\n", "", text, flags=re.MULTILINE)
    # Remove export statements
    text = re.sub(r"^export .+\n", "", text, flags=re.MULTILINE)
    # Collapse excess blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def get_section(text, *headings):
    for h in headings:
        pattern = rf"##\s+{re.escape(h)}\s*\n(.*?)(?=\n##\s|\Z)"
        m = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
        if m:
            return m.group(1).strip()
    return ""


def extract_intro(text):
    """Get the leading paragraph before the first ## heading."""
    m = re.match(r"\s*(.*?)(?=\n##|\Z)", text, re.DOTALL)
    if m:
        intro = m.group(1).strip()
        # Take only first 500 chars to keep it concise
        if len(intro) > 500:
            intro = intro[:500].rsplit(".", 1)[0] + "."
        return intro
    return ""


def extract_api_section(text):
    """Extract the Props / API section — may be under different headings."""
    return get_section(text, "Component API", "API", "Props", "Properties")


def extract_usage_demos(text):
    """Return a short usage description from the first demo section."""
    section = get_section(text, "Basic usage", "Basic", "Usage", "Introduction")
    if section:
        # Remove code fences and JSX, keep prose
        section = re.sub(r"```[\s\S]*?```", "", section)
        section = strip_mdx_components(section)
        section = section.strip()[:600]
    return section


# ---------------------------------------------------------------------------
# Doc maker
# ---------------------------------------------------------------------------

def to_pascal(slug):
    """button-group → ButtonGroup"""
    return "".join(w.capitalize() for w in slug.replace("-", " ").split())


def make_md(slug, docs_text, description):
    _, api_slug, import_path, _ = COMPONENTS[slug]
    component_name = to_pascal(slug)
    ds_tok = DS_TOKEN_MAP.get(slug, "—")

    cleaned = strip_mdx_components(docs_text) if docs_text else ""
    intro   = extract_intro(cleaned)
    api     = extract_api_section(cleaned)
    usage   = extract_usage_demos(cleaned)

    # Build import statement
    if import_path.endswith(component_name):
        import_stmt = f"import {component_name} from '{import_path}';"
    elif "@mui/icons-material" in import_path:
        import_stmt = "import HomeIcon from '@mui/icons-material/Home';\n// Replace 'Home' with any icon name from @mui/icons-material"
    else:
        import_stmt = f"import {component_name} from '{import_path}';"

    parts = [
        f"# {component_name}",
        "",
        f"**Library:** Material UI v6  ",
        f"**Package:** `{import_path.split('/')[0]}/{import_path.split('/')[1] if '/' in import_path else ''}`  ",
        f"**Docs:** https://mui.com/material-ui/react-{slug}/",
        "",
        "---",
        "",
        "## Overview",
        "",
        intro or description,
    ]

    if usage:
        parts += ["", "### Usage notes", "", usage]

    parts += [
        "",
        "---",
        "",
        "## Import",
        "",
        "```js",
        import_stmt,
        "```",
        "",
        "---",
    ]

    if api:
        parts += [
            "",
            "## Props / API",
            "",
            api[:3000],  # cap to keep files readable
            "",
            "---",
        ]

    parts += [
        "",
        "## AI Design System token mapping",
        "",
        "When using this component with the AI Design System adapter, these",
        "`--ds-*` hooks drive the component's appearance:",
        "",
        "```",
        ds_tok,
        "```",
        "",
        "Adapter file: `lib-adapters/material-ui.css`  ",
        "Adapter spec: `specs/adapters/material-ui.md`",
    ]

    parts += make_css_section(slug, ds_tok, "Material UI", "lib-adapters/material-ui.css")

    parts += [
        "",
        "---",
        "",
        "## Notes",
        "",
        f"- Full MUI {component_name} docs: https://mui.com/material-ui/react-{slug}/",
        "- CSS Variables Mode (`cssVariables: true`) is required for the AI DS adapter.",
        "- MUI uses the `sx` prop for one-off style overrides; prefer `--ds-*` tokens for theme-level changes.",
    ]

    return "\n".join(parts) + "\n"


def make_stub(slug, description):
    _, _, import_path, _ = COMPONENTS[slug]
    component_name = to_pascal(slug)
    return f"""# {component_name}

**Library:** Material UI v6
**Docs:** https://mui.com/material-ui/react-{slug}/

> Source docs not available from GitHub. Visit the link above for full documentation.

## Import

```js
import {component_name} from '{import_path}';
```

## Overview

{description}
"""


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    slugs   = list(COMPONENTS.keys())
    total   = len(slugs)
    results = []

    for i, slug in enumerate(slugs, 1):
        docs_path, _, _, description = COMPONENTS[slug]
        url = f"{BASE_RAW}/{docs_path}"
        print(f"[{i:02d}/{total}] {slug} … ", end="", flush=True)

        raw = fetch(url)
        if raw:
            md = make_md(slug, raw, description)
            print("ok")
            ok = True
        else:
            md = make_stub(slug, description)
            print("stub (404)")
            ok = False

        out_path = os.path.join(OUT_DIR, f"{slug}.md")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(md)

        results.append((slug, to_pascal(slug), description, ok))
        if i < total:
            time.sleep(DELAY)

    # Write INDEX.md
    rows = "\n".join(
        f"| [{r[1]}]({r[0]}.md) | {r[2]} | {'✓' if r[3] else 'stub'} |"
        for r in results
    )
    index = f"""# Material UI Component Docs — Index

Generated by `scripts/build-mui-docs.py`. Each file is an AI coding context
doc for a single Material UI v6 component.

Use with the AI Design System adapter: `lib-adapters/material-ui.css`

| Component | Description | Source |
|---|---|---|
{rows}
"""
    with open(os.path.join(OUT_DIR, "INDEX.md"), "w", encoding="utf-8") as f:
        f.write(index)

    scraped = sum(1 for r in results if r[3])
    print(f"\n✅  {OUT_DIR}/INDEX.md written — {scraped}/{total} components scraped, {total - scraped} stubbed.\n")


if __name__ == "__main__":
    main()
