---
atom_id: CA-R-1464
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Atom/Summary"
  depends_on:
    - "Atom"
    - "Atom/Identifier"
    - "Atom/Revision"
    - "Atom/Claim"
version: 1
updated_at: "2026-09-14 02:40:31 +0400"
relations: {}
---
# Keep Summary fixed for Atom identity

an Atom **must** keep the Summary created with it across **all** of its Revisions. **if** its Summary needs a change, **then** it **must** be replaced by a new Atom with a new Atom ID, even **if** its Claim is unchanged.
