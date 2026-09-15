# Adapter — Production / Business Data Analysis

## Default posture

Read-only. Do not modify production data, schema, permissions, or scheduled pipelines without a human gate.

## Orientation additions

Discover:

- warehouses/databases and effective read permissions;
- semantic layers/metrics definitions;
- dashboards/reports;
- lineage/pipeline/source code;
- table freshness/SLAs;
- known source-of-truth datasets;
- PII/confidentiality boundaries;
- existing notebooks/query repositories;
- SMEs/data owners.

Do not infer business meaning from column names alone. Inspect lineage/pipeline logic and authoritative metric documentation where available.

## Experiment pattern

Prefer query/sample/reconciliation experiments before large exports. Capture:

- query text or reproducible query identifier;
- warehouse/database/environment;
- snapshot/as-of time and freshness;
- filters/joins/assumptions;
- row counts and reconciliation totals;
- aggregate output or stable result reference;
- performance/resource considerations.

## Evaluation

Useful checks include:

- known-answer/golden queries;
- reconciliation to official totals;
- invariants and range checks;
- independent query formulation;
- sampling raw records;
- result comparison across sources;
- SME review of metric semantics.

## Hard gates

Production DML/DDL, exports across trust boundaries, changes to shared dashboards/pipelines, deanonymization, or sensitive-data exposure.
