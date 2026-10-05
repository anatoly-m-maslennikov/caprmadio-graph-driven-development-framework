---
subjects:
  governs: "Step/Agentic Execution Context"
  depends_on:
    - "Action/Execution Kind"
    - "Action"
    - "Step"
    - "Workflow"
    - "Step Run"
    - "Operator"
version: 4
updated_at: "2026-10-02 20:16:06 +0400"
relations: {"evaluation_for": ["CA-R-1526", "CA-R-1527", "CA-R-1509"]}
atom_id: "CA-E-495"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-495-CORE_META_MODEL-QA_CASE--validate-action-kinds-and-step-contexts.md
  source_atom_id: CA-E-495
  source_atom_revision: 4
  source_sha256: 4c986410371e9625333364147ca0dfec120378ec5d61c525cc69e99be53512f5
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Validate Action kinds and Step contexts

## Scope

Action Execution Kind **and** Agentic Step Execution Context.

## Claim

the Evaluation **must** check that Action Execution Kind **and** Agentic Step Execution Context remain distinct **and** support reuse **without** duplicate definitions.

## Details

- a Programmatic Action interacts with the Operator through code **without** AI judgment: accept Programmatic classification.
- code delegates the declared responsibility's judgment **to** an AI Agent: require Agentic classification rather than classifying by the surrounding code.
- two Steps invoke the same Agentic Action **in** Integrated **and** Isolated contexts with valid bindings: accept the shared Action identity **and** distinct invocation contexts.
- one Workflow mixes Programmatic, Integrated Agentic, **and** Isolated Agentic Steps: accept **without** a Workflow-wide context classification.
- missing **or** unavailable required context: block execution admission; do **not** silently select a substitute **or** classify a well-formed definition as malformed merely because a worker is unavailable.
- a Tool call appears inside an Agentic Step Run: retain **`=1`** declared Action for that Step rather than inferring another Step from the call.
- choosing Isolated grants additional permission, suppresses required Operator input, **or** permits concurrent mutations automatically: reject.

use definition fixtures **and** invocation evidence. these checks do **not** claim that an executor Implementation has been tested.
