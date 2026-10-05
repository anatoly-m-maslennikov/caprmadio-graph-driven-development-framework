---
atom_id: CA-O-111
content_role: Operations
type: Action
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 5
updated_at: "2026-10-04 02:57:00 +0400"
subjects:
  governs: "Repair RMED Review Batch"
  depends_on:
    - "Action"
    - "Atom"
    - "Atom/Revision"
    - "Atom/Summary"
    - "Operator"
    - "Autonomous Confidence Threshold"
    - "Journal"
relations: {"relates_to":["CA-D-496","CA-E-520","CA-O-028","CA-O-067","CA-R-1464"]}
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-111-CORE_META_MODEL-ACTION--fix-confirmed-local-rmed-atom-issues.md
  source_atom_id: CA-O-111
  source_atom_revision: 5
  source_sha256: 4408a09c5a8a4ce316a34d072a2a3ca3dd5d057f48f7853de390efb3615f4103
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Fix confirmed local RMED Atom issues

## Operation

Repair RMED Review Batch **means** the Action that applies the smallest authorized correction for confirmed local findings.

1. read the current Atom, applicable checking criteria, **and** its check report. **if** the checked source **or** applicable criteria changed, stop that item's repair with the mismatch recorded; retain the earlier report as historical evidence rather than inventing a current pass **or** adding an automatic recheck.
2. resolve confirmed findings under the applicable local rules, permissions, **and** confidence threshold. preserve necessary information, Subject targets, **and** relation targets.
   - correct forced execution as a capability Requirement **only** **when** its intended capability **and** target are established **and** the semantic change is authorized.
   - preserve required outcomes, validation gates, safeguards, **and** behavior during authorized execution. do **not** replace `must` with `may` mechanically **or** invent a target.
   - retirement requires explicit authority; unresolved intent **or** absent authority blocks the correction rather than weakening the Claim.
3. classify the change under CA-O-067. refresh `updated_at` on **every** edit; retain Version for formatting **or** equivalent wording, **and** increment it for a real meaning change. a Summary-value **or** genuine Type change requires replacement authority. for a Summary change, `allow_replacements=true` **with** fix permission delegates replacement **within** the selected Atom; the executor reserves a new ID **and** Version **`=1`**, archives the predecessor, **and** records the transition. retain required history.
4. apply the correction **and** record the actual changes **in** the same Atom report. uncertain, unauthorized, **or** outside-scope work remains blocked rather than expanding this Run.
5. return `fixed_not_rechecked` **or** `replaced_not_rechecked` **only** **when** **all** **`=6`** initial checks concluded **and** **all** findings were corrected **or** rejected with recorded reasons. otherwise return `blocked`, preserving safe partial edits **and** the remaining findings **or** unfinished coverage. this Action performs no proposal review, post-fix Evaluation, **or** automatic recheck loop.

## Details

at the configured context threshold, save the current Atom, unfinished correction, **and** completed edits **in** a short handoff. continue **in** a fresh subagent **without** repeating an already applied edit. context handoff does **not** consume a repair retry; genuine failed execution attempts remain subject **to** the admitted retry policy.

a correction record is evidence of an edit, **not** a passing check **or** completion of an unperformed check. preserve original check outcomes **and** blockers separately from corrections. a later check is a separately requested Run.
