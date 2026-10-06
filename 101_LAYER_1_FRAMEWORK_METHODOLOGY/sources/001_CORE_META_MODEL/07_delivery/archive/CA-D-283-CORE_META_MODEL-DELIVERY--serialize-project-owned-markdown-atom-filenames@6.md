---
atom_id: CA-D-283
cce_version: cce_1
cce_form: grammar
subjects:
  governs:
    continuant:
      - "Project-Owned Markdown Atom Carrier/Filename"
  depends_on:
    continuant:
      - "Atom/Identifier"
      - "Atom/Revision"
      - "Atom/Summary"
      - "Atom/Scope"
version: 6
updated_at: "2026-09-10 20:57:21 +0400"
relations: {}
---
# Serialize Project-Owned Markdown Atom Filenames

**every** identified Project-owned Markdown Atom filename other than a Task filename **must** match `<ATOM_ID>[-<CURRENT_SCOPE>][-<LOCAL_TIER>]-<ATOM_TYPE>[-<TARGET_SCOPE>]--<SUMMARY_SLUG>.<EXT>`. **every** same-identity Atom Revision, including a governed Summary **or** Scope change, **must** preserve its exact assigned Atom-ID segment **in** its Carrier filename.
