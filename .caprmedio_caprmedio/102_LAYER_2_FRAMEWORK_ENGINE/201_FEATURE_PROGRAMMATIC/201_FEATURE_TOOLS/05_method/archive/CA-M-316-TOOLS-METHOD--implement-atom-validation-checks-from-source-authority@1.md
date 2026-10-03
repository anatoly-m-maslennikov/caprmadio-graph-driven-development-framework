---
atom_id: CA-M-316
content_role: Method
type: Method
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: method
subjects:
  governs: "Tool/VALIDATE_ATOMS"
  depends_on:
    - "Tool"
    - "Atom"
    - "Atom/Property"
    - "Evaluation"
    - "Workflow"
    - "Step"
    - "Action"
    - "Single Source of Truth"
version: 1
updated_at: "2026-09-23 23:38:45 +0000"
relations:
  method_for:
    - CA-R-1622
    - CA-R-1623
  relates_to:
    - CA-E-506
    - CA-O-080
---
# Summary

Implement Atom validation checks from source authority

## Claim

**to** implement `VALIDATE_ATOMS`, use source-bound deterministic check adapters rather than an independently maintained methodology dictionary.

- reuse compatible canonical Carrier readers, safe parsers, section extractors, **and** Relation resolvers; repair their limitations under the Tool's tests rather than fork competing interpretations.
- make each check identify the exact governing Atom Revisions **and** supported condition; resolve applicable expansions through declared model inputs rather than a fixed list of this Project's names.
- generate **or** derive reusable machine-readable constraints from source declarations **where** supported. a hand-written adapter **must** retain its authority binding **and** tests; changed **or** unsupported authority is a visible coverage gap, **not** permission **to** guess natural-language meaning.
- keep Workflow routing, Step bindings, check implementation, **and** interface rendering separable. executable branches trace **to** the referenced O graph, **not** another authored procedure.
- use deterministic ordering of diagnostic records **and** preserve source spans; never reorder **or** normalize source bytes **to** hide a failed fidelity check.
