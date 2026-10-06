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
version: 4
updated_at: 2026-08-29 02:40:41 +0400
relations: {}
---
# Use Subject Path Slash Only for Bearer Qualification

**in** a Subject Path, `/` **must** express **only** one IS_BORNE_BY edge from the following Dependent Entity occurrence to the immediately preceding qualified Entity occurrence.
