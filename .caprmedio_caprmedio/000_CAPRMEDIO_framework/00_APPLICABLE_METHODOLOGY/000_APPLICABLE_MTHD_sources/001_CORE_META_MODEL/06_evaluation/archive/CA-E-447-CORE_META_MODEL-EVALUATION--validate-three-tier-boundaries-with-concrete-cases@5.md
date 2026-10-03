---
atom_id: CA-E-447
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - "Atom Tier Validation/concrete cases"
  depends_on:
    continuant:
      - "Atom/Local Tier"
      - "Atom/Global Tier"
      - "Scope Unit"
      - "Atom/Claim/Structural Entity"
      - "Subtree-targeting Atoms"
      - "Atom/Content Role"
      - "Atom/Status"
      - "Evaluation For Relation"
      - "Methodology Source/Expansion Boundary"
      - "Framework Instance Settings"
version: 5
updated_at: "2026-09-14 00:26:45 +0400"
relations:
  evaluation_for:
    - CA-R-1402
    - CA-R-1430
    - CA-R-155
    - CA-R-658
    - CA-R-659
    - CA-R-660
    - CA-R-1431
    - CA-R-680
    - CA-R-1442-CORE_META_MODEL-GENERAL-REQUIREMENT--order-non-project-local-tiers
    - CA-R-1388
    - CA-R-1389
    - CA-R-1390
    - CA-R-1391
    - CA-R-1392
    - CA-R-1393
    - CA-R-1449
    - CA-M-288
    - CA-R-1018
    - CA-R-1429
    - CA-R-1375
    - CA-R-796
    - CA-R-829
    - CA-M-235
    - CA-M-265
    - CA-M-272
    - CA-M-273
    - CA-D-280
    - CA-D-285
    - CA-D-368
    - CA-D-374
---
# Validate three-tier boundaries with concrete cases

## Test case

construct the following fixtures against their exact current source Revisions **and** the applicable authority:

1. classify the complete Claims of CA-R-1402, CA-R-1430, CA-M-235, CA-M-265, CA-E-456, CA-E-446, CA-D-280, **and** CA-D-368. use the exact prefix-versus-suffix cardinality specimen from CA-M-235, a renamed confidence field **and** a string percentage for CA-D-368, **and** the two-Project scenario of CA-E-446. keep the original semantic inputs **and** change **only** the selected concrete choice for **every** representation counterexample.
2. encode the same default **and** target override selections under `authority_modes` **and** under a counterfactual `instance_modes` decoder. **then** remove the default **and** require explicit values for **every** target while retaining one Operator-owned Settings Artifact for one Framework Instance **and** one Project. the counterfactuals are test specimens **and** do **not** authorize source replacement.
3. derive CA-M-265's groups from **all** twelve CA-E-446 targets using ordinary traversal, reversed traversal, **and** a target set; compare those results with a first-target-only implementation. include an unresolved target, an invalid Concern target, qualifying Evaluation **and** Ops targets whose authority the Evaluation checks, a targetless General policy, **and** a targetless Standard case.
4. place Principle, Core, General, **and** Standard at the Project, Core, General, **and** Standard at a direct child **and** grandchild, an external Project Goal, **and** parent-owned Goals for those two descendants. **then** use historical two-tier ranks, a non-Project Principle, a wrong Goal owner, missing parentage, **and** a structural cycle; leave one ordinary tier unoccupied **and** keep two siblings distinct.
5. construct one Active locally owned Current-scope Atom for **every** RMED Content Role, a local Active Plan Atom, a Draft Revision, an Archived Revision, an incoming Active Goal targeting the selected Scope Unit, an outgoing relational Claim targeting a Scope Unit outside the selected subtree, an inherited Claim targeting an ancestor, **and** one Active Requirement owned by **and** targeting a descendant Scope Unit. independently reassign the four local RMED tiers while retaining their complete Claims **and** structural targets. repeat with a complete empty frontier, an incomplete frontier, contradictory ownership, unresolved ancestry, **and** an unresolved required Claim Structural Entity.
6. attempt Project Configuration replacement of one CORE_META_MODEL Claim at **every** ordinary tier, including replacement by a numerically higher-ranked local Claim; compare with an addition at one explicitly active source-authorized variation point.
7. serialize ordinary Core, General, **and** Standard Atoms with `CORE`, `GENERAL`, **and** omission, **then** use `STD`, `STANDARD`, `DETAIL`, **and** combined tier segments. retain `CORE_META_MODEL` as the owner name, use the external Project Goal grammar, **and** keep concrete Goal, Objective, **and** Task identity, target, **and** sequence grammar intact.
8. classify the Principle, Core, General, **and** Standard definition Atoms from their complete Claims; **then** add Requirement tier-parent edges based on their defined values **or** between same-tier Requirement peers. use an independently replaceable settings definition **and** unrelated concrete serialization obligation merged into one candidate, **and** a candidate classified from an old filename **only**.

## Acceptance criteria

the first classification fixture yields Core, General, Standard, General, General, Standard, Standard, **and** Standard respectively. a concrete encoding change preserves its higher semantic contract while failing the unchanged concrete authority; the explicit-only mode policy preserves settings identity **and** ownership while failing CA-R-1430. complete target grouping yields Er **and** Ed for CA-E-446, accepts qualifying Evaluation **and** Ops targets under CA-R-1018 **without** inventing Er/Em/Ed membership for them, rejects unresolved **or** invalid targets including Concern, permits a legitimate targetless Core **or** General policy **without** invented groups, **and** rejects a targetless Standard case. structural fixtures follow the governing mappings **without** tier compression **or** sibling ownership merging. the Active RMED Subtree-targeting Atoms selected by the alias `spec` remain exactly the four local RMED Atoms, the incoming Goal, **and** the descendant Requirement through **every** tier-only reassignment; the outgoing Claim, ancestor-targeting inherited Claim, Plan Atom, Draft Revision, **and** Archived Revision are excluded. empty input is accepted **only** **when** complete, **and** failed binding remains identified **and** unresolved. source replacement fails at **every** tier, **and** a permitted addition respects its exact variation point. **only** canonical filename cases pass; all four constitutive tier definitions classify Core **without** fabricated parentage. mixed independent Claims **and** evidence-free classifications fail for explicit admission review.

## Failure disposition

identify the exact source Revision, fixture, expected result, **and** observed counterexample; restore the invalid fixture's governed source, owner, binding, classification evidence, relation, **or** representation **and** rerun that fixture. a repair **must not** rewrite frozen historical evidence, invent authority, transfer source ownership, **or** report an unexecuted operational case as passed.
