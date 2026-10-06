---
atom_id: CA-R-1229
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - Applicable Methodology/Compilation Output
  depends_on:
    continuant:
      - Applicable Methodology/Sources
      - Applicable Methodology
      - Artifact/Projection
version: 2
updated_at: 2026-08-27 20:40:00 +0400
relations: {}
---
# Require Projected Atom Source Provenance

every Applicable Methodology projected Atom Carrier **must** add exactly `projection: { source_carrier_path: <relative POSIX path> }`, where source_carrier_path resolves from the projected Atom Carrier parent directory to its authoritative Source Carrier under `000_APPLICABLE_MTHD_sources`.
