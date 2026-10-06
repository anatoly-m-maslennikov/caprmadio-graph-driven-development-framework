---
subjects:
  governs: "Atom/Revision/Frontmatter"
  depends_on:
    - "Atom/Revision/Version"
    - "Atom/Revision/Updated At"
version: 10
updated_at: "2026-09-24 14:16:19 +0000"
relations: {}
---
# Serialize Atom Revision Metadata in Frontmatter

**every** Markdown Atom Revision Carrier **must** serialize its positive integer Version as `version` **and** its Project-time Updated At value as `updated_at` **in** YAML frontmatter.

- `version` is a YAML integer **>=1**, **not** a Boolean **or** numeric string.
- `updated_at` is a quoted YAML string containing **=1** valid date, time **and** explicit UTC offset. accept the existing `YYYY-MM-DD HH:MM:SS +HHMM` form **and** the equivalent ISO 8601 `YYYY-MM-DDTHH:MM:SSZ` **or** `YYYY-MM-DDTHH:MM:SS+HH:MM` form, including optional fractional seconds. offset signs **may** be positive **or** negative; reject a missing timezone, impossible date, **or** invalid offset.
- lexical differences representing the same instant do **not** alone change Revision identity; formatting-only changes follow the existing Updated At preservation rule.
