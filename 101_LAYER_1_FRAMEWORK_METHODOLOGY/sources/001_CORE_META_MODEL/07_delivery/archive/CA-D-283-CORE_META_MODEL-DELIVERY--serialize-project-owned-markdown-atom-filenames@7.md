---
atom_id: CA-D-283
cce_version: cce_1
cce_form: grammar
subjects:
  governs: "Project-Owned Markdown Atom Carrier/Filename"
  depends_on:
    - "Atom/Identifier"
    - "Atom/Revision"
    - "Atom/Summary"
    - "Atom/Scope"
version: 7
updated_at: "2026-09-14 02:40:31 +0400"
relations: {}
---
# Serialize Project-Owned Markdown Atom Filenames

**every** identified Project-owned Markdown Atom filename other than a Task filename **must** match `<ATOM_ID>[-<CURRENT_SCOPE>][-<LOCAL_TIER>]-<ATOM_TYPE>[-<TARGET_SCOPE>]--<SUMMARY_SLUG>.<EXT>`. **every** same-identity Atom Revision **must** preserve its exact assigned Atom-ID segment **in** its Carrier filename **and** serialize its retained Summary under CA-D-282. a replacement filename **must** contain the successor Atom ID **and** the successor's Summary Slug; a Summary Slug **must not** be edited independently of its source Summary.
