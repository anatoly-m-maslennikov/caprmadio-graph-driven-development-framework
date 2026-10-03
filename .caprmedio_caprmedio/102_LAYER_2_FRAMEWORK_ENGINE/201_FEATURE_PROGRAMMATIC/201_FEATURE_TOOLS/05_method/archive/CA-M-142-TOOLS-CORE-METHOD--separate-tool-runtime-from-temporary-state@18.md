---
cce_version: cce_1
cce_form: method
subjects:
  governs: "runtime"
  depends_on: []
version: 18
updated_at: 2026-09-15 04:19:10 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a0263a-7510-7672-bce4-58830bc4d184
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  method_for:
    - CA-R-1065
  derived_from:
    - CA-A-057
---

# Separate Tool runtime from temporary state

place CAPRMEDIO-owned persistent operational state under the current Project's
`.caprmedio_runtime/` root. place selected Tool releases **and** stable launchers
under `.caprmedio_runtime/tools/`; keep these carriers reconstructible from
governed source **and** configuration. give each Tool-owned log, session, database,
service-state, **and** resumable-state Carrier an owned runtime descendant. these
Carriers **may** preserve a non-reconstructible operational timeline.

allocate a Tool-owned **and**, **when** concurrency is possible, run-specific
descendant below `.caprmedio_tmp/` for **every** temporary, scratch, staging,
cache, Python bytecode cache, build, intermediate Evaluation, atomic-write intermediate, **and**
interrupted-cleanup Carrier. pass that descendant explicitly **to** temporary-file
APIs **and** configure **every** invoked dependency **to** use it. do **not** use the
repository root, process working directory, source tree, Project control root,
Runtime State root, **or** host temporary location as a fallback.

for atomic replacement, stage below `.caprmedio_tmp/` **and** verify the
required same-filesystem atomicity precondition **before** mutation. stop with a
stable boundary diagnostic **when** safe placement cannot be established. attempt
bounded cleanup, but keep **every** cleanup remnant confined **to** temporary state.

keep both trees non-authoritative. deleting `.caprmedio_tmp/` can lose **only**
disposable state. deleting `.caprmedio_runtime/` **may** require reinstallation **or**
lose operational history **and** resumable progress, but cannot lose a governed
Artifact **or** Project Journal history.
