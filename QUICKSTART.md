# Quickstart

## Install once

### Windows
```powershell
git clone --depth 1 https://github.com/ZacharyThrasher/evidence-first-work-harness.git efwh
& .\efwh\scripts\install.ps1
```

### macOS / Linux
```bash
git clone --depth 1 https://github.com/ZacharyThrasher/evidence-first-work-harness.git efwh
./efwh/scripts/install.sh
```

The installers copy the canonical Skill into `~/.claude/skills/efwh/` and refuse to overwrite an existing install unless `-Force` / `--force` is supplied.

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

For company-managed deployment, see [`docs/company-rollout.md`](./docs/company-rollout.md).
