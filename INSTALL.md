# Install EFWH with Claude Code

This file is the canonical installation contract for humans and agents.

If a user asks Claude Code to install this repository, install **EFWH as a personal Claude Code Skill** so `/efwh` is available across that user's projects. Do not install it only into the current project unless the user explicitly asks for a project-scoped install.

## Recommended entry point

A user can run this from any directory:

```text
claude "Install EFWH from https://github.com/ZacharyThrasher/evidence-first-work-harness for me. Follow the repository's INSTALL.md and guide me through any approvals."
```

This intentionally starts an **interactive** Claude Code session so the user can review and approve any filesystem or network actions through the normal Claude Code permission flow.

## Installation contract

1. **Inspect before changing anything.** Confirm this repository is `ZacharyThrasher/evidence-first-work-harness` and locate the canonical Skill at `.claude/skills/efwh/`.
2. **Resolve the personal Claude configuration root correctly.** If `CLAUDE_CONFIG_DIR` is set, use that directory. Otherwise use `~/.claude` (`%USERPROFILE%\.claude` on Windows). The destination is `<config-root>/skills/efwh/`.
3. **Install the complete Skill directory.** Preserve the entire `.claude/skills/efwh/` tree and its relative paths. Do not rewrite `SKILL.md` or omit supporting resources.
4. **Do not modify unrelated Claude configuration.** Do not edit `settings.json`, hooks, MCP configuration, credentials, policies, project files, or managed settings unless the user separately requests it.
5. **Handle existing installs safely.** If `<config-root>/skills/efwh/` already exists, inspect its version first. If it is identical/current, report that no change is needed. If replacement is needed, tell the user what will change, preserve a timestamped backup, and obtain any approval required by the active Claude Code permission policy before replacing it.
6. **Respect enterprise precedence.** A managed/enterprise Skill with the same name can override a personal Skill. If such a conflict is detectable, report it rather than attempting to bypass managed configuration.
7. **Verify the result.** Confirm the destination contains `SKILL.md` plus the bundled resources, and that its metadata version matches this repository's `VERSION` file (`2.2.0`).
8. **Explain reload behavior.** Claude Code watches existing personal skill directories for changes. If the top-level personal `skills` directory did not exist when the current Claude session started, tell the user to restart Claude Code once so the new directory is discovered.
9. **Finish with a concrete result.** Report the install path, installed EFWH version, whether an old copy was backed up, whether a restart is needed, and the next command: `/efwh <problem>`.

## Deterministic manual fallback

If the user prefers a non-agentic install, clone/download this repository and run the platform installer:

**Windows / PowerShell**

```powershell
.\scripts\install.ps1
```

**macOS / Linux**

```bash
./scripts/install.sh
```

The fallback installers follow the same personal config-root rule and refuse to overwrite an existing install unless the user explicitly selects the force option.

## Scope

Installing EFWH copies a Claude Code Skill. It does **not** grant extra permissions, alter enterprise policy, enable tools, configure credentials, or modify the user's projects. EFWH remains explicitly user-invocable with `/efwh`.
