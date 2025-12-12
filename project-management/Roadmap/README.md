# Project Roadmap: devenv Cookiecutter Template

## Current Status
**Active Bullet:** #43 - Add CLI commands using UserService
**Phase:** BUILD
**Started:** 2025-12-12
**Milestone 5:** In Progress

---

## Milestone 1: Python Quickstart Enhancement ✅

*Completed 2025-11-29*

### Phase 1: Foundation Fixes (Bullets 1-3) ✅
- [x] **Bullet #1**: Fix broken paths in python-expert.md
- [x] **Bullet #2**: Sync .claude/ between root and template
- [x] **Bullet #3**: Add reference/python/ to template

### Phase 2: Python Scaffold (Bullets 4-8) ✅
- [x] **Bullet #4**: Create src/ package layout in template
- [x] **Bullet #5**: Add pyproject.toml with uv and hatch-vcs
- [x] **Bullet #6**: Create 3-layer architecture scaffold
- [x] **Bullet #7**: Add CLI entry point (Typer)
- [x] **Bullet #8**: Add pytest setup with initial tests

### Phase 3: BEACON & DX (Bullets 9-11) ✅
- [x] **Bullet #9**: Add project-management/ BEACON structure
- [x] **Bullet #10**: Add justfile with Python commands
- [x] **Bullet #11**: Update Dockerfile for uv

### Phase 4: Validation (Bullets 12-14) ✅
- [x] **Bullet #12**: Update template README.md
- [x] **Bullet #13**: Verify template structure
- [x] **Bullet #14**: Commit and test generation - 18 tests pass

---

## Milestone 2: Documentation Overhaul ✅

*Completed 2025-11-29*

### Phase 5: Template MkDocs Foundation (Bullets 15-17) ✅
- [x] **Bullet #15**: Create mkdocs.yml with mkdocs-material theme
- [x] **Bullet #16**: Add docs/ scaffold with index.md and structure
- [x] **Bullet #17**: Configure mkdocstrings for API reference

### Phase 6: Template Documentation Content (Bullets 18-20) ✅
- [x] **Bullet #18**: Write getting-started/ (installation, quickstart, config)
- [x] **Bullet #19**: Write architecture/ (3-layer overview, domain, adapters, services)
- [x] **Bullet #20**: Write api/ and reference/ (CLI, REST, auto-docs)

### Phase 7: Root devenv Documentation (Bullets 21-23) ✅
- [x] **Bullet #21**: Create root mkdocs.yml and docs/ scaffold
- [x] **Bullet #22**: Write getting-started/ and features/
- [x] **Bullet #23**: Write configuration/ and reference/

### Phase 8: Integration & Polish (Bullets 24-26) ✅
- [x] **Bullet #24**: Add justfile docs commands (docs-serve, docs-build)
- [x] **Bullet #25**: Update READMEs to reference full documentation
- [x] **Bullet #26**: Test generation, verify docs build correctly

---

## Milestone 3: CI/CD & Quality ✅

*Completed 2025-11-29*

### Phase 9: Continuous Integration (Bullets 27-29) ✅
- [x] **Bullet #27**: Add GitHub Actions CI workflow
- [x] **Bullet #28**: Auto-deploy docs to GitHub Pages on push to main
- [x] **Bullet #29**: Clean up cookiecutter.json and add CHANGELOG.md

### Phase 10: Quality & Housekeeping (Bullets 30-32) ✅
- [x] **Bullet #30**: Add pre-commit hooks to root devenv repo
- [x] **Bullet #31**: Create release workflow with semantic versioning
- [x] **Bullet #32**: Tag v0.3.0 release

---

## Milestone 4: Template Customization ✅

*Completed 2025-11-30*

### Phase 11: Conditional Features (Bullets 33-36) ✅
- [x] **Bullet #33**: Make enable_mcp_services toggle compose services
- [x] **Bullet #34**: Make .mcp.json conditional based on enable_* flags
- [x] **Bullet #35**: Add database choice (PostgreSQL, SQLite, None)
- [x] **Bullet #36**: Add API framework choice (FastAPI, None)

