# Adapter — Software Engineering

## Orientation additions

Inspect repository instructions, current branch/status, build/test commands, CI, architecture docs, package/runtime versions, issue context, and staging/sandbox options.

## Preferred containment

Use a dedicated branch/worktree or disposable copy. Do not modify unrelated user work. Production deployment is a hard gate unless explicitly delegated by policy.

## Evidence examples

- failing/passing test outputs;
- minimal reproductions;
- diffs/commits;
- runtime traces;
- profiler results;
- official API/OS documentation;
- end-to-end behavior observed through the user-facing interface.

## Evaluation

Prefer end-to-end behavior plus regression tests over unit tests alone. Do not remove or weaken tests merely to pass. If a test is demonstrably wrong, use `EVAL_DEFECT`.

## Completion

Code existing is not completion. Required behavior must work in the target-like environment and required regression/e2e checks must pass.
