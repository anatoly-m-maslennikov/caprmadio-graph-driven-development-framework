---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Relation Kind"
  depends_on:
    - "CAPRMEDIO Graph"
    - "Applicable Methodology"
    - "Projection"
    - "Relation Kind/Metadata"
version: 8
updated_at: "2026-09-15 01:47:49 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Keep relation vocabularies graph-specific

**every** Relation Kind **must** belong **to** **`=1`** kind of CAPRMEDIO Graph **and** be admitted as native **only** **in** instances of that graph kind. instances of the same graph kind governed by the same Applicable Methodology **must** reuse the same Relation Kind authority.

the owning graph kind **and** canonical name **must** determine the Relation Kind's graph-qualified identity. matching names **or** compatible endpoints **must not** make Relation Kinds from different graph kinds interchangeable.

the owning graph kind determines a Relation Kind's authority, **not** a requirement that **all** endpoints occupy the same graph. admitted cross-graph endpoints **and** source references under CA-R-1472 retain that graph-qualified ownership. another graph **may** represent a source-traceable reference **or** view of the Relation **without** registering it as native.
