---
atom_id: CA-P-913
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs:
    continuant:
      - Carrier and Project Delivery Authority
    occurrent:
      - Carrier Authority Update
  depends_on:
    occurrent:
      - CA-P-914
version: 1
updated_at: 2026-08-28 21:11:50 +0400
autonomous_confidence_threshold: 99
relations: {}
---
# Update Carrier and Project Delivery Authority

**when** CA-P-914 is Done, **then** the Assignee **must** make every Carrier-specific Claim, encoding, placement, and concrete Project-folder rule belong exclusively to Delivery with explicit Carrier relations.

## Scope

`((every CA-P-905 frontier entry assigned to CARRIER_AND_PROJECT_DELIVERY) union (every replacement or new authority Atom created from such an entry))`

## Definition of Done

the Task is **not done if** (any Carrier-specific Claim has a Content Role other than Delivery **or** Carrier is not classified as a Base Entity by Delivery authority **or** Carrier is modeled as bearer-dependent `Artifact/Carrier` **or** CARRIES and IS_CARRIED_BY do not explicitly relate Carrier to Artifact Revision in opposite directions **or** file extension is equated with Carrier identity **or** current File Carriers cannot distinguish Markdown, TOML, YAML, or another registered format **or** the open Carrier model forbids a future database Entity Carrier **or** any Folder represented in CAPRMEDIO is not a Directory Carrier for one Relational Artifact **or** CONTAINS or IS_CONTAINED_BY is persisted independently of canonical Carrier nesting **or** immediate Carrier-parent placement does not derive the direct containment pair **or** transitive Carrier ancestry does not derive recursive containment **or** Delivery authority omits frontmatter, main-content section placement and serialization, filename, folder placement, encoding, or Journal Carrier materialization **or** Claim-Subject relation frontmatter fails to serialize exactly one Kind and one Temporal Form without owning the referenced Subject **or** the shared `status` Carrier key is validated before Content Role and Type resolve its qualified Status Property **or** Active Status is placed in a status subfolder **or** any non-Active Status is not placed mechanically in its corresponding status subfolder **or** a Demand Carrier filename does not serialize Demand as `DEMANDS_FROM-<PRODUCER_SCOPE>` **or** an Applicable Methodology projected Atom file creates new Artifact identity, fails to carry its exact source Atom Revision, omits its repository-relative source Carrier path, or changes source Claim authority **or** a monolithic JSON document replaces projected Atom files as the compiled Methodology Carrier **or** concrete CAPRMEDIO folder names remain owned by Core Meta-Model or Local Methodology Configuration instead of Project Delivery Atoms **or** any replaced conflicting authority remains active).

## Details

keep R responsible for required Artifact structure, M for production and transformation methods, E for checks, and D exclusively responsible for every Carrier kind, format, encoding, address, frontmatter and main-content serialization, filename, folder placement, Journal serialization, projected file, and materialization. serialize Claim-Subject relations as `subjects.<governs|depends_on>.<continuant|occurrent>` lists while preserving the semantic relation cardinalities. treat current `.md`, TOML, and YAML forms as File Carrier formats. keep concrete CAPRMEDIO root and hidden-folder names in Project-level D authority: `.caprmedio_framework` stores Methodology and Tool governance; `.caprmedio_<PROJECT_NAME>` stores one governed Project's Artifacts and evidence, including `.caprmedio_caprmedio` for the CAPRMEDIO Project; `.caprmedio_install` stores the installed running Framework Engine files; and `.caprmedio_runtime` stores only ephemeral execution state.
