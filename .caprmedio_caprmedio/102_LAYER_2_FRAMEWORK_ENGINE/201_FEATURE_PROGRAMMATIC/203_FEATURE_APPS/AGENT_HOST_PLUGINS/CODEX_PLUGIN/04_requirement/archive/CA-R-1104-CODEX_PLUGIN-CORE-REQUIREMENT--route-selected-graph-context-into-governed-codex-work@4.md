---
subjects:
  declared:
    continuant:
      - graph-context-routing
version: 4
updated_at: 2026-08-23 16:16:20 +0400
---
# Route selected graph context into governed Codex work

`CODEX_PLUGIN` must let an operator transfer the canonical identities, paths, current digests, and declared selection boundary of GRAPH_APP nodes into a Codex conversation, ask questions about that bounded context, and request applicable CAPRMEDIO work through existing Skills and the provider-neutral MCP Tool interface. The plugin must not implement project mutation itself, widen the selected scope implicitly, bypass Tool validation or host permissions, expose secrets, or perform an irreversible action without the host's required operator confirmation; results must preserve Tool meaning, provenance, and explicit failure states.
