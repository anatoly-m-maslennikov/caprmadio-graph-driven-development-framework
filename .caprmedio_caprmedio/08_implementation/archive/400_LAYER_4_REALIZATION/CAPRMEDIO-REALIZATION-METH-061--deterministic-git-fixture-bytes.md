+++
semantic_id = "CAPRMEDIO-REALIZATION-METH-061--deterministic-git-fixture-bytes"
revision_mode = "atomic"
content_role = "definition"
governance_origin = "internal"
relation_shape = "standalone"
status = "accepted"
priority = "high"
authority = "operator:anatoly-m-maslennikov"
claim = "Test implementations isolate temporary Git newline settings and write or observe explicit fixture bytes before asserting byte preservation."
llm_session_ids = ["codex:019f591f-04f6-70f2-8de7-828b7cccc69d"]
rationale = "Deterministic fixture construction governs Test implementation and belongs in REALIZATION rather than the post-release FIELD Layer."
promotion = {}

[[relations]]
type = "replacement_of"
target = "CAPRMEDIO-FIELD-METH-074--deterministic-git-fixture-bytes"

[[relations]]
type = "child_of"
target = "CAPRMEDIO-SPEC-TOOLS-METH-052--portable-text-byte-policy"
+++

# Decision — Deterministic temporary Git bytes

Temporary Git repositories used by deterministic Tests disable autocrlf and
select LF through repository-local configuration before staging.
Byte-sensitive fixtures write explicit LF or capture the bytes actually
materialized before asserting preservation; they never inherit ambient Git or
text-I/O policy.

This Decision completely replaces `CAPRMEDIO-FIELD-METH-074--deterministic-git-fixture-bytes`.
