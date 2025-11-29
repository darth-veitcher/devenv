# Cookiecutter Options

All available options when generating a project with devenv.

## Options Reference

| Option | Default | Description |
|--------|---------|-------------|
| `project_name` | `My Project` | Human-readable project name |
| `project_slug` | (derived) | URL/package-safe name |
| `project_description` | `A sophisticated...` | Short description |
| `author_name` | `Your Name` | Your name |
| `author_email` | `your.email@example.com` | Your email |
| `github_username` | `yourusername` | GitHub username |
| `python_version` | `3.12` | Python version |
| `fastapi_version` | `0.115.0` | FastAPI version |
| `uvicorn_version` | `0.32.0` | Uvicorn version |
| `app_port` | `8000` | Default application port |

## Detailed Options

### project_name

The human-readable name of your project.

```
project_name [My Project]: My Awesome App
```

- Appears in documentation
- Used in CLI help text
- Displayed in API docs

### project_slug

URL and package-safe version of the project name.

```
project_slug [my-awesome-app]:
```

- Auto-generated from project_name (lowercase, hyphens)
- Used for package directory: `src/my_awesome_app/`
- Used for git repository name
- Used in Docker image names

!!! tip
    Usually accept the default derived from project_name.

### project_description

Short description of your project.

```
project_description [A sophisticated multi-layer...]: A task management API
```

- Appears in pyproject.toml
- Shown in API documentation
- Used in README

### author_name & author_email

Your details for package metadata.

```
author_name [Your Name]: Jane Developer
author_email [your.email@example.com]: jane@example.com
```

- Listed in pyproject.toml
- Appears in LICENSE
- Used for git configuration suggestions

### github_username

Your GitHub username.

```
github_username [yourusername]: janedeveloper
```

- Used in documentation URLs
- Repository links in pyproject.toml
- MkDocs configuration

### python_version

Minimum Python version required.

```
python_version [3.12]:
```

- Sets `requires-python` in pyproject.toml
- Determines Docker base image
- Affects type hint features available

!!! note
    Python 3.12+ is recommended for best type hint support.

### fastapi_version & uvicorn_version

Framework versions.

```
fastapi_version [0.115.0]:
uvicorn_version [0.32.0]:
```

- Pinned in pyproject.toml dependencies
- Consider updating to latest stable versions

### app_port

Default port for the application.

```
app_port [8000]:
```

- Used in Docker port mappings
- Development server default
- API documentation URLs

## Example Session

```bash
$ cookiecutter gh:JAMESVEITCH/devenv

project_name [My Project]: Task Tracker API
project_slug [task-tracker-api]:
project_description [A sophisticated...]: A simple task management API
author_name [Your Name]: Jane Developer
author_email [your.email@example.com]: jane@example.com
github_username [yourusername]: janedeveloper
python_version [3.12]:
fastapi_version [0.115.0]:
uvicorn_version [0.32.0]:
app_port [8000]: 3000
```

Results in:

- Project directory: `task-tracker-api/`
- Package: `src/task_tracker_api/`
- API at: `http://localhost:3000`

## Non-Interactive Mode

Skip prompts with `--no-input`:

```bash
cookiecutter gh:JAMESVEITCH/devenv --no-input \
  project_name="My API" \
  author_name="Jane" \
  github_username="janedeveloper"
```

## Replay Previous Values

```bash
# Use previous answers
cookiecutter gh:JAMESVEITCH/devenv --replay
```

## Config File

Create `~/.cookiecutterrc`:

```yaml
default_context:
  author_name: "Jane Developer"
  author_email: "jane@example.com"
  github_username: "janedeveloper"
```

These become new defaults for all cookiecutter projects.

## Next Steps

- [Customization](customization.md) - Modify after generation
- [Quickstart](../getting-started/quickstart.md) - Generate your first project
