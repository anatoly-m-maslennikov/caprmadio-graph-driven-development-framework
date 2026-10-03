---
artifact_subtype: implementation_decision
subject_scopes:
  - layout
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMEDIO-GOV-METH-032--separate-methodology-from-applied-project-artifacts
---

# Decision — Keep the control plane current

`.caprmedio` owns only current project-local DSET truth:

- the unique settings carrier;
- installed methodology;
- applied project, layer, and Version atoms;
- current evergreen specifications and plans; and
- current evidence and verification records.

Historical aggregate registries, completed migration records, compatibility
snapshots, pre-current change folders, and retained pre-current documentation
belong to the inert repository archive outside `.caprmedio`.

Skills and current semantic compilation search only `.caprmedio`. They do not
consult the external archive, use it as fallback authority, or include it in
current coverage. Git history and the archive's own readme provide historical
return paths when an operator deliberately investigates the past.

## Rationale

The active control plane should answer what governs the project now. Historical
transport and compatibility material answers a different question and must not
compete with current data governance.

## Primary claim

The project .caprmedio tree contains only current settings, installed methodology, applied artifacts, and Version truth; historical aggregates, completed migration records, and compatibility snapshots live in the repository's inert legacy archive outside .caprmedio and are never skill-discovery or current-compilation inputs.

## Rationale

The project-local DSET tree is an active data-governance plane. Mixing historical transport records with current authority makes discovery ambiguous and obscures the state that skills must use.
