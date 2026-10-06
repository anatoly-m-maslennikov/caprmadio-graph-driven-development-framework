---
atom_id: CA-O-107
content_role: Operations
type: Action
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 5
updated_at: "2026-09-30 17:56:15 +0000"
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

Repair RMED Review Batch **means** the Action that fixes supported local findings within the Operator's admitted mutation boundary **and** independently verifies the result.

1. verify the original candidate, local-rule bindings, complete local report, permissions, confidence threshold, context budget, **and** remaining retries **before** preparing a correction.
2. choose the smallest information-preserving correction under the supplied local rules. preserve the Entity model, Subject targets, **and** relation targets; fixing their local Carrier shape does **not** authorize changing their meaning. cross-Atom reconciliation is outside this Run.
3. classify the proposed change under CA-O-067. preserve identity for an admitted revision; a Summary **or** genuine Type change requires replacement authority. **if** a necessary split, replacement, archival, **or** outside-path change requires relation maintenance, retain the proposal **and** return blocked for separately authorized work; do **not** start a graph audit.
4. obtain independent review of the full candidate under the same local checklist **and** verify that necessary original information survives. malformed review output is a report repair, **not** permission for source mutation.
5. apply **only** verified, authorized corrections **after** a freshness check. refresh `updated_at` on **every** edit; increment Version **only** for a real meaning change. retain history **and** exact input/output bindings; independently recheck the saved output.
6. an initial failure consumes no retry; **every** further repair attempt consumes **`=1`** admitted retry. exhausted retries, no progress, low confidence, changed local authority, **or** missing permission return blocked with completed effects retained.
7. return `verified` **only** with current local passing evidence for **every** selected unchanged **or** repaired Atom. this result does **not** assert Entity-model **or** cross-Atom conformance.

## Details

current passing evidence includes matching saved candidate, checking-rule, settings, **and** prompt bindings at closure. a cached checking-rule binding becomes stale even **when** its Version stays unchanged. preserve earlier reports under their original bindings; admit fresh review **after** an authorized binding update.

**before** a worker consumes reserved headroom, checkpoint effects, unfinished Atom ordinals, the pending repair **or** verification stage, reports, **and** retry accounting; return `blocked/context_capacity`. the caller automatically starts a fresh subagent for the exact remaining work with revalidated bindings **and** preserves the independence of proposal **and** saved-output review. this handoff alone consumes no repair retry **and** authorizes no repeated mutation. a full parallel worker pool waits for a slot; actual host spawn refusal retains an external blocker **and** the unfinished queue.

the Action does **not** change its governing checks **to** obtain a pass. a required rule change ends this Run for fresh admission. deferred candidates remain incomplete.
