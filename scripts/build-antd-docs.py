#!/usr/bin/env python3
"""
build-antd-docs.py — Ant Design v5 component documentation scraper

Fetches component markdown from the Ant Design GitHub repository and generates
structured .md files in antd-docs/ that AI agents can use as coding context.

Output format mirrors shadcn-docs/ so agents have a consistent interface
regardless of which library is active.

Called by: scripts/build-docs.js
Output:    antd-docs/{component}.md + antd-docs/INDEX.md
"""

import os
import re
import time
import urllib.request
import urllib.error

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

OUT_DIR  = "antd-docs"
BASE_RAW = "https://raw.githubusercontent.com/ant-design/ant-design/master/components"
DELAY    = 0.4   # seconds between requests

COMPONENTS = [
    # General
    "button", "icon", "typography",
    # Layout
    "divider", "flex", "grid", "layout", "space",
    # Navigation
    "anchor", "breadcrumb", "dropdown", "menu", "pagination", "steps",
    # Data Entry
    "auto-complete", "cascader", "checkbox", "color-picker", "date-picker",
    "form", "input", "input-number", "mentions", "radio", "rate",
    "select", "slider", "switch", "time-picker", "transfer", "tree-select", "upload",
    # Data Display
    "avatar", "badge", "calendar", "card", "carousel", "collapse",
    "descriptions", "empty", "image", "list", "popover", "qr-code",
    "segmented", "statistic", "table", "tabs", "tag", "timeline",
    "tooltip", "tour", "tree",
    # Feedback
    "alert", "drawer", "message", "modal", "notification", "popconfirm",
    "progress", "result", "skeleton", "spin",
    # Other
    "affix", "app", "config-provider", "float-button", "watermark",
]

# One-line descriptions for the INDEX (fallback if we can't parse frontmatter)
DESCRIPTIONS = {
    "button":          "Triggers an operation",
    "icon":            "Semantic vector icons",
    "typography":      "Text, title, paragraph, and link styles",
    "divider":         "Separates content sections",
    "flex":            "Flexbox layout container",
    "grid":            "24-column responsive grid",
    "layout":          "Page-level layout scaffolding",
    "space":           "Consistent spacing between inline elements",
    "anchor":          "Scrollspy navigation to page sections",
    "breadcrumb":      "Shows the current page location in hierarchy",
    "dropdown":        "Contextual menu triggered by a control",
    "menu":            "Vertical or horizontal navigation list",
    "pagination":      "Paginates large data sets",
    "steps":           "Multi-step workflow indicator",
    "auto-complete":   "Input with dropdown suggestion list",
    "cascader":        "Hierarchical option selector",
    "checkbox":        "Boolean or multi-value toggle",
    "color-picker":    "Visual colour selection control",
    "date-picker":     "Calendar-based date/range selector",
    "form":            "Data entry container with validation",
    "input":           "Single-line text field",
    "input-number":    "Numeric input with step controls",
    "mentions":        "@-mention text input",
    "radio":           "Single selection from a group",
    "rate":            "Star rating control",
    "select":          "Dropdown option selector",
    "slider":          "Range or value slider",
    "switch":          "Toggle between two states",
    "time-picker":     "Time selection control",
    "transfer":        "Dual-panel item selector",
    "tree-select":     "Tree-structured option selector",
    "upload":          "File upload control",
    "avatar":          "User or entity image/initial display",
    "badge":           "Count or status indicator overlay",
    "calendar":        "Date display and selection calendar",
    "card":            "Content container with header and footer",
    "carousel":        "Slideshow of content panels",
    "collapse":        "Expandable/collapsible content panels",
    "descriptions":    "Key-value data display",
    "empty":           "Empty state placeholder",
    "image":           "Image with preview and fallback",
    "list":            "Uniform list of items",
    "popover":         "Rich popup triggered on hover or click",
    "qr-code":         "Renders a QR code from a URL",
    "segmented":       "Segmented button group selector",
    "statistic":       "Numerical stat with label",
    "table":           "Data table with sorting and filtering",
    "tabs":            "Content panels switching via tab bar",
    "tag":             "Label badge for categorisation",
    "timeline":        "Vertical event chronology",
    "tooltip":         "Short hint shown on hover",
    "tour":            "Guided step-by-step overlay tour",
    "tree":            "Hierarchical tree data display",
    "alert":           "Contextual feedback message",
    "drawer":          "Panel that slides in from the screen edge",
    "message":         "Transient feedback message (top of page)",
    "modal":           "Focused overlay dialog",
    "notification":    "Corner notification with icon and description",
    "popconfirm":      "Inline confirmation popover",
    "progress":        "Task or upload progress indicator",
    "result":          "Outcome feedback (success, error, etc.)",
    "skeleton":        "Placeholder while content loads",
    "spin":            "Loading spinner",
    "affix":           "Sticks an element to a scroll position",
    "app":             "Root context provider for message/notification APIs",
    "config-provider": "Global configuration for all Ant Design components",
    "float-button":    "Floating action button",
    "watermark":       "Adds a watermark to a container",
}

