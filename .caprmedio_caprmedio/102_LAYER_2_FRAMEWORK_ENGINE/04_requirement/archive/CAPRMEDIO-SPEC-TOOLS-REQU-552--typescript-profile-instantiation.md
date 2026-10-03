+++
semantic_id = "CAPRMEDIO-SPEC-TOOLS-REQU-552--typescript-profile-instantiation"
revision_mode = "atomic"
content_role = "definition"
governance_origin = "internal"
relation_shape = "standalone"
status = "accepted"
priority = "high"
version = 1
updated_at = "2026-08-17 19:36:01"
llm_session_ids = ["codex:019f591f-04f6-70f2-8de7-828b7cccc69d"]

[[relations]]
type = "child_of"
target = "CAPRMEDIO-SPEC-TOOLS-REQU-551--typescript-candidate-profile"
+++

# Requirement — Separate profile references from applied instances

DSET must distinguish an evidence-derived framework reference from an applied
project-owned enforcement profile. A reference records the pinned pilot and
reusable six-gate schema for comparison; it is not executable authority in an
adopter. An applied instance lives under the target repository's local TOOL
profile root, declares its reference origin, and owns that project's commands,
paths, thresholds, file populations, warning debt, blockers, promotion gates,
and evidence revisions.

Profile resolution must prefer a local applied instance and fail closed in an
adopter when only a distributed framework reference exists. The framework
source repository may resolve its own reference for bounded read-only
comparison. Neither role promotes OYOHA product, Obsidian, delivery, debt, or
supportability settings into TypeScript defaults.

## Rationale

The clean-upstream comparison proved that the six gate categories and
inspection mechanics generalize, while concrete commands, owners, counts,
thresholds, blockers, and delivery topology remain project-local. Encoding the
role boundary prevents a useful pilot snapshot from becoming accidental
cross-project authority.

This emitted Requirement is immutable. Later correction or replacement
requires a linked atom or append-only lifecycle event.
