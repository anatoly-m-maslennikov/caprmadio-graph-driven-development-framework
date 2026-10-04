---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Update Sealed Atom Carriers"
  depends_on:
    - "Action"
    - "Tool/ATOM_UPDATE"
    - "Atom"
    - "Atom/Revision"
    - "Atom/Summary"
    - "Atom/Revision/Updated At"
    - "Artifact/Carrier"
    - "Journal/Record"
version: 4
updated_at: "2026-09-17 03:42:35 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Update sealed CAPRMEDIO Atom carriers

Update Sealed Atom Carriers **means** the reusable Action that applies **`=1`** validated Revision **to** **every** Atom **in** an exact selected set as **`=1`** all-or-nothing transaction. the modeled boundary is the approved Revision set: partial application does **not** fulfill its operational contribution.

## Applicable conditions

- select **`=1`** Atom **or** a frozen bulk set of **`>=2`** Atoms by exact Carrier evidence. an unassigned Draft has no invented Atom ID; retain its exact locator **and** Version evidence.
- preserve identity, Summary, path, **and** filename. under CA-R-1464, a requested Summary change needs a new Atom **and** new Atom ID; this same-identity Action **must not** perform it as an update.
- apply **only** through authorized Project-local MCP delegation with a sealed Initiative action envelope. default **to** mutation-free preview.

## Action

1. resolve **every** target uniquely. reject repeated, missing, ambiguous, **or** stale selections; seal path, filename, assigned ID **when** present, Version, Updated At, **and** digest as preconditions.
2. prepare the requested frontmatter, body, **or** combined change **in** memory. preserve the immutable Summary **and** identity **and** reject an attempt **to** change them through this Action.
3. validate **every** complete resulting Carrier, including required metadata **and** direct Relations. calculate **`=1`** next Version per changed Atom under CA-R-1415 **and** retain the exact previous Revision under CA-R-1371. a formatting-only **or** lossless-serialization change preserves Updated At under CA-R-1492; a substantive change follows the applicable Updated At authority **and** **must not** be disguised as formatting.
4. freeze the complete target map, required historical Carriers, expected Revisions, **and** digests. expose the exact mutation-free dry-run diff **before** apply.
5. on explicit authorized `--apply`, recheck **every** frozen source **and** destination precondition. persist the exact prior Revisions **and** publish **all** selected current Revisions within the same all-or-nothing boundary. an archive collision **or** changed source blocks apply **without** overwriting evidence.
6. verify the published set **and** its exact prior history. **if** publication **or** post-write validation fails, restore **every** mutable Carrier **to** its before-state, including **any** newly created archive destinations; preserve pre-existing historical Carriers, unrelated targets, **and** accepted Journal Records.

## Outcome

success requires **every** selected Atom **to** advance **`=1`** Revision with identity, Summary, **and** placement preserved. stop **without** partial mutation on an invalid target **or** failed precondition. report a failed effect with its actual recovery outcome; incomplete **or** unverified restoration is **not** a successful update **or** rollback.