# AI Design System adapter token mapping (shown in every doc)
DS_TOKEN_MAP = {
    "button":    "--ds-interactive, --ds-interactive-hover, --ds-interactive-fg",
    "input":     "--ds-border, --ds-border-focus, --ds-text, --ds-bg",
    "select":    "--ds-border, --ds-border-focus, --ds-interactive",
    "form":      "--ds-text-danger (errors), --ds-border-focus (active fields)",
    "card":      "--ds-bg, --ds-border, --ds-shadow-sm",
    "table":     "--ds-border, --ds-bg-subtle (stripe), --ds-interactive (sort)",
    "modal":     "--ds-bg, --ds-shadow-lg, --ds-border",
    "drawer":    "--ds-bg, --ds-shadow-lg",
    "alert":     "--ds-bg-{variant}, --ds-border-{variant}, --ds-text-{variant}",
    "badge":     "--ds-interactive, --ds-text-danger (count)",
    "tag":       "--ds-bg-muted, --ds-border, --ds-text-subtle",
    "tabs":      "--ds-interactive (active tab), --ds-border",
    "menu":      "--ds-interactive (selected), --ds-bg-subtle (hover)",
    "progress":  "--ds-interactive, --ds-text-success, --ds-text-danger",
    "checkbox":  "--ds-interactive, --ds-border",
    "radio":     "--ds-interactive, --ds-border",
    "switch":    "--ds-interactive, --ds-bg-muted",
    "slider":    "--ds-interactive",
    "tooltip":   "--ds-bg-emphasis, --ds-text-inverse",
    "popover":   "--ds-bg, --ds-border, --ds-shadow-md",
}

# ---------------------------------------------------------------------------
# Helpers
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


def parse_frontmatter(text):
    """Extract YAML frontmatter fields as a dict."""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return {}
    block = m.group(1)
    result = {}
    for line in block.splitlines():
        kv = line.split(":", 1)
        if len(kv) == 2:
            result[kv[0].strip()] = kv[1].strip().strip("'\"")
    return result


def strip_frontmatter(text):
    return re.sub(r"^---\s*\n.*?\n---\s*\n", "", text, count=1, flags=re.DOTALL)


def get_section(text, heading):
    """Return the content under a specific ## heading."""
    pattern = rf"##\s+{re.escape(heading)}\s*\n(.*?)(?=\n##\s|\Z)"
    m = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
    return m.group(1).strip() if m else ""


def extract_api_tables(text):
    """Return all markdown tables found in the API section."""
    api_section = get_section(text, "API")
    if not api_section:
        # Try "Props" or "Properties"
        for heading in ("Props", "Properties", "Parameters"):
            api_section = get_section(text, heading)
            if api_section:
                break
    if not api_section:
        return ""
    # Keep only the table rows, drop <code> demo references
    lines = api_section.splitlines()
    cleaned = []
    for line in lines:
        # Strip demo-file references like <code src="./demo/...">
        line = re.sub(r"<code[^>]*>.*?</code>", "", line)
        cleaned.append(line)
    return "\n".join(cleaned).strip()


def extract_when_to_use(text):
    body = strip_frontmatter(text)
    section = get_section(body, "When To Use")
    if not section:
        # Sometimes it's just a paragraph after the first heading
        m = re.search(r"^([A-Z].*?\.)\s*\n", body, re.MULTILINE | re.DOTALL)
        if m:
            return m.group(1).strip()
    return section


def clean_text(text):
    """Remove JSX/HTML components from markdown."""
    text = re.sub(r"<code src=[^>]+>.*?</code>", "", text)
    text = re.sub(r"<[A-Z][^>]*/>", "", text)
    text = re.sub(r"<[A-Z][^>]*>.*?</[A-Z][^>]*>", "", text, flags=re.DOTALL)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


