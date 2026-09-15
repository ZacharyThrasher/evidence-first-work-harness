# Quickstart

## Install once

### Recommended: let Claude guide the install

Run this from **any directory**:

```text
claude "Install EFWH from https://github.com/ZacharyThrasher/evidence-first-work-harness for me. Follow the repository's INSTALL.md and guide me through any approvals."
```

Claude Code starts interactively, reads the repository's [`INSTALL.md`](./INSTALL.md), installs EFWH as a **personal Skill**, and guides you through any approvals. Personal Skills are available across all of your Claude Code projects.

If the personal `skills` directory did not exist when that Claude session started, restart Claude Code once after installation so it can discover the newly created directory.

### Deterministic manual fallback

**Windows / PowerShell**

```powershell
git clone --depth 1 https://github.com/ZacharyThrasher/evidence-first-work-harness.git efwh
& .\efwh\scripts\install.ps1
```

**macOS / Linux**

```bash
git clone --depth 1 https://github.com/ZacharyThrasher/evidence-first-work-harness.git efwh
./efwh/scripts/install.sh
```

The fallback installers use `CLAUDE_CONFIG_DIR` when it is set; otherwise they install to `~/.claude/skills/efwh/`. They refuse to replace an existing install unless `-Force` / `--force` is explicitly supplied.

## Use it

Start Claude Code in the repo, analysis folder, or document workspace where the work should happen:

```text
/efwh <problem in normal language>
```

Optional controls:

```text
/efwh --autonomy advisory <goal>
/efwh --autonomy experiment --rigor high <goal>
/efwh --autonomy builder <goal>
/efwh --autonomy sandbox --rigor high <goal>
/efwh --resume
/efwh --status
```

No GOAL/config file editing is required. EFWH writes its durable project state under `.efwh/`.

For company-managed deployment, see [`reference/company-rollout.md`](./reference/company-rollout.md).
