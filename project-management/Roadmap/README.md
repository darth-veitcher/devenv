# Project Roadmap: devenv Cookiecutter Template

## Current Status
**Active Bullet:** None - Milestone 3 Complete
**Phase:** SHIP
**Started:** 2025-11-29
**Completed:** 2025-11-29

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

## Milestone 4: Template Customization (Future)

*Not started*

### Phase 11: Conditional Features (Bullets 33-36)
- [ ] **Bullet #33**: Make enable_mcp_services toggle compose services
- [ ] **Bullet #34**: Make .mcp.json conditional based on enable_* flags
- [ ] **Bullet #35**: Add database choice (PostgreSQL, SQLite, None)
- [ ] **Bullet #36**: Add API framework choice (FastAPI, Flask, None)

### Phase 12: Feature Templates (Bullets 37-39)
- [ ] **Bullet #37**: Add authentication feature template
- [ ] **Bullet #38**: Add database migrations (Alembic) feature
- [ ] **Bullet #39**: Add background tasks (Celery/ARQ) feature

---

## Today's Focus
**Bullet:** None - Milestone 3 Complete
**Goal:** Housekeeping and cleanup
**Success Criteria:** All files synced, docs consistent

## Recent Completions
- 2025-11-29: Synced .mcp.json between root and template (fixed JSONC comments)
- 2025-11-29: Milestone 3 complete - CI/CD & Quality (v0.3.0 tagged)
- 2025-11-29: Milestone 2 complete - Documentation overhaul with MkDocs
- 2025-11-29: Milestone 1 complete - Python quickstart with 18 passing tests

## Decisions Made
- [x] Decision: CI → GitHub Actions with uv
- [x] Decision: Docs hosting → GitHub Pages via gh-deploy
- [x] Decision: Changelog format → Keep a Changelog

---
*Last Updated: 2025-11-29*
