---
subject_scopes:
  - graph-context-routing
tier: core
version: 3
updated_at: 2026-08-23 15:33:04 +0400
relations:
  relates_to:
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-719--delegate-mcp-calls-to-canonical-tools
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-723--bind-mcp-operation-to-the-current-project-frontier
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-725--bound-and-control-mcp-requests
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-726--enforce-least-authority-and-secret-boundaries
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-727--return-stable-model-readable-mcp-results
---
# Route selected graph context into governed Codex work

`CODEX_PLUGIN` must let an operator transfer the canonical identities, paths, current digests, and declared selection boundary of GRAPH_APP nodes into a Codex conversation, ask questions about that bounded context, and request applicable CAPRMEDIO work through existing Skills and the provider-neutral MCP Tool interface. The plugin must not implement project mutation itself, widen the selected scope implicitly, bypass Tool validation or host permissions, expose secrets, or perform an irreversible action without the host's required operator confirmation; results must preserve Tool meaning, provenance, and explicit failure states.
