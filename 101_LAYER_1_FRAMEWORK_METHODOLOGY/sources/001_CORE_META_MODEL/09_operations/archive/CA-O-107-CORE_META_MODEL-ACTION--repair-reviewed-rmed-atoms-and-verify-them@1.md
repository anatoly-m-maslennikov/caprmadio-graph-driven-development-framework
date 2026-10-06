---
atom_id: CA-O-107
content_role: Operations
type: Action
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: "Archived"
author: Anatoly Maslennikov
version: 1
updated_at: "2026-09-28 06:30:40 +0400"
subjects:
  governs: "Repair RMED Review Batch"
  depends_on:
    - "Action"
    - "Atom"
    - "Atom/Revision"
    - "Atom/Summary"
    - "Evaluation"
    - "Operator"
    - "Autonomous Confidence Threshold"
    - "Journal"
relations: {"relates_to":["CA-D-496","CA-E-520","CA-O-028","CA-O-067","CA-R-1464"]}
---
# Summary

Repair reviewed RMED Atoms and verify them

## Operation

Repair RMED Review Batch **means** the Action that resolves supported review findings sequentially within the Operator's admitted mutation boundary.

1. check each report's source **and** authority digests, exact proposed correction, effective confidence threshold, permissions, **and** remaining retry allowance. stale inputs, unresolved findings, **or** absent authority return `blocked` **before** mutation.
2. use applicable Principles **and** current authority **to** choose the smallest gap-free correction. for authority conflicts follow CA-O-028; freshness does **not** override higher-tier authority. preserve unrelated edits **and** necessary information.
3. classify the change under CA-O-067. preserve identity for an admitted revision; a Summary change requires a new Atom identity under CA-R-1464. split, replacement, archival, **or** changes outside selected paths require their applicable authorization; do **not** broaden GOVERNS **or** suppress a check **to** force a pass.
4. apply an authorized correction with required versioning, history, **and** relation maintenance. formatting-only edits preserve `updated_at`. record exact effects **and** predecessor/successor bindings **in** the original report.
5. invoke the same implemented CA-E-520 Evaluation on **every** resulting source **and** check affected active references. retain initial **and** later results. an initial failure consumes no retry; each additional fix-and-evaluate attempt consumes **=1** admitted retry. exhausted retries, no progress, changed authority, **or** low confidence return `blocked`, retaining completed effects.
6. return `verified` **only** **when** every selected Atom is unchanged with current passing evidence **or** repaired with current passing evidence, **and** no affected relation **or** required coverage gap remains.

## Details

this Action does **not** claim completion for deferred Atoms. it does **not** change its own governing Evaluation, Workflow, Action, **or** prompt to obtain a pass; such a required authority change ends the current Run for fresh admission. routing **and** resumption belong **to** the caller, **not** a self-started child Workflow.
