+++
artifact_subtype = "defect"
semantic_id = "CAPRMEDIO-SPEC-SKILLS-CONC-077--llm-session-provenance"
revision_mode = "atomic"
content_role = "observation"
governance_origin = "internal"
relation_shape = "standalone"
status = "accepted"
priority = "high"
version = 1
updated_at = "2026-08-17 19:36:01"
llm_session_ids = ["codex:019f591f-04f6-70f2-8de7-828b7cccc69d"]

[[relations]]
type = "recurrence_of"
target = "CAPRMEDIO-SPEC-TOOLS-CONC-055--runtime-terminalization"
+++

# Defect — Thin wrappers erase LLM session provenance

All thin wrappers invoke `dset skills context` without an LLM session ID, and
the CLI defaults the field to an empty list. The governing runtime interprets
an empty list as a human-only run, so ordinary LLM-driven skill runs are
misclassified unless a host supplies an undocumented extra argument.

## Rationale

This is a current skill defect because session provenance is required at the
wrapper-to-runtime boundary and empty provenance has a defined, different
meaning.
