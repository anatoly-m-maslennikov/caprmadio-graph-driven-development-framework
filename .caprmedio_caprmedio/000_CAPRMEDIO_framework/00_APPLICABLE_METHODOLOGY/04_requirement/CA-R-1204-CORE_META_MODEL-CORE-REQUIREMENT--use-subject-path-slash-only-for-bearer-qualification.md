---
atom_id: CA-R-1204
cce_version: cce_1
cce_form: requirement
subjects:
  governs:
    continuant:
      - Subject Path
  depends_on:
    continuant:
      - Dependent Entity
      - IS_BORNE_BY
version: 5
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1204-CORE_META_MODEL-CORE-REQUIREMENT--use-subject-path-slash-only-for-bearer-qualification.md
---
# Use Subject Path Slash Only for Bearer Qualification

**in** a Subject Path, `/` **must** express **only** one IS_BORNE_BY edge from the following Dependent Entity occurrence to the immediately preceding qualified Entity occurrence.
