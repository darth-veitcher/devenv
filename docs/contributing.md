# Contributing to devenv

Thank you for your interest in contributing to devenv!

## Ways to Contribute

- **Report bugs** - Open an issue describing the problem
- **Suggest features** - Open an issue with your idea
- **Submit fixes** - Create a pull request
- **Improve documentation** - Fix typos or add examples
- **Share feedback** - Let us know how you use devenv

## Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/darth-veitcher/devenv.git
cd devenv
```

### 2. Install Dependencies

The template itself doesn't have Python dependencies, but to test it:

```bash
pip install cookiecutter
```

### 3. Test Generation

```bash
# Generate a test project
cookiecutter . --no-input -o /tmp

# Verify it works
cd /tmp/my-project
uv sync --all-extras
uv run pytest
```

## Making Changes

### Template Files

Files in `{{cookiecutter.project_slug}}/` are templated:

```
# Uses Jinja2 syntax
{{ cookiecutter.project_name }}
{{ cookiecutter.author_name }}
```

### Root Files

Files at the root of devenv/ are for the template itself:

- `cookiecutter.json` - Template variables
- `hooks/` - Pre/post generation scripts
- `docs/` - Template documentation (this site)

### Escaping Just Variables

In justfiles, escape `just` variables:

```just
# Wrong - cookiecutter interprets {{ARGS}}
serve *ARGS:
    my_app serve {{ARGS}}

# Correct - escape for cookiecutter
serve *ARGS:
    my_app serve {{ '{{' }}ARGS{{ '}}' }}
```

## Testing Changes

### Generate and Test

```bash
# Clean test
rm -rf /tmp/test-project

# Generate
cookiecutter . --no-input \
  -o /tmp \
  project_name="test-project"

# Test
cd /tmp/test-project
uv sync --all-extras
uv run pytest
uv run mkdocs build
```

### Test Different Options

```bash
# Different Python version
cookiecutter . --no-input \
  -o /tmp \
  python_version="3.11"

# Different port
cookiecutter . --no-input \
  -o /tmp \
  app_port="3000"
```

## Pull Request Process

1. **Fork** the repository
2. **Create a branch** for your changes
3. **Make changes** and test thoroughly
4. **Update documentation** if needed
5. **Submit a PR** with clear description

### PR Checklist

- [ ] Generated projects pass all tests
- [ ] Documentation builds without errors
- [ ] Changes are described in PR
- [ ] No breaking changes (or clearly documented)

## Code Style

### Template Files

- Follow Python best practices
- Use type hints everywhere
- Google-style docstrings
- Ruff for linting/formatting

### Documentation

- Clear, concise language
- Include code examples
- Use admonitions for tips/warnings

## Project Structure

```
devenv/
├── {{cookiecutter.project_slug}}/  # Template files
├── docs/                            # This documentation
├── hooks/                           # Generation hooks
│   └── post_gen_project.py
├── cookiecutter.json                # Template variables
├── mkdocs.yml                       # Docs configuration
└── README.md                        # Repo readme
```

## Getting Help

- **Issues** - For bugs and feature requests
- **Discussions** - For questions and ideas

## Code of Conduct

Be respectful and constructive. We're all here to build great tools.

## License

Contributions are licensed under MIT, same as the project.
