# Evidence-First Work Harness (EFWH)

**A durable research → evidence → experiment → evaluation workflow for Claude Code.**

> Describe the problem once. EFWH orients to the environment, builds an evidence-backed working wiki, tests competing explanations/approaches, and leaves enough state for another session or engineer to continue.

**Created by Zach Thrasher** · Current release: **2.3.0**

## Start in 20 seconds

From any terminal/directory:

```text
npx --yes @zacharythrasher/efwh install
```

No Git checkout is required. The npm package contains the canonical EFWH Skill and installs it as a personal Claude Code Skill. After installation, start Claude Code in any workspace and type:

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

**Restricted network?** The release includes a self-contained offline ZIP and local npm tarball; neither requires GitHub access after download. See [INSTALL.md](./INSTALL.md).

**[Open the visual guide →](./docs/index.html)**

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

## Installation model

EFWH deliberately separates installation from agent reasoning:

```text
npx --yes @zacharythrasher/efwh install
        │
        ├─ deterministic filesystem install
        ├─ bundled Skill payload (no Git fetch)
        ├─ safe backup on replacement
        └─ byte-for-byte verification
                 │
                 ▼
         ~/.claude/skills/efwh/
                 │
                 ▼
              /efwh ...
```

The installer is dependency-free and uses the canonical `.claude/skills/efwh/` tree already in this repository. For npm-blocked environments, the same payload ships in an offline bundle.

## Why this is company-safe by default

EFWH does **not** grant itself extra permissions. The Skill declares no broad `allowed-tools` rule and is `disable-model-invocation: true`, so users explicitly opt in with `/efwh`. Existing Claude Code permissions, sandbox/auto-mode controls, enterprise policy, data classification, and system authorization remain authoritative.

Hard gates include production/primary writes, destructive or irreversible actions, external publication or messages, privilege changes, secret exposure, sensitive-data movement across trust boundaries, security-control bypass, and material legal/compliance/safety acceptance. See [SECURITY.md](./SECURITY.md).

## Company deployment

For pilots and individual installs, use `npx --yes @zacharythrasher/efwh install`. For restricted networks, use the offline bundle. For broad managed rollout, deploy `.claude/skills/efwh/` through your organization’s Claude Code managed Skills mechanism. See [Company rollout](./reference/company-rollout.md).

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

## Repository map

```text
.claude/skills/efwh/     canonical distributable Skill
installer/efwh.mjs       dependency-free `npx --yes @zacharythrasher/efwh` installer
package.json             npm distribution manifest
scripts/                 offline/manual installers + release validation
docs/                    GitHub Pages site + downloadable offline artifacts
reference/               architecture, rollout, release docs
reasoning.md             independent design rationale
INSTALL.md               canonical install documentation
.github/                  CI + contribution templates + ownership
```

## Contributing

Changes that alter EFWH behavior should explain the failure mode they address and how the change will be evaluated. See [CONTRIBUTING.md](./CONTRIBUTING.md).

## Release / legal note

This repository is currently published without an open-source license. Do not assume external redistribution rights beyond applicable company policy or explicit permission. Confirm ownership/licensing before treating EFWH as an external open-source release.
