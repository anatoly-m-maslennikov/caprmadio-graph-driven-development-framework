---
atom_id: CA-D-496
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 6
updated_at: "2026-10-03 06:11:33 +0400"
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

temporary evidence Carriers of a local RMED Atom review Run.

## Claim

the Run **must** store its temporary evidence under **`=1`** caller-admitted directory using this layout:

- `progress.json`: the original selection, per-Atom path **and** identity, current Step, state, report path, assigned worker, applicable context setting, **and** any blocked **or** unfinished work. a short handoff records the current Atom, completed edits, **and** next work **in** this file.
- `reports/<ordinal>.json`: **`=1`** report per selected Carrier, using its fixed four-digit ordinal. retain the check result **and** later applied corrections **in** this same file.

**every** report **must** contain the source path, carried Atom ID **and** Version, source observation, **all** **`=6`** local check outcomes, concise evidence, confirmed findings, unresolved coverage, applied corrections, **and** current state. a confirmed finding includes its location, source passage, applicable rule, **and** proposed fix. record the original checked source digest once so the fixer can notice concurrent changes.

## Details

shared checking rules **may** be stored once; reviewers receive their relevant actual contents. an existing mechanical report **may** be linked as supporting evidence. separate raw-part files, proposal reports, admission receipts, checkpoint files, **and** closure certificates are **not** required by this Workflow.

states are `pending`, `checked_clean`, `needs_fix`, `fixed_not_rechecked`, **or** `blocked`. `fixed_not_rechecked` records an applied correction **without** claiming a post-fix pass. missing identity **or** unfinished checks remain explicit. excluded checks are **not** marked as passed.

preserve earlier reports **and** completed work. a workflow-packaging **or** context-budget change alone does **not** invalidate a review of unchanged content under unchanged checking criteria. changed Atom content **or** a changed applicable criterion makes its earlier check historical; this Workflow does **not** automatically recheck it.
