---
atom_id: CA-P-1125
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: "Session-derived operational capability delivery"
  depends_on:
    - "Operations"
    - "Implementation"
version: 3
updated_at: "2026-10-04 06:57:00 +0400"
relations:
  is_decomposition_of:
    - CA-P-1118
  blocks:
    - CA-P-1151
    - CA-P-1152
    - CA-P-1153
    - CA-P-1154
    - CA-P-1126
    - CA-P-1127
    - CA-P-1128
    - CA-P-1129
---
# Summary

Freeze the session window and evidence manifest

## Objective

The assigned AI Agent must complete one bounded work packet for freeze the session window and evidence manifest, using the stated inputs and ownership restrictions, and record the required output without extending this leaf's scope.

### Inputs and bounded ownership

Use the request window [2026-09-04 05:54:15 +0400, 2026-10-04 05:54:15 +0400). Read the current Operator Goal and all active Project Principles before discovery. Inspect project-linked session metadata through available local/app read interfaces; do not scan denied paths, credentials, or unrelated project content. Compare existing Harvest Epic 014 and other active Plans for overlapping ownership.

### Required output

A timestamped corpus manifest with session identifiers, relevance reasons, retrieval sources/cursors, known gaps, date partitions, current authority revisions, and reusable existing work. If enumeration exceeds fifteen minutes, create additional bounded manifest subtasks before declaring the harvest stage complete.

### Composite packet and execution gate

This packet Plan is composite. Its initial preflight child has an estimate of <=15 minutes; actual execution children are created only after their inputs, ownership, output and verification are bound. Composite roll-up effort depends on the resulting decomposition. Before execution, the parent/preceding-task review must bind the exact evidence packet or capability IDs, live governing revisions, target file paths, output and verification command/scenario in this file. If they cannot be bound safely or exceed the estimate, create narrower subtasks before execution rather than starting an underspecified leaf. A remainder is represented by new Plan files and explicit dependency edges, not an untracked promise.

Inherit CA-P-1117 controls and the 90% confidence threshold through IS_DECOMPOSITION_OF. Every issue requires a typed C atom: blocker/failure -> Problem; unresolved choice -> Question; incompatible authority -> Conflict. Postpone a blocked task and work on another independent ready task. After completion, reassess and update affected dependent tasks before they start. Retain durable source/result/provenance evidence; do not mark the parent Done merely because this first packet is Done.

### Preparation result and remaining manifest frontier

CA-P-1150 completed bounded preparation at 2026-10-04 06:42:47 +0400. One app listing with limit 20 returned 20 recent records and 6 pinned overflow records; 7 exact project-linked Codex IDs are durably carried in the new child `02-CA-P-1175-TASK--bind-the-first-seven-session-metadata-sources.md`. No pagination cursor was supplied, and app updated_at does not enumerate in-window events. No session content was harvested.

CA-P-1175 completed the first metadata binding: all seven exact app session IDs have local sources, represented by nine continuation candidates. One filename-only enumeration returned 2,011 files with no limit reached; only the first session_meta record of the nine matches was read. Its durable result and exact paths are retained in `done/02-CA-P-1175-TASK--bind-the-first-seven-session-metadata-sources.md`; supplemental JSON is `.caprmedio_tmp/CA-P-1117/manifest-CA-P-1175.json`. Duplicate continuations and verified historical cwd values remain evidence, not restored Project bindings or proof of complete source history.

CA-P-1176 is the concrete next executable leaf: `03-CA-P-1176-TASK--enumerate-the-project-session-metadata-corpus.md`, with exact native active/archived roots, first-record bounds, optional one-page archived app source, and durable CA-A-905 corpus-manifest output. This parent remains Active until the required corpus manifest and actual discovery remainders are complete. Event-window body coverage is an explicit later harvest frontier, not metadata completion. The parent's existing gates plus CA-P-1176's direct BLOCKS edges retain all four partition preflights and parents as blocked; Done initial binding does not authorize substantive harvest.

Existing Harvest Epic 014 is a TOOLS-authority harvest: CA-P-1073 inventories reusable operations from the TOOLS RMEDO subtree, not the monthly session corpus. Reuse and cross-map its candidates in later reconciliation rather than duplicating that inventory. No monthly completion evidence is inferred from it. General adopted Operations route to CORE_META_MODEL and caprmedio-specific Operations to PROJECT_CONFIGURATION under CA-P-1117; this metadata packet authors neither.

CA-C-293 records the actual Project Python/environment verification failure. The saved Plan structure and prerequisite graph were checked with system Python's standard library; full YAML/parser validation was not run. This has a truthful nonblocking preparation disposition and does not authorize environment repair or bypass a later functional gate.

## Details

### Definition of Done

This Plan is not Done if the bound packet's required output or verification evidence is missing; any encountered issue lacks its typed Concern and disposition; any remaining work lacks explicit child/remainder tasks and appropriate BLOCKS edges; governing sources or authority boundaries were bypassed; or the affected dependent task(s) were not reviewed and updated from the completed result. A blocked or timed-out packet is not Done.
