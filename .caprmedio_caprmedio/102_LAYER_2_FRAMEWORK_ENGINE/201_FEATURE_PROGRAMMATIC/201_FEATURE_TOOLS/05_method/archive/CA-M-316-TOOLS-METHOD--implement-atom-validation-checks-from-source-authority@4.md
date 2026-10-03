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
version: 4
updated_at: "2026-09-24 19:16:49 +0000"
relations:
  method_for:
    - CA-R-1622
    - CA-R-1623
  relates_to:
    - CA-E-506
    - CA-O-087
---
# Summary

Implement Atom validation checks from source authority

## Claim

**to** implement `VALIDATE_ATOMS`, use source-bound deterministic check adapters rather than an independently maintained methodology dictionary.

- reuse compatible canonical Carrier readers, safe parsers, section extractors, **and** Relation resolvers; repair their limitations under the Tool's tests rather than fork competing interpretations.
- make each check identify the exact governing Atom Revisions **and** supported condition; resolve applicable expansions through declared model inputs rather than a fixed list of this Project's names.
- generate **or** derive reusable machine-readable constraints from source declarations **where** supported. a hand-written adapter **must** retain its authority binding **and** tests; changed **or** unsupported authority is a visible coverage gap, **not** permission **to** guess natural-language meaning.
- keep Action implementation **and** interface rendering separable. executable behavior traces **to** CA-O-087; Workflow routing **and** Step bindings remain executor concerns, **not** another procedure inside this Tool.
- use deterministic ordering of diagnostic records **and** preserve source spans; never reorder **or** normalize source bytes **to** hide a failed fidelity check.

### Property contract and coverage

- resolve the selected applicable authority **before** constructing the check inventory. derive a Property contract containing admitted field/section locations, value types, cardinalities, applicability conditions, defaults/override rules, **and** exact source bindings. this contract is a Projection, **not** independently maintained Property authority.
- inventory governing obligations independently of the available adapters. identify mechanically supported checks, semantic-review exclusions, unresolved obligations, **and** missing adapters explicitly; an absent adapter **must not** remove its obligation from the coverage denominator.
- bind source-dependent checks **to** canonical identity, Version, **and** a content digest. a digest mismatch, incomplete source set, contradictory Property declarations, **or** unresolved admission prevents complete coverage; no caller-supplied rule bundle **may** override source authority **or** supply executable code.
- **if** applicable Delivery authority does **not** settle a field spelling, value type, location, **or** required cardinality, report the exact schema gap. do **not** silently infer it from current fixtures, filenames, widespread usage, **or** the implementation.
- do **not** require `cce_version`, `cce_form`, **or** `llm_session_ids` on Atoms. apply the retired-field rule under CA-D-478; CCE authority resolves from the applicable methodology **and** the admitted Claim classification, **not** from those removed fields.

### Boundary libraries

- use Pydantic for strict closed JSON request/result models under CA-M-286, **and** PyYAML for bounded safe YAML parsing **in** `VALIDATE_ATOMS`. reuse compatible shared Carrier splitting rather than recreate it.
- use a safe YAML loader with duplicate-key rejection **and** bounded nesting, aliases, **and** input size. do **not** construct arbitrary objects, execute tags, **or** silently discard unsupported syntax. distinguish malformed input from an unsupported check.
- pin the selected dependencies **in** the root Python configuration under CA-D-250. dependency adoption does **not** relax read-only execution, protected-input handling, source-bound rule coverage, **or** golden-corpus acceptance.
