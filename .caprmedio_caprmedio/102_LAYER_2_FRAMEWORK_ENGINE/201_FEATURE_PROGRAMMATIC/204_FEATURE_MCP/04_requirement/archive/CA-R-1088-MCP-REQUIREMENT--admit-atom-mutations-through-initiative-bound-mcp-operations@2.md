---
subjects:
  - framework-engine-mcp
cce_version: cce_1
cce_form: obligation
version: 2
updated_at: 2026-08-23 15:33:04 +0400
---
# Admit Atom mutations through Initiative-bound MCP operations

Every mutation of a CAPRMEDIO Markdown Atom MUST enter through an authorized project-local MCP operation that delegates to the canonical Atom Tool. Search and read operations remain mutation-free. Create, update, move, archive, promote, upgrade, replacement, and every atomic or bulk composition of those operations MUST seal one Initiative and stable action identity before mutation and validate the current project frontier. After the mutation succeeds and before acknowledging the operation, MCP MUST invoke `COMMIT_TRIGGER` and receive durable intake acknowledgment for that sealed action.

Multiple MCP service instances and sessions MAY operate concurrently. Every mutation of an existing Atom MUST carry its expected Atom Revision or carrier digest; a mismatch MUST reject that target rather than overwrite concurrent work. A bulk operation MUST seal its complete target set and report per-target conflicts without silently widening or changing that set. Direct or otherwise unowned Atom writes outside this gateway MUST NOT be admitted as governed MCP mutations.
