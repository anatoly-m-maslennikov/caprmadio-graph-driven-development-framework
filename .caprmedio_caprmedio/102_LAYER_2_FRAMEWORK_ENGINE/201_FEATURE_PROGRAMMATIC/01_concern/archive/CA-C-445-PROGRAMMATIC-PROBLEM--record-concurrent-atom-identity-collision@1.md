---
atom_id: CA-C-445
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Concurrent Atom Identity Collision"
  depends_on: [Implementation, Projection, Journal, Carrier]
version: 1
updated_at: 2026-10-04 22:57:31
relations: {concern_about: [CA-M-276, CA-E-448, CA-D-378]}
---
# Summary

Record concurrent Atom identity collision

## Concern

Two distinct active Concern carriers currently assert CA-C-443. Concurrent sessions must not silently select one, overwrite a Claim, or renumber an admitted valid owner. Collision repair is blocked pending an established original assignment owner and an explicitly authorized identity-safe correction through MCP.

## Evidences

The PROGRAMMATIC carrier CA-C-443-PROGRAMMATIC-PROBLEM--migrate-legacy-projection-and-runtime-log-consumer-atoms.md was created through Run storage-i-ca-c-443-20261005-v2; its exact target and completed effect are recorded in _journal/run-support-2026-10-04-part-2.ndjson. A separate project carrier 01_concern/CA-C-443-caprmedio-PROBLEM--record-denied-applicable-methodology-projection-relocation.md asserts the same ID for a different Claim. Its carrier timestamp alone cannot establish assignment precedence. CA-M-276v9 requires recorded owner evidence or an Operator decision, preservation of original identity and histories, and correction only of context-resolved current references. The same-identity Update MCP route rejects changed atom_id; a missing identity-repair capability must not be bypassed with direct carrier edits.

## Blast radius

ID-only CA-C-443 lookup is ambiguous. Both Claims and their recorded histories remain untouched until repair is authorized and supported. Publication of unrelated methodology sources is independent of this concern; do not report the collision repaired.
