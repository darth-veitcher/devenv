# CLAUDE.md - Project Context for Claude Code

## 🚨 SESSION START CHECKLIST (DO THIS FIRST!)

When starting any new session on this project:

1. **Initialize Serena Context**

   ```
   mcp__serena__initial_instructions()
   mcp__serena__list_memories()
   # Read any relevant memories
   ```

2. **Check Project Status**

   - Read `project-management/IMPLEMENTATION_PLAN.md`
   - Identify current week and tasks
   - Review completed vs pending items

3. **Plan Session with Sequential Thinking**

   ```
   mcp__sequential-thinking("What should I work on this session based on the implementation plan?")
   ```

4. **Set Up Tool Fallbacks**
   - WebSearch → mcp**searxng → mcp**crawl4ai
   - Fetch → mcp\_\_crawl4ai
   - Read → mcp**serena**find_symbol

## 📝 MEMORY CREATION TRIGGERS

**ALWAYS create a Serena memory when:**

1. **Starting a new project or major feature** - Document goals, architecture, and approach
2. **Making architectural decisions** - Record the decision, rationale, and alternatives considered
3. **Completing major milestones** - Capture what was accomplished and lessons learned
4. **Discovering important patterns or solutions** - Save for future reference
5. **Establishing project conventions** - Document agreed-upon standards and practices

**Memory Naming Convention**: Use descriptive names like `project_name_topic` (e.g., `claude_memory_project_overview`, `auth_system_architecture`)

**What to Include**: Summary, key decisions, technical details, file locations, current status, next steps

## 🏁 SESSION END CHECKLIST

Before ending a session, consider:

1. **Document significant work** - Did you complete something memory-worthy? (See triggers above)
2. **Update project status** - Does the "Current Phase" in CLAUDE.md need updating?
3. **Commit changes** - Are there uncommitted changes that should be saved?
4. **Note blockers** - Document any blockers or issues for the next session

## Project Overview

You are working on a **Cookiecutter template** that creates sophisticated containerized development environments with AI agent superpowers for solo developers.

**Current Implementation Status:**
- ✅ **Complete Containerization**: Multi-layer Docker architecture with VS Code Dev Containers
- ✅ **MCP Services Integration**: SearxNG, Crawl4AI, Context7, Memgraph with AI Toolkit
- ✅ **Quality Gates**: Comprehensive pre-commit hooks with linting, formatting, and security
- ✅ **FastAPI Application**: Production-ready Python web framework template
- ✅ **AI-Ready Infrastructure**: Full Claude Code integration with MCP server configuration
- 🔄 **Agent System**: In development - AI agents for deployment, feature generation, debugging
- 🔄 **Instant Deployment**: Planned - 30-second deployment to Railway/Fly/Render

This project aims to transform solo developers into "AI Orchestra Conductors" who can build and deploy applications 10x faster using Claude Code's agent capabilities.

## Key Project Goals

1. **Zero to Deployed in 30 seconds** - One command from code to live URL
2. **Parallel AI Agents** - Up to 10 agents working simultaneously
3. **Magic, Not Manual** - Common tasks automated (auth, payments, deployment)
4. **Solo Dev Focused** - No enterprise complexity, just tools that help ship

## Documentation Structure

### Project Management (`/project-management/`)

- **PRD_SOLO_DEV_CONTAINERIZED_ENVIRONMENT.md** - Full requirements and specifications
- **IMPLEMENTATION_PLAN.md** - 4-week sprint plan with daily tasks
- **AGENT_IMPLEMENTATION_GUIDE.md** - Technical details for agent implementation
- **ULTIMATE_SOLO_DEV_MLP.md** - Vision and philosophy

Check this directory in general for:

- Project requirements and specifications
- Implementation plans and roadmaps
- Technical architecture decisions
- Feature specifications

Use these documents as canonical sources of intent and background context for all development decisions.

### Current Project Structure

```
devenv/                           # Cookiecutter template repository
├── .claude/                      # Claude configuration (this template project)
├── .devcontainer/               # VS Code container config for template development
├── .serena/                     # Serena MCP configuration
├── hooks/                       # Cookiecutter post-generation hooks
│   └── post_gen_project.py     # Handles git init, submodules, and pre-commit setup
├── project-management/          # All planning documentation
├── {{cookiecutter.project_slug}}/  # Template files (what gets generated)
│   ├── .claude/                # Generated project Claude config
│   ├── .devcontainer/          # Generated container setup with MCP services
│   │   ├── compose.yml         # Development services (SearxNG, Crawl4AI, etc.)
│   │   ├── devcontainer.json   # VS Code settings
│   │   └── mcp/               # MCP service configurations
│   ├── .serena/               # Generated Serena configuration
│   ├── app/                   # FastAPI application template
│   │   ├── Dockerfile         # Application container
│   │   ├── compose.yml        # Application stack
│   │   ├── main.py           # FastAPI app
│   │   └── requirements.txt   # Python dependencies
│   ├── .pre-commit-config.yaml # Pre-commit hooks configuration
│   ├── .mcp.json             # MCP server configuration
│   ├── .gitignore            # Git ignore rules
│   └── README.md             # Generated project documentation
├── cookiecutter.json           # Template variables
└── README.md                   # Template documentation
```

