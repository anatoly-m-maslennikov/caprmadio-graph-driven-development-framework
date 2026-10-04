---
atom_id: CA-P-1184
content_role: Plan
type: Plan
label: Task
work_sequence_number: 6
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: "Session evidence/event-window index"
  depends_on:
    - "Project"
    - "Operations"
version: 2
updated_at: "2026-10-04 07:40:00 +0400"
relations:
  is_decomposition_of:
    - CA-P-1118
---
# Summary

Index admitted session event windows

## Objective

Within <=15 minutes, index the already admitted native source snapshots from CA-A-905 v1 once, so the four harvest partitions can bind exact packets without repeatedly scanning the corpus. This Task reads event metadata and computes source/message fingerprints; it does not interpret decisions or declare content harvested.

### Inputs, ownership and bounds

- Durable input: `.caprmedio_caprmedio/02_analysis/CA-A-905-ANALYSIS_RPRT--inventory-the-session-evidence-corpus.md`, its complete embedded JSON and unchanged [2026-09-04 05:54:15 +0400, 2026-10-04 05:54:15 +0400) window. CA-P-1125 is Done.
- Read only admitted exact paths, up to their recorded snapshot byte lengths. Keep the single alias candidate unread and visibly pending under CA-C-294; its identity check remains substantive harvest work.
- Scan <=8 GiB, <=64 MiB per record and <=8 minutes. Stop truthfully on a bound or failure, preserving exact file/byte/line frontier. Read only permitted sources; no credentials, unrelated bodies, account changes, environment repair or engine implementation.
- Classify canonical response_item user/assistant messages separately from event_msg mirrors, internal analysis, Tool output and machine environment context. Preserve primary versus subagent origin; worker evidence is not independent Operator input. Preserve continuation files without claiming deduplication.
- Own only this Plan, temporary analytical helper/index under `.caprmedio_tmp/CA-P-1117`, durable CA-A-910 at `.caprmedio_caprmedio/02_analysis/CA-A-910-ANALYSIS_RPRT--index-session-event-windows.md`, and narrowly necessary remainder/Concern/gate updates. This helper is not a delivered framework Tool.

### Required result and verification

Retain per-source snapshot digest/byte/record counts, four window counts, source origin, canonical message timestamp/role/channel/line/byte/hash boundaries, exclusions and exact unprocessed frontier. CA-A-910 retains durable source-level coverage and limitations; a disposable detailed index is only a retrieval accelerator for the original source files.

Verify that every admitted manifest row has exactly one disposition, the candidate remains explicit and unread, every indexed message falls in exactly one half-open partition, source offsets fit their snapshot, and source IDs/window match CA-A-905. Incomplete or bounded coverage is never a pass; bind concrete <=15-minute remainder and required BLOCKS edges before completing this leaf. Inherit CA-P-1117's 90% policy and actual permission boundaries. Other harvest leaves still own interpretation and supersession.

## Details

### Execution result

CA-A-910 v1 retains all1659 manifest-row dispositions and source snapshot digests/counts. The completed bounded index read6604133498 bytes in37.692 seconds, below all declared bounds. It indexed1658 admitted snapshots; CA-C-294's single identity candidate remains explicitly unread. There were no input/read/record-bound errors. Four PRIMARY window counts are1949/1826/1398/1415; worker counts are474/476/1422/4051. Total13011 canonical message boundaries are indexed, not substantively harvested.

Root independently compared all1659 durable coverage rows with the exact detailed index, checked source identity/order, all message offsets against declared snapshot lengths, exactly one partition per message and every source's count totals. All passed. Every required source has a disposition; no bounded remainder was needed for this indexing leaf. The candidate's actual identity check remains harvest work under CA-C-294. No methodology stage is unlocked and all unprocessed content remains owned by1126–1129 and their bound remainders. Temporary analytical helper/index are accelerators; original native sources plus CA-A-905/CA-A-910 retain the durable retrieval basis.

### Definition of Done

This Task is not Done without a durable verified per-source coverage record and all actual incomplete frontiers/typed Concerns/remainder gates. Index completion is not thirty-day harvest completion. No methodology or implementation stage is unlocked by this Task alone.
