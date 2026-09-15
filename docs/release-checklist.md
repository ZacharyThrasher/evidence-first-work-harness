# Release checklist

- [ ] `VERSION`, Skill metadata, and changelog agree.
- [ ] `python scripts/validate_release.py` passes.
- [ ] `/efwh --status` works in a clean test workspace.
- [ ] A new `/efwh <simple research problem>` initializes durable state without asking the user to edit files.
- [ ] A bounded build/data-analysis smoke test respects the selected autonomy boundary.
- [ ] A deliberately risky action produces a precise human gate.
- [ ] A narrow failed experiment remains a scoped failure rather than a global `EXHAUSTED` claim.
- [ ] Resume in a fresh Claude session using `/efwh --resume`.
- [ ] Site (`index.html`) renders locally and attribution is visible but unobtrusive.
- [ ] Company policy additions (if any) were reviewed by the appropriate owner.
- [ ] Release notes identify behavioral changes and migration impact.
