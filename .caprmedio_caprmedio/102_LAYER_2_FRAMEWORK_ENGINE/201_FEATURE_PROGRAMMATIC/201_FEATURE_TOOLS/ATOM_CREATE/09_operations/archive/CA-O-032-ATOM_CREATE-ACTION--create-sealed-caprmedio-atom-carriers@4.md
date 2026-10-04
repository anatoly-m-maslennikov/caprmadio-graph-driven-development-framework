---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Create Sealed Atom Carriers"
  depends_on:
    - "Action"
    - "Tool/ATOM_CREATE"
    - "Atom"
    - "Atom/Identifier"
    - "Atom/Revision"
    - "Atom/Summary"
    - "Artifact/Carrier"
    - "Journal/Record"
version: 4
updated_at: "2026-09-17 04:46:13 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Create sealed CAPRMEDIO Atom carriers

Create Sealed Atom Carriers **means** the reusable Action that admits **and** publishes an exact requested set of new Atom Carriers as **`=1`** all-or-nothing creation transaction. its contribution is the complete admitted set; a partially created set is **not** an independently successful outcome.

## Applicable conditions

- accept **`=1`** new Atom **or** a frozen bulk set of **`>=2`** new Atoms under CA-R-865.
- actual creation requires authorized Project-local MCP delegation with a sealed Initiative action envelope. preview alone does **not** authorize apply.
- an assigned Project Atom ID follows CA-D-450 **and** CA-D-378. an unassigned Draft uses the applicable Draft Carrier grammar **without** inventing an Atom ID.

## Action

1. normalize a complete path **or** directory-plus-filename request into **`=1`** target mapping per Carrier, with complete frontmatter **and** Markdown content.
2. validate the complete requested set **before** filesystem mutation: configured control-root Content Role placement, current filename grammar, required metadata, direct Relations, Summary, **and** initial Revision metadata.
3. prove that **every** destination is absent **and** unique within the request. for **every** assigned ID, establish the next unreused Project-wide number for its Content Role using current authority **and** preserved assignment/history evidence under CA-D-450. absence from active Carriers alone does **not** prove that an ID is unused; archived, replaced, **or** absorbed Atoms do **not** release their IDs for reuse. missing **or** conflicting evidence leaves admission unresolved.
4. freeze the complete target map, validated content, identity-admission evidence, expected empty destinations, **and** digests. publish the exact mutation-free dry run with **every** proposed Carrier **and** validation result.
5. on explicit authorized `--apply`, recheck the complete frozen absence **and** identity-admission preconditions. stage **all** new Carriers **and** publish the full set as **`=1`** transaction. changed evidence **or** a competing admission invalidates the preview; do **not** silently allocate a different ID **or** change the selected set during apply.
6. **if** staging, publication, **or** post-write validation fails, restore the complete mutable before-state **and** remove **only** owned unpublished staging. preserve unrelated Carriers **and** accepted Journal evidence of actual effects. report the failed attempt **and** its recovery result rather than successful creation.

## Outcome

the selected set is fully absent **or** fully present as the validated first Revisions, with no partial creation. stop on invalid content, collision, uncertain identity admission, changed preconditions, changed targets, **or** failed publication. incomplete **or** unverified restoration is **not** successful recovery.
