---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Rename Generic Artifact Carrier"
  depends_on:
    - "Journal/Record"
    - "Action"
    - "Artifact"
    - "Artifact/Carrier"
    - "Artifact/Revision"
    - "Relation"
version: 7
updated_at: "2026-09-17 22:44:46 +0000"
relations: {"evaluation_for":["CA-R-1133","CA-O-040","CA-R-1491"]}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify rename one generic Artifact carrier

## Claim checked

CA-O-040 performs a grammar-valid generic carrier rename with complete canonical-reference rewrites **or** rolls back entirely.

## Applicable when

Apply whenever generic filename grammar, canonical-reference discovery, **or** rename transaction mechanics change.

## Test case

Prepare one generic Artifact with two current mutable governed canonical references **and** immutable historical evidence of its old identity. request a valid new filename; repeat using a filename that collides with another carrier.

## Acceptance criteria

the valid case changes the carrier name, records one old-to-new identity mapping, **and** rewrites both current mutable canonical references with **none** retaining the old identity. accepted Journal Records **and** exact historical Revisions remain byte-for-byte unchanged under CA-R-1491; their old identity is **not** a missed current rewrite. The collision case changes no carrier **or** reference.

## Failure disposition

Reject the realization **and** preserve source **and** target names, grammar result, mapping, reference inventory, transaction evidence, **and** collision finding.

## Post-effect failure coverage

from an independent recorded before-state, inject a failure **after** the Carrier rename and before completion of all required reference rewrites **and** **before** the complete transition is accepted.

- verify restoration of **every** selected mutable Carrier, metadata value, **and** canonical reference **to** the exact before-state, including the prior existence **or** absence of owned destination paths. unrelated Carriers remain unchanged.
- distinguish failed preflight, failed apply, successful restoration, **and** incomplete restoration. **none** is an accepted successful transition.
- retain evidence that the injected failure followed a real selected effect. preflight rejection alone does **not** prove recovery; incomplete **or** unverified restoration fails the rollback guarantee.
