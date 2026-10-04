---
atom_id: CA-P-1176
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: "Project session metadata corpus"
  depends_on:
    - "Project"
    - "Operations"
    - "Atom/Content Role: Plan"
version: 1
updated_at: "2026-10-04 06:57:00 +0400"
relations:
  is_decomposition_of:
    - CA-P-1125
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

Enumerate the project session metadata corpus

## Objective

The assigned AI Agent must enumerate the permitted Project-relevant local session metadata corpus, reconcile the seven known app sessions, and save a durable retrieval manifest within <=15 minutes. This is the substantive corpus-discovery leaf, not another generic preflight and not body-content harvest. Inherit CA-P-1117 permissions and 90% confidence policy through CA-P-1125.

### Exact inputs and ownership

- Frozen evidence window: [2026-09-04 05:54:15 +0400, 2026-10-04 05:54:15 +0400). An older-created session can contain in-window turns; neither creation time, local modification time nor current app updated_at independently excludes it.
- Completed initial slice: `done/02-CA-P-1175-TASK--bind-the-first-seven-session-metadata-sources.md` in this same container, v2. It carries seven verified app Project IDs mapped to nine native files, including duplicate continuations. Supplemental JSON: `.caprmedio_tmp/CA-P-1117/manifest-CA-P-1175.json`; original app listing: `.caprmedio_tmp/CA-P-1117/preflight-CA-P-1150-app-metadata.json`. Use the durable Plan if the disposable copies are unavailable.
- Native metadata roots verified to exist: `/Users/am/.codex/sessions` and `/Users/am/.codex/archived_sessions`. Their metadata records and filenames are read-only inputs; no credential, denied path or unrelated Project body may be consumed.
- Exact current Project cwd: `/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework`. CA-P-1175 positively links historical metadata cwd suffixes `dset-loops-framework` and `caprmadio-vibe-coding-to-production-framework` to this Project through exact known IDs and current app projectId `f02ccd27-26aa-4d95-8be7-6508b3986699`. These aliases are observed evidence only, never restored Project/runtime bindings. Alias-only additional rows are candidates requiring explicit identity/relevance validation, not automatically accepted unrelated content.
- Live external Project Goal v13 and all active Project Principles, including legacy Actor Principles CA-P-032 v5 and CA-P-033 v9, plus permission Core CA-P-034 v6.
- Current core source authority: CA-R-1589 v4, CA-R-1580 v4, CA-D-460 v6, CA-D-470 v7, CA-D-481 v4 and CA-D-461 v6 under `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL`. Re-read changed sources. CA-C-293 is an existing nonblocking environment limitation: use system Python standard-library metadata checks, no uv/install/cache retries.
- Owned results: this leaf's result and Done placement; the parent CA-P-1125 corpus/frontier roll-up; durable `.caprmedio_caprmedio/02_analysis/CA-A-905-ANALYSIS_RPRT--inventory-the-session-evidence-corpus.md` (ID confirmed unused when this leaf was created); supplemental `.caprmedio_tmp/CA-P-1117/manifest-CA-P-1176.json`; narrowly required remainder Plans/Concerns and readiness edges. No O/RMED authoring, implementation or Docker work is included.

### Bounded execution and required output

1. Make one filename enumeration across the two exact native roots, stopping at 10,000 files or 60 seconds. Read only each candidate's first session_meta JSONL record with a 128 KiB per-file and 256 MiB aggregate read bound; do not parse or expose message bodies. Record actual count, limits, malformed/unreadable records and exact unfinished filename frontier. Match permitted Project metadata and known IDs before any later content access.
2. Retain every admitted session ID, local continuation path, declared creation timestamp/cwd, observed file size/modification time and relevance basis. Distinguish exact current-cwd matches, positively verified historical-ID matches, alias-only candidates awaiting validation and excluded unrelated metadata. Group continuation candidates by session ID without dropping overlapping or stale files by assumption. Subagent/session-source metadata remains explicit so primary Operator conversations can be distinguished from derived worker records later.
3. If archived app discovery is needed to bind sources absent from the native/known set, make at most one `mcp__codex_app__list_archived_threads({source: "codex", hostId: "local", limit: 20})` request. Retain exact Project matches, actual nextCursor and limitations. Do not call read_thread or read any message content in this leaf. A returned continuation cursor is unfinished discovery, not a completed corpus claim.
4. Save CA-A-905 with the frozen window, full relevant/candidate metadata manifest, source availability, discovery counts/bounds, continuation dispositions, current authority revisions and reuse mapping to Harvest Epic 014. The Analysis is the durable manifest source; supplemental JSON is not the sole completion evidence. Unknown event-window membership remains an explicit per-source body/cursor harvest frontier, not a fabricated missing-evidence disposition.
5. Reassess CA-P-1125 from observed discovery coverage. It may become Done only if its required corpus output is complete and every actual metadata-discovery remainder is completed or has a justified unavailable-evidence disposition; otherwise keep it Active and create concrete <=15-minute leaves for the exact remainder. Body/event processing belongs to CA-P-1126–1129 and does not by itself require another generic metadata preflight. Update their exact source bindings and readiness gates from the manifest, without claiming substantive harvest done or enabling downstream implementation early.

### Functional verification and next frontier

Compare saved Analysis and supplemental JSON rows with the admitted metadata set and the seven-ID initial slice; every relevant ID must have a source or truthful unavailable disposition, and every continuation file must remain represented. Every local path must exist and its first session_meta identity must match; any app pagination cursor must be copied from the actual response. Verify the window, unique CA-A-905 identity, the immediate decomposition target, required body sections, status placement and acyclic explicit prerequisite/decomposition graph. Record exclusions as metadata categories without retaining unrelated Project content.

The expected next execution frontier is actual bounded content harvest under CA-P-1126–1129 using this manifest: <=100 relevant human/assistant messages per packet with an exact source/event/cursor boundary. Do not generate an endless chain of unbound preflights. Any actual discovery limit, inaccessible primary evidence or unresolved relevance choice gets its typed Concern, bounded next leaf and truthful parent state.

## Details

### Definition of Done

This leaf is not Done if the native enumeration lacks counts/bounds and an exact frontier; an admitted or candidate metadata source disappears without disposition; the seven known IDs are lost; the durable CA-A-905 manifest is missing; source completeness is inferred only from size/timestamps/ID; unrelated bodies or denied data are accessed; required unfinished discovery lacks a bounded remainder and BLOCKS edges; the parent or harvest gates overstate coverage; verification fails; or execution exceeds <=15 minutes without narrower unfinished Plans.

