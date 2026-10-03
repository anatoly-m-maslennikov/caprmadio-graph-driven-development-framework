---
atom_id: CA-M-316
content_role: Method
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
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
version: 6
updated_at: "2026-10-01 21:46:55 +0400"
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

## Scope

implementation of Atom validation checks from source authority for `VALIDATE_ATOMS`.

## Claim

**to** implement `VALIDATE_ATOMS`, use source-bound deterministic check adapters rather than an independently maintained methodology dictionary.

- reuse compatible canonical Carrier readers, safe parsers, section extractors, **and** Relation resolvers; repair their limitations under the Tool's tests rather than fork competing interpretations.
- make each check identify the exact governing Atom Revisions **and** supported condition; resolve applicable expansions through declared model inputs rather than a fixed list of this Project's names.
- generate **or** derive reusable machine-readable constraints from source declarations **where** supported. a hand-written adapter **must** retain its authority binding **and** tests; changed **or** unsupported authority is a visible coverage gap, **not** permission **to** guess natural-language meaning.
- keep Action implementation **and** interface rendering separable. executable behavior traces **to** CA-O-087-CORE_META_MODEL-ACTION--check-atoms; Workflow routing **and** Step bindings remain executor concerns, **not** another procedure inside this Tool.
- use deterministic ordering of diagnostic records **and** preserve source spans; never reorder **or** normalize source bytes **to** hide a failed fidelity check.

### Property contract and coverage

- resolve the selected applicable authority **before** constructing the check inventory. derive a Property contract containing admitted field/section locations, value types, cardinalities, applicability conditions, defaults/override rules, **and** exact source bindings. this contract is a Projection, **not** independently maintained Property authority.
- inventory governing obligations independently of the available adapters. identify mechanically supported checks, semantic-review exclusions, unresolved obligations, **and** missing adapters explicitly; an absent adapter **must not** remove its obligation from the coverage denominator.
- bind source-dependent checks **to** canonical identity, Version, **and** a content digest. a digest mismatch, incomplete source set, contradictory Property declarations, **or** unresolved admission prevents complete coverage; no caller-supplied rule bundle **may** override source authority **or** supply executable code.
- **if** applicable Delivery authority does **not** settle a field spelling, value type, location, **or** required cardinality, report the exact schema gap. do **not** silently infer it from current fixtures, filenames, widespread usage, **or** the implementation.
- do **not** require `cce_version`, `cce_form`, **or** `llm_session_ids` on Atoms. apply the retired-field rule under CA-D-478; CCE authority resolves from the applicable methodology **and** the admitted Claim classification, **not** from those removed fields.

### Boundary libraries

- use Pydantic for strict closed JSON request/result models under CA-M-286-PROGRAMMATIC-CORE-METHOD--validate-untrusted-structured-data-with-pydantic, **and** PyYAML for bounded safe YAML parsing **in** `VALIDATE_ATOMS`. reuse compatible shared Carrier splitting rather than recreate it.
- use a safe YAML loader with duplicate-key rejection **and** bounded nesting, aliases, **and** input size. do **not** construct arbitrary objects, execute tags, **or** silently discard unsupported syntax. distinguish malformed input from an unsupported check.
- pin the selected dependencies **in** the root Python configuration under CA-D-250-PROGRAMMATIC-CORE-DELIVERY--provide-programmatic-software-carriers. dependency adoption does **not** relax read-only execution, protected-input handling, source-bound rule coverage, **or** golden-corpus acceptance.

### Body and Actor adapters

- select the body contract by the carried Content Role under CA-D-479-CORE_META_MODEL-DELIVERY--use-stable-headings-for-atom-body-properties; reuse **`=1`** section parser across section, Property-location, **and** Plan-model checks. use the current CA-D-470-CORE_META_MODEL-DELIVERY--serialize-plan-file-sections nesting for the Plan Definition of Done, **not** its retired sibling-section layout.
- parse actual heading boundaries outside fenced examples. check required cardinality, order, content, **and** nesting independently; an empty admitted Details section is **not** a missing section. retain an explicit gap for an unresolved role **or** extension contract.
- check Author by exact membership **in** the selected Operator registry under CA-D-274-CORE_META_MODEL-DELIVERY--serialize-explicit-atom-revision-author **and** CA-D-494-CORE_META_MODEL-DELIVERY--store-operator-registry-in-project-root. read the registry through the bounded, fingerprinted file reader; fail unlisted names **only after** its schema is valid. do **not** infer aliases, Actor records, **or** permissions. retain malformed, stale, unavailable, **or** absent registry context as incomplete coverage.
- omit effective Plan Assignee resolution for now; retain its deferred coverage explicitly **without** inferring an Assignee from Author **or** from the registry. this does **not** change the optional carried `assignee` encoding.
- refresh an adapter's source binding **only after** reconciling its behavior **and** positive/negative tests with the changed governing Claim. a pin refresh alone is **not** an implementation fix.

## Details
