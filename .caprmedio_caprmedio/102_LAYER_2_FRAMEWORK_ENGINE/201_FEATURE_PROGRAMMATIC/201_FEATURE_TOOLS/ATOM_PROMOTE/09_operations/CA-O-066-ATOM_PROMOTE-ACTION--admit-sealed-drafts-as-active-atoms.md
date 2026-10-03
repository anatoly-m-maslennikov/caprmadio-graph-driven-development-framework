---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Admit Sealed Drafts as Active Atoms"
  depends_on:
    - "Action"
    - "Tool/ATOM_PROMOTE"
    - "Atom"
    - "Atom/Identifier"
    - "Atom/Revision"
    - "Artifact/Carrier"
    - "Journal/Record"
version: 1
updated_at: "2026-09-17 23:09:21 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Admit sealed drafts as active Atoms

Admit Sealed Drafts as Active Atoms **means** the reusable Action that accepts the complete selected set of Drafts into active Atom authority as **`=1`** all-or-nothing admission transaction. a partially admitted set is **not** an independently successful outcome.

## Applicable conditions

- select **`=1`** Draft **or** a frozen bulk set of **`>=2`** Drafts under CA-R-869.
- actual promotion requires an authorized Project-local MCP delegation with a sealed Initiative action envelope. preview alone grants no apply authority.
- the Operator supplies the stable Project Atom IDs. validate their admission under CA-D-450 **and** CA-D-378; do **not** silently substitute another ID.

## Action

1. resolve **every** source as a current Draft **and** bind it **to** **`=1`** Operator-supplied stable Atom ID. retain the exact source paths **and** bytes, digests, assigned IDs **and** expected active destinations.
2. validate role matching, uniqueness within the request **and** the next unreused Project-wide numbers for the applicable Content Roles. use current authority **and** preserved assignment/history evidence; absence from active files alone does **not** establish non-use. archived, replaced **or** absorbed Atoms do **not** release their IDs. missing **or** conflicting evidence leaves admission unresolved.
3. derive **`=1`** canonical active filename **and** location per Draft. remove **only** the `drafts` lifecycle path segment **and** change the Carrier filename under the applicable Delivery grammar; preserve the complete Draft bytes. reject non-Drafts, invalid **or** mismatched IDs, collisions **and** incomplete mappings.
4. freeze the complete source, identity-admission evidence **and** destination map. return its mutation-free dry run **without** accepting authority.
5. on explicit authorized `--apply`, recheck source digests, identity-admission evidence **and** destination absence. a competing admission **or** changed evidence invalidates the preview. move the complete selected set as **`=1`** rollbackable transaction.
6. verify exact byte identity, unique active identity, canonical placement, absence from the Draft surface **and** complete set membership.
7. **if** **any** effect **or** postcondition fails, restore **every** selected mutable source **and** destination **to** its exact before-state. preserve unrelated Carriers **and** immutable accepted Journal evidence. report the failed attempt **and** recovery result rather than promotion success.

## Outcome

**every** accepted Draft becomes **`=1`** byte-identical active Atom with its admitted Operator-supplied identity. remain **in** dry-run mode **without** delegated apply authority. stop **or** roll back on invalid input, uncertain identity admission, collision, stale Carrier, changed destination absence **or** incomplete promotion. incomplete **or** unverified restoration is **not** successful recovery.
