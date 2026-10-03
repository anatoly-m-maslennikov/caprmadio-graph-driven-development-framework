---
subject_scopes:
  - lifecycle-traceability
version: 4
updated_at: 2026-08-20 20:04:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
---
# Migrate replacement relations to direct replaced_by

1. [x] Register one canonical relation-type dictionary in which `replaced_by` is direct and `replacement_of` is its derived inverse.
2. [x] Require every direct relation authored by an active Atom to target an active Atom with `target_global_tier <= source_global_tier`.
3. [ ] Inventory every active, draft, done, and archived carrier that authors `replacement_of` or `replaced_by`.
4. [ ] For each recoverable replacement, require the successor to exist as an active Atom before changing the predecessor.
5. [ ] Add direct `replaced_by` to each predecessor and archive that predecessor in the same governed `MOVE+UPDATE`; then remove every authored `replacement_of` from the successor.
6. [ ] Preserve one-to-one, split, merge, many-to-many, and multi-generation replacement chains by storing direct edges on predecessor carriers and deriving inverse and transitive views.
7. [ ] Keep replacement Journal events as provenance when useful, but do not use Journals as a second owner of replacement-relation meaning.
8. [ ] Update relation schemas, writers, validators, graph traversal, commit-context gathering, and Projections to accept direct names and derive inverse names only.
9. [ ] Verify that no Atom authors `replacement_of`, every archived replaced predecessor authors `replaced_by`, every successor was active when its edge was created, active direct relations satisfy lifecycle and global-tier direction, and inverse navigation exactly mirrors the direct graph.
