# Contributing

EFWH should stay smaller than the problems it helps solve. Changes need a reason, not merely more process.

## Before opening a PR

Run:

```bash
python scripts/validate_release.py
```

Then check the PR against these questions:

1. What observed failure mode or adoption problem does this change address?
2. Is the behavior change in the canonical `.claude/skills/efwh/` copy?
3. Does it weaken a hard gate, trust boundary, or evidence requirement? If so, why is that justified?
4. How will we know the change improved outcomes rather than merely adding instructions?
5. Does `reasoning.md` need an update?
6. Could a stronger/newer model make an older workaround removable instead?

## Design rules

- Prefer the simplest mechanism that measurably works.
- Do not add broad tool permissions to make demos smoother.
- Keep instruction trust separate from evidence authority.
- Scope negative conclusions to the experiment performed.
- Define acceptance evidence before meaningful execution.
- Preserve failed experiments when they materially narrow the search space.
- Avoid duplicating the canonical protocol in a second directory.

## Release versioning

Use semantic versioning for the distributed Skill:

- PATCH: wording/clarity fixes with no intended behavioral change;
- MINOR: backward-compatible workflow/policy capabilities;
- MAJOR: changes that materially alter invocation, state layout, hard-gate semantics, or project compatibility.

Update `VERSION`, Skill metadata, `CHANGELOG.md`, and relevant docs together.
