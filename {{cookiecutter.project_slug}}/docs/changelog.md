# Changelog

All notable changes to {{ cookiecutter.project_name }} will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial project structure with 3-layer architecture
- Domain entities with `EntityBase` and `ExampleEntity`
- Service layer with `ExampleService`
- In-memory repository implementation
- FastAPI REST API with CRUD endpoints
- Typer CLI with commands: version, config, create, get, serve
- Comprehensive test suite (unit + integration)
- MkDocs documentation with mkdocs-material theme
- Docker and Docker Compose support
- BEACON project-management structure

### Changed
- Nothing yet

### Deprecated
- Nothing yet

### Removed
- Nothing yet

### Fixed
- Nothing yet

### Security
- Nothing yet

---

## Version History

### [0.1.0] - YYYY-MM-DD

Initial release.

#### Added
- Core domain entities
- Basic CRUD operations
- REST API
- CLI interface
- Documentation

---

## Release Process

1. Update version in `pyproject.toml` (or let hatch-vcs handle it)
2. Update this changelog
3. Create a git tag: `git tag v0.1.0`
4. Push the tag: `git push origin v0.1.0`

The version is automatically derived from git tags via hatch-vcs.
