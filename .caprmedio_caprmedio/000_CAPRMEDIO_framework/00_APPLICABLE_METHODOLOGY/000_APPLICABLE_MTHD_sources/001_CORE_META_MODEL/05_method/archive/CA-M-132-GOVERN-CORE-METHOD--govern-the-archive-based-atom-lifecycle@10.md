---
subjects:
  - artifact-model
  - lifecycle-traceability
cce_version: cce_1
cce_form: method
version: 10
updated_at: "2026-08-23 11:37:28"
relations:
  child_of:
    - CA-R-356
    - CA-R-957
    - CA-R-958
---
# Govern the archive-based Atom lifecycle

TO govern an Atom lifecycle, the Operator or Agent MUST PERFORM ALL OF:

1. Keep a mutable unaccepted Atom in the role-local `drafts/` place without an assigned Atom ID.
2. Keep an accepted current Atom directly in its Content-role place.
3. Keep a closed Concern in `solved/` and a completed Analysis or Plan in `done/` when preserved as post-acceptance evidence.
4. Move a replaced, retired, or otherwise historical Atom Revision to the role-local `archive/` place.
5. Preserve an assigned Atom ID across lifecycle moves.
6. Encode every archived Revision filename with its metadata version suffix.
7. Create a new draft and new Atom ID when an archived matter recurs.
