---
atom_id: CA-C-445
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: resolved
author: Anatoly Maslennikov
subjects:
  governs: "Concurrent Atom Identity Collision"
  depends_on: [Implementation, Projection, Journal, Carrier]
version: 2
updated_at: "2026-10-05 00:22:30 +0000"
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

## Repair result on 2026-10-05

The preceding Concern and Evidence sections retain the pre-repair snapshot. The Operator approved preserving the PROGRAMMATIC legacy-consumer Concern as CA-C-443 and correcting the separate project relocation Problem. The sealed MCP Replace Run identity-alignment-20261005-ca-c-447-collision-v1 completed: the relocation Problem is now CA-C-447, and its complete predecessor is preserved at 01_concern/archive/CA-C-443-caprmedio-PROBLEM--record-denied-applicable-methodology-projection-relocation@1.md. The shared Run records retain the exact predecessor-to-successor binding. Current CA-C-443 and CA-C-447 resolve uniquely; no unambiguous incoming current relation to the relocation predecessor required rewriting. Historical evidence is not rewritten. The underlying relocation Problem remains Active as CA-C-447; resolving this collision does not claim the physical relocation was completed.
