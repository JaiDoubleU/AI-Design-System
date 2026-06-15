#!/usr/bin/env node
/**
 * build-vanilla-docs.js — Vanilla HTML/CSS/JS documentation generator
 *
 * Generates vanilla-docs/ from the AI Design System's own component CSS.
 * No network requests — all examples are derived from the component specs
 * in specs/components/ and the CSS classes defined in src/components/.
 *
 * Each output file contains three code sections for every component pattern:
 *   - HTML  — ready-to-paste markup using AI DS class names
 *   - CSS   — import block (link tags + bundler alternative)
 *   - JS    — interactive behaviour patterns where applicable
 *
 * Called by: scripts/build-docs.js --library=vanilla
 * Output:    vanilla-docs/{component}.md + vanilla-docs/INDEX.md
 */

'use strict';

const fs   = require('fs');
const path = require('path');

const OUT_DIR = 'vanilla-docs';

/* ─── Shared CSS setup snippet ───────────────────────────────────────────── */

const CSS_SETUP = `\
<!-- In your <head> — link order matters -->
<link rel="stylesheet" href="tokens.css">
<link rel="stylesheet" href="src/base/reset.css">
<link rel="stylesheet" href="src/components/{file}.css">`;

const CSS_BUNDLER = `\
/* Via CSS @import (PostCSS / Vite / webpack) */
@import 'ai-design-system/tokens.css';
@import 'ai-design-system/src/base/reset.css';
@import 'ai-design-system/src/components/{file}.css';`;

function setup(file, extras = []) {
  const links  = [CSS_SETUP.replace(/{file}/g, file), ...extras.map(e => `<link rel="stylesheet" href="src/components/${e}.css">`)].join('\n');
  const imports = [CSS_BUNDLER.replace(/{file}/g, file), ...extras.map(e => `@import 'ai-design-system/src/components/${e}.css';`)].join('\n');
  return { links, imports };
}

/* ─── Component definitions ──────────────────────────────────────────────── */

