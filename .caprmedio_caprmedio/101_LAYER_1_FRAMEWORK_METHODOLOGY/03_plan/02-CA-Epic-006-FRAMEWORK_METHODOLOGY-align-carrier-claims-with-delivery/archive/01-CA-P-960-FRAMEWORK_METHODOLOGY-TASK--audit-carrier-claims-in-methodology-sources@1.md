---
atom_id: CA-P-960
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs:
    occurrent:
      - Atom/Content Role
  depends_on:
    continuant:
      - Atom/Claim
      - Atom/Claim/Scope
      - Carrier
      - Atom/Local Tier
      - Atom/Revision
      - Autonomous Confidence Threshold
version: 1
updated_at: "2026-09-10 13:41:47 +0400"
autonomous_confidence_threshold: 99
relations: {}
---
# Audit Carrier Claims in methodology sources

the Assignee **must** produce a complete, source-bound inventory of Carrier-related Claims **and** their current Content Roles across active methodology RMED Atoms.

## Claim Scope

(**all** active RMED Atoms **in** CORE_META_MODEL **or** LOCAL_CONFIGURATION)

## Definition of Done

the Task is **not** Done **if** (an active source Atom is omitted from the review **or** a Carrier-related Claim has no exact source identity, Version, path, **and** content digest **or** an inventory disposition relies **only** on a filename, Summary, keyword match, **or** Local Tier **or** existing D authority **and** mixed Claims are omitted).

## Details

review the complete Claim of **every** active source Atom. classify candidates as a Carrier specification, a mixed semantic **and** Carrier Claim, an existing D owner, **or** a justified non-D Claim. distinguish required meaning **and** cardinality (R), reusable procedure **or** writing style (M), falsifiable check (E), **and** storage, representation, **or** placement (D).

the earlier 698-Atom audit is a starting observation, **not** a fixed membership count. refresh source membership **and** bytes at execution time. examine filenames, Identifier grammar, folder placement, YAML **and** TOML keys, timestamp formats, Type tokens, document section placement, **and** Projection payload encoding. including a Carrier reference does **not** by itself make a Claim D.

seed examples include CA-R-165, CA-R-728, CA-R-737, CA-R-1304, CA-R-1305, CA-R-1369, GOV-323, GOV-362, GOV-373, GOV-383, GOV-676, **and** GOV-760. resolve abbreviated GOV labels **to** exact current identities; do **not** use the abbreviations as relation targets. include the Type-admission Claims that also prescribe Carrier tokens. check CA-D-270 **and** CA-D-310 as existing encoding owners.

this Task changes no source Atom. the entire Epic excludes Draft **and** Archived Claim normalization, Project-level Content Role normalization, selected Settings changes, source-owner migration, Tool implementation, installed artifacts, **and** generated APPLICABLE_METHODOLOGY. historical Carriers remain evidence, **not** active repair targets. directory sequence is navigational; do **not** invent a dependency on Epic 005 closure. refresh **any** affected inventory record **after** intervening source changes.
