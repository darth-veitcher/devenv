# ADR-003: MkDocs for Documentation

## Status

Accepted

## Context

Projects need documentation for:
- Getting started guides
- Architecture explanations
- API reference (auto-generated from docstrings)
- Development guides

Options considered:

- **Sphinx**: Traditional Python choice, powerful but complex RST syntax
- **MkDocs**: Markdown-based, simpler, modern themes available
- **Docusaurus**: React-based, overkill for Python projects
- **Read the Docs**: Hosting service, not a generator

## Decision

Use **MkDocs** with the following stack:

- **mkdocs-material**: Modern, feature-rich theme
- **mkdocstrings**: Auto-generate API docs from Python docstrings
- **pymdown-extensions**: Enhanced Markdown features

Configuration in `mkdocs.yml`:
```yaml
theme:
  name: material
  palette:
    primary: indigo

plugins:
  - search
  - mkdocstrings:
      handlers:
        python:
          options:
            docstring_style: google
```

## Consequences

### Positive

- Markdown is familiar and easy to write
- Material theme is beautiful out of the box
- mkdocstrings auto-generates API reference from code
- Fast build times
- Easy GitHub Pages deployment (`mkdocs gh-deploy`)
- Great search functionality

### Negative

- Less powerful than Sphinx for complex documentation
- Some advanced features require extensions
- Material theme features require configuration

### Neutral

- Hosted via GitHub Pages (free)
- Requires learning mkdocs.yml configuration

## Escape Hatch

If MkDocs proves insufficient:
1. Markdown files are portable to any system
2. docstrings work with Sphinx too
3. Can run both in parallel during migration
4. Content is the same, only the generator changes

---

_Created: 2025-11-29_
_Last Updated: 2025-11-29_
