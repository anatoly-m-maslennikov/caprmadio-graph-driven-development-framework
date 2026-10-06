+++
semantic_id = "CAPRMEDIO-GOV-REQU-386--self-hosted-governance-loci"
revision_mode = "atomic"
content_role = "definition"
governance_locus = "internal"
status = "accepted"
priority = "high"
authority = "operator:anatoly-m-maslennikov"
claim = "In the DSET self-hosting repository, root methodology sources and applied project artifacts outside the installed methodology are internally governed, while the installed methodology under .caprmedio/000_caprmedio_methodology is externally governed from the consuming project's context."
version = 1
updated_at = "2026-08-17 19:36:01"
llm_session_ids = ["codex:019f591f-04f6-70f2-8de7-828b7cccc69d"]
rationale = "Recursive self-hosting gives the same methodology two contextual roles: the repository owns the root framework source, while the applied project consumes the installed copy through the same boundary an adopter uses."

[promotion]
affected_children = ["meta", "governance", "tool", "skill", "implementation", "ops"]
applies_unchanged = true
local_context_required = false

[[relations]]
type = "child_of"
target = "CAPRMEDIO-META-REQU-196--three-axis-artifact-routing"
+++

# Requirement — Self-hosted governance loci

This repository assigns governance locus by contextual boundary:

| Repository surface | Default governance locus |
|---|---|
| Project-root framework and methodology sources outside `.caprmedio` | `internal` |
| Installed framework under `.caprmedio/000_caprmedio_methodology` | `external` |
| Other applied project artifacts under `.caprmedio` | `internal` |

The installed methodology is external from the consuming project's context even
when it was synchronized from root sources in the same repository. This
classification describes governance responsibility, not Git authorship,
filesystem ownership, or byte identity.

The table supplies defaults for non-relational artifacts. An artifact whose
primary subject is a relation uses `governance_locus = "relation"` regardless
of its carrier path, and its endpoints independently declare internal or
external origin.
