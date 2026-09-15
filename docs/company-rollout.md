# Company rollout

## Recommended path

### 1. Review the policy surface

Before broad deployment, have your Claude Code/platform owner review:

- `.claude/skills/efwh/SKILL.md`
- `resources/harness/policies/HARD_GATES.md`
- `resources/harness/policies/TRUST_MODEL.md`
- `resources/harness/policies/SECURITY.md`
- `resources/harness/policies/SIDE_EFFECTS.md`

Add organization-specific requirements for data classification, retention, regulated systems, production access, audit logging, and required reviewers. `R3_ORG_CRITICAL` is intentionally incomplete until those controls exist.

### 2. Pilot with real work

Use a small cross-section of engineering/data/research users. Capture: time-to-first-use, number of human gates, incorrect gates, unsupported claims caught, false `COMPLETED`/`EXHAUSTED` attempts, and whether `.efwh/` handoffs actually let another person/session resume.

The goal is not maximum harness complexity. Remove ceremony that does not measurably improve outcomes.

### 3. Deploy the Skill centrally

Current Claude Code supports enterprise/managed Skills. Deploy the contents of `.claude/skills/efwh/` through your managed settings directory so all intended users receive `/efwh`. Keep `disable-model-invocation: true` for the default company profile unless your governance team deliberately chooses otherwise.

Do not add blanket `allowed-tools` permissions to EFWH as a convenience shortcut. Tool permissions belong in your organization’s established Claude Code permission/sandbox policy.

### 4. Choose an artifact-retention policy

EFWH does not decide whether `.efwh/` should be committed. Recommended defaults:

- **code/design investigations:** commit high-value evidence/wiki/decision artifacts when they are useful to reviewers;
- **production-data investigations:** do not commit raw sensitive extracts; retain query provenance and derived summaries according to data policy;
- **confidential/security work:** follow the existing restricted-workspace and retention policy;
- **throwaway exploration:** remove `.efwh/` after exporting any decisions worth keeping.

### 5. Establish ownership

Assign an owner for:

- Skill releases and compatibility;
- organization-specific hard-gate policy;
- reported failures or prompt-injection findings;
- periodic model-upgrade review;
- deciding whether old harness mechanisms are still load-bearing.

The repository ships `CODEOWNERS` with `@ZacharyThrasher` as the default owner; organizations can replace or extend it after adoption.

## Recommended success metrics

Measure the harness against ordinary agent use, not against an idealized process:

- investigation/build success rate;
- unsupported-conclusion rate;
- regression/rollback incidents;
- time to resume after a fresh context/session;
- human review effort;
- approval prompt/gate count;
- evidence traceability;
- user abandonment/friction.

A company-wide rollout is successful if EFWH improves outcomes and inspectability without becoming process theater.

## Update cadence

Review EFWH after major Claude Code/model releases and at least quarterly during active deployment. Harness assumptions go stale as models and containment features improve. Use `resources/harness/maintenance/MODEL_UPGRADE_REVIEW.md`.