### Phase 12: Polish & Ship (Bullets 37-40) ✅
- [x] **Bullet #37**: Separate SQLAlchemy models from repositories (adapters/models.py)
- [x] **Bullet #38**: Add Pydantic schemas for API DTOs (api/schemas.py)
- [x] **Bullet #39**: Expose PostgreSQL port 5433 for integration testing
- [x] **Bullet #40**: Enhance `just test-integration` with DATABASE_URL
- [x] **Bullet #41**: Verify full configuration matrix (6 combinations, all pass)

---

## Milestone 5: Production Patterns ⏳

*Started 2025-12-12*

### Phase 13: Documentation & DX (Bullets 42-44)
- [x] **Bullet #42**: Document cache/graph extension patterns in docs
- [ ] **Bullet #43**: Add CLI commands using UserService (create, get, list)
- [ ] **Bullet #44**: Expand /health endpoint for Redis/FalkorDB status

### Phase 14: Database Migrations (Bullets 45-47)
- [ ] **Bullet #45**: Add Alembic to pyproject.toml with conditional deps
- [ ] **Bullet #46**: Create initial migration for User model
- [ ] **Bullet #47**: Add justfile commands (migrate, migrate-create)

### Phase 15: Background Tasks (Bullets 48-50)
- [ ] **Bullet #48**: Add ARQ (async Redis queue) as optional dependency
- [ ] **Bullet #49**: Create task infrastructure module with example task
- [ ] **Bullet #50**: Add task worker to docker-compose

### Phase 16: Authentication (Bullets 51-54)
- [ ] **Bullet #51**: Add JWT token generation/validation infrastructure
- [ ] **Bullet #52**: Create auth middleware and dependencies
- [ ] **Bullet #53**: Add login/register endpoints
- [ ] **Bullet #54**: Protect User endpoints with auth decorators

---

## Configuration Matrix

All combinations verified:

| api_framework | database_backend | cache_backend | Tests | Status |
|---------------|------------------|---------------|-------|--------|
| fastapi | none | none | 27 | ✅ |
| fastapi | sqlite | none | 27 | ✅ |
| fastapi | sqlite | redis | 27 | ✅ |
| fastapi | sqlite | falkordb | 27 | ✅ |
| fastapi | postgresql | falkordb | 18 | ✅ |
| none | none | none | 12 | ✅ |
| none | sqlite | none | 12 | ✅ |
| none | postgresql | none | 12 | ✅ |

---

## Recent Completions
- 2025-12-12: Bullet #42 - Document cache/graph extension patterns (docs/architecture/cache-graph.md)
- 2025-11-30: Bullet #41 - Full matrix verification, Milestone 4 complete!
- 2025-11-30: Bullet #40 - Enhanced just test-integration for PostgreSQL
- 2025-11-30: Bullet #39 - Exposed PostgreSQL port for host integration testing
- 2025-11-30: Bullet #38 - Added Pydantic schemas (api/schemas.py)
- 2025-11-30: Bullet #37 - Separated SQLAlchemy models (adapters/models.py)
- 2025-11-29: Bullet #36 - API framework choice (FastAPI, None)
- 2025-11-29: Bullet #35 - Database backend choice (PostgreSQL, SQLite, None)
- 2025-11-29: Bullet #34 - Conditional .mcp.json based on enable_* flags
- 2025-11-29: Bullet #33 - Conditional compose services based on enable_* flags
- 2025-11-29: Milestone 3 complete - CI/CD & Quality (v0.3.0 tagged)
- 2025-11-29: Milestone 2 complete - Documentation overhaul with MkDocs
- 2025-11-29: Milestone 1 complete - Python quickstart with 18 passing tests

## Decisions Made
- [x] Decision: CI → GitHub Actions with uv
- [x] Decision: Docs hosting → GitHub Pages via gh-deploy
- [x] Decision: Changelog format → Keep a Changelog
- [x] Decision: Phase 12 revised - Ship solid v0.4.0 instead of feature bloat

---
*Last Updated: 2025-12-12*
