---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Patch Generic Artifact Relations"
  depends_on:
    - "Action"
    - "Artifact"
    - "Artifact/Carrier"
    - "Artifact/Revision"
    - "Relation"
    - "Scope Unit"
version: 6
updated_at: "2026-09-17 03:32:31 +0000"
relations: {"evaluation_for":["CA-R-1131","CA-O-039"]}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify patch generic Artifact relations

## Claim checked

CA-O-039 changes **only** valid direct relation targets **and** endpoint descriptors while preserving the source Artifact body **and** unrelated metadata.

## Applicable when

Apply whenever generic relation-patch validation, canonical-reference resolution, **or** endpoint-descriptor handling changes.

## Test case

Seal one source Artifact with known body digest **and** existing relations. Submit one valid relative Scope Unit target with its endpoint descriptor together with one target that violates the registered relation direction; **then** submit **only** the valid relation change.

## Acceptance criteria

the mixed request changes nothing **and** identifies the invalid target. The valid request writes **only** the canonical direct target **and** endpoint descriptor, advances revision once, **and** preserves body digest **and** unrelated metadata.

## Failure disposition

Reject the realization **and** preserve relation policy, source-owner context, requested targets, endpoint descriptors, dry-run, exact diff, revision, **and** body digest.

## Post-effect failure coverage

from an independent recorded before-state, inject a failure **after** a selected Relation or endpoint-descriptor write **and** **before** the complete transition is accepted.

- verify restoration of **every** selected mutable Carrier, metadata value, **and** canonical reference **to** the exact before-state, including the prior existence **or** absence of owned destination paths. unrelated Carriers remain unchanged.
- distinguish failed preflight, failed apply, successful restoration, **and** incomplete restoration. **none** is an accepted successful transition.
- retain evidence that the injected failure followed a real selected effect. preflight rejection alone does **not** prove recovery; incomplete **or** unverified restoration fails the rollback guarantee.
