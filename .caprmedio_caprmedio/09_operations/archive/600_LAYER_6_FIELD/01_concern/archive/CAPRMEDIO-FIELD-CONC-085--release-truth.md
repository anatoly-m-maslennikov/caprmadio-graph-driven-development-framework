+++
artifact_subtype = "defect"
semantic_id = "CAPRMEDIO-FIELD-CONC-085--release-truth"
revision_mode = "atomic"
content_role = "observation"
governance_origin = "internal"
relation_shape = "standalone"
status = "accepted"
priority = "high"
version = 1
updated_at = "2026-08-17 19:36:01"
llm_session_ids = ["codex:019f591f-04f6-70f2-8de7-828b7cccc69d"]
+++

# Defect — Active Change and release truth contradict each other

The active Change still models a bootstrap transaction targeting `0.3.1` and
PR 9, while the evergreen version surfaces treat `0.3.1` as the published
baseline and assign active development to `0.4`. The release gate therefore
cannot identify one current candidate transaction.

## Rationale

This is a current operations defect because the repository exposes mutually
exclusive release states for the same version and Change.
