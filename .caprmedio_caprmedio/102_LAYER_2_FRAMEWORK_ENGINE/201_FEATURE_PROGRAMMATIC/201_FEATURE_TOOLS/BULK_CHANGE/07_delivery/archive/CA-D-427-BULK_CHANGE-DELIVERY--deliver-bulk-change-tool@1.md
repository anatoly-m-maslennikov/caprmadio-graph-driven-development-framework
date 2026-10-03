---
atom_id: CA-D-427
cce_version: cce_1
cce_form: delivery
subjects:
  governs:
    continuant:
      - Tool/BULK_CHANGE/Carrier
  depends_on:
    continuant:
      - Tool/BULK_CHANGE
version: 1
updated_at: 2026-09-12 04:14:47 +0400
relations:
  delivery_for:
    - CA-R-1155
    - CA-M-254
---
# Deliver BULK_CHANGE Tool

The `BULK_CHANGE` Tool must deliver its canonical executable Carrier at `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/301_TOOLS/BULK_CHANGE/bulk_change.py`; that Carrier realizes `CA-R-1155` through `CA-M-254`.
