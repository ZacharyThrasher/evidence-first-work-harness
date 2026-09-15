# EFWH Agent Skill

This directory is the canonical distributable EFWH Skill.

Recommended personal installation: follow the repository root `INSTALL.md`. Personal skills live at `<Claude config root>/skills/efwh/`, where the config root is `CLAUDE_CONFIG_DIR` when set and otherwise `~/.claude`.

Other supported scopes:

- Project: `.claude/skills/efwh/`
- Organization: deploy as a managed Agent Skill

Then run:

```text
/efwh <problem>
```

No GOAL/CONFIG editing is required. The skill creates `.efwh/` project state itself.
