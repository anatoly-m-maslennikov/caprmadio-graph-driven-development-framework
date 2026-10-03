---
atom_id: CA-P-965
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
relations:
  depends_on:
    - CA-P-964
---
# Validate Carrier Content Role normalization

the Assignee **must** demonstrate source-level closure of Carrier Content Role normalization across CORE_META_MODEL **and** LOCAL_CONFIGURATION.

## Claim Scope

(**all** active RMED Atoms **in** CORE_META_MODEL **or** LOCAL_CONFIGURATION **and** the disposition, preservation, **and** reference evidence produced by CA-P-960 through CA-P-964)

## Definition of Done

the Task is **not** Done **if** (an active source Atom has no final review disposition **or** a Carrier specification remains outside D **without** an admitted role-boundary justification **or** a mixed Claim loses its original semantic contribution **or** a Claim has duplicate authority owners **or** a changed Atom fails current identity, Revision, Subject, Scope, tier, **or** Carrier rules **or** a new blocking source conflict remains **or** downstream work is presented as completed **without** execution evidence).

## Details

refresh the complete final source set, including additions **and** retirements; do **not** validate **only** the original keyword matches. compare **every** original clause against its surviving owner **and** **every** resulting Atom against its applicable R, M, E, **and** D authority. verify that **all** four Content Roles remain represented according **to** their contributions **and** that Local Tier has **not** substituted for Content Role.

check the original R165 / D270 case, Projection timestamp encoding, Identifier grammars, directory bindings, settings-field representations, Type-token mappings, **and** mixed settings policies. use existing deterministic checks **where** applicable **and** explicit reviewed evidence for semantic classification; do **not** report passing syntax checks as proof of correct role classification.

the final report **must** list exact additions, revisions, replacements, retirements, reference repairs, preserved prior Revisions, unresolved legacy diagnostics, **and** downstream impacts. keep Project-wide normalization, generated APPLICABLE_METHODOLOGY rebuilds, Tool/runtime changes, selected Settings changes, Journal work, commits, **and** pushes outside this Epic. do **not** declare those surfaces aligned merely because source normalization passes.

mark the Epic Done **only** **after** **all** six Tasks satisfy their Definitions of Done; do **not** mark **any** Task Done **when** this plan is created.
