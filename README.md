# Cookiecutter Multi-Layer Containerized Development Environment

A [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for creating a sophisticated multi-layer containerized development environment with complete host isolation and AI-powered development support.

> 📋 **Project Documentation**: See the [`project-management/`](project-management/) folder for detailed PRD, implementation plan, and architectural decisions for the Solo Dev AI Agent enhancements.

## Features

- 🔒 **Complete Host Isolation**: Zero development dependencies on host machine
- 🌐 **Network Segmentation**: Isolated networks for development tools and application services
- 🐳 **Docker-First**: Everything runs in containers with Docker Compose
- 🤖 **AI-Powered Development**: Integrated Claude AI with MCP services
- 🔧 **VS Code Dev Containers**: Professional development experience
- 🚀 **FastAPI Application**: Modern Python web framework included
- 🗄️ **PostgreSQL Database**: Production-ready database setup
- 🔍 **Development Services**: SearxNG, Crawl4AI, Context7, and more

## Quick Start

### Prerequisites

- Python 3.8+ (for Cookiecutter)
- Docker Desktop
- VS Code with Dev Containers extension
- Git

### Installation

1. Install Cookiecutter:
   ```bash
   pip install cookiecutter
   ```

2. Generate a new project:
   ```bash
   cookiecutter https://github.com/darth-veitcher/devenv.git
   ```

3. Answer the prompts:
   - `project_name`: Your project's human-readable name
   - `project_slug`: Directory name for your project (auto-generated)
   - `author_name`: Your name
   - `author_email`: Your email
   - `python_version`: Python version for the application (default: 3.12)
   - `app_port`: Port for your application (default: 8000)
   - And more...

4. Navigate to your new project:
   ```bash
   cd your-project-slug
   code .
   ```

5. When VS Code opens, it will prompt to "Reopen in Container" - click yes!

## Template Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `project_name` | Human-readable project name | Multi-Layer Containerized Development Environment |
| `project_slug` | Directory name (auto-generated from project_name) | multi-layer-containerized-development-environment |
| `project_description` | Short project description | A sophisticated multi-layer containerized development environment |
| `author_name` | Your name | Your Name |
| `author_email` | Your email | your.email@example.com |
| `github_username` | Your GitHub username | yourusername |
| `python_version` | Python version for containers | 3.12 |
| `fastapi_version` | FastAPI framework version | 0.104.1 |
| `uvicorn_version` | Uvicorn server version | 0.24.0 |
| `postgres_version` | PostgreSQL version | 15 |
| `postgres_user` | Database username | appuser |
| `postgres_password` | Database password | password |
| `postgres_db` | Database name | appdb |
| `app_port` | Application port | 8000 |
| `enable_mcp_services` | Enable MCP AI services | yes |
| `use_claude_ai` | Configure Claude AI integration | yes |

## Project Structure

After generation, your project will have:

```
your-project-slug/
├── .devcontainer/              # VS Code Dev Container configuration
│   ├── compose.yml             # Development services (SearxNG, Crawl4AI, etc.)
│   ├── devcontainer.json       # VS Code settings and container config
│   └── mcp/                   # MCP service configurations and submodules
│       ├── context7/          # Context7 documentation service
│       └── memgraph-ai-toolkit/ # Memgraph AI Toolkit (git submodule)
├── app/                       # Your FastAPI application
│   ├── compose.yml            # Application stack (app + PostgreSQL)
│   ├── Dockerfile             # Application container
│   ├── main.py               # FastAPI application entry point
│   └── requirements.txt       # Python dependencies
├── .claude/                   # Claude AI configuration
│   ├── CLAUDE.md             # Project context and instructions
│   ├── COMMANDS.md           # Available slash commands
│   ├── FLAGS.md              # Command flags reference
│   ├── PRINCIPLES.md         # Development principles
│   ├── RULES.md              # Operational rules
│   ├── MCP.md                # MCP server configurations
│   ├── PERSONAS.md           # AI personas system
│   ├── ORCHESTRATOR.md       # Routing intelligence
│   └── MODES.md              # Operational modes
├── .serena/                   # Serena MCP configuration
├── .pre-commit-config.yaml    # Pre-commit hooks (linting, formatting, security)
├── .gitignore                # Git ignore rules
├── .gitmodules               # Git submodule configuration
├── .mcp.json                 # MCP server configuration
└── README.md                 # Project documentation
```

## Customization

### Adding Dependencies

Edit `app/requirements.txt` to add Python packages:
```
fastapi=={{ cookiecutter.fastapi_version }}
uvicorn=={{ cookiecutter.uvicorn_version }}
your-package==1.0.0
```

### Modifying Services

Edit `app/compose.yml` to add new services or modify existing ones.

### Configuring MCP Services

Edit `.mcp.json` to configure AI services and tools.

### Using Pre-commit Hooks

The template includes comprehensive pre-commit hooks that run automatically on each commit:

- **Code Quality**: Python linting and formatting with Ruff
- **Security**: Bandit security analysis and private key detection
- **Standards**: YAML, JSON, TOML syntax validation
- **Consistency**: Trailing whitespace, line endings, file size checks
- **Testing**: Optional fast test runs (manual trigger)

To run hooks manually:
```bash
uv run pre-commit run --all-files      # Run all hooks
uv run pre-commit run ruff             # Run specific hook
uv run pre-commit run --hook-stage manual bandit  # Run security checks
```

## Post-Generation

The template includes a post-generation hook (`hooks/post_gen_project.py`) that automatically:
- **Initializes git repository**: Creates `.git` and makes initial commit
- **Sets up MCP submodules**: Adds memgraph-ai-toolkit submodule for AI integration
- **Installs pre-commit hooks**: Automatically configures code quality gates
  - Installs `pre-commit` as dev dependency using `uv`
  - Sets up git hooks with comprehensive linting, formatting, and security checks
  - Includes Python (ruff), YAML, Markdown, and custom project validations
  - Graceful fallbacks if `uv` is not available
- **Provides next steps guidance**: Clear instructions for getting started

This ensures your generated project has production-ready development practices from day one.

## Architecture

The generated project uses a four-layer architecture:

1. **Host Machine**: Only Docker runtime
2. **Development Environment**: VS Code devcontainer
3. **Development Services**: MCP servers and utilities
4. **Application Stack**: Your application and databases

## Security

- No development tools on host machine
- Isolated networks for different concerns
- Internal-only networks for sensitive services
- Non-root containers

## Contributing

1. Fork this repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This template is open source and available under the [MIT License](LICENSE).

## Accessing Services

When running in the devcontainer, these services are available:

- **Crawl4AI**: http://crawl4ai:11235
- **SearxNG**: http://searxng:8080
- **Memgraph**: bolt://memgraph:7687
- **Memgraph Lab**: http://memgraph-lab:3000 (Visual graph exploration)
- **Redis**: redis:6379
- **Context7**: http://context7-mcp:8080

From the host machine (if port forwarding is enabled):
- **SearxNG**: http://localhost:8080
- **Crawl4AI**: http://localhost:11235
- **Memgraph Lab**: http://localhost:3000

## Acknowledgments

- [Cookiecutter](https://github.com/cookiecutter/cookiecutter) for the templating engine
- [VS Code Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers) for the development experience
- [Claude AI](https://claude.ai) and MCP for AI-powered development tools
- [Memgraph](https://memgraph.com) for the graph database with MAGE algorithms
