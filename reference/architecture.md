# Architecture

EFWH has two layers.

## 1. Distribution layer

`.claude/skills/efwh/SKILL.md` is the single canonical Skill payload. The command is `/efwh`. Detailed protocol files live beside it under `resources/harness/` and are loaded progressively as needed.

Personal installation is deliberately deterministic: the root npm package exposes `npx --yes @zacharythrasher/efwh install`, and its package tarball contains the canonical Skill tree directly. The installer copies that tree into the effective personal Claude config root, backs up any differing existing copy, and verifies the result. It does not clone GitHub or ask an agent to reconstruct repository files.

For networks where npm is unavailable, release artifacts include the same payload in a self-contained offline ZIP plus a local npm tarball. Organization-wide rollout should still prefer managed Skills.

The Skill intentionally has no blanket `allowed-tools` grant. It is `disable-model-invocation: true`, so the user chooses when EFWH begins.

## 2. Per-problem state

Each invocation creates or resumes state under `.efwh/projects/<slug>/` in the **user's current workspace**, not in this framework repository. The durable state records goal, environment capabilities, evidence, hypotheses/candidates, task contracts, experiments, evals, decisions, and session handoff.

## Control model

**Autonomy** answers “how far may the agent act without another approval inside the current containment boundary?”

**Rigor** answers “how much proof is required before accepting a conclusion?”

They are independent. High autonomy inside a disposable sandbox can still use high rigor. Repeated approval clicks are not treated as a substitute for containment.

Hard gates override both dimensions. Organization policy overrides EFWH.

## Evidence model

Material claims use scoped states:

- `OBSERVED`
- `DOCUMENTED`
- `INFERRED`
- `HYPOTHESIS`
- `DISPROVEN`
- `SUPERSEDED`

Negative evidence is scoped to what was actually tested. A failed implementation or experiment cannot silently become a global impossibility claim.

## Evaluation model

Preferred evidence of success, in order:

1. deterministic/environment-state verification;
2. independent/fresh-context model evaluation against a prewritten rubric;
3. human or SME judgment where governance or domain judgment matters.

An invalid acceptance test is recorded as `EVAL_DEFECT`; the agent does not rewrite the criterion after seeing a failure merely to pass.
