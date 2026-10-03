---
atom_id: CA-D-429
cce_version: cce_1
cce_form: delivery
subjects:
  governs:
    continuant:
      - Tool/IMPLEMENTATION_INVENTORY/Carrier
  depends_on:
    continuant:
      - Tool/IMPLEMENTATION_INVENTORY
version: 1
updated_at: 2026-09-12 04:14:47 +0400
relations:
  delivery_for:
    - CA-R-1071
    - CA-M-101
---
# Deliver IMPLEMENTATION_INVENTORY Tool

The `IMPLEMENTATION_INVENTORY` Tool must deliver its canonical executable Carrier at `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/301_TOOLS/IMPLEMENTATION_INVENTORY/implementation_inventory.py`; that Carrier realizes `CA-R-1071` through `CA-M-101`.
