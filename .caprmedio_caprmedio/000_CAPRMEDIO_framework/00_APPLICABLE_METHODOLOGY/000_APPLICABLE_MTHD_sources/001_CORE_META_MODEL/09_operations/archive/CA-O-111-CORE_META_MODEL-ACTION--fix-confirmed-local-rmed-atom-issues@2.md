---
atom_id: CA-O-111
content_role: Operations
type: Action
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-03 06:11:33 +0400"
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
---
# Summary

Fix confirmed local RMED Atom issues

## Operation

Repair RMED Review Batch **means** the Action that applies the smallest authorized correction for confirmed local findings.

1. read the current Atom **and** its check report. **if** the source changed since the check, stop that item's repair with the mismatch recorded.
2. resolve confirmed findings under the applicable local rules, permissions, **and** confidence threshold. preserve necessary information, Subject targets, **and** relation targets.
   - correct forced execution as a capability Requirement **only** **when** its intended capability **and** target are established **and** the semantic change is authorized.
   - preserve required outcomes, validation gates, safeguards, **and** behavior during authorized execution. do **not** replace `must` with `may` mechanically **or** invent a target.
   - retirement requires explicit authority; unresolved intent **or** absent authority blocks the correction rather than weakening the Claim.
3. classify the change under CA-O-067. refresh `updated_at` on **every** edit; retain Version for formatting **or** equivalent wording, **and** increment it for a real meaning change. a Summary-value **or** genuine Type change requires replacement authority. retain required history.
4. apply the correction **and** record the actual changes **in** the same Atom report. uncertain, unauthorized, identity-changing, **or** outside-scope work remains blocked rather than expanding this Run.
5. return `fixed_not_rechecked` for applied corrections **or** `blocked` with the remaining issue. this Action performs no proposal review, post-fix Evaluation, **or** automatic recheck loop.

## Details

at the configured context threshold, save the current Atom, unfinished correction, **and** completed edits **in** a short handoff. continue **in** a fresh subagent **without** repeating an already applied edit. context handoff does **not** consume a repair retry; genuine failed execution attempts remain subject **to** the admitted retry policy.

a correction record is evidence of an edit, **not** a passing check. a later check is a separately requested Run.