const COMPONENTS = {

  /* ── Button ─────────────────────────────────────────────────────────── */
  button: {
    title: 'Button',
    description: 'Triggers an action. Use semantic `<button>` or `<a>` elements. All styling is applied via CSS classes — no JavaScript required for basic usage.',
    cssFile: 'button',
    sections: [
      {
        heading: 'Variants',
        html: `\
<button class="btn btn-primary">Primary</button>
<button class="btn btn-secondary">Secondary</button>
<button class="btn btn-ghost">Ghost</button>
<button class="btn btn-danger">Delete</button>`,
      },
      {
        heading: 'Sizes',
        html: `\
<button class="btn btn-primary btn-sm">Small</button>
<button class="btn btn-primary">Default</button>
<button class="btn btn-primary btn-lg">Large</button>
<button class="btn btn-primary btn-xl">Extra large</button>`,
      },
      {
        heading: 'Icon button',
        html: `\
<button class="btn btn-ghost btn-icon" aria-label="Settings">
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
    <circle cx="12" cy="12" r="3"/><path d="M12 1v4M12 19v4M4.22 4.22l2.83 2.83M16.95 16.95l2.83 2.83M1 12h4M19 12h4M4.22 19.78l2.83-2.83M16.95 7.05l2.83-2.83"/>
  </svg>
</button>`,
      },
      {
        heading: 'Disabled state',
        html: `\
<button class="btn btn-primary" disabled>Disabled primary</button>
<button class="btn btn-secondary" disabled>Disabled secondary</button>`,
      },
      {
        heading: 'Loading state',
        html: `\
<button class="btn btn-primary btn-loading" aria-busy="true" disabled>
  Saving…
</button>`,
        note: 'Add `.btn-loading` and `aria-busy="true"` while an async operation is in progress. Remove both when it resolves.',
      },
      {
        heading: 'Link styled as button',
        html: `\
<a href="/dashboard" class="btn btn-primary">Go to dashboard</a>`,
      },
    ],
    js: `\
// Toggle a loading state during an async action
function setLoading(btn, loading) {
  btn.classList.toggle('btn-loading', loading);
  btn.setAttribute('aria-busy', String(loading));
  btn.disabled = loading;
}

document.querySelector('#save-btn').addEventListener('click', async function () {
  setLoading(this, true);
  try {
    await saveData();
  } finally {
    setLoading(this, false);
  }
});

// Confirm before a danger action
document.querySelector('#delete-btn').addEventListener('click', function () {
  if (!window.confirm('Delete this item? This cannot be undone.')) return;
  deleteItem();
});`,
  },

  /* ── Card ────────────────────────────────────────────────────────────── */
  card: {
    title: 'Card',
    description: 'Groups related content into a visual container. All parts (header, body, footer, media) are optional.',
    cssFile: 'card',
    extraCss: ['button'],
    sections: [
      {
        heading: 'Minimal card',
        html: `\
<div class="card">
  <div class="card-body">
    <p>Simple content with no header or footer.</p>
  </div>
</div>`,
      },
      {
        heading: 'Full structure',
        html: `\
<div class="card">
  <div class="card-header">
    <div>
      <h3 class="card-title">Project Alpha</h3>
      <p class="card-subtitle">Last updated 2 hours ago</p>
    </div>
    <button class="btn btn-ghost btn-sm">Edit</button>
  </div>
  <div class="card-body">
    <p>Main card content goes here.</p>
  </div>
  <div class="card-footer">
    <button class="btn btn-secondary btn-sm">Cancel</button>
    <button class="btn btn-primary btn-sm">Save</button>
  </div>
</div>`,
      },
      {
        heading: 'Card with media',
        html: `\
<article class="card">
  <img class="card-media" src="cover.jpg" alt="Article cover image">
  <div class="card-body">
    <h3 class="card-title">Article headline</h3>
    <p>Summary text that introduces the article.</p>
  </div>
</article>`,
      },
      {
        heading: 'Interactive (clickable) card',
        html: `\
<article class="card card-interactive" tabindex="0" role="button" aria-label="Open Project Alpha">
  <div class="card-body">
    <h3 class="card-title">Clickable card</h3>
    <p>Entire card surface is interactive.</p>
  </div>
</article>`,
      },
      {
        heading: 'Variants',
        html: `\
<div class="card card-elevated">
  <div class="card-body">Elevated — stronger shadow, no border</div>
</div>

<div class="card card-flat">
  <div class="card-body">Flat — subtle background, no shadow</div>
</div>

<div class="card card-danger">
  <div class="card-body"><strong>Action required:</strong> Your subscription expired.</div>
</div>

<div class="card card-success">
  <div class="card-body"><strong>Setup complete:</strong> Your account is ready.</div>
</div>`,
      },
      {
        heading: 'Card grid',
        html: `\
<div class="card-group card-group-3">
  <div class="card"><div class="card-body">Card one</div></div>
  <div class="card"><div class="card-body">Card two</div></div>
  <div class="card"><div class="card-body">Card three</div></div>
</div>`,
        note: 'Use `.card-group-2`, `.card-group-3`, or `.card-group-4` for responsive column grids.',
      },
    ],
    js: `\
// Handle interactive card click (keyboard + mouse)
document.querySelectorAll('.card-interactive').forEach(card => {
  function activate() {
    const href = card.dataset.href;
    if (href) window.location.href = href;
  }

  card.addEventListener('click', activate);
  card.addEventListener('keydown', e => {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      activate();
    }
  });
});`,
  },

  /* ── Input ───────────────────────────────────────────────────────────── */
  input: {
    title: 'Input',
    description: 'Form controls: text input, textarea, select, checkbox, and radio. Wrap inputs in `.field` for labels, hints, and error messages.',
    cssFile: 'input',
    sections: [
      {
        heading: 'Text field',
        html: `\
<div class="field">
  <label class="field-label" for="username">Username</label>
  <input class="input" id="username" type="text" placeholder="e.g. jsmith" autocomplete="username">
  <p class="field-hint">Only letters, numbers, and underscores.</p>
</div>`,
      },
      {
        heading: 'Error state',
        html: `\
<div class="field field-error">
  <label class="field-label" for="email">Email</label>
  <input class="input" id="email" type="email" value="not-an-email"
         aria-describedby="email-error" aria-invalid="true">
  <p class="field-error-msg" id="email-error" role="alert">
    Enter a valid email address.
  </p>
</div>`,
      },
      {
        heading: 'Password field',
        html: `\
<div class="field">
  <label class="field-label" for="password">Password</label>
  <div class="input-group">
    <input class="input" id="password" type="password" autocomplete="current-password">
    <button class="btn btn-ghost btn-icon input-addon" type="button" aria-label="Show password">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
        <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/>
      </svg>
    </button>
  </div>
</div>`,
      },
      {
        heading: 'Textarea',
        html: `\
<div class="field">
  <label class="field-label" for="bio">Bio</label>
  <textarea class="textarea" id="bio" rows="4"
            placeholder="Tell us about yourself…"
            maxlength="280" aria-describedby="bio-count"></textarea>
  <p class="field-hint" id="bio-count">0 / 280</p>
</div>`,
      },
      {
        heading: 'Select',
        html: `\
<div class="field">
  <label class="field-label" for="country">Country</label>
  <select class="select" id="country">
    <option value="">Select a country…</option>
    <option value="us">United States</option>
    <option value="gb">United Kingdom</option>
    <option value="ca">Canada</option>
  </select>
</div>`,
      },
      {
        heading: 'Checkbox group',
        html: `\
<fieldset>
  <legend class="field-label">Notifications</legend>
  <label class="field-checkbox">
    <input class="checkbox" type="checkbox" name="notify" value="email" checked>
    Email
  </label>
  <label class="field-checkbox">
    <input class="checkbox" type="checkbox" name="notify" value="sms">
    SMS
  </label>
  <label class="field-checkbox">
    <input class="checkbox" type="checkbox" name="notify" value="push">
    Push
  </label>
</fieldset>`,
      },
      {
        heading: 'Radio group',
        html: `\
<fieldset>
  <legend class="field-label">Plan</legend>
  <label class="field-radio">
    <input class="radio" type="radio" name="plan" value="free" checked>
    Free
  </label>
  <label class="field-radio">
    <input class="radio" type="radio" name="plan" value="pro">
    Pro — $12/mo
  </label>
  <label class="field-radio">
    <input class="radio" type="radio" name="plan" value="team">
    Team — $39/mo
  </label>
</fieldset>`,
      },
      {
        heading: 'Input group (prefix / suffix)',
        html: `\
<!-- With prefix -->
<div class="field">
  <label class="field-label" for="handle">Twitter handle</label>
  <div class="input-group">
    <span class="input-addon">@</span>
    <input class="input" id="handle" type="text" placeholder="username">
  </div>
</div>

<!-- With suffix -->
<div class="field">
  <label class="field-label" for="price">Price</label>
  <div class="input-group">
    <input class="input" id="price" type="number" min="0" step="0.01">
    <span class="input-addon">USD</span>
  </div>
</div>`,
      },
    ],
    js: `\
// Live character counter for a textarea
const bio   = document.querySelector('#bio');
const count = document.querySelector('#bio-count');
bio.addEventListener('input', () => {
  count.textContent = \`\${bio.value.length} / \${bio.maxLength}\`;
});

// Show/hide password toggle
document.querySelectorAll('[aria-label="Show password"]').forEach(btn => {
  btn.addEventListener('click', () => {
    const input = btn.closest('.input-group').querySelector('input');
    const isHidden = input.type === 'password';
    input.type = isHidden ? 'text' : 'password';
    btn.setAttribute('aria-label', isHidden ? 'Hide password' : 'Show password');
  });
});

// Inline validation — mark field invalid on blur
document.querySelectorAll('.field .input').forEach(input => {
  input.addEventListener('blur', () => {
    const field = input.closest('.field');
    const valid = input.checkValidity();
    field.classList.toggle('field-error', !valid);
    input.setAttribute('aria-invalid', String(!valid));

    const errEl = document.getElementById(input.getAttribute('aria-describedby'));
    if (errEl && !valid) errEl.textContent = input.validationMessage;
  });
});

// Reset field errors on focus
document.querySelectorAll('.field .input').forEach(input => {
  input.addEventListener('focus', () => {
    input.closest('.field').classList.remove('field-error');
    input.removeAttribute('aria-invalid');
  });
});`,
  },

  /* ── Badge ───────────────────────────────────────────────────────────── */
  badge: {
    title: 'Badge',
    description: 'Short status label or count indicator. Use `<span>` for non-interactive badges and `<button>` semantics when the badge itself is clickable.',
    cssFile: 'badge',
    sections: [
      {
        heading: 'Semantic variants',
        html: `\
<span class="badge badge-default">Default</span>
<span class="badge badge-primary">Primary</span>
<span class="badge badge-success">Active</span>
<span class="badge badge-danger">Expired</span>
<span class="badge badge-warning">Pending</span>
<span class="badge badge-info">Info</span>`,
      },
      {
        heading: 'Solid variants',
        html: `\
<span class="badge badge-solid-primary">New</span>
<span class="badge badge-solid-success">Verified</span>
<span class="badge badge-solid-danger">Error</span>
<span class="badge badge-solid-warning">Review</span>`,
      },
      {
        heading: 'Dot indicator',
        html: `\
<span class="badge badge-success badge-dot">Online</span>
<span class="badge badge-danger badge-dot">Offline</span>
<span class="badge badge-warning badge-dot">Away</span>`,
      },
      {
        heading: 'Count badge',
        html: `\
<!-- Standalone count -->
<span class="badge badge-count badge-solid-danger" aria-label="12 unread">12</span>

<!-- Count adjacent to a nav link -->
<a href="/inbox" style="display:inline-flex;align-items:center;gap:6px;">
  Inbox
  <span class="badge badge-count badge-solid-danger" aria-label="3 unread">3</span>
</a>`,
      },
      {
        heading: 'Removable tag',
        html: `\
<span class="badge badge-primary" id="tag-design">
  Design
  <button class="badge-remove" type="button" aria-label="Remove Design tag">×</button>
</span>

<span class="badge badge-primary" id="tag-ux">
  UX Research
  <button class="badge-remove" type="button" aria-label="Remove UX Research tag">×</button>
</span>`,
      },
      {
        heading: 'Sizes',
        html: `\
<span class="badge badge-success badge-sm">Small</span>
<span class="badge badge-success">Default</span>
<span class="badge badge-success badge-lg">Large</span>`,
      },
    ],
    js: `\
// Remove a tag when its × button is clicked
document.addEventListener('click', e => {
  const removeBtn = e.target.closest('.badge-remove');
  if (!removeBtn) return;
  const badge = removeBtn.closest('.badge');
  badge.remove();
});

// Dynamically update a count badge
function setCount(selector, count) {
  const el = document.querySelector(selector);
  if (!el) return;
  el.textContent = count;
  el.setAttribute('aria-label', \`\${count} unread\`);
  el.style.display = count === 0 ? 'none' : '';
}

// Example: update unread count after reading messages
setCount('.badge-count[aria-label*="unread"]', 0);`,
  },

  /* ── Alert ───────────────────────────────────────────────────────────── */
  alert: {
    title: 'Alert',
    description: 'Contextual feedback for user actions or system events. Use `role="alert"` for important errors and `role="status"` for informational or success messages.',
    cssFile: 'alert',
    extraCss: ['button'],
    sections: [
      {
        heading: 'Info alert',
        html: `\
<div class="alert alert-info" role="status">
  <div class="alert-content">
    <strong class="alert-title">Heads up</strong>
    <p class="alert-description">Your free trial ends in 3 days.</p>
    <div class="alert-actions">
      <button class="btn btn-sm btn-secondary">Dismiss</button>
      <button class="btn btn-sm btn-primary">Upgrade now</button>
    </div>
  </div>
</div>`,
      },
      {
        heading: 'Danger alert',
        html: `\
<div class="alert alert-danger" role="alert">
  <div class="alert-content">
    <strong class="alert-title">Payment failed</strong>
    <p class="alert-description">Your card ending in 4242 was declined.</p>
  </div>
  <button class="alert-close" type="button" aria-label="Dismiss">×</button>
</div>`,
      },
      {
        heading: 'Success alert',
        html: `\
<div class="alert alert-success" role="status">
  <div class="alert-content">
    <strong class="alert-title">Profile saved</strong>
    <p class="alert-description">Your changes have been applied.</p>
  </div>
</div>`,
      },
      {
        heading: 'Warning alert',
        html: `\
<div class="alert alert-warning" role="status">
  <div class="alert-content">
    <strong class="alert-title">Storage almost full</strong>
    <p class="alert-description">You've used 90% of your 5 GB allowance.</p>
  </div>
</div>`,
      },
      {
        heading: 'Banner (full-width, no radius)',
        html: `\
<div class="alert alert-warning alert-banner" role="status">
  <div class="alert-content">
    <strong class="alert-title">Scheduled maintenance</strong>
    <p class="alert-description">The service will be unavailable Saturday 02:00–04:00 UTC.</p>
  </div>
</div>`,
      },
      {
        heading: 'Toast (floating notification)',
        html: `\
<!-- Place this at the end of <body> -->
<div class="toast-region" aria-live="polite" aria-atomic="false">
  <!-- Toasts are injected here by JavaScript — see JS section below -->
</div>`,
        note: 'The `.toast-region` is a fixed-position container. Inject `.alert-toast` elements into it via JavaScript.',
      },
    ],
    js: `\
// Dismiss an alert by clicking its close button
document.addEventListener('click', e => {
  const closeBtn = e.target.closest('.alert-close');
  if (!closeBtn) return;
  const alert = closeBtn.closest('.alert');
  alert.setAttribute('aria-hidden', 'true');
  // Remove after CSS transition completes (or immediately if no transition)
  alert.addEventListener('transitionend', () => alert.remove(), { once: true });
  setTimeout(() => alert.remove(), 400); // fallback
});

// Dismiss an alert programmatically
function dismissAlert(alertEl) {
  alertEl.setAttribute('aria-hidden', 'true');
  alertEl.addEventListener('transitionend', () => alertEl.remove(), { once: true });
  setTimeout(() => alertEl.remove(), 400);
}

// Create and show a toast notification
function showToast({ title, description = '', variant = 'info', duration = 5000 }) {
  const region = document.querySelector('.toast-region');
  if (!region) return;

  const toast = document.createElement('div');
  toast.className = \`alert alert-toast alert-\${variant}\`;
  toast.setAttribute('role', variant === 'danger' ? 'alert' : 'status');
  toast.innerHTML = \`
    <div class="alert-content">
      <strong class="alert-title">\${title}</strong>
      \${description ? \`<p class="alert-description">\${description}</p>\` : ''}
    </div>
    <button class="alert-close" type="button" aria-label="Dismiss">×</button>
  \`;

  region.appendChild(toast);

  // Auto-dismiss
  const timer = duration > 0 ? setTimeout(() => dismissAlert(toast), duration) : null;

  // Manual dismiss
  toast.querySelector('.alert-close').addEventListener('click', () => {
    if (timer) clearTimeout(timer);
    dismissAlert(toast);
  });
}

// Usage examples:
// showToast({ title: 'Saved successfully', variant: 'success' });
// showToast({ title: 'Upload failed', description: 'File exceeds 10 MB limit.', variant: 'danger', duration: 0 });`,
  },

  /* ── Typography ──────────────────────────────────────────────────────── */
  typography: {
    title: 'Typography',
    description: 'Typography utility classes. No JavaScript required. Wrap long-form content in `.prose` for automatic rhythm and spacing.',
    cssFile: 'typography',
    extraCss: [],
    sections: [
      {
        heading: 'Display headings (marketing / hero)',
        html: `\
<h1 class="display-lg">Display large</h1>
<h1 class="display-md">Display medium</h1>
<h2 class="display-sm">Display small</h2>`,
      },
      {
        heading: 'Section headings',
        html: `\
<h1 class="heading-xl">Heading XL (≈ h1)</h1>
<h2 class="heading-lg">Heading LG (≈ h2)</h2>
<h3 class="heading-md">Heading MD (≈ h3)</h3>
<h4 class="heading-sm">Heading SM (≈ h4)</h4>
<h5 class="heading-xs">HEADING XS (≈ h5/h6)</h5>`,
      },
      {
        heading: 'Body text',
        html: `\
<p class="text-lg">Large body — introductory paragraphs</p>
<p class="text-md">Default body — general copy</p>
<p class="text-sm">Small body — supporting detail</p>
<p class="text-xs">Extra small — metadata, timestamps</p>`,
      },
      {
        heading: 'Color modifiers',
        html: `\
<p class="text-md">Default text color</p>
<p class="text-md text-subtle">Subtle — secondary information</p>
<p class="text-md text-muted">Muted — disabled or de-emphasised</p>
<p class="text-md text-danger">Danger — errors or destructive warnings</p>
<p class="text-md text-success">Success — confirmations</p>
<p class="text-md text-warning">Warning — caution messages</p>
<p class="text-md text-info">Info — neutral hints</p>`,
      },
      {
        heading: 'Weight modifiers',
        html: `\
<p class="text-md font-normal">Normal weight (400)</p>
<p class="text-md font-medium">Medium weight (500)</p>
<p class="text-md font-semibold">Semibold weight (600)</p>
<p class="text-md font-bold">Bold weight (700)</p>`,
      },
      {
        heading: 'Inline code',
        html: `\
<p class="text-md">
  Install with <code class="code-inline">npm install ai-design-system</code>
  then import <code class="code-inline">tokens.css</code>.
</p>`,
      },
      {
        heading: 'Code block',
        html: `\
<pre class="code-block"><code>import { applyAdapter } from 'ai-design-system/lib-adapters';
applyAdapter('shadcn');</code></pre>`,
      },
      {
        heading: 'Prose (long-form content)',
        html: `\
<article class="prose">
  <h2>Getting started</h2>
  <p>The AI Design System is a token-first CSS framework. All values are
     expressed as CSS custom properties so they respond to theme changes.</p>
  <h3>Installation</h3>
  <p>Add the package and import the stylesheet that matches your setup:</p>
  <pre><code>npm install ai-design-system</code></pre>
  <ul>
    <li>Use <code>tokens.css</code> for the complete token layer.</li>
    <li>Use <code>src/components/*.css</code> for individual component styles.</li>
    <li>Use <code>lib-adapters/shadcn.css</code> to bridge shadcn/ui variables.</li>
  </ul>
  <blockquote>
    <p>All component CSS is free of raw values — every property references a
       Layer 2 token so themes propagate automatically.</p>
  </blockquote>
</article>`,
        note: '`.prose` applies typographic rhythm to all direct-descendant block elements. Max-width is 65ch.',
      },
    ],
    js: null,   // no JS for typography
  },
};

