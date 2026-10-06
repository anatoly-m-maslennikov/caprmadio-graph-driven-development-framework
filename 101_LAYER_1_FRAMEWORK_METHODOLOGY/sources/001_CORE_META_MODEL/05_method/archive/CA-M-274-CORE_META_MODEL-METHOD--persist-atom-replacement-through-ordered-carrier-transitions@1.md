---
atom_id: CA-M-274
cce_version: cce_1
cce_form: method
subjects:
  governs:
    occurrent:
      - Atom Carrier Replacement
  depends_on:
    continuant:
      - Atom
      - Artifact/Revision
      - Atom/Carrier
      - Git Commit
      - Work Journal
      - Artifact/Revision/Archive Carrier Basename
version: 1
updated_at: "2026-09-10 06:39:08 +0400"
relations:
  method_for:
    - CA-R-1432
    - CA-R-807
---
# Persist Atom replacement through ordered Carrier transitions

**to** persist an Atom replacement, CAPRMEDIO **must** perform **all** of:

1. commit the successor as Active **before** archiving the predecessor.
2. archive the predecessor as one whole Carrier under CA-D-303 **in** a `MOVE` whose authoritative Work Journal Event records explicit predecessor **and** successor Atom IDs under CA-R-807.
3. preserve the predecessor's content, identity, frontmatter, **and** Version exactly; change its basename **only** by adding the canonical `@<version>` Archive suffix under CA-D-289.
4. keep **every** successor **and** predecessor Carrier change as a separate one-file Git Commit, following the canonical direct typed-relation commit-message rule under CA-D-334 **and** CA-D-335.
5. keep replacement history out of predecessor **and** successor Atom frontmatter; formal replacement relations **and** inverse navigation remain deferred under CA-R-807.
