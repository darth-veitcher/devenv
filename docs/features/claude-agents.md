# Claude AI Agents

Generated projects come pre-configured for AI pair programming with Claude.

## What's Included

### `.claude/` Directory

```
.claude/
├── agents/                  # Specialized agent prompts
│   ├── python-expert.md    # Python development specialist
│   ├── frontend-typescript-dev.md
│   └── synthetic-data-specialist.md
├── common/                  # Shared documentation
│   ├── pragmatic-principles.md
│   └── tool-usage-guide.md
├── reference/              # Architecture docs for Claude
│   └── python/
│       └── package-layout-and-architecture.md
├── settings.json           # Claude Code settings
└── settings.local.json     # Local overrides
```

### CLAUDE.md

The main system prompt at the project root. It includes:

- BEACON Framework instructions
- Project management structure
- Development workflow
- Core principles

## Agent Types

### Python Expert

Located at `.claude/agents/python-expert.md`

Specializes in:

- Clean Python architecture
- Type hints and modern Python
- Testing best practices
- Performance optimization

Use when writing Python code:

```
@python-expert Help me implement a new repository
```

### Frontend TypeScript Dev

For JavaScript/TypeScript frontend work.

### Synthetic Data Specialist

For generating test data and fixtures.

## How It Works

1. **Claude Code** reads CLAUDE.md on startup
2. The agent understands your project structure
3. It follows BEACON methodology
4. It can use specialized agents for specific tasks

## Using with Claude Code

### In Terminal

```bash
# Start Claude Code
claude

# Claude now understands your project
> Help me add a new entity to the domain layer
```

### In VS Code

1. Install Claude Code extension
2. Open your project
3. Claude reads CLAUDE.md automatically

## Customizing Agents

### Modify Existing Agents

Edit files in `.claude/agents/`:

```markdown
# My Custom Agent

## Role
You are a specialist in...

## Guidelines
- Always follow...
- Never...
```

### Add New Agents

Create a new `.md` file in `.claude/agents/`:

```markdown
# Database Expert

## Role
You are a PostgreSQL and database design specialist.

## Guidelines
- Prefer normalized schemas
- Always add indexes for foreign keys
- Use migrations for schema changes
```

Reference it in CLAUDE.md:

```markdown
<standard>For database work, use @database-expert</standard>
```

## MCP Integration

Claude can use MCP servers when available:

| Server | Claude Can... |
|--------|---------------|
| **context7** | Look up documentation |
| **searxng** | Search the web |
| **crawl4ai** | Read web pages |
| **memgraph** | Query graph databases |

Example:

```
> Use context7 to find FastAPI documentation about dependency injection
```

## Best Practices

### Be Specific

```
# Good
Help me create a repository interface for User entities with async methods

# Less Good
Help me with databases
```

### Reference the Architecture

```
# Good
Following our 3-layer architecture, add a UserService to the services layer

# Less Good
Add user functionality
```

### Use BEACON Terminology

```
# Good
Create a tracer bullet for user authentication

# Less Good
Add login
```

## Troubleshooting

### Claude Doesn't Understand Project Structure

Ensure CLAUDE.md exists at the project root and contains the correct paths.

### Agent Not Found

Check the agent file exists in `.claude/agents/` and is referenced correctly.

### MCP Servers Not Available

MCP servers require the Dev Container. Ensure you're running inside the container.

## Next Steps

- [MCP Servers](mcp-servers.md) - Available integrations
- [BEACON Framework](beacon-framework.md) - Development methodology
