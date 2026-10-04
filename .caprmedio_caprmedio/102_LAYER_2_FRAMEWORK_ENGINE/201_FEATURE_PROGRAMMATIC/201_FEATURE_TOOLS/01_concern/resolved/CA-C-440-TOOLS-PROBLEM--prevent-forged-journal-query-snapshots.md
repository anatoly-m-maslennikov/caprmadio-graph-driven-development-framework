---
atom_id: CA-C-440
content_role: Concern
type: Problem
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: resolved
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-04 22:52:48 +0000"
subjects:
  governs: "Prevent forged Journal query snapshots"
  depends_on: [Journal, Projection, Evaluation, Implementation]
relations:
  concern_about: [CA-P-1526, CA-P-1544, CA-P-1545, CA-P-1547]
---
# Summary

Prevent forged Journal query snapshots

## Concern

The Journal query accepts caller-controlled snapshot records, members and source roots after a plain SHA rehash, so it can return an injected Event not derived from the configured canonical Journal.

## Evidences

CA-P-1544's in-memory probe substituted source_root '.', zero members and an INJECTED record; the query returned status complete and INJECTED. Repair must retain/authenticate the real captured snapshot and enforce the canonical _journal frontier.

## Blast radius

Resolved disposition: P1545 repaired opaque server-retained snapshot trust and canonical-root/member validation. Independent P1547@3 accepted the adversarial core contract. Actual queue/Run/image gates remain separate and are not bypassed.

Neither query Tool is admitted to MCP until its current repair and independent acceptance gates are satisfied. No source write, real Run, image or aggregate Epic completion is inferred from the initial passing unit suites.
