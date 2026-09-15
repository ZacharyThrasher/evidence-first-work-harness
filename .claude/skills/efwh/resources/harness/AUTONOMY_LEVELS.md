# Autonomy Levels

Hard gates in `policies/HARD_GATES.md` override every level.

## L0_ADVISORY

The model reads available material and recommends actions. The user performs all consequential actions. Harness artifact writes may be allowed if the user permits them.

Best for unfamiliar environments, sensitive systems, or users who want to drive every step.

## L1_GUIDED_RESEARCH — default

The model may inspect resources, search internal/external sources, and write research/wiki/state artifacts. It stops before experiments that alter the work product, run nontrivial code, or query sensitive/production data unless the user authorizes the next step.

Best for initial adoption and ambiguous problems.

## L2_BOUNDED_EXPERIMENT

In addition to L1, the model may run reversible experiments in an approved sandbox and/or read-only data queries. It may create scratch artifacts. It does not modify the primary work product without a checkpoint.

Best for technical investigations and production-data analysis with read-only access.

## L3_BOUNDED_BUILDER

The model may modify an isolated branch/worktree/copy or derived analysis artifacts and iterate against tests/evals. It may not write production systems, publish externally, access secrets beyond pre-scoped tooling, or perform destructive/privileged actions without a human gate.

Best for code implementation and serious analysis after orientation.

## L4_AUTONOMOUS_SANDBOX

The model may execute a full research→experiment→evaluate loop autonomously inside a preapproved containment boundary until it hits a stop condition, material scope change, budget limit, or hard gate.

This is not “unrestricted.” It should have the strongest environmental isolation and explicit egress/data boundaries.

## Preset selection heuristic

Choose the highest level whose worst plausible unreviewed action is acceptable inside the configured environment. Increase autonomy by strengthening isolation and reversibility first, not by simply removing prompts.
