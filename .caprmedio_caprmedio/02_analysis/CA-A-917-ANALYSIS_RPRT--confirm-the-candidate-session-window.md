---
atom_id: CA-A-917
content_role: Analysis
type: Analysis Report
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Historical session candidate/window disposition"
  depends_on:
    - "Project"
    - "Operations"
version: 1
updated_at: "2026-10-04 07:55:00 +0400"
relations:
  relates_to:
    - CA-P-1196
    - CA-C-294
    - CA-A-905
    - CA-A-910
---
# Summary

Confirm the candidate session window

## Question

Does the retained historical source candidate provide any canonical evidence in the frozen monthly harvest window?

## Scope

Only the exact5865276-byte source prefix declared by CA-A-905v1 for session01a01cb6-4ee4-7553-b68d-0823dda35094: `/Users/am/.codex/sessions/2026/08/20/rollout-2026-08-20T05-08-24-01a01cb6-4ee4-7553-b68d-0823dda35094.jsonl`. Historical Project identity is not inferred or asserted. The monthly window is [2026-09-04T01:54:15Z,2026-10-04T01:54:15Z).

## Approach

Root read and decoded only the declared source prefix, inspecting event metadata rather than adopting semantic source statements. Every record was newline-terminated, valid JSON and carried a timestamp; timestamp comparison used the same exact half-open bounds as the shared index. Source/message type and role/channel were classified only for in-window records. No candidate message content was adopted or used to author Operations. No credentials, referenced files or unrelated source bodies were followed.

Current Epic1117v1, Goalv13 and the previously read active Principles govern safe evidence preservation and truthful limits; no new autonomy/implementation decision was made. P1196 inherits the90% control. The unresolved broader identity remains preserved in C294 rather than being invented from an alias or modified date.

## Results

| Evidence | Observed value |
|---|---|
| Exact read/snapshot bytes | 5865276 /5865276 |
| Native records | 1570 |
| Prefix SHA256 | `4f9d453d6cbbb76f50573c64b73c3b0f2b2d77e502b9ae955ae1c93b055ea49f` |
| Earliest native event timestamp | 2026-08-20T01:08:25.629Z |
| Latest native event timestamp | 2026-09-23T00:04:22.945Z |
| Four canonical human/assistant-message counts | 0 /0 /0 /0 |
| Missing/invalid timestamp, incomplete/invalid record, read error | 0 |
| In-window records of any kind | 1 |

The sole in-window record is line1570, bytes[5862497,5865276), timestamp2026-09-23T00:04:22.945Z, type`event_msg`, payload type`thread_settings_applied`. It is metadata, not a canonical human/assistant decision, a Tool result, or a reusable Operation execution. Its payload content was not promoted to semantic harvest evidence.

This proves a no-canonical-evidence disposition for all four monthly partitions. It does not prove or deny historical Project identity. CA-A-905/910 retain their earlier snapshot/candidate classification; this later exact prefix result supplements them rather than changing what the earlier indexing task observed. Original native evidence remains retained. No substantive harvest remainder is needed for this source within the frozen window. All other sources and unprocessed messages remain unfinished.

CA-C-294 remains active for the broader historical-identity question, with an explicit nonblocking current-window disposition. Any future different-window content adoption still requires identity confirmation. The first-source/window timestamp and byte coverage check was complete; a second narrow metadata-only check independently identified the sole in-window record's line/type/offset. Root later strict-YAML/heading verification covers the saved carriers, not source semantics.

## TLDR

The single uncertain historical source has no canonical messages in the monthly window. Its only in-window record is thread-settings metadata. Monthly content adoption is unnecessary; historical identity remains unasserted and preserved as a nonblocking limitation.
