+++
artifact_subtype = "defect"
semantic_id = "CAPRMEDIO-SPEC-SKILLS-CONC-078--installed-skill-integrity"
revision_mode = "atomic"
content_role = "observation"
governance_origin = "external"
relation_shape = "standalone"
status = "accepted"
priority = "high"
authority = "external:skill-refactor-audit"
claim = "Installed wrapper and shared-runtime verification accepts post-install content mutation because it reports observed digests without comparing them to a sealed installation identity."
version = 1
updated_at = "2026-08-17 19:36:01"
llm_session_ids = ["codex:019f591f-04f6-70f2-8de7-828b7cccc69d"]
rationale = "A verifier that authenticates only shape can bless modified executable instructions and code as a valid DSET installation."
promotion = {}

[[relations]]
type = "child_of"
target = "CAPRMEDIO-SPEC-SKILLS-REQU-568--shared-skill-runtime"
+++

# Defect — Installed skill integrity is not authenticated

The installed wrapper verifier accepts a changed `SKILL.md`, and the runtime
verifier accepts changed installed runtime code. Receipts can therefore report
the modified digest as success instead of rejecting drift from the source-bound
installation manifest.

This emitted Problem atom is immutable. Resolution requires implementation,
proof, and an append-only lifecycle event.
