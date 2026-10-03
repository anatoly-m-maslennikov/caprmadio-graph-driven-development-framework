---
subject_scopes:
  - artifact-model
version: 2
updated_at: 2026-08-19 07:37:46
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
---
# Apply the Content-role and Type Artifact model

1. [x] Resolve the exact active authority frontier for Content roles, Types, default internal Types, external Type naming, role letters, Type short names, Atom identity, numbering, and carrier-derived classification.
2. [ ] Execute this Plan in the same identity-migration transaction as P-014 or after P-014 establishes the final Project and Structural-unit prefixes so each active carrier is renamed only once.
3. [ ] Build a deterministic lossless migration map from every enabled legacy Artifact Type and subtype pair to exactly one Content-role and Type pair, failing on missing, ambiguous, or colliding mappings.
4. [ ] Replace `artifact_subtype`, `enabled_subtypes`, Type/subtype route pairs, and other subtype-dependent active schemas or settings with the Content-role and Type model; preserve unrelated Tool-specialization taxonomies.
5. [ ] Register and project every enabled Type, its owning Content role, Governance locus, default status where applicable, canonical short name, and external-name derivation or explicit non-default name.
6. [ ] Allocate one project-wide monotonic Atom number sequence per Content role and migrate active and draft Atom identities to `<PROJECT>-<ROLE_LETTER>-<NNN>-<TYPE_SHORT_NAME>[-<SCOPE_PATH>]--<SUMMARY>.<ext>` without reusing numbers or changing immutable summaries.
7. [ ] Rewrite every affected active relation endpoint, exact revision reference, source map, Project Setting, Projection frontier, Tool selector, Skill instruction, and current native document; preserve done and archived carriers unchanged as historical identities.
8. [ ] Update writers, resolvers, validators, migrations, and generated views to derive Content role and Type from canonical placement and filename and to reject Artifact subtype properties or ambiguous classification.
9. [ ] Regenerate affected Project Settings and Projections to a fixed point, then verify identity uniqueness, role-local numbering, Type-short-name uniqueness, relation resolution, default-Type resolution, external Type naming, and absence of the Artifact subtype model from active authority and realization.
