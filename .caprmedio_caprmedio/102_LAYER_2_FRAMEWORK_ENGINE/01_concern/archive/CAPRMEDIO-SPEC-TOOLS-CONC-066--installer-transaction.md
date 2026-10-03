+++
artifact_subtype = "gap"
semantic_id = "CAPRMEDIO-SPEC-TOOLS-CONC-066--installer-transaction"
revision_mode = "atomic"
content_role = "observation"
governance_origin = "internal"
relation_shape = "standalone"
status = "accepted"
priority = "medium"
version = 1
updated_at = "2026-08-17 19:36:01"
llm_session_ids = ["codex:019f591f-04f6-70f2-8de7-828b7cccc69d"]
+++

# Gap — Host installation lacks transaction-wide rollback

The installer replaces skill directories one at a time and installs the shared
runtime afterward. A mid-copy I/O failure after an earlier replacement can
leave a host with a mixed old/new distribution because no transaction-wide
rollback restores every prior destination.

## Rationale

This is a missing tool capability because per-directory atomic replacement is
not equivalent to an atomic multi-package installation transaction.
