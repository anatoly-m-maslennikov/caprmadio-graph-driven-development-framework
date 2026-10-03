---
subject_scopes:
  - framework-engine-python
version: 1
updated_at: 2026-08-22 02:15:57
relations: {}
---
# Provide bounded Python source and external assets

Deliver hand-authored Python through cohesive carriers no larger than 200 physical lines and executable units that target 25 logical lines, permit 26–40 only for one coherent job, and exceed 40 only under an explicit Operator exception. Keep declarative classes and schemas bounded by one responsibility within the file limit.

Deliver large reusable static mappings outside Python: TOML by default, JSON for schemas or machine interchange, and YAML only where its distinct features are required. Keep generated Runtime and Delivery output outside the software-source distribution.

Candidate alignment: CA-D-001, CA-D-002, CA-M-002, CA-M-005, CA-R-861.

## Sources

- [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [Python documentation: tomllib](https://docs.python.org/3/library/tomllib.html)
- [Python documentation: json](https://docs.python.org/3/library/json.html)
