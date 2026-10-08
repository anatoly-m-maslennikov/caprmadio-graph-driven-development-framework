---
atom_id: CA-C-505
content_role: Concern
type: Question
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: resolved
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-06 18:38:40 +0000"
subjects:
  governs: "Align prepared replacement successors"
  depends_on: [Implementation, Evaluation, Action, Workflow Run, Journal]
relations:
  concern_about: [CA-P-1799, CA-P-1794, CA-P-1655]
---
# Summary

Align prepared replacement successors

## Concern

Replace authority says successors must already be Active on input, while the intended admitted Replace creates complete proposed successors and activates them before archival.

## Evidences

the final source-to-code review confirmed this bounded discrepancy. independent adjudication separated it from unsupported status-transition and authorization-model proposals. focused fixture results establish repair behavior, not actual release completion.

## Blast radius

the affected selected capability and its current release candidate. installed N, historical Events and frozen test snapshots remain preserved.

## Decision

clarify source authority to admit only the sealed complete prepared-new successor set, with all resulting successors Active before predecessor archival; keep the Operator's single Replace boundary.

## Result

R1041 v8 and O128 v4 retain exact predecessor bytes and admit only complete sealed prepared-new successor sets. the actual registered pin refresh is recorded. the replacement suite passes 22 cases, explicitly proving all successors Active before archival, exact destination-collision refusal and distinct used-ID/unused-destination atom-id-collision refusal without effects. independent review accepts this packet; no release success is implied.
