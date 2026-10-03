---
atom_id: CA-R-1477
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "FPF"
  depends_on:
    - "Analysis Report"
    - "Scope Unit"
    - "Carrier"
version: 1
updated_at: "2026-09-15 02:22:01 +0400"
relations: {}
---
# Persist Analysis Reports in the governed Scope Unit

**when** an executable FPF analysis produces a persistent Project artifact, FPF **must** by default create a correctly formatted `CA-A` Analysis Report Carrier in the `02_analysis/` Folder of the narrowest resolved Scope Unit that contains the analyzed Claim Scope; routing-only work **must not** persist a report, an explicit non-persistent request **must** remain non-persistent, and unresolved identity, admission, topology, or placement **must** stop persistence rather than fall back to an ad hoc report Folder.
