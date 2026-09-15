# Model Upgrade Review

Harness components encode assumptions about model weaknesses. Re-test those assumptions when the primary model changes materially.

For each component ask:

- Does this still prevent a measured failure?
- Can the model now perform this reliably without scaffolding?
- Does the component add cost/context/latency that exceeds its benefit?
- Can a deterministic tool/environment control replace prompt instructions?
- Are new model/tool capabilities available that reduce complexity?

Remove one component at a time and compare against representative evals. Do not preserve process merely because it used to be necessary.
