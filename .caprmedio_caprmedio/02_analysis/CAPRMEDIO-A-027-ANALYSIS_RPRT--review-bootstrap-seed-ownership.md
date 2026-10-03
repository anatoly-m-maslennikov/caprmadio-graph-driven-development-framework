---
subject_scopes:
  - scope-topology
version: 1
updated_at: 2026-08-19 16:25:58
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
---
# Review Bootstrap Seed ownership

## Result

The review assigns every scanned governed carrier exactly one current or proposed owner without relocating or changing it. The proposed Bootstrap Seed split is METAMODEL, SEMANTICS, and GOVERNANCE. Project-owned carriers remain owned by the Project root, its Project Layers, or their Features.

One current META carrier is a preserved-owner exception rather than an inferred relocation: `CAPRMEDIO-META-REQU-723--define-governance-scope`. Action 6 must decide whether its one claim belongs in SEMANTICS or GOVERNANCE before any target relocation is proposed.

## Review method

The review scanned regular files below `.caprmedio/` only. It excluded `.f4f/`, `.git/`, `.caprmedio_runtime/`, symlink targets, and native root implementation. It did not assign CAPRMEDIO Artifact coordinates to native targets.

Each governed carrier was classified once by these rules:

1. Artifact form is Journal for the three admitted NDJSON work journals; Projection for the named or generated Catalog, Map, Hub, and Project Settings views; every other governed carrier is an Atom.
2. Content role is derived from the nearest canonical role directory. The root Goal is Requirement, the Project Settings Projection is Implementation, and Journals retain their form-specific cross-role record function.
3. All current GOV carriers belong to Bootstrap GOVERNANCE because their current claims control accepted meaning through carrier, identity, placement, frontmatter, validation, provenance, versioning, or change constraints.
4. Current META carriers with `artifact-model`, `scope-topology`, or `subject-scope` as their declared Subject scope belong to Bootstrap METAMODEL. The remaining current META carriers belong to Bootstrap SEMANTICS, except the preserved-owner exception stated above.
5. Project-root carriers, work journals, Project Layers, and their Features retain their current Project owner. An Artifact form, Content role, Type, lifecycle state, or filename does not override that semantic-owner rule.
6. A relocation is address-equivalent only when all carrier-derived facts and governed meaning remain unchanged. No relocation has been approved as address-equivalent by this review. Every META or GOV carrier assigned to a Bootstrap Seed unit is therefore classified as governed relocation because its current owner coordinate changes. Retained Project ownership has no relocation disposition yet.

## Coverage evidence

The input snapshot contained 1,358 regular files under `.caprmedio/`: 1,354 governed carriers and four `.gitkeep` structural placeholders. The review does not traverse the ten convenience symlinks under `000_caprmedio_framework`. The new P-025 Plan and this Analysis Report add two governed carriers, so the final classified set is 1,356 governed carriers plus four structural placeholders, or 1,360 regular files in total.

| Artifact form | Final count | Coverage rule |
| --- | ---: | --- |
| Atom | 1,341 | Every governed carrier other than the identified Journal or Projection carriers |
| Journal | 3 | `010_journals` NDJSON record sequences |
| Projection | 12 | Project Settings, Project Settings Map, and named Catalog or Hub views |
| Governed total | 1,356 | Exactly one Artifact-form class per carrier |
| Structural placeholder | 4 | Empty Layer placeholders; not governed Artifacts |

| Owner classification | Final count | Relocation disposition |
| --- | ---: | --- |
| Project root | 308 | Retain owner; no relocation is proposed |
| Project work journals | 3 | Retain Project owner; no relocation is proposed |
| Bootstrap METAMODEL | 149 | Governed relocation from the current META unit |
| Bootstrap SEMANTICS | 147 | Governed relocation from the current META unit |
| Preserved current META semantic owner | 1 | No inferred relocation; Action 6 review exception |
| Bootstrap GOVERNANCE | 422 | Governed relocation from the current GOV unit |
| FRAMEWORK_METHODOLOGY Layer | 47 | Retain Layer owner; no relocation is proposed |
| FRAMEWORK_ENGINE Layer | 99 | Retain Layer owner; no relocation is proposed |
| FRAMEWORK_ENGINE Application Feature | 7 | Retain Feature owner; no relocation is proposed |
| FRAMEWORK_ENGINE Skills Feature | 20 | Retain Feature owner; no relocation is proposed |
| FRAMEWORK_ENGINE Tools Feature | 153 | Retain Feature owner; no relocation is proposed |
| Governed total | 1,356 | Exactly one owner class per carrier |

The scan includes all nine Content roles. The owner algorithm is Type-independent, so it covers every present Type without treating a legacy filename spelling as a second owner. It includes all lifecycle states present in the final classified set: 652 active, 687 archived, six draft, four done, and seven solved carriers.

## Carrier boundaries

Generated Project Settings and its YAML Source Map are Projections owned by their Project Implementation scope. They are non-authoritative outputs, not new settings authority. The three work journals are Project-governed Journal carriers. The ten `000_caprmedio_framework` symlinks are convenience links only. Root implementation, framework settings, repository documentation, and other native targets remain Implementation unless separately admitted or bound as governed Artifacts.

Historical Catalogs, Hubs, TOML reference carriers, and archived Atoms retain the owner selected by the same semantic rule. Their lifecycle is preserved in this review; it is not a reason to discard, relocate, or reclassify them.

## Review exception

`CAPRMEDIO-META-REQU-723--define-governance-scope` has a unique current META semantic owner but sits on the METAMODEL–SEMANTICS–GOVERNANCE boundary. The current record cannot be assigned to a narrower Bootstrap Seed unit with at least 95% confidence without deciding whether its definition of GOVERNANCE scope is a semantic definition or a governance-owned self-definition. The carrier is assigned once to its preserved current META semantic owner for this no-mutation review. P-020 action 6 must resolve the boundary before action 8 freezes a final target inventory.

## Handoff

P-020 action 6 receives the single preserved-owner exception and may review structural gaps or reducible scope claims. P-020 actions 7–15 remain responsible for any semantic remediation, frozen inventory, approved migration, relation repair, generated-state work, and closure. This review approves none of those changes.
