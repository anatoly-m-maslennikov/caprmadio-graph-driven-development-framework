---
subject_scopes:
  - artifact-catalog
tier: core
version: 2
updated_at: 2026-08-19 16:45:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-METH-035--discover-project-artifacts-by-identity
    - CAPRMEDIO-GOV-METH-037--keep-the-control-plane-current
  child_of:
    - CAPRMEDIO-META-REQU-085--separate-active-authority-from-preserved-history
---

# Discover active authority by identity

Every CAPRMEDIO skill begins at the target repository's `.caprmedio` control root,
locates the unique settings carrier, and resolves requested artifact, rule,
document, and carrier identities within that bounded tree. Zero active matches
or multiple active matches stop.

Active discovery includes installed methodology, settings, active atomic
artifacts, Journals, and applicable Projections. It excludes every role-local
`archive/` subtree and never falls back to root framework source, inert legacy
material, completed migrations, a remote copy, or a global installation.

CAPRMEDIO-to-CAPRMEDIO references persist identities, not physical carrier paths. A tool
may retain a resolved path in memory for the current operation. Implementation
outside `.caprmedio` may be located only after accepted authority identifies the
implementation subject.

## Rationale

The merged successor preserves topology-independent discovery while aligning
current authority with role-local archives and the project-local control-plane
boundary.
