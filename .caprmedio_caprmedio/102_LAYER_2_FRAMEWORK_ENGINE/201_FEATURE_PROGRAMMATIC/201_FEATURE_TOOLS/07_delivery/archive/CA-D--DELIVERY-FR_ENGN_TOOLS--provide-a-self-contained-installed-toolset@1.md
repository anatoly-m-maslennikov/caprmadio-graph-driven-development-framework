---
subject_scopes:
  - installation
version: 1
updated_at: 2026-08-21 20:35:00
relations: {}
---
# Provide a self-contained installed Toolset

Deliver one content-addressed Toolset whose executable code and required static resources are complete inside the project installation place. Declare the supported Python and platform prerequisite envelope explicitly. Do not import canonical source files from the project root after installation.

Keep mutable state, caches, logs, locks, and retained operational history in the separate runtime place. A verified installation must be reproducible from canonical Tool sources and identify the exact installed release.

Candidate alignment: CA-D-001, CA-D-002, CA-R-861, CA-M-002.

## Sources

- [PyPA: pyproject.toml specification](https://packaging.python.org/en/latest/specifications/pyproject-toml/)
- [PyPA: core metadata requires-python](https://packaging.python.org/en/latest/specifications/core-metadata/#requires-python)
