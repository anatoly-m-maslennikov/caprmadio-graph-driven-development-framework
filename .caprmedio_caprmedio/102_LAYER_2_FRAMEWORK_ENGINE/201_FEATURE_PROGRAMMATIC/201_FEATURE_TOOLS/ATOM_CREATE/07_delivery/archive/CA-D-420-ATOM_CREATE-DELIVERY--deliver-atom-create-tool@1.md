---
atom_id: CA-D-420
cce_version: cce_1
cce_form: delivery
subjects:
  governs:
    continuant:
      - Tool/ATOM_CREATE/Carrier
  depends_on:
    continuant:
      - Tool/ATOM_CREATE
version: 1
updated_at: 2026-09-12 04:14:47 +0400
relations:
  delivery_for:
    - CA-R-865
    - CA-M-185
---
# Deliver ATOM_CREATE Tool

The `ATOM_CREATE` Tool must deliver its canonical executable Carrier at `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/301_TOOLS/ATOM_CREATE/atom_create.py`; that Carrier realizes `CA-R-865` through `CA-M-185`.
