---
atom_id: CA-C-462
content_role: Concern
type: Problem
current_scope_unit: ATOM_LIFECYCLE
local_tier: Standard
global_tier: 11
status: resolved
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 06:14:04 +0000"
subjects:
  governs: "Record non-atomic Draft promotion recovery"
  depends_on: [Tool, Manifest, Evaluation, Runtime]
relations:
  concern_about: [CA-P-1690]
---
# Summary

Record non-atomic Draft promotion recovery

## Concern

Independent helper review rejects at98%: deterministic concurrent finalizers wrote two identified_promotion children for one Draft head; terminal-receipt failure followed by old-Draft removal could not recover because active-state validation required the removed path before matching its existing successor. P1690 repairs atomic single consumption and recovery ordering, and supplies a supported lookup API before P1685 can finish native retry dispatch. Earlier thirteen passing cases did not cover these failures.

## Evidences

The reviewer observed results2/errors0/promotion_children2/history_entries3 and a path-invalid retry after Draft removal in disposable development fixtures.

## Blast radius

Draft identity recovery and native promotion acceptance; parent integration remains unfinished.

## Resolution

P1690's exact repaired helpers are independently ACCEPT at97%; sixteen focused cases pass. The reviewer reproduces one shared successor under concurrent finalization and successful same-successor terminal recovery/replay after old-Draft removal. Native retry remains separately owned by P1694; this resolved Problem closes only the two reproduced helper failures.
