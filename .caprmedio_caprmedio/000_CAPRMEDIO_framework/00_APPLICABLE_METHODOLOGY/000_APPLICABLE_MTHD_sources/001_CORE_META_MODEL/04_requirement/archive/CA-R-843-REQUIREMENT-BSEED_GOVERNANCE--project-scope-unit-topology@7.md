---
atom_id: CA-R-843
subject_scopes:
  - settings
version: 7
updated_at: 2026-08-22 02:24:53
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
relations:
  child_of:
    - CA-R-858-REQUIREMENT-BSEED_METAMODEL--define-scope-unit-name-prefix-and-places
    - CA-R-842-REQUIREMENT-BSEED_METAMODEL--define-ordered-upstream-unit
    - CAPRMEDIO-GOV-REQU-626--encode-project-settings-as-a-generated-toml-projection
    - CAPRMEDIO-GOV-REQU-647--register-project-settings-projection-mechanics
---
# Project Scope Unit topology

Each Project Graph State Projection must expose exactly one complete current `scope_units` list and no separate folder or contribution lists. Every row exposes the Unit's human-readable `name`, applicable filename `scope_path_name`, Structural kind, Structural level, Structural coordinate, and immediate `structural_parent`. Each row exposes exactly two physical-place paths: `authority_path` for the CAPRMEDIO Atom place and `delivery_path` for the realized Delivery place. Both are parent-relative when the Unit has a parent, while a root-level path is stated directly. `structural_parent` supplies the graph parent; the Projection adds no third `scope_path` and no separate authority or Delivery parent field. An `ordered_unit` row also exposes its `local_order` and derived `upstream_unit`, with absence explicit for the first ordered peer. When only a Delivery boundary is known, the row records that boundary, `delivery_status = "tbd"`, and no invented exact path. A Delivery place may be inside or outside `.caprmedio`, and a folder without a governed Scope Unit does not create a Scope Unit row. The Projection must not enumerate Content-role folders or their role-local organizational subfolders as Scope Units.
