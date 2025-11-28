# Work Directory

This is the **transient workspace** for active development artifacts.

## Subdirectories

- `sessions/` - Session notes and summaries (delete after merge)
- `planning/` - Feature planning documents (delete after implementation)
- `analysis/` - Code analysis notes (delete after captured in ADR)

## Lifecycle

1. **During Work**: Create freely in this directory
2. **After Commit**: Promote important insights to ADRs or Background/
3. **After Merge**: Clean slate - delete all session files

## Cleanup Policy

After merging to main/develop:

```bash
cd project-management/Work
rm -rf sessions/*
rm -rf planning/*
rm -rf analysis/*
```

**Retention**: Max 1-2 sprints of history (2-4 weeks)

---

Files in this directory are temporary. Don't rely on them for long-term reference.
