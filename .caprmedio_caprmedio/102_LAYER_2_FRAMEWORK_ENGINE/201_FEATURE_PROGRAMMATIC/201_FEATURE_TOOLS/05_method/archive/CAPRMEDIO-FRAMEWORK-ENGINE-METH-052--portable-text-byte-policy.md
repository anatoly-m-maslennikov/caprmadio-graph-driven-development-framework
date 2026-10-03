+++
semantic_id = "CAPRMEDIO-FRAMEWORK-ENGINE-METH-052--portable-text-byte-policy"
revision_mode = "atomic"
content_role = "definition"
governance_origin = "internal"
relation_shape = "standalone"
status = "accepted"
priority = "high"
tier = "core"
authority = "operator:anatoly-m-maslennikov"
claim = "Repository-controlled text has one portable LF byte policy owned by TOOL configuration rather than by post-implementation operations."
version = 3
updated_at = "2026-08-19 16:45:00"
llm_session_ids = ["codex:019f591f-04f6-70f2-8de7-828b7cccc69d"]
rationale = "Worktree byte normalization is repository/tool configuration that protects all carriers before implementation or release; it is not an operational release rule."
promotion = {}

[[relations]]
type = "replacement_of"
target = "CAPRMEDIO-FIELD-METH-070--portable-text-byte-policy"

[[relations]]
type = "child_of"
target = "CAPRMEDIO-GOV-METH-039--place-executable-methodology-by-role"
+++

# Decision — Own portable text bytes in TOOL

Git-controlled text worktree content uses LF through the root repository
policy `* text=auto eol=lf`. The checkout boundary therefore preserves the byte
identity of immutable carriers on Linux, macOS, native Windows, and WSL without
weakening carrier-digest validation. Binary content is not line-ending
normalized.

This Decision completely replaces `CAPRMEDIO-FIELD-METH-070--portable-text-byte-policy`. The earlier atom
remains immutable history.
