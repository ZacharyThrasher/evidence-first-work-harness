# Quickstart

## Install once

From **any directory**:

```text
npx --yes @zacharythrasher/efwh install
```

No Git checkout is required. The npm package carries the full EFWH Skill and installs it at personal scope so `/efwh` is available across your Claude Code projects.

The installer honors `CLAUDE_CONFIG_DIR` when set; otherwise it installs to `~/.claude/skills/efwh/`. Existing installs are backed up before replacement and the final copy is verified.

### Restricted network / offline

If npm is blocked, download the self-contained `efwh-offline-2.3.0.zip` release artifact (or obtain it from your approved internal mirror), extract it, and run:

**Windows**

```text
install.cmd
```

**macOS / Linux**

```bash
./install.sh
```

No GitHub or npm access is needed after you have the offline bundle.

If you have the local npm tarball instead:

```text
npx --yes ./efwh-2.3.0.tgz install
```

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

No GOAL/config file editing is required. EFWH writes durable project state under `.efwh/`.

For company-managed deployment, see [`reference/company-rollout.md`](./reference/company-rollout.md).