# ---------------------------------------------------------------------------
# Doc generator
# ---------------------------------------------------------------------------

COMPONENT_NAME = {
    "auto-complete":   "AutoComplete",
    "color-picker":    "ColorPicker",
    "date-picker":     "DatePicker",
    "float-button":    "FloatButton",
    "input-number":    "InputNumber",
    "time-picker":     "TimePicker",
    "tree-select":     "TreeSelect",
    "config-provider": "ConfigProvider",
    "qr-code":         "QRCode",
}

def to_component_name(slug):
    if slug in COMPONENT_NAME:
        return COMPONENT_NAME[slug]
    return "".join(w.capitalize() for w in slug.split("-"))


def make_md(slug, raw):
    fm     = parse_frontmatter(raw)
    body   = strip_frontmatter(raw)
    body   = clean_text(body)
    name   = to_component_name(slug)
    desc   = fm.get("description", DESCRIPTIONS.get(slug, ""))
    group  = fm.get("group", fm.get("category", "—"))
    when   = extract_when_to_use(body)
    api    = extract_api_tables(body)
    ds_tok = DS_TOKEN_MAP.get(slug, "—")

    import_line = f"import {{ {name} }} from 'antd';"
    if slug == "form":
        import_line = "import { Form, Form.Item } from 'antd';"
    elif slug == "grid":
        import_line = "import { Row, Col } from 'antd';"
    elif slug == "layout":
        import_line = "import { Layout } from 'antd';  // Layout.Header, Layout.Content, Layout.Sider, Layout.Footer"
    elif slug == "message":
        import_line = "import { message } from 'antd';  // message.success(), message.error(), ..."
    elif slug == "notification":
        import_line = "import { notification } from 'antd';"

    parts = [
        f"# {name}",
        "",
        f"**Library:** Ant Design v5  ",
        f"**Category:** {group}  ",
        f"**Docs:** https://ant.design/components/{slug}",
        "",
        "---",
        "",
        "## Overview",
        "",
        desc or "—",
    ]

    if when:
        parts += ["", "### When to use", "", when]

    parts += [
        "",
        "---",
        "",
        "## Import",
        "",
        "```js",
        import_line,
        "```",
        "",
        "---",
    ]

    if api:
        parts += [
            "",
            "## Props / API",
            "",
            api,
            "",
            "---",
        ]

    parts += [
        "",
        "## AI Design System token mapping",
        "",
        f"When using this component with the AI Design System adapter, these",
        f"`--ds-*` hooks drive the component's appearance:",
        "",
        f"```",
        ds_tok,
        "```",
        "",
        "Adapter file: `lib-adapters/ant-design.css`  ",
        "Adapter spec: `specs/adapters/ant-design.md`",
        "",
        "---",
        "",
        "## Notes",
        "",
        f"- Full Ant Design {name} docs: https://ant.design/components/{slug}",
        "- Props are subject to change across Ant Design patch versions.",
        "- CSS Variables Mode (`cssVar: true`) is required for the AI DS adapter to work.",
    ]

    return "\n".join(parts) + "\n"


def make_stub(slug):
    name = to_component_name(slug)
    return f"""# {name}

**Library:** Ant Design v5
**Docs:** https://ant.design/components/{slug}

> Docs not available from the GitHub source. Visit the link above for full documentation.
"""


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    results = []
    total   = len(COMPONENTS)

    for i, slug in enumerate(COMPONENTS, 1):
        url = f"{BASE_RAW}/{slug}/index.en-US.md"
        print(f"[{i:02d}/{total}] {slug} … ", end="", flush=True)

        raw = fetch(url)
        if raw:
            md = make_md(slug, raw)
            print("ok")
        else:
            md = make_stub(slug)
            print("stub (404)")

        out_path = os.path.join(OUT_DIR, f"{slug}.md")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(md)

        results.append((slug, to_component_name(slug), DESCRIPTIONS.get(slug, "—"), raw is not None))
        if i < total:
            time.sleep(DELAY)

    # Write INDEX.md
    rows = "\n".join(
        f"| [{r[1]}]({r[0]}.md) | {r[2]} | {'✓' if r[3] else 'stub'} |"
        for r in results
    )
    index = f"""# Ant Design Component Docs — Index

Generated by `scripts/build-antd-docs.py`. Each file is an AI coding context
doc for a single Ant Design v5 component.

Use with the AI Design System adapter: `lib-adapters/ant-design.css`

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
