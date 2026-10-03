---
atom_id: CA-P-110
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - Applicable Methodology
    occurrent:
      - Applicable Methodology Compilation
  depends_on:
    occurrent:
      - CA-P-109
version: 7
updated_at: 2026-08-27 21:40:42 +0400
autonomous_confidence_threshold: 99
relations: {}
---
# Compile the First Applicable Methodology

**when** CA-P-109 and CA-P-107 version 8 are Done and the exact three-Source-Layer carrier topology is present, **then** the Assignee **must** implement and use `COMPILE_APPLICABLE_METHODOLOGY` to compile the first conflict-gated generated projected RMEDO Atom Carrier tree from CORE_META_MODEL and LOCAL_CONFIGURATION with zero INSTALLED_EXTENSIONS contribution.

## Scope

`((the migrated CORE_META_MODEL Carriers) union (the empty INSTALLED_EXTENSIONS Source Layer) union (the migrated LOCAL_CONFIGURATION Carriers) union (the exact CA-P-107 version 8 compiler authority) union (the COMPILE_APPLICABLE_METHODOLOGY RMED authority, executable Carrier, and tests) union (the CA-P-108 predicted generated projected RMEDO Atom Carriers) union (the dry-run conflict report) union (the generated Applicable Methodology Carriers if every conflict is durably approved))`

## Definition of Done

the Task is **not done if** (`COMPILE_APPLICABLE_METHODOLOGY` or its minimal RMED authority and tests is absent **or** dry-run does not select only current active RMEDO Source Atom revisions from CORE_META_MODEL and LOCAL_CONFIGURATION **or** INSTALLED_EXTENSIONS is not empty and non-contributing **or** dry-run omits a duplicate selected Atom identity, unresolved replacement, incompatible retained Candidate, unresolved priority, or output-path collision **or** any reported conflict lacks one exact durable Operator approval in LOCAL_CONFIGURATION bound to its conflict ID and source-frontier digest **or** unapproved conflict produces or replaces output **or** generated output is not a projected RMEDO Atom Carrier tree in the canonical role directories **or** generated output contains CAP, IMPLEMENTATION, Draft, archive, monolithic JSON methodology, or a persistent GOVERNS or DEPENDS_ON Index Carrier **or** a projected Carrier differs from its source beyond `projection.source_carrier_path` **or** any source Carrier changes **or** staged replacement cannot roll back completely **or** identical resolved Source Frontiers produce different output **or** removing generated output Carriers prevents complete regeneration **or** generated output gains independent authority **or** any consumer is rewritten before CA-P-113).

## Details

implement the deterministic Tool in the current FRAMEWORK_ENGINE PROGRAMMATIC/TOOLS Delivery topology and govern it in the corresponding `.caprmedio_caprmedio` Tool Scope. dry-run first. use `003_LOCAL_CONFIGURATION/applicable_methodology_conflict_approvals.toml` as the native durable approval Carrier outside the eligible RMEDO candidate directories, so an approval does not recursively change the source-frontier digest to which it is bound. if dry-run reports any conflict without one exact current approval, keep this Task active and do not create or replace generated output. derive GOVERNS and DEPENDS_ON only on demand. defer every consumer rewrite and representative retrieval test to CA-P-113.

## Completion Record

PASS. `COMPILE_APPLICABLE_METHODOLOGY` and CA-R-1240, CA-M-226, CA-E-380, and CA-D-254 implement the governed conflict-gated compiler boundary. eight Tool tests pass. the live dry-run selected 527 current active RMEDO Source Atom revisions from CORE_META_MODEL and LOCAL_CONFIGURATION, confirmed empty INSTALLED_EXTENSIONS, calculated source-frontier digest `da419d079ba666c852aaaf6abfa482cc0f3fac48a4ebc315a309b8695470cd07`, and reported zero conflicts. apply generated 478 Requirement, 26 Method, 18 Evaluation, five Delivery, and zero Ops projected Carriers with tree digest `e946d378a384bd34acaf634afde0d1f5af413d922923ff7ad43a1d949545f830`. every projection mapping resolves to its exact Source Carrier, and removing that mapping restores the Source Carrier bytes exactly. an identical live rerun and fresh disposable-root regeneration produced the same frontier and tree digests. no Source Carrier, consumer Carrier, persistent Subject Index, monolithic methodology JSON, CAP output, Implementation output, Draft, or archive was produced or changed. [CA-P-110 compilation evidence](../execution_evidence/CA-P-110-applicable-methodology-compilation.projection.json) records the proof.
