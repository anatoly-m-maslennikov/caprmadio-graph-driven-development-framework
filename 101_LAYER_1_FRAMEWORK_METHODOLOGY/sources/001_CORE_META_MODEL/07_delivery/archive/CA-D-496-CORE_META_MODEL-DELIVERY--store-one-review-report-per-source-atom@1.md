---
atom_id: CA-D-496
content_role: Delivery
type: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-09-25 21:01:05 +0000"
subjects:
  governs: "Workflow Run"
  depends_on:
    - "Atom"
    - "Atom/Revision"
    - "Evaluation"
    - "File Carrier"
    - "Projection"
relations: {"relates_to":["CA-E-520"]}
---
# Summary

Store one review report per source Atom

## Scope

temporary evidence Carriers of a batched RMED Atom review Run.

## Claim

the Run **must** store its temporary evidence under **=1** caller-admitted Run directory using this layout:

- `manifest.json`: Run identity, complete requested selection, selected batch **and** deferred members, source identity/Revision/path/SHA-256 bindings, effective limits **and** their provenance, estimated work, authority bindings, permissions, confidence **and** retry policy.
- `reports/<ordinal>.json`: **=1** report for **every** selected source Carrier, using its fixed four-digit batch ordinal rather than an untrusted filename **or** a possibly invalid Atom ID.
- `mechanical/`: unchanged mechanical checker requests **and** raw results referenced by the reports.

**every** report **must** contain `schema_version`, `run_id`, `ordinal`, the original `source` binding, `evaluations`, `repairs`, `current_sources`, **and** `state`. **every** evaluation records its own source binding, authority bindings, **all** CA-E-520 check results, evidence, findings **and** proposed fixes, missing coverage, mechanical evidence, **and** overall result. findings identify the affected section **or** Property, an exact excerpt **or** observed absence, the checked authority, **and** concise reasoning. **every** repair records the exact input/output bindings, changed paths, disposition, **and** verification references.

keep initial evaluations **and** later attempts **in** the same report; do **not** overwrite earlier evidence with a final pass. include passed **and** blocked Atoms, **not only** failed Atoms. report states are `evaluated`, `unchanged`, `verified`, **or** `blocked`; a verified state requires a current passing evaluation of **every** resulting source **and** completed affected-reference checks. these files are derived temporary evidence, **not** Atom authority **or** a substitute for required durable history.

## Details

a missing **or** ambiguous Atom ID is represented explicitly, **not** invented. source path **and** digest still identify the inspected Carrier. replacements **or** splits retain their predecessor/successor mapping **in** the original report. a report's apparent pass becomes stale **when** a bound source **or** applicable authority changes.
