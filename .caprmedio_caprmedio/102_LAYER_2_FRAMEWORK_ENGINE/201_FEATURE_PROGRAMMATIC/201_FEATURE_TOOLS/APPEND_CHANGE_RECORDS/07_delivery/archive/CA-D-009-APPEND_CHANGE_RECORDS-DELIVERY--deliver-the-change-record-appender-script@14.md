---
atom_id: CA-D-009
subjects:
  governs:
    continuant:
      - provenance
version: 14
updated_at: 2026-09-15 03:37:12
relations:
  delivery_for:
    - CA-R-812
    - CA-R-1124
    - CA-R-1064
---
# Deliver the change-record appender script

Realize `APPEND_CHANGE_RECORDS` through the canonical source script `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/301_TOOLS/APPEND_CHANGE_RECORDS/append_change_records.py` and its content-identical carrier in the selected `.caprmedio_runtime/tools` release. It must expose the common Doer CLI contract with dry-run and apply modes and use the release-local shared non-executable Journal append implementation. It validates and appends schema-version-3 `governed_project_change` records for file or folder subjects, including the complete ordered folder entry set, while retaining read compatibility with accepted schema-version-2 file records. That shared implementation is a library, not a fifth Tool or executable entry point; its mutable lease and append state remains under `.caprmedio_runtime`.
