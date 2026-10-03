+++
artifact_subtype = "defect"
semantic_id = "CAPRMEDIO-SPEC-TOOLS-CONC-058--immutable-toml-migration"
revision_mode = "atomic"
content_role = "observation"
governance_origin = "internal"
relation_shape = "standalone"
status = "accepted"
priority = "high"
authority = "repository:self-host-review"
claim = "The TOML migration plans writes to byte-stable sealed atoms, promoted proof, and registered legacy Decision carriers."
version = 1
updated_at = "2026-08-17 19:36:01"
llm_session_ids = ["codex:019f591f-04f6-70f2-8de7-828b7cccc69d"]
rationale = "A representation migration cannot prove self-application by rewriting the immutable history that authorizes and evidences it."
promotion = {}

[[relations]]
type = "relates_to"
target = "CAPRMEDIO-GOV-REQU-395--verbose-project-settings"
+++

# Defect — TOML migration rewrites immutable history

The current migration planner treats all DSET Markdown YAML frontmatter as
mutable. Its preview therefore includes sealed atomic carriers, promoted proof
records, and registered legacy Decision carriers, and reconciliation attempts
to legitimize the mutation by rebasing digests.

## Completion condition

Immutable carriers are explicitly classified, excluded byte-for-byte from
conversion and reference rewriting, and covered by pre/post digest tests. Seal
rebasing is removed. Only mutable CAPRMEDIO-owned authority and projections are
eligible for the format cutover.
