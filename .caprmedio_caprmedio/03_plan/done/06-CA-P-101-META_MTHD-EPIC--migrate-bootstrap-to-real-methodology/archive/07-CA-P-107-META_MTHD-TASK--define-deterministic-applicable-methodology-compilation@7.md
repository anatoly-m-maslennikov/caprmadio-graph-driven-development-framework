---
atom_id: CA-P-107
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
      - CA-P-106
version: 7
updated_at: 2026-08-27 21:13:36 +0400
autonomous_confidence_threshold: 99
relations: {}
---
# Define Deterministic Applicable Methodology Compilation

**when** CA-P-106 is Done, **then** the Assignee **must** define one deterministic CORE_META_MODEL-owned compilation authority for a generated projected RMEDO Atom Carrier tree from CORE_META_MODEL and LOCAL_CONFIGURATION, while retaining INSTALLED_EXTENSIONS as an empty non-contributing structural Source Layer.

## Scope

`((all active and draft CORE_META_MODEL Atoms and Carriers that govern projected Atom Carrier selection, deterministic ordering, projection-only frontmatter, output path and filename rules, on-demand GOVERNS and DEPENDS_ON projections, compilation Evaluations, deletion and regeneration, and subject- or process-scoped retrieval) union (the exact empty INSTALLED_EXTENSIONS manifest and LOCAL_CONFIGURATION selection, replacement, priority, and compatibility-resolution inputs referenced by that authority))`

## Definition of Done

the Task is **not done if** (any generic compilation authority is owned outside CORE_META_MODEL **or** LOCAL_CONFIGURATION owns any generic compilation rule instead of only Project-owned selection and resolution inputs **or** the three structural Source Layers are not CORE_META_MODEL, INSTALLED_EXTENSIONS, and LOCAL_CONFIGURATION in that order **or** the compilation contract can omit CORE_META_MODEL or LOCAL_CONFIGURATION **or** INSTALLED_EXTENSIONS contributes any Source Atom revision **or** a selected Carrier has Content Role outside (REQUIREMENT, METHOD, EVALUATION, DELIVERY, OPS) **or** a selected Carrier is a CONCERN, ANALYSIS, PLAN, IMPLEMENTATION, Draft, or archived revision **or** selection does not resolve one current revision per Atom identity **or** dry-run does not report the complete deterministic conflict set and proposed Candidate resolutions **or** an approval is not durably recorded in LOCAL_CONFIGURATION and bound to the exact conflict and source-frontier digest **or** a stale, partial, missing, ambiguous, or mismatched approval can produce or replace output **or** structural Source Layer order resolves a conflict **or** a projected Carrier does not preserve its source Atom identity, revision, Claim content, and source frontmatter except for the exact projection mapping **or** the projection mapping cannot resolve to an authoritative source Carrier **or** generated output contains a non-RMEDO role directory, Draft, archive, monolithic JSON methodology, or persistent Subject Index Carrier **or** the compiler requires LLM inference **or** generated Applicable Methodology can gain independent authority **or** deleting generated RMEDO output directories cannot permit complete regeneration **or** this Task implements or executes CA-P-110 Tool work).

## Details

place the generic compiler contract, deterministic ordering, projection-only frontmatter, output path and filename rules, on-demand GOVERNS and DEPENDS_ON projections, and compilation Evaluations in CORE_META_MODEL without materializing generated Carriers. treat INSTALLED_EXTENSIONS as an empty non-contributing structural Source Layer and LOCAL_CONFIGURATION as Project-owned selection and resolution inputs only. define the `COMPILE_APPLICABLE_METHODOLOGY` Tool contract for CA-P-110 implementation: dry-run detects every conflict and proposes Candidate resolutions, and apply uses only durable Local Configuration Operator approvals bound to the exact conflict and source-frontier digest before staged atomic replacement of generated RMEDO output directories only. define subject- or process-scoped retrieval to derive matching GOVERNS paths and add DEPENDS_ON authority only through prerequisite closure. defer Tool implementation and first final-carrier compilation to CA-P-110.

## Task Scope Resolution

the Assignee used CA-P-102 through CA-P-106 evidence and their accepted successors. CA-R-1224 selects CORE_META_MODEL followed by LOCAL_CONFIGURATION as the only contributing Source Layers. CA-R-1225 and CA-R-1221 establish that INSTALLED_EXTENSIONS is empty and contributes zero Candidates. CA-R-1226 defines the one-revision Project Customization boundary, and CA-R-1227 selects no local Tool, MCP, or App mode. [CA-P-107 generated Atom Carrier tree authority](../execution_evidence/CA-P-107-generated-atom-carrier-tree-authority.projection.json) records the projected-tree contract, Atom revisions, and deferred CA-P-110 Tool boundary.

## Completion Record

PASS. CA-R-1229 requires the exact projection-only relative Source Carrier mapping. CA-R-1230 forbids persistent Subject Index Carriers. CA-M-224 defines the deterministic generated RMEDO Atom Carrier tree and deferred `COMPILE_APPLICABLE_METHODOLOGY` Tool contract. CA-M-225 defines on-demand Subject and Process retrieval. CA-E-379 defines the falsifying compilation validation. CA-D-253 binds the source and generated output tree locations. No generated Applicable Methodology Carrier, Tool, source modification, consumer change, or monolithic methodology JSON was created, and all Definition-of-Done conditions pass at 99 percent execution confidence.
