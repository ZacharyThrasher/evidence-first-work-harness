# Current Task Contract

**Task ID:** ORIENT-001  
**Status:** READY

## Objective

Perform environment orientation and produce the capability/source map.

## Why this is the next task

We should not design a research or execution plan until we know what internal sources, tools, permissions, and sandboxes are actually available.

## Inputs

`GOAL.md`, `CONFIG.yaml`, current workspace, visible tool/connector catalog.

## Allowed actions

Read-only discovery and harness-artifact updates. No production writes, external communications, privileged changes, or work-product modifications.

## Human gates

Any action needed to connect/authorize a new source or reveal a secret value.

## Acceptance criteria

- capability map records relevant tools/resources and effective read/write classes;
- source registry identifies likely authoritative sources;
- missing/unavailable resources are explicit;
- security/data boundaries are noted without exposing secrets;
- recommended active toolset is small and goal-relevant;
- `STATE.json.environment_oriented` becomes true only when the above exist.

## Evaluation

Human-readable inspection against the acceptance criteria. No model claim alone is sufficient.

## Evidence to capture

Read-only probe results and source identifiers sufficient to establish availability/permissions.

## Rollback / recovery

Not applicable; orientation should not alter the work product.

## Actual outcome

<!-- Fill after execution. -->
