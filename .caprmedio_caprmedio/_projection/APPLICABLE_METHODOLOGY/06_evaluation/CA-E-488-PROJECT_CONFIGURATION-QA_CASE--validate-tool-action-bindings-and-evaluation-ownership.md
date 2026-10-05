---
subjects:
  governs: "Tool"
  depends_on:
    - "Action"
    - "Workflow"
    - "Step"
    - "Methodology"
    - "Methodology Source"
    - "Scope Unit"
    - "Atom/Content Role: Operations"
    - "Atom/Content Role: Evaluation"
    - "Atom/Content Role: Implementation"
version: 6
updated_at: "2026-10-02 20:16:06 +0400"
relations:
  evaluation_for: [CA-R-1515, CA-R-1516, CA-R-1517, CA-R-1518]
atom_id: "CA-E-488"
content_role: "Evaluation"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/06_evaluation/CA-E-488-PROJECT_CONFIGURATION-QA_CASE--validate-tool-action-bindings-and-evaluation-ownership.md
  source_atom_id: CA-E-488
  source_atom_revision: 6
  source_sha256: a7e7aba272be20d9a9ffadfd4fe76840290d00abecfa2113a49d98d1f564423d
  original_relations_sha256: 8a86c5a55a2f9aee1e1111d08b0f0b2254ec89520b80843ce2927cce497d0cd5
---
# Summary

Validate Tool Action bindings and Evaluation ownership

## Scope

a CAPRMEDIO Tool's methodology binding **and** Evaluation responsibility.

## Claim

the Evaluation of a CAPRMEDIO Tool's methodology binding **must** check the canonical Action owner, binding cardinality, **and** division of Evaluation responsibility under CA-R-1515-PROJECT_CONFIGURATION-GENERAL-REQUIREMENT--keep-canonical-actions-and-workflows-in-methodology, CA-R-1516-PROJECT_CONFIGURATION-REQUIREMENT--bind-each-tool-to-one-methodology-action, CA-R-1517-PROJECT_CONFIGURATION-REQUIREMENT--keep-tool-operational-authority-outside-its-own-subtree, **and** CA-R-1518-PROJECT_CONFIGURATION-GENERAL-REQUIREMENT--separate-methodology-and-tool-evaluation-responsibilities.

## Details

### Cases and expected results

- the Tool implements **`=1`** resolvable applicable Action owned by a methodology source outside the Tool's subtree: pass the binding check.
- the Tool has **`=0`** **or** **`>1`** implemented Action bindings, an unresolved definition, **or** a copied operational definition owned by the Tool: fail.
- an implementation reference targets an O Atom owned by the Tool's Scope Unit **or** a descendant: fail. a methodology Evaluation checking its own O definition **must not** fail this Tool-only containment rule.
- Tool Evaluations check the Tool's realization of its Action while methodology Evaluations check the operational definitions: pass the responsibility check.
- a Tool Evaluation independently owns Action **or** Workflow definition-validity rules: fail for misplaced authority; invoking an existing methodology check does **not** transfer that authority.
- a Workflow **contains** an unresolved Step Action **or** an unbounded retry loop: report the defect against the methodology definition through its methodology Evaluation, rather than silently repairing the Workflow inside the Tool's specification.

report binding conformance separately from actual Implementation results. valid ownership **and** references alone **must not** be reported as proof that the Tool works **or** that **all** indirect cycles are absent.
