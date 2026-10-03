---
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Evidence/Git reference"
  depends_on:
    - "Carrier"
    - "Artifact/Revision"
    - "Journal/Record"
    - "Projection"
    - "Extension"
version: 1
updated_at: "2026-09-16 17:31:26 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  relates_to:
    - "CA-D-329"
    - "CAPRMEDIO-GOV-REQU-353"
---
# Encode exact Git references in release evidence

**when** the GIT Extension supplies the Git binding for a selected release candidate, its evidence references **must** identify the repository **and** the full immutable commit object ID representing the checked content.

- a branch name, HEAD, **or** a tag name alone is **not** an exact Revision reference. retain a selected tag as a label **only** alongside its resolved commit ID.
- a commit ID **must not** represent uncommitted content as evaluated committed content; material working-tree differences **must** remain explicit under the applicable candidate binding.
- a release manifest **must** bind the released candidate **to** that exact reference; a later branch movement does **not** rebind earlier evidence.
- use the existing proof-frontier **and** Journal Carriers. do **not** create a second authoritative release log **or** redefine the generic Journal schema.

this Git-specific encoding does **not** select a branch strategy, require Git outside the selected Extension capability, **or** authorize commit, merge, tag, push, **or** publication.
