---
artifact_subtype: change_plan
subject_scopes:
  - scope-topology
version: 6
updated_at: 2026-08-19 07:24:03
---
# Apply compact Structural-unit prefixes and finish the Structural migration

The physical root and `.caprmedio` Structural directories are partly migrated. The authority, identities, settings, references, and verification remain incomplete. `CAPRMEDIO` remains the full framework and Project name; `CA` becomes its short Project prefix.

1. Replace the current Project identity authority with one Core Project Requirement that declares scope `project`, full name `CAPRMEDIO`, and prefix `CA`; change the generated `artifacts.identity.project_prefix` value from `CAPRMEDIO` to `CA` without renaming the framework.
2. Complete the Structural-unit declaration authority before migrating carriers. One Standard Project Requirement must declare each immediate Project Layer's scope, full name, short prefix, and `local_order`. Feature declarations remain in their owning Layer and declare scope, full name, and short prefix without `local_order`.
3. Use this accepted compact mapping:

   | Structural unit | Scope | Full name | Prefix | Local order |
   |---|---|---|---|---|
   | Project | `project` | `CAPRMEDIO` | `CA` | — |
   | Meta-unit | `metamodel` | `METAMODEL` | `META` | — |
   | Meta-unit | `governance` | `GOVERNANCE` | `GOV` | — |
   | Project Layer | `framework_methodology` | `FRAMEWORK_METHODOLOGY` | `FR_MTHD` | `1` |
   | Project Layer | `framework_engine` | `FRAMEWORK_ENGINE` | `FR_ENGN` | `2` |
   | Project Layer | `users_documentation` | `USERS_DOCUMENTATION` | `FR_USERDOC` | `3` |
   | Project Layer | `extensions` | `EXTENSIONS` | `EXTNS` | `4` |
   | Project Layer | `releases` | `RELEASES` | `RELSS` | `5` |
   | Project Layer | `field` | `FIELD` | `FIELD` | `6` |
   | FRAMEWORK_ENGINE Feature | `skills` | `SKILLS` | `SKILLS` | — |
   | FRAMEWORK_ENGINE Feature | `tools` | `TOOLS` | `TOOLS` | — |
   | FRAMEWORK_ENGINE Feature | `app` | `APP` | `APP` | — |

4. Add the missing SEMANTICS Meta-unit prefix declaration before execution; do not invent its prefix inside the migration Tool.
5. Reconcile existing authority with the mapping: rename `DOCUMENTATION` authority to `USERS_DOCUMENTATION`; place `EXTENSIONS` immediately after `USERS_DOCUMENTATION` as Project Layer `4`, shift `RELEASES` to `5`, and shift `FIELD` to `6`; update Project composition, Layer ordering, Layer scope, dependency, and Contract authority for the resulting six Project Layers; encode all missing Layer and Project prefixes; and revise the `ca-` Skill-prefix rule so it no longer says that `CA` is not the Project prefix.
6. Repair and extend the deterministic migration Tools so they resolve the current `.caprmedio/caprmedio_project_settings.toml` carrier and current Structural directories rather than removed settings and `IMPLEMENTATION` paths. Require dry-run, explicit target inventory, collision detection, transactional application, rollback, and a complete backup under `.caprmedio_runtime/migrations/`.
7. Verify the already renamed root and `.caprmedio` directories, then migrate the remaining active carrier identities and filenames from the long Project and Structural-unit prefixes to the compact prefixes.
8. Rewrite every affected active relation, exact revision reference, generated binding, source-map entry, Tool constant, Skill instruction, workflow, and current native document. Preserve `CAPRMEDIO` wherever it means the full framework or Project name rather than an identity prefix.
9. Do not rename or rewrite archived carriers solely for this convention change. Do not rewrite append-only Journal records. Resolvers and migration verification must continue to recognize preserved historical identities without treating them as active naming authority.
10. Rebuild Project Settings and all affected Projections from the migrated active frontier, then reach a generator fixed point.
11. Verify that every active carrier, active relation endpoint, configured Project prefix, Structural directory, Tool, Skill, workflow, and current document uses the accepted compact mapping; verify that no active `CAPRMEDIO-` identity prefix or long Structural prefix remains except where explicitly registered as a historical reference.
12. Close this Plan only after the migration verifier, deterministic project-integrity validator, relation checks, generated-carrier currentness checks, and repository diff checks all pass.
