---
subject_scopes:
  - framework-engine-mcp
version: 1
updated_at: 2026-08-22 02:15:57
relations: {}
---
# Provide versioned MCP adapter surfaces

Deliver MCP client or server carriers as replaceable adapters over existing Framework Engine capabilities. Include the supported protocol revision, negotiated capability declarations, versioned request and response schemas, stable error mapping, timeout and cancellation behavior, progress and task correlation where applicable, and bounded resource limits.

Keep credentials and authorization state transport-bound and outside governed source. The adapter exposes no project meaning or business decision unavailable through its underlying Engine capability.

Candidate alignment: CA-D-001, CA-D-002, CA-M-002, CA-M-006, CA-R-827, CA-R-861.

## Sources

- [Model Context Protocol: lifecycle](https://modelcontextprotocol.io/specification/2025-06-18/basic/lifecycle)
- [Model Context Protocol: authorization](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)
- [Model Context Protocol: tasks](https://modelcontextprotocol.io/specification/2025-11-25/basic/utilities/tasks)
