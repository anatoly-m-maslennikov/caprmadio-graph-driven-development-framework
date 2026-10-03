---
atom_id: CA-D-250
subject_scopes:
  - framework-engine-software
tier: core
version: 3
updated_at: 2026-09-01 02:35:00 +0400
relations:
  child_of:
    - CA-D-001
  delivery_for:
    - CA-M-110
    - CA-M-229
---
# Provide Python FRAMEWORK_ENGINE Software carriers

Deliver applicable FRAMEWORK_ENGINE Tools, App backend services, and MCP
components as Python source and installable runtime carriers under the
technical contract in `pyproject.toml`, table
`tool.caprmedio.framework_engine_software`. For every admitted dependency or
non-Python carrier, deliver its bounded exception record and integration
contract at the contract's declared Delivery location, with the corresponding
acceptance evidence at its Evaluation location. Keep this realization
replaceable so CAPRMEDIO governed meaning does not depend on Python syntax,
packages, or runtime objects.

This Delivery owns the root `pyproject.toml` placement and encoding for the
technical configuration boundary selected by CA-M-229. It does not own the
interpreter, dependency, or workflow-tool selections materialized there.
