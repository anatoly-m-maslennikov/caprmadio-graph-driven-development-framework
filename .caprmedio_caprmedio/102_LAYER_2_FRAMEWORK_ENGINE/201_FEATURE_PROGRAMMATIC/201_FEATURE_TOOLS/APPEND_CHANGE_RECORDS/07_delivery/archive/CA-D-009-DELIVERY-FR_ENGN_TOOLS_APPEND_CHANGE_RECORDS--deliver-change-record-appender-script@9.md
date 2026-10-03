---
subject_scopes:
  - provenance
version: 9
updated_at: 2026-08-23 13:21:41
relations:
  delivery_for:
    - CA-R-812-REQUIREMENT-FR_ENGN_TOOLS_APPEND_CHANGE_RECORDS--append-governed-file-change-journal-records
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-520--own-deterministic-scripts-in-tools
    - CA-R-1064
---
# Deliver the change-record appender script

Realize `APPEND_CHANGE_RECORDS` through the canonical source script `002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/APPEND_CHANGE_RECORDS/append_change_records.py` and its content-identical carrier in the selected `.caprmedio_install` release. It must expose the common Doer CLI contract with dry-run and apply modes and use the release-local shared non-executable Journal append implementation. It validates and appends schema-version-3 `governed_project_change` records for file or folder subjects, including the complete ordered folder entry set, while retaining read compatibility with accepted schema-version-2 file records. That shared implementation is a library, not a fifth Tool or executable entry point; its mutable lease and append state remains under `.caprmedio_runtime`.
