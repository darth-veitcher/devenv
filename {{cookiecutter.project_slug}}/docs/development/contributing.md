# Contributing

Thank you for your interest in contributing to {{ cookiecutter.project_name }}!

## Development Setup

### Prerequisites

- Python {{ cookiecutter.python_version }}+
- uv (recommended) or pip
- Git

### Getting Started

1. **Clone the repository**

    ```bash
    git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
    cd {{ cookiecutter.project_slug }}
    ```

2. **Install dependencies**

    ```bash
    uv sync --all-extras
    ```

3. **Run tests**

    ```bash
    just test
    ```

4. **Start development server**

    ```bash
    just dev
    ```

## Development Workflow

### Branch Naming

Use descriptive branch names:

- `feature/add-user-authentication`
- `fix/entity-validation-error`
- `docs/update-api-reference`
- `refactor/simplify-service-layer`

### Making Changes

1. Create a feature branch from `main`
2. Make your changes
3. Write/update tests
4. Run the full test suite
5. Update documentation if needed
6. Submit a pull request

### Code Style

This project uses:

- **Ruff** for linting and formatting
- **MyPy** for type checking
- **Google-style docstrings**

Run all checks:

```bash
just lint      # Ruff linting
just format    # Ruff formatting
just typecheck # MyPy type checking
just check     # All checks
```

### Commit Messages

Follow conventional commits:

```
type(scope): description

[optional body]

[optional footer]
```

Types:

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance

Examples:

```
feat(api): add pagination to entity list endpoint
fix(domain): correct validation for empty names
docs(readme): update installation instructions
```

## Testing

### Running Tests

```bash
# All tests
just test

# With coverage
just test-cov

# Specific file
uv run pytest tests/unit/domain/test_entities.py -v

# Specific test
uv run pytest tests/unit/domain/test_entities.py::test_create_entity -v
```

### Writing Tests

Follow the Arrange-Act-Assert pattern:

```python
async def test_create_entity(service):
    # Arrange
    name = "Test Entity"
    description = "A test"

    # Act
    entity = await service.create(name, description)

    # Assert
    assert entity.name == name
    assert entity.description == description
```

### Test Organization

```
tests/
├── conftest.py          # Shared fixtures
├── unit/                # Unit tests (fast, isolated)
│   ├── domain/
│   └── services/
└── integration/         # Integration tests (slower, realistic)
    └── test_api.py
```

## Pull Request Process

1. **Ensure all tests pass**

    ```bash
    just check && just test
    ```

2. **Update the changelog** if applicable

3. **Create a pull request** with:
    - Clear description of changes
    - Link to related issues
    - Screenshots for UI changes

4. **Address review feedback**

5. **Squash and merge** when approved

## Code of Conduct

Be respectful and constructive. We're all here to learn and build great software.

## Questions?

Open an issue or reach out to the maintainers.
