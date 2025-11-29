# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- GitHub Actions CI workflow for template testing and docs deployment
- CHANGELOG.md following keep-a-changelog format

### Changed
- Cleaned up cookiecutter.json with better defaults and removed unused options
- Reorganized project-management/ to follow BEACON framework structure

## [0.2.0] - 2025-11-29

### Added
- Comprehensive MkDocs documentation for devenv template (15+ pages)
- MkDocs documentation scaffold for generated projects (20+ pages)
- mkdocstrings integration for auto-generated API reference
- Root justfile with docs commands (docs-serve, docs-build, docs-deploy)
- uv project configuration with docs dependency group

### Changed
- Updated root README.md with cleaner structure and documentation links
- Updated template README.md to reference MkDocs documentation

## [0.1.0] - 2025-11-29

### Added
- Python 3-layer architecture scaffold (domain/adapters/services)
- FastAPI REST API with health check and CRUD endpoints
- Typer CLI with version, config, and serve commands
- uv package manager with hatch-vcs versioning
- pytest test suite with 18 passing tests
- justfile with comprehensive development commands
- pre-commit hooks for code quality
- VS Code Dev Container configuration
- Claude AI agent configurations
- MCP server integrations (SearxNG, Crawl4AI, Context7, Memgraph)
- BEACON framework project-management structure
- ADRs documenting key architectural decisions

### Changed
- Migrated from pip/requirements.txt to uv/pyproject.toml
- Updated Dockerfile to use uv for dependency management

## [0.0.1] - 2025-11-28

### Added
- Initial cookiecutter template structure
- Docker Compose development environment
- Basic FastAPI application scaffold

[Unreleased]: https://github.com/JAMESVEITCH/devenv/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/JAMESVEITCH/devenv/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/JAMESVEITCH/devenv/compare/v0.0.1...v0.1.0
[0.0.1]: https://github.com/JAMESVEITCH/devenv/releases/tag/v0.0.1
