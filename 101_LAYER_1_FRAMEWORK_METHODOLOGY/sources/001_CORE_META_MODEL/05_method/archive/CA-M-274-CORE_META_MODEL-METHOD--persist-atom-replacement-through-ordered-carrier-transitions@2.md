---
atom_id: CA-M-274
cce_version: cce_1
cce_form: method
subjects:
  governs: "Atom Carrier Replacement"
  depends_on:
    - "Atom"
    - "Artifact/Revision"
    - "Atom/Carrier"
    - "Journal"
    - "Artifact/Revision/Archive Carrier Basename"
version: 2
updated_at: "2026-09-14 06:21:07 +0400"
relations:
  method_for:
    - CA-R-1432
    - CA-R-807
---
# Persist Atom replacement through ordered Carrier transitions

**to** persist an Atom replacement, CAPRMEDIO **must** perform **all** of:

1. persist the successor as Active **before** archiving the predecessor.
2. archive the predecessor as one whole Carrier under CA-D-303 **and** record the corresponding replacement **in** the authoritative Journal with explicit predecessor **and** successor Atom IDs under CA-R-807.
3. preserve the predecessor's content, identity, frontmatter, **and** Version exactly; change its basename **only** by adding the canonical `@<version>` Archive suffix under CA-D-289.
4. keep replacement history out of predecessor **and** successor Atom frontmatter; formal replacement relations **and** inverse navigation remain deferred under CA-R-807.
