# Evidence-First Work Harness (EFWH)

**A durable research → evidence → experiment → evaluation workflow for Claude Code.**

> Describe the problem once. EFWH orients to the environment, builds an evidence-backed working wiki, tests competing explanations/approaches, and leaves enough state for another session or engineer to continue.

**Created by Zach Thrasher** · Current release: **2.2.0**

## Start in 30 seconds

From any terminal/directory, start Claude Code with the guided installer:

```text
claude "Install EFWH from https://github.com/ZacharyThrasher/evidence-first-work-harness for me. Follow the repository's INSTALL.md and guide me through any approvals."
```

Claude opens interactively, follows [`INSTALL.md`](./INSTALL.md), installs the canonical Skill at personal scope, and guides you through any approvals. After installation, `/efwh` is available across your local Claude Code projects. If the personal skills directory did not exist when the current session started, Claude will tell you to restart once.

Prefer a deterministic/manual path? See [`INSTALL.md`](./INSTALL.md#deterministic-manual-fallback) or [`QUICKSTART.md`](./QUICKSTART.md).

Then start Claude Code in any workspace and type:

```text
/efwh <your problem in normal language>
```

Examples:

```text
/efwh Why did production yield fall after last week's process change?
/efwh --autonomy builder Make this service reconnect reliably after sleep
/efwh --rigor high Prove whether these two datasets disagree and why
```

Resume later with `/efwh --resume`. Check state with `/efwh --status`.

**[Open the 90-second visual guide →](./docs/index.html)**

## What EFWH changes

Normal chat is optimized for answering. EFWH is optimized for **investigating and building without losing the chain of evidence**.

1. **Orient** — discover the repo, internal docs, data, connectors, test environments, policies, and useful human dependencies actually available.
2. **Frame** — preserve the desired outcome without prematurely locking onto an implementation.
3. **Research** — separate observation, documentation, inference, hypothesis, contradiction, and disproof.
4. **Branch the hypothesis space** — keep materially different explanations/approaches visible instead of falling in love with the first one.
5. **Contract before action** — define scope, acceptance evidence, evaluation, rollback, and human gates before a meaningful experiment.
6. **Execute inside a boundary** — autonomy increases inside sandboxes/worktrees/read-only data access; hard gates still stop high-impact actions.
7. **Evaluate the real outcome** — environment state and independent checks outrank the model saying “done.”
8. **Persist the handoff** — `.efwh/` carries the project across context windows, sessions, and coworkers.

## Why this is company-safe by default

EFWH does **not** grant itself extra permissions. The Skill declares no broad `allowed-tools` rule and is `disable-model-invocation: true`, so users explicitly opt in with `/efwh`. Existing Claude Code permissions, sandbox/auto-mode controls, enterprise policy, data classification, and system authorization remain authoritative.

Hard gates include production/primary writes, destructive or irreversible actions, external publication or messages, privilege changes, secret exposure, sensitive-data movement across trust boundaries, security-control bypass, and material legal/compliance/safety acceptance. See [SECURITY.md](./SECURITY.md).

## Company deployment

For pilots, use the guided personal install above (or the deterministic fallback in `INSTALL.md`). For a managed rollout, deploy `.claude/skills/efwh/` through your organization’s Claude Code managed Skills mechanism so users receive `/efwh` without per-user installation. See [Company rollout](./reference/company-rollout.md).

## What gets written into a user's workspace

```text
.efwh/
  INDEX.json
  projects/<problem>/
    PROJECT.md
    CONFIG.json
    STATE.json
    environment/
    evidence/
    wiki/
    candidates/
    tasks/CURRENT.md
    experiments/
    evals/
    decisions/
    runs/HANDOFF.md
```

The Skill does **not** silently add `.efwh/` to a project's `.gitignore` or commit it. The team decides whether an investigation's artifacts belong in version control.

## Design basis

EFWH is intentionally simple and file-based. Its structure is grounded in current work on long-running agent harnesses, evaluation, context engineering, containment, Agent Skills, and production data agents. The full rationale and reading list live in [reasoning.md](./reasoning.md).

Key design influences include Anthropic’s long-running harness research, Claude Code Skills and containment guidance, OpenAI’s internal data-agent write-up, OpenAI’s 2026 audit showing that evals themselves can be defective, NIST AI RMF guidance, and OWASP agent/prompt-injection guidance.

## Repository map

```text
.claude/skills/efwh/     canonical distributable Skill
  SKILL.md
  resources/harness/     auditable vendor-neutral protocol
docs/                    GitHub Pages site (HTML only)
reference/               architecture, rollout, release docs
reasoning.md             independent design rationale
INSTALL.md              canonical human/agent install contract
scripts/                 deterministic install fallback + release validation
docs/index.html          self-contained visual guide
.github/                  CI + contribution templates + ownership
```

## Contributing

Changes that alter EFWH behavior should explain the failure mode they address and how the change will be evaluated. See [CONTRIBUTING.md](./CONTRIBUTING.md).

## Release / legal note

This repository is currently published without an open-source license. Do not assume external redistribution rights beyond applicable company policy or explicit permission. Confirm ownership/licensing before treating EFWH as an external open-source release.
