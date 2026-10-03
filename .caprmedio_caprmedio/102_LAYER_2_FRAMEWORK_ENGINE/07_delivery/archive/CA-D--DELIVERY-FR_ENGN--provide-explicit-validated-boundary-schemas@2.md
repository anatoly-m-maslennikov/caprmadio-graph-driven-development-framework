---
subject_scopes:
  - framework-engine-software
  - framework-engine-python
version: 2
updated_at: 2026-08-22 02:15:57
relations: {}
---
# Provide explicit validated boundary schemas

Deliver every admitted untrusted Python structured-data boundary with an explicit Pydantic model or TypeAdapter, a declared strictness and extra-field policy, structured validation errors, and deterministic serialization where serialization is public behavior. Publish generated JSON Schema when another Tool, App, MCP peer, or external system consumes the contract.

Keep Pydantic-specific models at the adapter or contract boundary unless their validation behavior is itself part of the governed domain meaning. Keep the deterministic core usable through plain typed values or replaceable interfaces, and declare the supported Pydantic version boundary so an upgrade cannot silently change validation or schema behavior.

Candidate alignment: CA-D-001, CA-D-002, CA-M-002, CA-M-005, CA-E-002.

## Sources

- [Pydantic: models](https://docs.pydantic.dev/latest/concepts/models/)
- [Pydantic: TypeAdapter](https://docs.pydantic.dev/latest/concepts/type_adapter/)
- [Pydantic: JSON Schema](https://docs.pydantic.dev/latest/concepts/json_schema/)
