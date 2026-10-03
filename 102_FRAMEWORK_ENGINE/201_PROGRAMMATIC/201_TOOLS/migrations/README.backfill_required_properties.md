# Backfill required Atom properties

`backfill_required_atom_properties.py` migrates absent frontmatter properties from
an explicitly reviewed evidence map. It does not discover values from names or
folders, change Claims, overwrite existing values, or provide reader defaults.
The evidence preparer is responsible for resolving semantic ambiguities. An
unknown value stays missing; a placeholder is not a repair.

Inputs are an existing `VALIDATE_ATOMS` report, its exact source boundary, and a
JSON object of this shape:

```json
{"carriers": {"/absolute/source/atom.md": {
  "atom_id": {"value": "CA-R-1", "evidence": "Reviewed legacy identity"}
}}}
```

Supported fields are `atom_id`, `content_role`, `type`, `current_scope_unit`,
`claim_target_scope_unit`, `local_tier`, `global_tier`, `status`, and `author`.
Every addition must correspond to a reported `PROPERTY_REQUIRED` finding.

```sh
python backfill_required_atom_properties.py --report report.json \
  --source-root /absolute/source --evidence evidence.json --output plan.json
python backfill_required_atom_properties.py --apply plan.json --output receipt.json
```

Review the entire plan, its per-field evidence, unresolved values, and blockers
before applying. The tool verifies the whole selected baseline before any write,
rejects unsafe paths and ambiguous YAML, archives each exact prior Revision, and
increments `version`. Existing metadata, Markdown, and `updated_at` are preserved.
All writes use the same checked filesystem primitives as the retired-property
fixer. Apply is idempotent; stale inputs, changed history, or altered planned
Claims fail closed. A concurrent failure can leave an applied prefix; rerunning
the same reviewed plan safely resumes it. Outputs never overwrite existing files.

Journal integration and refreshing exact-byte validator authority pins remain
the governed caller's responsibility. Pin refresh is justified only after
checking that Claims and all previously present properties except `version`
are unchanged. This migration does not repair other validator findings.

Tests:

```sh
python -m unittest discover -s tests -p 'test_*atom_properties.py'
```
