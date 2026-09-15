# Side-Effect Classification

Classify proposed actions before execution.

## S0 — Read only

Search/read/list/inspect with no meaningful external side effect.

## S1 — Local reversible scratch

Create temporary analysis files or run computation in an isolated workspace.

## S2 — Isolated work-product mutation

Modify a dedicated branch/worktree/copy, derived dataset, or sandbox environment with easy rollback.

## S3 — Shared/reversible external mutation

Update a shared non-production resource, create a ticket/draft, or change a staging system. Usually requires explicit scope/approval depending on autonomy.

## S4 — High impact / irreversible / production / external

Production writes, destructive actions, credential/security changes, financial or public actions, sensitive data movement. Default hard gate.

Prefer lower-side-effect experiments that answer the same question.
