---
subjects:
  governs: "Projection/Type: Implementation Overview"
  depends_on:
    - "Projection"
    - "Atom"
    - "Artifact/Revision"
    - "Implementation Binding"
    - "Journal"
    - "Implementation"
    - "Verification"
project_graph_state:
  artifacts:
    enabled_types:
      - implementation_record
version: 22
updated_at: 2026-09-15 05:51:38
relations:
  relates_to:
    - CAPRMEDIO-GOV-REQU-313
    - CAPRMEDIO-META-REQU-105
---
# Register the Implementation Overview Projection

Implementation Overview **means** the internal Type value under Projection that presents current realization, coverage, source-to-target bindings, relevant provenance, **and** unresolved gaps derived from its declared source frontier.

the Projection declares the exact normative Atom, native-target, provenance, **and** **any** registered implementation-lineage frontier it represents. its Implementation Bindings derive from the shared Project Journal under CAPRMEDIO-META-REQU-105. regeneration replaces its rendered content **without** converting it into an Atom **or** granting it authority over the Journal, native project, normative specification, Operations evidence, **or** Verification. historical implementation event records remain **in** the Journal; this Projection presents the current view **without** replacing those records.

its storage **and** retention policy is configured separately. a generated runtime copy **may** be disposable; a committed current view **may** be reviewable history. the two storage choices do **not** change the Projection's semantic role.

## Rationale

the predecessor incorrectly bundled Change Plan **and** Implementation Record under one Implementation-role Projection rule. the split preserves the record while routing Change Plan **to** the new Plan Atom family.

the historical name Implementation Record **in** this rationale referred **to** the current-state Projection now named Implementation Overview; the name change distinguishes that view from the implementation event records retained **in** the Journal.
