---
cce_version: cce_1
cce_form: obligation
subjects:
  - provenance
project_graph_state:
  git:
    commit_each_atom_edit: true
    initialize_if_missing: true
    required: true
version: 11
updated_at: 2026-08-23 12:02:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-158--make-journals-canonical-for-governed-provenance
    - CAPRMEDIO-GOV-REQU-309--use-direct-typed-relation-change-set-commit-messages
---
# Mirror every governed file change in Git

Every governed repository-file change MUST be a separate Git commit for exactly one governed subject file identity and one classified change set: `ADD`, `MOVE`, `UPDATE`, `MOVE+UPDATE`, or `REMOVE`. `MOVE` changes Structural location; `UPDATE` changes content, filename, or other governed carrier state; and `MOVE+UPDATE` records both for the same identity. Before the commit is created, the same action MUST be appended to the Project Work Journal as one canonical structured file-change event plus every other related sidecar record required by that action. The commit MUST include the governed subject change and every and only receipt-bound Journal line sharing that action identity, even when those lines span multiple Journal carriers. The canonical Git message is a deterministic Projection of the structured file-change event and MUST NOT be stored again as an `action_message`. Related Journal carriers and lines are provenance sidecars of the same action, not additional governed subjects or new Hook triggers. Atom creation, accepted refinement, relocation, archival, and replacement use this same one-action boundary. Git preserves repository snapshots and Implementation changes as a secondary loss-prevention mirror but does not replace the Work Journal as canonical governed provenance.