## Development Workflow

### When implementing features:

1. Check `IMPLEMENTATION_PLAN.md` for current sprint tasks
2. Reference `AGENT_IMPLEMENTATION_GUIDE.md` for technical patterns
3. Follow the philosophy in `ULTIMATE_SOLO_DEV_MLP.md`

### Post-Generation Setup

The cookiecutter template includes automatic setup via `hooks/post_gen_project.py`:

1. **Git Initialization**: Creates git repository and initial commit
2. **Submodule Setup**: Adds Memgraph AI Toolkit submodule for MCP integration
3. **Pre-commit Installation**: Automatically installs and configures pre-commit hooks
   - Installs `pre-commit` as dev dependency using `uv`
   - Sets up git hooks with comprehensive linting and formatting
   - Includes security checks, code quality validation, and more
   - Provides graceful fallbacks if `uv` is not available

### Key Implementation Areas

#### 1. Agent System (`{{cookiecutter.project_slug}}/.claude/agents/`)

Create YAML configurations for:

- Deploy Agent (handles deployment to Railway/Fly/Render)
- Feature Factory Agent (generates auth, payments, email features)
- Debug Detective Agent (auto-fixes errors)
- Optimization Agent (background performance improvements)
- Documentation Agent (keeps docs updated)

#### 2. Smart Makefile (`{{cookiecutter.project_slug}}/Makefile`)

Human-friendly commands:

- `make deploy` - Deploy to production in 30 seconds
- `make share` - Get public URL with QR code
- `make save` - Smart git commit and push
- `make add-feature auth` - Complete auth system
- `make idea` - Research → Build → Deploy flow

#### 3. Deployment Templates

- Railway configuration (`railway.toml`)
- Fly.io configuration (`fly.toml`)
- Environment variable management
- Zero-downtime deployment scripts

#### 4. Feature Templates (`{{cookiecutter.project_slug}}/.claude/templates/`)

Complete, production-ready implementations:

- Authentication (JWT, OAuth, password reset)
- Payments (Stripe integration, subscriptions)
- Email (transactional, queues, templates)

## MCP Tool Usage Guidelines

### Tool Selection and Fallback Strategies

#### Web Research Hierarchy

1. **Primary**: `WebSearch` for general queries
2. **Fallback**: `mcp__searxng` when WebSearch fails or returns limited results
3. **Deep Dive**: `mcp__crawl4ai` for specific page content when Fetch fails

#### Documentation and Learning

1. **Always Start With**: `mcp__context7` for official library documentation
   - Use for: FastAPI, Docker, Railway, Fly.io docs
   - Command: First `resolve-library-id` then `get-library-docs`
2. **Fallback**: WebSearch → SearxNG → Crawl4AI

#### Complex Problem Solving

1. **Use Sequential Thinking** for:
   - Architecture decisions
   - Multi-step implementations
   - Debugging complex issues
   - Planning agent interactions
2. **Minimum Usage**: At least once per complex task

#### Code Analysis (Serena)

1. **Session Start**: ALWAYS run `mcp__serena__initial_instructions`
2. **Memory Usage**:
   - Check memories with `mcp__serena__list_memories`
   - Read relevant memories for context
   - Write new memories for important decisions
3. **Code Navigation**:
   - Use `mcp__serena__find_symbol` over basic Read
   - Use `mcp__serena__search_for_pattern` for code searches

### MCP Tool Best Practices

#### Research Flow

```
1. mcp__serena__initial_instructions (get project context)
2. mcp__context7 (check official docs)
3. WebSearch (general research)
4. mcp__searxng (if WebSearch fails)
5. mcp__crawl4ai (for specific pages)
6. mcp__sequential-thinking (synthesize findings)
```

#### Implementation Flow

```
1. mcp__sequential-thinking (plan approach)
2. mcp__serena__find_symbol (understand existing code)
3. Task tool (spawn parallel agents if needed)
4. Write/Edit (implement changes)
5. mcp__serena__write_memory (document decisions)
```

#### Debugging Flow

```
1. mcp__sequential-thinking (analyze problem)
2. mcp__serena__search_for_pattern (find related code)
3. mcp__playwright (if UI testing needed)
4. Fix issue
5. mcp__serena__write_memory (document solution)
```

### Required Tool Usage Per Task Type

#### Feature Implementation

- ✅ Sequential thinking for planning
- ✅ Context7 for framework patterns
- ✅ Serena for code structure understanding
- ✅ Task tool for parallel work

#### Debugging

- ✅ Sequential thinking for root cause analysis
- ✅ Serena pattern search
- ✅ WebSearch → SearxNG for error research

#### Documentation

- ✅ Context7 for best practices
- ✅ Serena memories for project decisions
- ✅ Sequential thinking for structure

### Session Initialization Checklist

Every new session MUST:

