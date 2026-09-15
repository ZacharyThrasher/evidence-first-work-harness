# Evaluation Protocol

## Principle

Evaluate the actual outcome, not the generator's confidence or prose.

## Preferred grader order

1. **Deterministic/environment graders** — tests, invariants, reconciliations, database state, file diff, service response, statistical checks.
2. **Independent model grader** — fresh context, explicit rubric, no needlessly persuasive generator rationale.
3. **Human/SME grader** — subjective/high-impact/domain-critical review.

Use combinations when appropriate.

## Before execution

Define acceptance in `tasks/CURRENT.md` and register material evals in `eval-registry.json`.

## After execution

Record:

- pass/fail/partial;
- actual observed state;
- grader type;
- evidence IDs;
- uncertainty and known blind spots.

## Nondeterminism

For material stochastic/model-dependent tasks at R2+, use multiple trials when practical. Distinguish one successful trial from a reliable capability.

## EVAL_DEFECT

If an acceptance criterion/test is internally inconsistent, stale, impossible, or measures the wrong thing:

1. do not silently modify it to make the work pass;
2. mark `EVAL_DEFECT`;
3. preserve the failing result;
4. explain the defect with evidence;
5. repair/replace the eval under the allowed review process;
6. rerun the affected work if needed.

Evaluators are fallible too.
