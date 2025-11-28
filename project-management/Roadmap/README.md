# Project Roadmap: Python Quickstart Enhancement

## Current Status
**Active Bullet:** #14 - Commit and test
**Phase:** BUILD
**Started:** 2025-11-28
**Target Completion:** 2025-11-28

## Tracer Bullet Progress

### Phase 1: Foundation Fixes (Bullets 1-3) ✅
- [x] **Bullet #1**: Fix broken paths in python-expert.md - Agent works correctly
- [x] **Bullet #2**: Sync .claude/ between root and template - Consistent experience
- [x] **Bullet #3**: Add reference/python/ to template - Architecture guidance included

### Phase 2: Python Scaffold (Bullets 4-8) ✅
- [x] **Bullet #4**: Create src/ package layout in template - Modern Python structure
- [x] **Bullet #5**: Add pyproject.toml with uv and hatch-vcs - Dependency management + versioning
- [x] **Bullet #6**: Create 3-layer architecture scaffold - domain/adapters/services
- [x] **Bullet #7**: Add CLI entry point (Typer) - `just cli` works
- [x] **Bullet #8**: Add pytest setup with initial tests - Tests included

### Phase 3: BEACON & DX (Bullets 9-11) ✅
- [x] **Bullet #9**: Add project-management/ BEACON structure to template
- [x] **Bullet #10**: Add justfile with Python commands (replaced Makefile)
- [x] **Bullet #11**: Update Dockerfile for uv, update docker-compose.yml

### Phase 4: Validation (Bullets 12-14)
- [x] **Bullet #12**: Update template README.md
- [x] **Bullet #13**: Verify template structure
- [ ] **Bullet #14**: Commit changes, test generation

## Today's Focus
**Bullet:** #1
**Goal:** Fix path references so python-expert agent works
**Success Criteria:** Agent can read its referenced files without errors

## Recent Completions
- 2025-11-28: Project assessment completed, roadmap created

## Upcoming Work
1. Next: Bullet #1 - Fix python-expert.md paths
2. Then: Bullet #2 - Sync template .claude/ with root
3. Later: Bullet #3 - Add reference docs to template

## Blockers & Decisions
- [x] Decision: Scaffold depth → Full 3-layer architecture
- [x] Decision: BEACON inclusion → Yes, always include
- [ ] Decision: Template vs root as source of truth for .claude/

## Notes
- Branch: feat/python-architecture
- Previous work added package-layout-and-architecture.md (50KB)
- Template currently has simpler python-expert.md than root

---
*Last Updated: 2025-11-28*
*Next Review: After completing Phase 1*