1. Run `mcp__serena__initial_instructions`
2. Check `mcp__serena__list_memories`
3. Read CLAUDE.md (this file)
4. Review current task in IMPLEMENTATION_PLAN.md
5. Use `mcp__sequential-thinking` to plan session

## Agent Development Guidelines

### Creating New Agents

```yaml
# .claude/agents/example.yml
name: "Agent Name"
description: "What this agent does"
tools: [Read, Write, Edit, Bash, Task]
triggers: ["when to activate"]
prompt: |
  Clear instructions for the agent
  including specific behaviors and goals
```

### Parallel Execution

- Use Task tool to spawn sub-agents
- Maximum 10 agents running simultaneously
- Each agent has independent context window
- Coordinate through shared file system

## Testing Approach

1. **Template Generation**: Test cookiecutter renders correctly
2. **Agent Functionality**: Verify agents perform tasks
3. **Integration**: Ensure all pieces work together
4. **User Experience**: Time from idea to deployed app

## Success Metrics

- **Setup Time**: <5 minutes to working environment
- **Deploy Time**: <30 seconds to production
- **Feature Time**: <2 minutes for auth/payments
- **Debug Time**: Errors fixed before noticed

## MCP Tool Usage Patterns

### Research Pattern (Use for all new features)

```python
# 1. Plan with sequential thinking
mcp__sequential-thinking("How should I implement deployment to Railway?")

# 2. Check official docs
mcp__context7__resolve-library-id("railway")
mcp__context7__get-library-docs(library_id, topic="deployment")

# 3. Search for examples
WebSearch("Railway FastAPI deployment example 2025")
# If limited results:
mcp__searxng("Railway Python deployment tutorial")

# 4. Deep dive specific pages
mcp__crawl4ai("https://docs.railway.app/deploy/deployments")
```

### Code Analysis Pattern (Use before any edits)

```python
# 1. Get Serena context
mcp__serena__initial_instructions()

# 2. Find relevant code
mcp__serena__find_symbol("Makefile")
mcp__serena__search_for_pattern("deploy")

# 3. Understand relationships
mcp__serena__find_referencing_symbols("deploy_command")
```

### Parallel Implementation Pattern

```python
# Use Task tool for parallel work
Task("Deploy Agent", "Create Railway deployment configuration")
Task("Feature Agent", "Create authentication template")
Task("Doc Agent", "Update README with new commands")
```

### Common Pitfalls to Avoid

#### ❌ Bad Pattern: Direct implementation without research

```python
# DON'T DO THIS
Write("railway.toml", "some config I think might work")
```

#### ✅ Good Pattern: Research → Plan → Implement

```python
# DO THIS
mcp__sequential-thinking("Plan Railway deployment")
mcp__context7("Railway deployment docs")
mcp__serena__search_for_pattern("deployment")
Write("railway.toml", "validated config from docs")
```

#### ❌ Bad Pattern: Using Fetch without fallback

```python
# DON'T DO THIS
Fetch("https://some-site.com") # Often fails
```

#### ✅ Good Pattern: Fetch → Crawl4AI fallback

```python
# DO THIS
try:
    WebFetch("https://some-site.com")
except:
    mcp__crawl4ai("https://some-site.com")
```

#### ❌ Bad Pattern: Sequential work that could be parallel

```python
# DON'T DO THIS
create_auth_system()
create_payment_system()
create_email_system()
```

#### ✅ Good Pattern: Parallel agents for independent tasks

```python
# DO THIS
Task("Auth Agent", "Create auth system")
Task("Payment Agent", "Create payment system")
Task("Email Agent", "Create email system")
```

## Common Commands During Development

```bash
# Test template generation
cookiecutter . --no-input

# Test with custom values
cookiecutter . --no-input project_name="Test Project"

# Clean test outputs
rm -rf test-project/

# Test agent configurations
cd test-project && make add-feature auth
```

## Important Context

### Target User: Solo Developer

- Coding from home/basement
- Wants to ship fast, not configure
- Values magic over manual processes
- Building side projects and startups

### NOT Target User: Enterprise Teams

- No Kubernetes needed
- No complex CI/CD pipelines
- No extensive monitoring
- No multi-environment complexity

## Your Role

You are helping implement this cookiecutter template that will empower thousands of solo developers to build and ship applications faster than ever before. Focus on:

1. **Simplicity** - If it requires documentation, it's too complex
2. **Speed** - Every second counts for deployment and feedback
3. **Magic** - Tasks should feel automatic, not manual
4. **Joy** - Development should be fun, not frustrating

When in doubt, refer to the vision in `ULTIMATE_SOLO_DEV_MLP.md` and remember: we're building for the solo dev who just wants to ship cool stuff from their basement.

## Next Actions

Check `IMPLEMENTATION_PLAN.md` for the current week's tasks. As of now, we're ready to begin Week 1: Foundation Sprint, starting with enhancing the cookiecutter template with agent support.

---

_Remember: The goal is to make solo developers feel like they have superpowers. Every feature should contribute to that feeling._