/* ─── Doc generator ──────────────────────────────────────────────────────── */

function makeMd(slug, comp) {
  const s = setup(comp.cssFile, comp.extraCss || []);

  const htmlForSection = (section) => [
    `### ${section.heading}`,
    '',
    '```html',
    section.html,
    '```',
    ...(section.note ? ['', `> ${section.note}`] : []),
    '',
  ].join('\n');

  const parts = [
    `# ${comp.title}`,
    '',
    `**Library:** Vanilla HTML/CSS/JS  `,
    `**CSS file:** \`src/components/${comp.cssFile}.css\`  `,
    `**Spec:** \`specs/components/${slug}.md\``,
    '',
    '---',
    '',
    '## Overview',
    '',
    comp.description,
    '',
    '---',
    '',
    '## Setup',
    '',
    '### HTML — link tags',
    '',
    '```html',
    s.links,
    '```',
    '',
    '### CSS — bundler / PostCSS',
    '',
    '```css',
    s.imports,
    '```',
    '',
    '---',
    '',
    '## HTML examples',
    '',
    ...comp.sections.map(htmlForSection),
    '---',
    '',
  ];

  if (comp.js) {
    parts.push(
      '## JavaScript',
      '',
      '```js',
      comp.js,
      '```',
      '',
      '---',
      '',
    );
  } else {
    parts.push(
      '## JavaScript',
      '',
      '_No JavaScript required for this component._',
      '',
      '---',
      '',
    );
  }

  parts.push(
    '## Class reference',
    '',
    `See full API table: [\`specs/components/${slug}.md\`](../specs/components/${slug}.md)`,
    '',
  );

  return parts.join('\n');
}

