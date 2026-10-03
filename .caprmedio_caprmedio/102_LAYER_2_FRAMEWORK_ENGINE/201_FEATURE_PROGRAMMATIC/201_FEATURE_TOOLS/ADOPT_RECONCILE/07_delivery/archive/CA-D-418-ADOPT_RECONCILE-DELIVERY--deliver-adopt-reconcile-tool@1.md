---
atom_id: CA-D-418
cce_version: cce_1
cce_form: delivery
subjects:
  governs:
    continuant:
      - Tool/ADOPT_RECONCILE/Carrier
  depends_on:
    continuant:
      - Tool/ADOPT_RECONCILE
version: 1
updated_at: 2026-09-12 04:14:47 +0400
relations:
  delivery_for:
    - CA-R-1072
    - CA-M-102
---
# Deliver ADOPT_RECONCILE Tool

The `ADOPT_RECONCILE` Tool must deliver its canonical executable Carrier at `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/301_TOOLS/ADOPT_RECONCILE/adopt_reconcile.py`; that Carrier realizes the review-only structural CRMED-draft derivation required by `CA-R-1072` and specified by `CA-M-102`.
