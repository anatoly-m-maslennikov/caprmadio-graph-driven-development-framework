---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "artifact-operations"
  depends_on: []
version: 9
updated_at: "2026-09-17 23:09:18 +0000"
relations:
  evaluation_for:
    - CA-M-187
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify move selected caprmedio atom carriers

## Claim checked

CA-M-187 relocates the complete sealed Atom target set while preserving **every** carrier byte, filename, **and** stable Atom ID.

## Applicable when

apply **to** **any** realization of CA-M-187 **before** it can move individual Atom carriers **or** recursive subtrees.

## Test case

use one fixture with one explicitly selected Atom **and** a two-level subtree containing three Atom carriers **and** one non-Atom file. record a shape-preserving subtree dry-run **and** an explicitly flattened subtree dry-run; introduce a destination collision into the shape-preserving map **and** attempt delegated apply, **then** remove the collision **and** apply the unchanged exact **and** shape-preserving requests through sealed Initiative envelopes.

## Post-effect recovery cases

from independent fixture baselines, inject an effect failure **after** a destination write **and** a failed post-move verification. cover singular **and** bulk requests, including failure **after** an earlier bulk member was moved. require restoration of **every** selected mutable source **and** destination **to** its exact before-state while preserving unrelated files **and** immutable accepted Journal evidence. reject incomplete **or** unverified recovery **and** preserve the actual failure **and** recovery evidence. preflight collision rejection alone does **not** prove rollback; this recovery check does **not** settle the owner-dependent scope **and** filename conflict recorded **in** CA-C-119.

## Acceptance criteria

the collision attempt moves nothing; the valid applies move the explicitly selected Atom **and** **all** three subtree Atoms **to** their mapped destinations, preserve the default subtree shape, leave the non-Atom untouched, remove **all** selected sources, **and** preserve **every** selected carrier's filename, stable ID, **and** digest. the explicit-flatten dry-run exposes a flat map **and** makes no mutation.

## Failure disposition

reject the realization **and** preserve source **and** destination maps, flattening map, authority result, collision evidence, before-and-after digests, **and** **any** incomplete move state.