/* ─── Main ───────────────────────────────────────────────────────────────── */

function main() {
  const outDir = path.resolve(OUT_DIR);
  fs.mkdirSync(outDir, { recursive: true });

  const slugs = Object.keys(COMPONENTS);

  for (const slug of slugs) {
    const comp = COMPONENTS[slug];
    const md   = makeMd(slug, comp);
    fs.writeFileSync(path.join(outDir, `${slug}.md`), md, 'utf8');
    console.log(`  ✓  ${slug}.md`);
  }

  const rows = slugs.map(slug => {
    const comp = COMPONENTS[slug];
    const hasJs = !!comp.js;
    return `| [${comp.title}](${slug}.md) | \`src/components/${comp.cssFile}.css\` | ${hasJs ? '✓' : '—'} |`;
  }).join('\n');

  const index = `# Vanilla HTML/CSS/JS Docs — Index

Generated by \`scripts/build-vanilla-docs.js\`. Each file contains ready-to-use
HTML, CSS setup, and JavaScript patterns for every AI Design System component.

No framework required — just link \`tokens.css\` and the component CSS files.

| Component | CSS file | JS patterns |
|---|---|---|
${rows}

## Full page template

\`\`\`html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My App</title>

  <!-- AI Design System -->
  <link rel="stylesheet" href="path/to/tokens.css">
  <link rel="stylesheet" href="path/to/src/base/reset.css">
  <link rel="stylesheet" href="path/to/src/base/typography.css">

  <!-- Add only the components you use -->
  <link rel="stylesheet" href="path/to/src/components/button.css">
  <link rel="stylesheet" href="path/to/src/components/card.css">
  <link rel="stylesheet" href="path/to/src/components/input.css">
  <link rel="stylesheet" href="path/to/src/components/badge.css">
  <link rel="stylesheet" href="path/to/src/components/alert.css">
</head>
<body>

  <!-- Toast region — place at end of body -->
  <div class="toast-region" aria-live="polite"></div>

</body>
</html>
\`\`\`

## Token customisation

Override any \`--ds-*\` variable before \`tokens.css\` to change the theme:

\`\`\`css
/* custom-theme.css — link BEFORE tokens.css */
:root {
  --ds-interactive: #6366f1;   /* primary action colour */
  --ds-font-sans:   'Inter', sans-serif;
  --ds-radius-md:   8px;
}
\`\`\`

Full \`--ds-*\` reference: \`specs/adapters/custom.md\`
`;

  fs.writeFileSync(path.join(outDir, 'INDEX.md'), index, 'utf8');

  console.log(`\n✅  vanilla-docs/INDEX.md written — ${slugs.length} components.\n`);
}

main();
