---
atom_id: CA-P-969
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    occurrent:
      - "Applicable Methodology Compilation"
  depends_on:
    continuant:
      - "Core Meta-Model"
      - "Applicable Methodology/Carrier"
      - "Applicable Methodology/Carrier Set"
      - "Applicable Methodology/Projected Atom Carrier/Source Carrier Path"
      - "Atom/Content Role: Delivery"
      - "Carrier"
      - "Confidence Threshold"
version: 1
updated_at: "2026-09-11 02:58:19 +0400"
relations:
  depends_on:
    - CA-P-968
---
# Complete compilation Delivery Atoms

the Assignee **must** complete the generic Delivery authority for Applicable Methodology compilation **in** CORE_META_MODEL against the accepted Requirement **and** Method coverage.

## Scope

(Delivery authority for Applicable Methodology compilation **in** CORE_META_MODEL, including necessary new **or** replacement Delivery Atoms)

## Definition of Done

the Task is **not** Done **if** ((a D gap accepted from CA-P-966 remains unaddressed) **or** (the source/output boundary, output location binding, projected file representation, **or** source-link encoding lacks an unambiguous Delivery owner) **or** (source **and** projected Carriers can become independent competing authority) **or** (the generic Carrier contract hard-codes the current Project's Extension names **or** Local Configuration contents) **or** (a selected Project Implementation Folder binding is changed) **or** (a changed prior Revision is lost) **or** (an edit exceeds this Claim Scope)).

## Details

reuse CA-D-253, CA-D-305, CA-D-306, **and** CA-D-313; they already cover source/output separation, derived identity, projected RMEDO files, **and** repository-relative source paths. add independent Carrier specifications **only** **where** the inventory demonstrates a gap.

distinguish the Implementation Folder binding from the rules for filenames, frontmatter, main-content placement, source references, **and** the delivered Projection itself. generic D authority explains how an instance supplies **and** resolves its target; this Task does **not** move current folders **or** change their selected bindings. preserve projected Atom files rather than replacing the methodology with one monolithic JSON file.
