---
atom_id: CA-D-430
cce_version: cce_1
cce_form: delivery
subjects:
  governs:
    continuant:
      - Tool/PROJECTION_REBUILD/Carrier
  depends_on:
    continuant:
      - Tool/PROJECTION_REBUILD
version: 1
updated_at: 2026-09-12 04:14:47 +0400
relations:
  delivery_for:
    - CA-R-1156
    - CA-M-255
---
# Deliver PROJECTION_REBUILD Tool

The `PROJECTION_REBUILD` Tool must deliver its canonical executable Carrier at `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/301_TOOLS/PROJECTION_REBUILD/projection_rebuild.py`; that Carrier realizes `CA-R-1156` through `CA-M-255`.
