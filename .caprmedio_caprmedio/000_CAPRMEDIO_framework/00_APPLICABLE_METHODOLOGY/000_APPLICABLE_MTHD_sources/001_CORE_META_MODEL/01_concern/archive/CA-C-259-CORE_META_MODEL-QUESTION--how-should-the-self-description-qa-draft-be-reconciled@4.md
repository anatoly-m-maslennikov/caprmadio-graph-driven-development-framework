---
subjects:
  governs: "Atom"
  depends_on:
    - "Atom/Claim"
    - "Artifact/Revision"
    - "Project"
    - "Operator"
priority: medium
version: 4
updated_at: "2026-09-22 23:02:20 +0000"
relations: {}
---
# Summary

How should the Self-description QA draft be reconciled?

## Claim

how should the identified Draft Atom be reconciled **with** active authority **and** Project Principles **without** losing useful information **or** promoting it?

### Draft under review

- archived Carrier: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/archive/CA-E--MMODEL-QA_CASE--validate-artifact-self-description-and-carrier-agreement@1.md`.
- inspected SHA-256: `8afd778ec5e5f5b2c407db2ae1f39b6a55cc29b8fc10b7296b0d24b889a77074`.
- review point: 50 of 79; campaign `draft-review-8afeac79`.

### Prior review finding

> **Revise** — Invert fixtures that require duplicate/default metadata; validate the admitted sole encoding and permitted agreement.
>
> Basis: `CA-D-267`, `CA-D-269`; I3. Reviewer confidence: 99%.

### Active authority cited by the review

- `CA-D-267@8`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-267-CORE_META_MODEL-DELIVERY--derive-address-facts-without-duplicated-frontmatter.md`; SHA-256 `d186c63788a393e2d20076b2a6138da43516248a7d9862ccc214d0589b425d40`.
- `CA-D-269@9`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-269-CORE_META_MODEL-DELIVERY--serialize-atom-subjects-in-frontmatter.md`; SHA-256 `f3b43a72109dbdb710295e46c37c1c5d86b7c15ff982f980bae8a845f6756f0b`.

### Principles to apply

- [CA-M-002](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md).
- [CA-M-005](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md).
- [CA-M-006](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md).
- [CA-R-1490](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md).
- [CA-E-001](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/06_evaluation/CA-E-001-PRINCIPLE-EVALUATION--make-governed-commitments-and-results-checkable.md).

### Resolution

resolved under the Operator's later explicit approval **to** update, replace, promote, **and** archive group 5. that approval supersedes the earlier no-promotion review constraint **and** the address-only proposal quoted above.

- Atom Properties have **`=1`** canonical internal location: frontmatter **or** a registered body section. literal `# Summary` **and** `## Claim` headings support programmatic extraction; applicable additional sections follow their own Delivery rules.
- DRY preserves one authoritative Property value **and** one owning declaration per Atom Relation. outward addresses **and** inverse Relations remain derived representations, **not** independent facts.
- every Plan requires its own Markdown file **and** Definition of Done; its optional folder does **not** create another Atom. the decomposing Plan declares `IS_DECOMPOSITION_OF`; derive `DECOMPOSES_INTO` from that same edge.
- selected Atom values remain inside their Carrier. unselected optional Settings overrides remain inherited **without** copying external authority.
- exact prior Draft **and** replaced authority bytes are preserved. the promoted content is Atom-specific; this decision does **not** impose Atom frontmatter on non-Atom Artifacts.
- this is an authority-content change, **not** a claim that the whole corpus, Tools, **or** compiled Projections have already migrated.

active successors: CA-E-506.
