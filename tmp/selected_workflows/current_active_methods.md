# Current active Method input projection

Derived execution input only. Sources remain authoritative. Selected R/E/D inputs are separate. No harvesting or broad audit is authorized.

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-111-CORE_META_MODEL--author-one-cce-claim-and-derived-summary.md

SHA-256: c762357b6e9c9478e559d2abeaa5dc86ccd316e66957123b50d5391e0ba703c5

```markdown
---
subjects:
  governs: "Atom Claim Authoring"
  depends_on:
    - "Atom/Claim"
    - "CCE"
    - "Atom/Summary"
version: 25
updated_at: "2026-10-02 20:25:13 +0400"
relations: {"relates_to": ["CA-R-1624", "CA-O-103", "CA-D-479", "CA-R-1465"]}
atom_id: "CA-M-111"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Author one CCE Claim and derived Summary

## Scope

authoring an Atom's primary contribution, its applicability, **and** its derived Summary.

## Claim

**to** author one CCE Claim **and** its derived Summary, an Author **must** use these authoring constraints:

- express **`=1`** independently replaceable contribution using the applicable CCE Content Role profile. carry it under the primary contribution heading registered **in** CA-D-479 rather than imposing the literal heading Claim on **every** role.
- resolve **`=1`** Claim Target Scope Unit independently of ownership. select the current Scope Unit as the authoring default **or** an explicitly permitted different target; carry the resolved value under CA-D-482. express applicability under CA-D-495. for RMED, describe what the Claim applies **to**, including applicable conditions **and** exclusions, **in** Scope; do **not** merely repeat the carried current **or** target Scope Unit; those restrictions alone do **not** make the Atom Relational.
- keep Details within the primary contribution under CA-R-1624. for RMED, read the Claim within its Scope; Details **must not** change either. **if** supporting content reveals an incomplete **or** inaccurate contribution **or** applicability, revise the affected Scope **or** primary contribution explicitly **and** recheck agreement; do **not** hide the change **in** Details.
- write Summary **only after** the other body sections **and** the contribution review are complete. shorten the finalized primary contribution under CA-R-1465 **and** CA-R-1273. for RMED, summarize the Claim within its finalized Scope, **not** the Scope alone; do **not** substitute supporting Results **or** TLDR as the source.
- for an existing Atom, retain the established Summary **and** check its faithfulness; **if** the Summary needs changing, use a new Atom identity under CA-R-1464.
- derive **every** Translation from the full corresponding source content, **not** the Summary.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-112-CORE_META_MODEL-METHOD--use-english-as-the-project-language.md

SHA-256: 86b21d1fd3d11fae92d60f901cd1026201711d3a7801a16350c5049efc41e595

```markdown
---
subjects:
  governs: "language"
  depends_on:
    - "CCE"
version: 14
updated_at: "2026-09-29 22:20:38 +0000"
relations:
  child_of:
    - CA-R-940
atom_id: "CA-M-112"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary
Use English as the Project language

## Scope
expressing CAPRMEDIO Project meaning.

## Claim

**to** express CAPRMEDIO Project meaning, the Author **must** use English as the base language.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-113-CORE_META_MODEL--write-claims-in-caprmedio-controlled-english.md

SHA-256: 81a512b270a42421edf5a5a3f576b334581e8b407b8acd1d4f7d3370f3f54e77

```markdown
---
subjects:
  governs: "language"
  depends_on:
    - "artifact-model"
    - "CCE"
    - "Author"
    - "Atom/Claim"
version: 17
updated_at: "2026-10-02 20:25:13 +0400"
relations:
  child_of:
    - CA-M-111
    - CA-M-112
    - CA-R-941
  relates_to:
    - CA-M-229
    - CA-M-301
    - CA-M-294
    - CA-M-307
    - CA-M-308
    - CA-M-315
atom_id: "CA-M-113"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Write Claims in CAPRMEDIO Controlled English

## Scope

Claim authoring **in** CAPRMEDIO Controlled English.

## Claim

**to** write one Claim **in** CAPRMEDIO Controlled English, the Author **must** satisfy **all** of the following:

- use the controlled English subset of the identified CCE version.
- name **every** necessary participant **and** relation explicitly.
- state **every** necessary modality, quantity, condition, **and** boundary explicitly.
- use exact canonical Terms owned by active Definition Atoms.
- resolve the effective CCE Role Profile under CA-M-308-CORE_META_MODEL-CORE-METHOD--resolve-the-effective-cce-role-profile **and** satisfy that profile under CA-M-315-CORE_META_MODEL-CORE-METHOD--validate-claims-against-effective-cce-role-profiles.
- choose wording under CA-M-294-CORE_META_MODEL-METHOD--use-simpler-words-without-losing-meaning.
- exclude ambiguous pronouns, anaphora, ellipsis, unstated defaults, **and** mixed logical groupings.
- make the content understandable under CA-M-301-CORE_META_MODEL-METHOD--make-atom-claims-easy-to-understand **and** render Terms **and** CCE Operators under CA-M-229-CORE_META_MODEL--render-governed-terms-and-cce-operators-distinctly.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-114-CORE_META_MODEL--derive-terminology-projection-from-definition-atoms.md

SHA-256: 16513dca0a7370d9a98999f537da293fd8d14ae4d9a47fee7f70fb1f8a9b1dd6

```markdown
---
subjects:
  governs: "Terminology Projection Derivation"
  depends_on:
    - "Projection/Type: Catalog"
    - "Generator"
    - "Definition Atom"
    - "Governed Term"
    - "Project"
    - "Atom/Claim"
    - "Subject"
    - "Subject Path"
    - "Entity"
    - "Term"
    - "Action"
    - "Workflow"
version: 20
updated_at: "2026-10-01 21:33:03 +0400"
relations: {}
atom_id: "CA-M-114"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Derive Terminology Projection from Definition Atoms

## Scope

derivation of a terminology Projection from active Definition Atoms.

## Claim

**to** build a terminology list using the Catalog Type, the Generator **must** derive **every** Governed Term's name **and** Project-specific meaning from its active Definition Atom. read the Term named by the defining Claim **and** verify that the Definition Atom's GOVERNS Subject Relation identifies its defined target under CA-R-1279-CORE_META_MODEL-CORE-REQUIREMENT--govern-every-defined-term. extract Term references from **every** named component of a Subject Path, **not** **only** its terminal component; obtain **every** referenced Term's meaning from that Term's own defining Claim, **not** by treating **all** path components as definitions supplied by the referencing Atom. include an entry **only** **when** the defining Claim establishes a Project-specific meaning; consistent use, capitalization, **or** occurrence **in** a Subject Path alone does **not** supply defining authority. an unresolved named component is a Term-reference gap **to** report, **not** permission **to** invent a definition **or** silently treat that component as ordinary vocabulary. exclude words **and** phrases used **only** with their ordinary English meanings. retain the source reference **without** classifying the direct Subject reference **or** a complete composite Subject Path as a Term **or** creating independent vocabulary authority.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-115-CORE_META_MODEL--author-one-cce-claim-per-atom.md

SHA-256: caf1459a6cce687b0e981e258783ed8efa417f289b6034623ddec7c6f6645dcc

```markdown
---
subjects:
  governs: "Atom Claim Boundary Authoring"
  depends_on:
    - "Atom"
    - "Claim"
    - "Atom/Claim"
    - "CCE"
    - "Author"
    - "Scope Unit"
    - "Atom/Claim/Target Scope Unit"
    - "Relational Atom"
version: 23
updated_at: "2026-09-28 15:12:22 +0400"
relations: {}
atom_id: "CA-M-115"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Author one CCE Claim per Atom

## Scope

authoring the boundary of **`=1`** independently replaceable Atom contribution.

## Claim

**to** author an Atom, the Author **must** perform **all** of:

1. identify one statement whose complete effect **must** be accepted, replaced, **and** retired together.
2. split **every** independently replaceable component into another Atom.
3. resolve **`=1`** Claim Target Scope Unit independently of ownership. select the current Scope Unit **as** the default during authoring **or** select an explicitly permitted different target; carry the resolved value under CA-D-482-CORE_META_MODEL-DELIVERY--carry-the-resolved-claim-target-scope-unit. express applicability **in** the registered body sections under CA-D-495-CORE_META_MODEL-CORE-DELIVERY--carry-applicability-in-the-registered-body-sections; for RMED, use Scope **and** write the Claim within that applicability; those restrictions alone do **not** make the Atom Relational.
4. write the complete Claim **in** the current CCE version.
5. remove **every** duplicate alternate authoritative statement.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-116-CORE_META_MODEL-CORE--derive-navigation-projections-from-the-cce-claim.md

SHA-256: e0eff5e7fcfbe3a2384f00b3a195829e49136e5ecbda2a929e5cc6ff83d4a22d

```markdown
---
subjects:
  governs: "Atom Claim Projection"
  depends_on:
    - "Atom/Claim"
    - "Atom/Summary"
    - "Translation"
version: 14
updated_at: "2026-10-02 20:25:13 +0400"
relations:
  relates_to:
    - CA-M-294
atom_id: "CA-M-116"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Derive navigation Projections from the CCE Claim

## Scope

navigation values derived from an Atom Claim.

## Claim

**to** derive navigation values from an Atom Claim, the Generator **must** derive the concise human-readable Summary **when** creating the Atom **and** derive requested Translations directly from the Claim, **without** adding authoritative meaning. choose wording under CA-M-294-CORE_META_MODEL-METHOD--use-simpler-words-without-losing-meaning. for an existing Atom identity, retain **and** check the Summary under CA-R-1273-CORE_META_MODEL-CORE-REQUIREMENT--keep-summary-source-faithful **and** CA-R-1464-CORE_META_MODEL-REQUIREMENT--keep-summary-fixed-for-atom-identity rather than regenerating it as an independent Projection.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-120-CORE_META_MODEL-CORE--compile-the-direct-relation-registry.md

SHA-256: 4f1a2004c885b1134ef57e309c37e1ab14c86bf008a3374fc93bbc20a2c104db

```markdown
---
subjects:
  governs: "Relation Kind/registry compilation"
  depends_on:
    - "Relation Kind"
    - "Relation Kind/Metadata"
    - "CAPRMEDIO Graph"
    - "Applicable Methodology"
    - "Relation/authority"
    - "Atom/Content Role: Requirement"
    - "Projection"
    - "Generator"
    - "Relation"
    - "Single Source of Truth"
version: 14
updated_at: "2026-10-02 20:25:13 +0400"
relations:
  child_of:
    - CA-R-295
    - CA-R-326
  method_for:
    - CA-R-806
    - CA-R-1246
    - CA-R-1437
    - CA-R-1472
atom_id: "CA-M-120"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Compile the direct-relation registry

## Scope

direct-relation registry compilation.

## Claim

**to** compile the direct-relation registry, the Generator **must** perform **all** of:

1. derive the metadata required by CA-R-806-CORE_META_MODEL-GENERAL-REQUIREMENT--register-complete-relation-kind-metadata for **every** declared Relation Kind from its active governing Requirement authority. report missing **or** conflicting metadata **without** inventing a graph owner, meaning, endpoint class, **or** constraint.
2. group Relation Kinds by their owning kind of CAPRMEDIO Graph **and** resolve **every** lookup by graph kind **and** canonical name. reuse the same source authority across instances of the same graph kind governed by the same Applicable Methodology; do **not** merge registrations from different graph kinds because their names match.
3. derive inverse navigation from its declared owning direction **without** independently authoring an inverse Relation fact. distinguish **`=1`** authoritative declaration for an independently authored Relation fact from the governing derivation authority **and** input facts of a derived Relation under CA-R-1437-CORE_META_MODEL-CORE-REQUIREMENT--keep-one-source-for-each-relation-fact; do **not** invent a direct source declaration for a computed result.
4. retain source traceability for the compiled registry as a non-authoritative Projection. resolve cross-graph **and** authoritative-source endpoints against their admitted graph contexts under CA-R-806-CORE_META_MODEL-GENERAL-REQUIREMENT--register-complete-relation-kind-metadata **and** CA-R-1472-CORE_META_MODEL-GENERAL-REQUIREMENT--admit-typed-secondary-graph-connections. cross-graph references **or** views **must not** register a foreign Relation Kind as native **or** reclassify an external endpoint as a native node of the receiving graph.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-121-CORE_META_MODEL-METHOD--evaluate-scope-expressions.md

SHA-256: 6b5139e9e507051863dcac7faa4eb75fb70cd38592e68bf05914e9dc6accdb14

```markdown
---
subjects:
  governs: "Scope Expression Evaluation"
  depends_on:
    - "Scope Expression"
version: 17
updated_at: "2026-09-29 22:34:56 +0000"
relations: {}
atom_id: "CA-M-121"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary
Evaluate Scope Expressions

## Scope
evaluation of a Scope Expression.

## Claim
**to** evaluate one Scope Expression, the Resolver **must** perform **all** of:

1. resolve **every** exact Atom ID **or** other atomic identity **to** **`=1`** Governed Entity.
2. interpret **all** `<ENTITY_KIND>` as **every** Governed Entity of that kind within Atom Scope.
3. interpret **or** as set union.
4. interpret **and** as set intersection.
5. interpret **without** as left-side set exclusion.
6. interpret **where** as retention of **only** members whose field predicate evaluates **to** true according **to** `CA-M-122-CORE_META_MODEL-METHOD--evaluate-condition-expressions`.
7. evaluate the innermost parenthesized set function **before** its containing set function.
8. use another Scope function **only** **when** an active CCE Method gives that function **`=1`** set meaning.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-122-CORE_META_MODEL-METHOD--evaluate-condition-expressions.md

SHA-256: f9c8e95aaf79f92b2c92d3cedfdf173870102cac58f6a134fedb830cfe3c5197

```markdown
---
subjects:
  governs: "CCE Condition Expression Evaluation"
  depends_on:
    - "CCE Condition Expression"
    - "CCE Operator"
version: 16
updated_at: "2026-10-01 21:33:03 +0400"
relations:
  child_of:
    - CA-M-113
atom_id: "CA-M-122"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Evaluate Condition Expressions

## Scope

evaluation of CCE Condition Expressions.

## Claim

**to** evaluate one CCE condition expression, the Resolver **must** perform **all** of:

1. evaluate the innermost parenthesized function **before** its containing function.
2. evaluate **`=`** **and** **`!=`** as exact equality **and** inequality between one governed property **and** one canonical value.
3. evaluate **`<`**, **`<=`**, **`>`**, **and** **`>=`** **only** for properties with one governed comparison order.
4. evaluate **in** **and** **not in** as scalar membership **and** non-membership **in** one explicitly parenthesized value list, **or** according **to** CA-M-127-CORE_META_MODEL-METHOD--evaluate-set-valued-property-membership **when** the governed property is set-valued.
5. evaluate **is empty** **and** **is not empty** as absence **and** presence of a governed property value.
6. evaluate **contains**, **starts with**, **and** **ends with** **only** for governed textual property values.
7. evaluate **and** as true **only** **when** **every** argument is true.
8. evaluate **or** as true **when** **`>=1`** argument is true.
9. evaluate **not** as the inverse truth value of its argument.
10. evaluate **if** ... **then** as false **only** **when** its antecedent is true **and** its consequent is false.
11. evaluate **every** as true **only** **when** its predicate is true for **every** member of its population.
12. evaluate **any** as true **when** its predicate is true for **`>=1`** member of its population.
13. evaluate **none** as true **only** **when** its predicate is false for **every** member of its population.
14. evaluate **where** as restriction of one population **to** members whose predicate is true.
15. use another logical function **only** **when** an active CCE Method gives that function **`=1`** logical meaning.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-123-CORE_META_MODEL-METHOD--write-definitions-of-done.md

SHA-256: 5aaaa1e47a069d6a24f00fe4b1a4f5e81353bf9b03b2c9131ffd5315d72f49a3

```markdown
---
subjects:
  governs: "semantics"
  depends_on:
    - "CCE"
version: 17
updated_at: "2026-10-01 21:38:15 +0400"
relations:
  child_of:
    - CA-M-113
    - CA-M-122
    - CA-R-1581
    - CA-R-1583
atom_id: "CA-M-123"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Write Definitions of Done

## Scope

authoring one Definition of Done.

## Claim

**to** write one Definition of Done, the Author **must** perform **all** of:

1. begin the falsification condition expression with: the Plan is **not** Done **if**.
2. make **every** atomic condition observable **and** decidable.
3. enclose **every** composite condition **and** **every** function argument **in** explicit parentheses.
4. evaluate the condition expression according **to** CA-M-122-CORE_META_MODEL-METHOD--evaluate-condition-expressions.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-125-CORE_META_MODEL--assign-subjects-from-the-claim.md

SHA-256: 3c4a8960bac48476767cb4deda9a7771ea48b8fb303a1c6b85da2dc9a0f19e31

```markdown
---
subjects:
  governs: "Subject Assignment"
  depends_on:
    - "Atom/Claim"
    - "Atom/Summary"
    - "Atom/Subjects"
    - "Subject Path"
    - "Author"
    - "Subject"
    - "Term"
    - "Atom/Content Role: Evaluation"
    - "Evaluation For Relation"
    - "Entity"
    - "Dependent Entity"
version: 25
updated_at: "2026-10-02 20:25:13 +0400"
relations: {}
atom_id: "CA-M-125"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Assign Subjects from the Claim

## Scope

Subject assignment for an Atom from its Claim **and** complete Markdown Main Content.

## Claim

**to** assign an Atom's Subjects, the Author **must** perform **all** of:

1. read the entire Markdown Main Content, including Summary, Scope, Claim, Details, other registered sections, nested headings, tables, examples, **and** reference labels. build an inventory of canonical Entity mentions with exact locations **and** full resolved paths. treat an Atom citation label rendered under `CA-M-301-CORE_META_MODEL-METHOD--make-atom-claims-easy-to-understand` as the referenced Atom's complete filename **without** its `.md` extension **or** directory path. under `CA-R-1280-CORE_META_MODEL-CORE-REQUIREMENT--reference-every-prerequisite-subject-through-depends-on`, the label is readable reference evidence, **not** an Entity mention **or** Subject target, including **when** it occurs **in** the same sentence as Entity language; inventory an Entity **only** **when** surrounding prose independently uses it.

   recognize Terms through their existing definitions, including `Term` itself under `CA-R-1318-CORE_META_MODEL-CORE-REQUIREMENT--define-term`. `Evaluation` remains a Term **when** used inside an Evaluation Atom under `CA-R-1341-CORE_META_MODEL-CORE-REQUIREMENT--define-evaluation-content-role`. resolve its referenced Entity from that definition **and** the usage context. self-reference alone does **not** (remove a mentioned Entity from the inventory **or** establish a new Entity); a Term's spelling alone does **not** establish its Subject target. retain unresolved meaning as an explicit gap rather than treating it as ordinary wording.
2. select the **`=1`** canonical Entity that the Claim governs **and** reference its narrowest exact Subject Path directly through GOVERNS.

   - for a Claim about entry **or** exit criteria of a Dependent Entity, apply this same narrowest-target rule rather than substituting its wider bearer.
   - **when** the Atom has Content Role Evaluation **and** its Claim defines a conformance check, select the canonical target whose conformance is checked; do **not** select a generic Evaluation label **or** the execution of the check merely from its Content Role. bind the checked authority separately with `evaluation_for` under `CA-R-1018-CORE_META_MODEL-CORE-REQUIREMENT--register-evaluation-targets`.
3. connect **every** other Entity **in** the mention inventory through DEPENDS_ON using its narrowest exact full Subject Path. include mentions outside Claim; do **not** repeat GOVERNS **or** add unmentioned Entities. unresolved mentions block completion rather than disappearing from the inventory.
4. for a definition Claim, use its defined Term **in** the Subject Path that identifies the target being defined, under `CA-R-1279-CORE_META_MODEL-CORE-REQUIREMENT--govern-every-defined-term`. resolve **every** named path component as a Term reference; the path identifies the target **and** the GOVERNS link is the Subject Relation. the path does **not** define its component Terms.
5. split the Atom **before** assignment **when** the Claim governs **`>1`** canonical targets.
6. verify that the distinct GOVERNS **and** DEPENDS_ON targets equal the mention inventory. record **every** reference once **without** creating an intermediate Subject object, repeating definitions, **or** treating path components **and** implicit bearer prefixes as separate Entity mentions.
7. serialize the direct references under `CA-D-269-CORE_META_MODEL-DELIVERY--serialize-atom-subjects-in-frontmatter`. its migration-limited legacy compatibility preserves existing temporal carrier evidence; it does **not** add temporal nesting **to** a migrated flat Carrier.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-127-CORE_META_MODEL-METHOD--evaluate-set-valued-property-membership.md

SHA-256: bb09a5845cbff2aef2b4b36e84e452f0e798a9771e177150937453fef30bf64d

```markdown
---
subjects:
  governs: "Set-valued Property Membership Evaluation"
  depends_on:
    - "CCE Condition Expression Evaluation"
    - "Set-valued Property"
version: 15
updated_at: "2026-10-01 21:38:15 +0400"
relations:
  child_of:
    - CA-M-122
atom_id: "CA-M-127"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Evaluate Set-valued Property Membership

## Scope

evaluation of **in** **or** **not in** for one set-valued governed property.

## Claim

**to** evaluate **in** **or** **not in** for one set-valued governed property, the Resolver **must** evaluate **in** as true exactly **when** **`>=1`** property member **`=`** one listed value **and** **must** evaluate **not in** as true exactly **when** no property member **`=`** **any** listed value.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-135-CORE_META_MODEL-METHOD--exclude-generated-only-implementation-edges.md

SHA-256: 21d7a124cdb31b41665fefbda11604ede8cadeb635c0c3873511bab303969420

```markdown
---
subjects:
  governs: "provenance"
  depends_on: []
version: 18
updated_at: "2026-10-01 21:38:15 +0400"
relations: {}
atom_id: "CA-M-135"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Exclude generated-only implementation edges

## Scope

provenance validation of recorded changes in the governed selection.

## Claim

provenance validation inspects **every** recorded change **in** the governed selection. a change contributes an Implementation Relation, implementation coverage, **or** semantic traceability edge **only** **when** it changes **`>=1`** non-generated governed source.

an update **only** **to** generated Projections remains an auditable refresh. it retains its required Journal provenance but cannot become an implementation input **to** the semantic graph that produced the generated Carrier. a mixed change participates **only** through its substantive non-generated governed source changes.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-225-CORE_META_MODEL--retrieve-applicable-methodology-mechanically.md

SHA-256: a5b42abbafdd7458d70e4282e6912f1ac3073ab697caca67d2d262c85d66b4b5

```markdown
---
subjects:
  governs: "Applicable Methodology Retrieval"
  depends_on:
    - "Applicable Methodology"
    - "Atom/Subjects"
version: 15
updated_at: "2026-10-02 20:25:13 +0400"
relations: {}
atom_id: "CA-M-225"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Retrieve Applicable Methodology Mechanically

## Scope

Applicable Methodology retrieval for one Subject **or** Workflow query.

## Claim

**to** retrieve Applicable Methodology for one Subject **or** Workflow query, the Retriever **must** derive GOVERNS **and** DEPENDS_ON indexes on demand from projected Atom Subjects, select matching GOVERNS paths, add DEPENDS_ON authority **only** through transitive prerequisite closure, retain Applicable Methodology membership order, make no inference, **and** return no Atom **if** no matching GOVERNS path exists.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-228-CORE_META_MODEL-METHOD--write-subject-expressions-with-bearer-and-value-qualification.md

SHA-256: f5a2152648b95c04af56c49118f43ac64ee46dd8183b23913cb64f335d6f26df

```markdown
---
subjects:
  governs: "Subject Expression Writing"
  depends_on:
    - "Subject Path"
    - "Entity"
    - "Relation"
    - "Term"
    - "Subject"
    - "GOVERNS"
    - "DEPENDS_ON"
version: 14
updated_at: "2026-10-01 21:38:15 +0400"
relations: {}
atom_id: "CA-M-228"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Write Subject Expressions with Bearer and Value Qualification

## Scope

authoring one Subject Expression.

## Claim

**to** write a Subject Expression, start with a canonical Entity reference **and** apply `/` **or** `:` qualification **only** **where** the registered relation admits the exact endpoints. `/` retains bearer qualification **and** `:` retains allowed-value qualification; resolve **every** named component, including names **before** **and** **after** the separators, as a Term reference under CA-R-1321. the resulting qualified path identifies its existing canonical target **without** copying it; connecting the Atom **to** that target through GOVERNS **or** DEPENDS_ON creates the Subject Relation, **not** another target Entity.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-229-CORE_META_MODEL--render-governed-terms-and-cce-operators-distinctly.md

SHA-256: 5c2a07ec7999cffffc142edcb4569622e74eda19f2b2f01ac1121a20c9891c84

```markdown
---
subjects:
  governs: "Governed Term Rendering"
  depends_on:
    - "CCE Operator"
    - "General Term"
    - "Governed Term"
    - "Scope Unit/Name"
    - "Author"
    - "Markdown Atom Carrier/Main Content/CCE Operator"
version: 12
updated_at: "2026-10-02 20:25:13 +0400"
relations:
  relates_to:
    - CA-D-280
    - CA-M-299
atom_id: "CA-M-229"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Render Governed Terms and CCE Operators Distinctly

## Scope

CAPRMEDIO content lexical-case rendering.

## Claim

**to** render CAPRMEDIO content, the Author **must** apply the following lexical-case rules:

- start **every** Governed Term with a capital letter.
- start **every** General Term with a lowercase letter.
- preserve the lowercase spelling of **every** ordinary English word at the start of a sentence **or** list item **unless** an active rule requires an exact-case token.
- preserve the required case of canonical Terms, Scope Unit Names, **and** exact registered references, including at sentence **and** list-item starts.
- preserve the canonical spelling of **every** registered CCE Operator. use CA-D-280 for its representation **in** Markdown Atom Carrier Main Content.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-230-CORE_META_MODEL-METHOD--define-registered-cce-operators-through-cce-methods.md

SHA-256: b232fd54b2e93341c7227621683ab58cdf5abeabbece3a13c543a44fe4773519

```markdown
---
subjects:
  governs: "CCE Operator"
  depends_on:
    - "CCE Method"
version: 12
updated_at: "2026-10-01 21:38:15 +0400"
relations: {}
atom_id: "CA-M-230"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Define Registered CCE Operators through CCE Methods

## Scope

registered CCE Operators in CCE.

## Claim

within CCE, a CCE Operator **means** one canonical lowercase word-form token **or** token sequence **or** one canonical symbolic token that one active CCE Method assigns one syntactic **or** logical function.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-231-CORE_META_MODEL--derive-navigation-projections-from-the-cce-claim.md

SHA-256: 8bf9e52af16c589304cfc952b90467fb9819411a2ee7d917675a2464c987d09a

```markdown
---
subjects:
  governs: "Navigation Projection Derivation"
  depends_on:
    - "Atom/Claim"
    - "Atom/Summary"
version: 18
updated_at: "2026-10-02 20:25:13 +0400"
relations: {}
atom_id: "CA-M-231"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Derive Navigation Projections from the CCE Claim

## Scope

derivation of an Atom's navigation values from its authoritative content.

## Claim

**to** derive an Atom's navigation values, derive them from authoritative content rather than another navigation value:

- derive a new Atom's Summary from its finalized primary contribution within its applicability under CA-R-1465 **and** CA-M-111. for RMED, use Claim read within Scope, **not** Scope alone.
- derive **every** requested Projection from its applicable complete source content, including relevant textual applicability restrictions, **not** from the Summary.
- for an existing Atom identity, retain its Summary **and** check source faithfulness. a needed Summary change follows CA-R-1464 **and** **must not** be applied as a same-identity refresh.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-232-CORE_META_MODEL-CORE--derive-atom-subjects-graph-from-current-atom-subjects.md

SHA-256: 01e1f3355f52762beabcc19fe30746a536c12f79015f581d00b6ff765a202cd7

```markdown
---
subjects:
  governs: "Subject Projection Derivation"
  depends_on:
    - "Projection/Type: Atom Subjects Graph"
    - "Atom/Subjects"
    - "Subject Path"
    - "Subject"
    - "Atom"
    - "GOVERNS"
    - "DEPENDS_ON"
version: 12
updated_at: "2026-10-02 20:25:13 +0400"
relations: {}
atom_id: "CA-M-232"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Derive Atom Subjects Graph from Current Atom Subjects

## Scope

Atom Subjects Graph derivation from current Atom Subjects.

## Claim

**to** derive an Atom Subjects Graph, the Generator **must** reproduce **every** selected Subject as a direct GOVERNS **or** DEPENDS_ON graph link from its source Atom **to** its target with its exact canonical target, Subject Path, **and** Relation Kind **without** adding authority, requiring a duplicate target-kind field **in** the Atom's Subjects, **or** creating a separately identified Subject object. a Projection **may** derive a target's kind from its canonical authority **when** the Projection's own Spec calls for that classification; it **must not** independently reauthor that kind **or** require it as duplicated source Subjects metadata. an unmigrated temporal Carrier admitted temporarily by CA-D-269 retains its source classification as migration evidence **without** changing the direct reference **or** requiring that classification **in** the canonical flat representation.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-233-CORE_META_MODEL--prefer-positive-normative-statements.md

SHA-256: c377b64f94f41a68f97151370042bc08ec743ef7068ac723475acbe61b62e167

```markdown
---
subjects:
  governs: "Normative Atom Prose Authoring"
  depends_on:
    - "Atom"
    - "Atom/Claim"
    - "CCE"
version: 12
updated_at: "2026-10-02 20:25:13 +0400"
relations: {}
atom_id: "CA-M-233"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Prefer Positive Normative Statements

## Scope

normative Atom prose authored **in** CCE.

## Claim

**to** author normative Atom prose, state applicable conditions **and** required behavior positively **when** this preserves the complete Claim; an explicit prohibition is warranted **only** **when** it prevents a real ambiguity **or** protects an important boundary.

## Details

- use the positive statement **when** it already makes the required behavior clear.
- make a necessary prohibition explicit **when** the positive statement alone leaves a materially different interpretation **or** fails **to** protect the boundary.
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-234-CORE_META_MODEL--register-expandable-canonical-cce-operator-list.md

SHA-256: 76e25a9c4bc88ecf5d9e44f7379ed4ba421e3248ae80583efef48ac2e43ad2c5

```markdown
---
subjects:
  governs: "CCE Operator Registry"
  depends_on:
    - "CCE Operator"
    - "CCE Method"
version: 12
updated_at: "2026-10-02 20:25:13 +0400"
relations: {}
atom_id: "CA-M-234"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Register Expandable Canonical CCE Operator List

## Scope

the canonical CCE Operator Registry.

## Claim

the current canonical CCE Operator Registry **must** contain this expandable set:

1. statement form: **to**, **means**.
2. modality: **must**, **must not**, **may**.
3. condition: **if**, **then**, **when**, **otherwise**.
4. temporal condition: **before**, **after**, **until**, **unless**.
5. quantification: **all**, **every**, **any**, **none**.
6. logical/set: **and**, **or**, **not**, **without**, **where**.
7. restriction: **only**.
8. predicate: **in**, **not in**, **is empty**, **is not empty**, **contains**, **starts with**, **ends with**.
9. comparison: **`=`**, **`!=`**, **`<`**, **`<=`**, **`>`**, **`>=`**.

## Details

another token **may** enter the CCE Operator Registry **when** one active CCE Method assigns the token one syntactic **or** logical function.
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-235-CORE_META_MODEL--express-cardinality-with-comparison-operators-and-integer-literals.md

SHA-256: 738043ae13bf80391f1bd5ac62b179a7f68df6b6203474f322e78d8469f8456d

```markdown
---
subjects:
  governs: "Cardinality Constraint Authoring"
  depends_on:
    - "Cardinality Constraint"
    - "CCE Operator Registry"
    - "Nonnegative Integer Literal"
version: 11
updated_at: "2026-10-02 20:25:13 +0400"
relations: {}
atom_id: "CA-M-235"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Express Cardinality with Comparison Operators **and** Integer Literals

## Scope

numeric Cardinality Constraint authoring.

## Claim

**to** author one numeric Cardinality Constraint, the Author **must** serialize one canonical comparison CCE Operator immediately followed by one Nonnegative Integer Literal as a prefix immediately **before** the counted Entity **or** expression; examples: **`=1`** Author, **`>=1`** Requirement Atom, **`<=1`** Type, **`>=0`** Property.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-236-CORE_META_MODEL--normalize-noncanonical-cce-operator-expressions.md

SHA-256: 11adc0ba64795bc0b33892dfed8ce46c24c93a3fcc364ba1179a2a84aaa096b9

```markdown
---
subjects:
  governs: "CCE Operator Expression Normalization"
  depends_on:
    - "CCE Operator Expression"
    - "CCE Operator Registry"
version: 12
updated_at: "2026-10-02 20:25:13 +0400"
relations: {}
atom_id: "CA-M-236"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Normalize Noncanonical CCE Operator Expressions

## Scope

noncanonical CCE Operator Expressions.

## Claim

**to** normalize one noncanonical CCE Operator Expression, the Author **must** apply **all** applicable rewrites:

- `each` **to** **every**.
- `equals` **to** **`=`**.
- `does not equal` **to** **`!=`**.
- `both <A> and <B>` **to** `(<A>` **and** `<B>)`.
- `either <A> or <B>` **to** `(<A>` **or** `<B>)`.
- `neither <A> nor <B>` **to** **not** `(<A>` **or** `<B>)`.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-237-CORE_META_MODEL--author-claim-value-sets.md

SHA-256: f9293974e41c66ef9e209c37203fa8135d012b1a62acdc28c31d116a34891b92

```markdown
---
subjects:
  governs: "Claim Value Set Authoring"
  depends_on:
    - "Atom/Claim"
    - "Author"
    - "Claim Value Set"
    - "Property"
    - "Subject Expression"
    - "IS_ALLOWED_VALUE_OF"
version: 10
updated_at: "2026-10-02 20:25:13 +0400"
relations:
  child_of:
    - CA-M-115
atom_id: "CA-M-237"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Author Claim Value Sets

## Scope

Claim Value Set authoring.

## Claim

**to** author one Claim Value Set, the Author **must**:

1. identify **`=1`** Property X within **`=1`** Claim;
2. write its finite allowed-value set as `X: (A, B, C)`;
3. include **`>=1`** unique canonical values **and** treat their order as non-authoritative;
4. retain the complete set as **`=1`** Claim **only** **if** **all** values **must** be accepted, replaced, **and** retired together;
5. interpret `:` as Claim Value-Set syntax inside that Claim **and** as **`=1`** IS_ALLOWED_VALUE_OF relation **only** inside a Subject Expression.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-239-CORE_META_MODEL--derive-dependency-order-from-explicit-edges.md

SHA-256: 287f47cd2fcf0ed1b4090a376b3924a6aa3e45838d837fbcea306b8e46a81ad6

```markdown
---
subjects:
  governs: "Dependency Order Derivation"
  depends_on:
    - "DEPENDS_ON"
    - "DERIVED_FROM"
    - "Atom/Direct Relation Serialization"
    - "Artifact/Revision"
    - "Artifact"
    - "Atom/Content Role: Plan/Type: Plan"
version: 11
updated_at: "2026-10-02 20:25:13 +0400"
relations:
  child_of:
    - CA-M-120
atom_id: "CA-M-239"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Derive Dependency Order from Explicit Edges

## Scope

non-Plan Artifact dependency order derivation from explicit edges.

## Claim

**to** derive one non-Plan Artifact dependency order, the resolver **must**:

1. construct one directed graph from direct `relations.depends_on` edges from **every** dependent Artifact **to** **every** prerequisite Artifact;
2. derive its `required_by` inverse view **without** authoring inverse edges;
3. calculate one deterministic prerequisite-first topological order with canonical identity **only** as a tie-breaker; **and**
4. reject a cycle.

the resolver **must not** use target-list position, Local Order, **or** `relations.derived_from` as a dependency edge.

## Details

Plan readiness follows `BLOCKS` under CA-R-1580: **all** blockers **must** be Done, **and** independent ready Plans **may** execute concurrently subject **to** their permissions; navigation order **must not** add blocking.
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-240-CORE_META_MODEL-METHOD--derive-restricted-cce-canonical-signatures-without-source-rewrite.md

SHA-256: 03b8fab73bd3a910adeac50371d62fea8a5833836671fb9e3d502ff0062e654c

```markdown
---
subjects:
  governs: "Canonical Signature Derivation"
  depends_on:
    - "Atom/Claim"
    - "Atom/Claim/Canonical Signature"
    - "CCE Operator"
version: 9
updated_at: "2026-10-01 21:38:15 +0400"
relations:
  child_of:
    - CA-M-115
atom_id: "CA-M-240"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Derive Restricted CCE Canonical Signatures **without** Source Rewrite

## Scope

derivation of Canonical Signatures from one selected Atom Carrier folder.

## Claim

**to** derive Canonical Signatures from one selected Atom Carrier folder, the Tool **must** inspect **only** active single-statement Atom Claims, identify **every** outermost parenthesized expression that **contains** the **and** Operator **or** the **or** Operator, derive a Canonical Signature **only** **if** the expression satisfies the Restricted Boolean Expression grammar, emit source-identity evidence **and** **every** exclusion diagnostic, **and** make no source-Carrier rewrite, lifecycle change, Claim merge, **or** authority decision.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-241-CORE_META_MODEL--derive-canonical-scope-signatures-without-source-rewrite.md

SHA-256: 97f0b470a85ecdd81c279fea0008177f6fefabb5669030c94ca6e65ee15f2efc

```markdown
---
subjects:
  governs: "Canonical Scope Signature Derivation"
  depends_on:
    - "Scope Expression"
    - "Scope Expression/Canonical Scope Signature"
    - "Atom/Carrier"
version: 9
updated_at: "2026-10-01 21:38:15 +0400"
relations:
  child_of:
    - CA-M-121
atom_id: "CA-M-241"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Derive Canonical Scope Signatures **without** Source Rewrite

## Scope

derivation of Canonical Scope Signatures from one caller-selected Atom Carrier folder.

## Claim

**to** derive Canonical Scope Signatures from one caller-selected Atom Carrier folder, the Tool **must** inspect **only** active Carriers with **`=1`** unwrapped Scope Expression **in** one `## Scope` section, resolve **every** atomic identity against active Atom IDs **in** that selected folder, derive a signature **only** **if** the Scope Expression satisfies the restricted Canonical Scope Signature grammar, emit source identity, source revision, source Carrier digest, source frontier digest, source expression, signature, **and** exclusion diagnostic, **and** make no source-Carrier rewrite, lifecycle change, Claim merge, authority decision, **or** dependency relation.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-264-CORE_META_MODEL-METHOD--write-evaluations-with-reproducible-falsification.md

SHA-256: 49351d2882bbc07435ca189e3779a60259852306923820dbf99c9f5ce76f1584

```markdown
---
subjects:
  governs: "Atom/Content Role: Evaluation/authoring"
  depends_on:
    - "Atom/Content Role: Evaluation"
    - "Atom/Content Role: Method"
    - "Atom/Scope"
    - "Atom/Local Tier"
    - "Evaluation For Relation"
version: 8
updated_at: "2026-10-01 21:38:15 +0400"
relations: {}
atom_id: "CA-M-264"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Write evaluations with reproducible falsification

## Scope

authoring or maintaining an Evaluation.

## Claim

**to** write **or** maintain an Evaluation, identify its checked authority **and** Scope, select a suitable test technique, specify recoverable inputs, procedure, **and** observable falsifying conditions, **and** preserve the distinction between Core foundations, independent General evaluation criteria **where** General is admitted, **and** the default Standard tier; keep writing techniques, test frameworks, **and** authoring conventions **in** Method authority rather than treating them as test results.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-265-CORE_META_MODEL-GENERAL-METHOD--derive-evaluation-groups-from-checked-authority.md

SHA-256: 81de91e40b950ce608649dd6c263411acdf91b70a44dd212efcafede2f9b10ff

```markdown
---
subjects:
  governs: "Atom/Content Role: Evaluation/grouping"
  depends_on:
    - "Atom/Content Role"
    - "Evaluation For Relation"
version: 9
updated_at: "2026-10-01 21:38:15 +0400"
relations: {}
atom_id: "CA-M-265"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Derive evaluation groups from checked authority

## Scope

derivation of Er, Em, and Ed groups from checked authority.

## Claim

**to** derive Er, Em, **and** Ed groups, resolve the Content Role of **every** `evaluation_for` target **and** include the Evaluation **in** the corresponding Requirement, Method, **or** Delivery group; **if** targets span multiple roles, **then** include it **in** **every** applicable group **without** assigning a new Content Role **or** persisting a duplicate target-role field. absence of individual targets on a Core **or** General Evaluation policy admitted by CA-R-1018-CORE_META_MODEL-CORE-REQUIREMENT--register-evaluation-targets **must not** require an invented classification.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-271-CORE_META_MODEL-METHOD--resolve-confidence-thresholds-by-source-precedence.md

SHA-256: 1a8af9646ed7959358cfc6e67c77a3efabc242f989719fa9e8ce8fd81ecda79b

```markdown
---
subjects:
  governs: "Confidence Threshold/resolution"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Confidence Threshold"
    - "Operator"
    - "Hub Atom"
    - "Framework Instance Settings"
    - "Property"
    - "AI Agent"
version: 8
updated_at: "2026-09-29 22:34:37 +0000"
relations:
  child_of:
    - "CA-R-1428"
atom_id: "CA-M-271"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary
Resolve confidence thresholds by source precedence

## Scope
resolution of a Confidence Threshold.

## Claim
**to** resolve an effective Confidence Threshold, select the first applicable explicit source **in** this precedence:

1. direct Operator input for the current decision context.
2. an explicit value on the current Plan.
3. the nearest Hub with an explicit value, walking `IS_DECOMPOSITION_OF` from nearest **to** farthest; read its own current Plan File Carrier under `CA-D-472-CORE_META_MODEL-DELIVERY--serialize-explicit-plan-confidence-overrides`, **not** a separate Objective targeting a folder.
4. the Framework Instance Settings default.

### resolution constraints

- an omitted optional override preserves inheritance; another explicit field does **not** stop lookup for the omitted field. a missing mandatory Plan file is invalid, **not** an inherited-setting selection.
- use current Plan Revisions, **not** historical Carrier copies **or** unrelated nearby files; a Label is **not** an override source.
- **if** a reached source is invalid **or** ambiguous, **or** no source supplies a value, request Operator disposition **before** the affected autonomous action; do **not** invent a value **or** silently fall through past invalid authority.
- direct Operator input applies **only** within its stated context.
- do **not** copy inherited values into Plan overrides. preserve an explicit selection even **when** it **`=`** the inherited value; a later upstream change **must not** overwrite it.
- this resolution **must not** create another Atom, settings file, **or** execution permission.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-272-CORE_META_MODEL-METHOD--classify-an-atom-local-tier-from-its-complete-claim.md

SHA-256: 1aaf2686d62ef1346ad2cb06d69e9208d19e4a2e872ee5496df91ac70352a8bc

```markdown
---
subjects:
  governs: "Atom/Local Tier/classification"
  depends_on:
    - "Atom/Claim"
    - "Atom/Scope"
    - "Atom/Content Role"
    - "Atom/Local Tier"
    - "Atom/Global Tier"
    - "Scope Unit"
    - "Type"
    - "Methodology Source"
    - "Autonomous Confidence Threshold"
version: 12
updated_at: "2026-10-01 21:38:15 +0400"
relations: {"method_for": ["CA-R-1566", "CA-R-659", "CA-R-1431", "CA-R-1573"]}
atom_id: "CA-M-272"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Classify an Atom Local Tier from its complete Claim

## Scope

classification of an Atom's Local Tier against the tiers admitted **in** its current Scope Unit.

## Claim

**to** classify one Atom's Local Tier, the Author **must** perform **all** of:

1. resolve the exact current Atom identity **and** Revision, complete independently replaceable Claim, governed Subject, authority owner, Atom Scope, Claim Target Scope Unit **and** textual Claim Scope, Content Role, Type, **and** governing boundary; resolve the Local Tiers admitted **in** its current Scope Unit under CA-R-680-CORE_META_MODEL-GENERAL-REQUIREMENT--order-project-local-tiers **or** CA-R-1442-CORE_META_MODEL-GENERAL-REQUIREMENT--order-non-project-local-tiers **and** apply the existing Project Principle **and** Goal exceptions **and** Type restrictions **before** classifying an ordinary Claim. CAPO **and** I content resolves **to** Standard under CA-R-1566-CORE_META_MODEL-GENERAL-REQUIREMENT--keep-change-and-implementation-content-at-standard **and** proceeds directly **to** the preservation check; this explicit role-tier rule is **not** an inference from the governed Subject. resolve ownership **and** targeting under CA-M-273-CORE_META_MODEL-METHOD--derive-ownership-and-claim-target-atom-sets **and** read applicability restrictions from the body sections registered by CA-D-495-CORE_META_MODEL-CORE-DELIVERY--carry-applicability-in-the-registered-body-sections, including Scope for RMED, **when** deriving local applicability is required. an unresolved referent, contradictory boundary, unadmitted Type, unexplained source change, **or** independently replaceable mixed contribution stops that Atom's classification for the existing admission **or** Atom-boundary review.
2. test the complete Claim against CA-R-659-CORE_META_MODEL-CORE-REQUIREMENT--define-core-local-tier. identify the Core foundation it establishes for **all** Atoms at greater Global Tiers **in** the Scope Unit under CA-R-1573-CORE_META_MODEL-CORE-REQUIREMENT--govern-greater-global-tiers-within-each-scope-unit, including General **and** Standard, **and** explain which identity, purpose, owner, fundamental separation, **or** conservation boundary would cease **to** hold **if** the Claim were negated. **if** the dependency is established, **then** assign Core **and** proceed **to** the preservation check; usefulness, scope-wide occurrence, importance, precision, **and** reuse alone establish no constitutive dependency.
3. **if** the Core test is false **and** General is admitted **in** the current Scope Unit, **then** test the complete Claim against CA-R-1431-CORE_META_MODEL-CORE-REQUIREMENT--define-general-local-tier. identify **all** Standard Atoms **in** the Scope Unit governed under CA-R-1573-CORE_META_MODEL-CORE-REQUIREMENT--govern-greater-global-tiers-within-each-scope-unit; do **not** filter them by matching Content Role **or** Subject. record **`=2`** materially different realizations that preserve its complete contract **and** a changed shared contract that preserves its Core boundaries while changing its conformance. explain how this independently replaceable specification can be accepted, revised, **or** retired **without** duplicating a Core premise **or** concrete realization. assign General **only** **when** both witnesses **and** the independent authority unit are established. **if** General is **not** admitted, **then** skip this test.
4. **if** no applicable higher Local Tier **or** explicit tier rule applies, **then** use Standard as the default lowest Local Tier under CA-R-660-CORE_META_MODEL-CORE--define-standard-local-tier. no concrete Carrier field, path, token, format, realization procedure, test specimen, **or** representation-change witness is required for Standard. an omitted Local Tier token resolves **to** Standard under CA-D-285-CORE_META_MODEL-DELIVERY--serialize-local-tier-filename-tokens, subject **to** its Project Goal exception; that Carrier default does **not** override an applicable higher-tier requirement **or** resolve missing classification evidence.
5. perform the preservation check **before** accepting the classification: record the exact source identity, Revision, Claim contribution, clause-based test evidence, witnesses required by the tests actually applied, previous **and** proposed tier **and** structural rank, Scope **and** relation impacts, **and** disposition. classify a definition by its own complete Claim rather than by the value it defines. preserve identity, ownership, unchanged Claim meaning, Scope binding, **and** necessary direct relations; remove **or** correct an invalid tier-parent edge **only** with its explicit authority rationale. return an identified unresolved result **if** the applicable tiers **or** classification evidence are unresolved, the evidence conflicts, **or** independently replaceable contributions require different tiers; do **not** use Standard **to** conceal an unresolved decision, invent a General Atom, **or** average the tiers. consult applicable Project Principles **and** request **`=1`** exact Operator disposition **only** **when** a material unresolved proposition remains below the effective Autonomous Confidence Threshold.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-273-CORE_META_MODEL--derive-ownership-and-claim-target-atom-sets.md

SHA-256: 2f2a40037201679c18e7b0722f1d1fa26796758b7f797b575df0574c0a4e26ef

```markdown
---
subjects:
  governs: "Atom selection"
  depends_on:
    - "Atom/Revision/Author"
    - "Owned Atoms"
    - "Targeting Atoms"
    - "Subtree-owned Atoms"
    - "Subtree-targeting Atoms"
    - "Scope Unit"
    - "Atom Collection"
    - "Atom/Claim/Target Scope Unit"
    - "Atom/Content Role"
    - "Atom/Status"
    - "Artifact/Revision"
    - "Directory Carrier"
version: 13
updated_at: "2026-10-01 21:40:53 +0400"
relations: {}
atom_id: "CA-M-273"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Derive Ownership **and** Claim-target Atom Sets

## Scope

selection of Owned Atoms, Targeting Atoms, Subtree-owned Atoms, **and** Subtree-targeting Atoms for a Scope Unit.

## Claim

**to** derive the four Atom sets for a selected Scope Unit, the resolver **must** perform **all** of:

1. establish the complete authoritative source frontier, including Atoms outside the selected subtree that can target a Scope Unit inside it; scanning **only** locally stored Atoms is insufficient for Targeting Atoms **or** Subtree-targeting Atoms.
2. read **every** candidate Atom's carried current Scope Unit **and** check it against its nearest containing Scope Unit, passing through Atom Collections **and** Plan Hub Carriers **without** treating their nesting as additional Scope Unit ownership. preserve the carried external-Atom Author fallback under CA-D-276-CORE_META_MODEL-DELIVERY--use-economical-yaml-frontmatter **when** no containing Scope Unit exists; do **not** invent a Scope Unit owner.
3. resolve **every** candidate's Claim Target Scope Unit independently of ownership. read the internally carried target; absence of a required value is invalid, **not** permission **to** infer it from placement; apply CA-R-1588-CORE_META_MODEL-CORE-REQUIREMENT--default-plan-target-to-the-enclosing-scope-unit for Plans within Hub decomposition. an unresolved required target remains unresolved. a reference **to** another Scope Unit **must not** transfer ownership, **and** the target **must** resolve **to** a Scope Unit, **not** a Hub Atom **or** another non-Scope-Unit object. Claim Scope restrictions remain **in** the body sections registered by CA-D-495, including Scope for RMED, **and** do **not** create extra targets.
4. derive Owned Atoms, Targeting Atoms, Subtree-owned Atoms, **and** Subtree-targeting Atoms under CA-R-1447-CORE_META_MODEL-GENERAL-REQUIREMENT--define-owned-atoms, CA-R-1448-CORE_META_MODEL-GENERAL-REQUIREMENT--define-targeting-atoms, CA-R-942-CORE_META_MODEL-GENERAL-REQUIREMENT--define-subtree-owned-atoms, **and** CA-R-1449-CORE_META_MODEL-GENERAL-REQUIREMENT--define-subtree-targeting-atoms respectively. use the Scope Unit tree for descendant coverage; do **not** substitute physical subtree membership for Claim targeting **or** inferred inherited applicability for an explicit **or** default Claim target.
5. retain source Atom **and** Revision references **without** creating additional authoritative Atom copies. apply Content Role, Status, **and** other requested filters **after** resolving the selected set; the alias `spec` selects the Active RMED subset under CA-M-288-CORE_META_MODEL-METHOD--use-spec-as-an-alias-for-active-rmed-subtree-targeting-atoms, independently of Local Tier.
6. report the exact missing source, owner, target, ancestry, **or** required filter value **and** withhold a complete affected result **when** it is unresolved **or** contradictory. a complete empty set remains empty; an incomplete frontier **must not** be reported as a complete empty set.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-275-CORE_META_MODEL-METHOD--format-scope-unit-names.md

SHA-256: 8f594812eb0ff5144de3b84bca79ec243f40c4636ba10e1006fc7a784999e042

```markdown
---
subjects:
  governs: "Scope Unit/Name"
  depends_on:
    - "Scope Unit"
version: 7
updated_at: "2026-10-01 21:40:53 +0400"
relations:
  method_for:
    - "CA-R-962"
atom_id: "CA-M-275"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Format Scope Unit Names

## Scope

Scope Unit Names.

## Claim

**to** write a Scope Unit Name, join nonempty uppercase letter-or-digit word tokens with single underscores.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-276-CORE_META_MODEL-METHOD--repair-accidental-atom-id-reuse.md

SHA-256: 99bb048b7aabaaadab2bab139acaaba852fe8df1bc7e75bff898f063cedd5249

```markdown
---
subjects:
  governs: "Atom/Identity/collision repair"
  depends_on:
    - "Atom/Identity"
    - "Atom/Content Role"
    - "Atom/Claim"
    - "Atom/Scope"
    - "Artifact/Revision"
    - "Carrier/Canonical Address"
    - "Project"
    - "Operator"
    - "AI Agent"
    - "Confidence Threshold"
    - "Work Journal"
version: 9
updated_at: "2026-10-01 21:40:53 +0400"
relations: {"method_for":["CA-R-728"]}
atom_id: "CA-M-276"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Repair accidental Atom ID reuse

## Scope

repair of accidental reuse of assigned Project Atom IDs.

## Claim

**to** repair accidental reuse of an assigned Project Atom ID, an AI Agent **must** perform **all** of:

1. identify the distinct source Atoms by exact Carrier address, Revision, **and** recorded history. distinguish accidental reuse from legitimate Revisions of the same Atom **and** derived copies of its Carrier.
2. establish the original valid owner from recorded assignment history. **if** the original owner cannot be established at the effective Confidence Threshold, request an Operator decision for that collision **before** changing its identities **or** references. filename order, discovery order, current filesystem timestamps, **or** the highest Version **must not** select the owner.
3. preserve the original owner's Atom ID. give **every** later accidental reuse the next unreused Project-wide number for its own Content Role under CA-D-450-CORE_META_MODEL-DELIVERY--number-project-owned-atoms-within-each-content-role, using the encoding under CA-D-378-CORE_META_MODEL-DELIVERY--serialize-assigned-atom-identities. this corrects invalid reuse **and** does **not** authorize changing a valid owner's immutable identity.
4. preserve **every** affected Atom's Claim, Content Role, Atom Scope, Claim Target Scope Unit, **and** textual Claim Scope. preserve its immutable prior Revisions **and** recorded history; record the exact predecessor-to-corrected-identity mapping **in** the existing Work Journal **without** rewriting historical Carriers **or** Records.
5. resolve **every** affected current reference against its intended Atom using the reference's context **and** recorded history. update references **only** **when** their intended targets are established; request an Operator decision for unresolved references. do **not** replace the ambiguous ID indiscriminately.
6. verify that the repaired active identities resolve uniquely **and** **every** affected current reference still identifies its intended Claim **before** declaring the collision repaired. keep unrelated Claims **and** identities unchanged.
7. perform repair as an explicitly authorized source change, **not** as an automatic side effect of lookup **or** compilation. preserve CA-D-336-CORE_META_MODEL-DELIVERY--resolve-active-atoms-from-canonical-carrier-identities's failure on ambiguous lookup **until** source repair is complete, **and** regenerate affected Projections from their corrected sources through their existing governed workflows.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-277-CORE_META_MODEL-METHOD--report-in-silent-mode.md

SHA-256: e34f632c28b8450bee6689e3c76bd752feeb6106c32fea1e14656ca1ac656170

```markdown
---
subjects:
  governs: "Framework Instance Settings/interaction/reporting mode: silent"
  depends_on:
    - "Framework Instance Settings/interaction/reporting mode"
    - "Framework Instance Settings/interaction/reporting mode/effects"
    - "Framework Instance Settings/interaction/reporting mode/mandatory information"
    - "Artifact"
    - "Skill"
    - "Project"
version: 11
updated_at: "2026-10-01 21:40:53 +0400"
relations: {"relates_to":["CA-R-1628","CA-R-1439","CA-R-1440","CA-R-1558","CA-O-052","CA-R-1750"]}
atom_id: "CA-M-277"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Report **in** silent mode

## Scope

silent-mode reporting.

## Claim

**to** report **in** `silent` mode, answer exploratory input normally **and**, apart from the mandatory information governed by CA-R-1440-CORE_META_MODEL-GENERAL-REQUIREMENT--preserve-mandatory-information-in-every-reporting-mode, report **only** durable Artifacts **or** Project state that CAPRMEDIO created, updated, archived, committed, **or** **otherwise** changed; omit ordinary announcements of mode selection, workflow routing, Skill chaining, **and** gate transitions.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-278-CORE_META_MODEL--report-in-verbose-mode.md

SHA-256: 28a9c6a6e3143994fa1219f196480063245a917ac0917bcb4e54d331a98c3d0d

```markdown
---
subjects:
  governs: "Framework Instance Settings/interaction/reporting mode: verbose"
  depends_on:
    - "Framework Instance Settings/interaction/reporting mode"
    - "Framework Instance Settings/interaction/reporting mode/effects"
    - "Framework Instance Settings/interaction/reporting mode/mandatory information"
    - "Artifact"
    - "Skill"
version: 9
updated_at: "2026-10-02 20:25:13 +0400"
relations: {"relates_to":["CA-R-1628","CA-R-1439","CA-R-1440","CA-O-052","CA-R-1750"]}
atom_id: "CA-M-278"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Report **in** verbose mode

## Scope

reporting **in** `verbose` mode.

## Claim

**to** report **in** `verbose` mode, explicitly report relevant workflow modes, mode transitions, selected Skill chains, entry **and** exit gates, **and** planned **or** completed Artifact operations, together with the mandatory information governed by CA-R-1440-CORE_META_MODEL-GENERAL-REQUIREMENT--preserve-mandatory-information-in-every-reporting-mode.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-279-CORE_META_MODEL-GENERAL-METHOD--resolve-missing-framework-parameters-from-default-settings.md

SHA-256: a7168156a9c28bb73462090e158d8d7ece430a8db561dbe0ceadfd7873d170b3

```markdown
---
subjects:
  governs: "Framework Instance Settings/parameter resolution"
  depends_on:
    - "Framework Instance Settings"
    - "Default Settings"
    - "Project"
    - "Operator"
version: 8
updated_at: "2026-09-29 22:34:37 +0000"
relations:
  relates_to:
    - "CA-R-1402"
    - "CA-R-1441"
    - "CA-R-1750"
    - "CA-D-407"
    - "CA-D-408"
atom_id: "CA-M-279"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary
Resolve missing framework parameters from Default Settings

## Scope
resolution of a Framework Instance Settings parameter.

## Claim
**to** resolve a Framework Instance Settings parameter, use its explicit value **if** that parameter is present **in** the current Project's Framework Instance Settings; **otherwise**, use the corresponding value from Default Settings. determine presence for the individual parameter, **not** its containing section **or** the truthiness of its value, so valid `false`, `0`, **and** empty values remain explicit selections. validate the selected value against its governing parameter authority **and** reject an invalid explicit value **without** falling back. **if** neither source supplies a required parameter, report that parameter as unresolved **and** stop the operation that requires it; an optional parameter **may** remain absent. do **not** copy inherited values into Framework Instance Settings as explicit selections.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-287-CORE_META_MODEL-METHOD--exclude-activity-labels-from-content-role-names.md

SHA-256: 50eaddff1271ff1ef1eac2eb559762a12f0a284ed30c96026f15c7a69aecafdd

```markdown
---
subjects:
  governs: "Content Role Naming"
  depends_on:
    - "Atom/Content Role/Name"
    - "Author"
    - "Status"
version: 10
updated_at: "2026-10-01 21:40:53 +0400"
relations: {}
atom_id: "CA-M-287"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Exclude Activity Labels from Content Role Names

## Scope

Content Role names.

## Claim

**to** name a Content Role, the Author **must not** use a verb, imperative, workflow instruction, Status, **or** activity label.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-288-CORE_META_MODEL-METHOD--use-spec-as-an-alias-for-active-rmed-subtree-targeting-atoms.md

SHA-256: 3543b6ea429b92783e9f357be927e0157488f1bfadbf097a275279f447a64e5f

```markdown
---
subjects:
  governs: "Subtree-targeting Atoms"
  depends_on:
    - "Atom/Content Role"
    - "Atom/Status"
    - "Author"
version: 7
updated_at: "2026-10-01 21:40:53 +0400"
relations: {}
atom_id: "CA-M-288"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Use spec as an Alias for Active RMED Subtree-targeting Atoms

## Scope

Active RMED Subtree-targeting Atom references.

## Claim

**to** refer **to** Subtree-targeting Atoms filtered **to** Active Revisions **and** Content Role **in** (Requirement, Method, Evaluation, Delivery), an Author **may** use `spec` as a non-authoritative alias for that same filtered set.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-291-CORE_META_MODEL-GENERAL--author-project-structure-without-competing-declarations.md

SHA-256: cb32963b5b127d9679484cdc39b159949d1338f00536672d495409cd93e86584

```markdown
---
subjects:
  governs: "Project Structure"
  depends_on:
    - "Scope Unit"
    - "Scope Unit/Name"
    - "Scope Unit/Type"
    - "Scope Unit/Label"
    - "Scope Unit/Local Order"
    - "Scope Unit/Navigational Order Number"
    - "Goal"
    - "Framework Instance Settings"
    - "Carrier"
version: 5
updated_at: "2026-10-01 21:40:53 +0400"
relations:
  relates_to:
    - "CA-R-1483"
    - "CA-R-1484"
    - "CA-R-1485"
    - "CA-R-1430"
atom_id: "CA-M-291"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Author Project Structure **without** competing declarations

## Scope

Project Structure declarations.

## Claim

**to** express Project Structure, use one declaration for **every** non-root Scope Unit, reference its parent by the reserved Project-root reference **or** the parent's unique Name, **and** keep structural Local Order distinct from Navigational Order Number. retain an explicit Label independently of Ordered/Unordered Type. retain readable Structural Level **and** authority path **only** with their checked derivation from declared parentage **and** applicable Carrier conventions; physical nesting **must not** silently replace logical parentage. use concrete Carrier bindings as declared values rather than repeating them **in** Goal, Requirement, **or** Delivery Atoms. write an Authority Mode override **only** **when** explicitly selected for that unit; an omitted override remains inherited rather than copied as an explicit value. references **and** observations **must** distinguish the declared unit from its existing Carrier **and** Goal coverage.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-294-CORE_META_MODEL--use-simpler-words-without-losing-meaning.md

SHA-256: f43b99c71608021b8e927996c4924fb1ece77c55346c73cbd82d1fc3a9407700

```markdown
---
version: 4
updated_at: "2026-10-02 20:35:16 +0400"
relations:
  child_of:
    - CA-R-940
    - CA-R-941
  method_for:
    - CA-R-940
    - CA-R-941
  relates_to:
    - CA-M-229
    - CA-R-1273
subjects:
  governs: "language"
  depends_on:
    - "Author"
    - "Atom/Claim"
    - "Atom/Summary"
    - "CCE"
    - "Governed Term"
    - "CCE Operator"
atom_id: "CA-M-294"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Use simpler words without losing meaning

## Scope

CAPRMEDIO content wording.

## Claim

**when** choosing wording for CAPRMEDIO content, the Author **must** choose words **and** phrases that are simpler **and** more familiar **to** the intended reader **when** they preserve the intended meaning **without** adding ambiguity.

## Details

- prefer clear everyday wording over unnecessary jargon **or** specialized wording.
- preserve who **or** what the statement concerns, its obligations **or** permissions, quantities, conditions, boundaries, **and** logical distinctions.
- prefer a clear longer phrase over a shorter obscure expression; fewer words do **not** necessarily make the content simpler.
- retain specialized wording **when** replacing it would lose a necessary distinction **or** make the meaning less precise.
- retain exact canonical Terms, CCE Operators, **and** references. simpler wording does **not** authorize an unregistered synonym **or** a silent Term rename.

for a Summary, simplify its wording while preserving its source faithfulness under CA-R-1273; this does **not** require restating the complete Claim.
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-295-CORE_META_MODEL--resolve-implementation-retry-limits-by-source-precedence.md

SHA-256: 2d3c0506dcedfda929c9f391340eca3afb829f93d5807bd1be5db924069ca81c

```markdown
---
version: 9
updated_at: "2026-09-28 15:12:22 +0400"
relations:
  child_of:
    - CA-R-1489
  depends_on:
    - CA-M-279
subjects:
  governs: "Implementation Retry Limit/resolution"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Implementation Retry Limit"
    - "Operator"
    - "Framework Instance Settings"
    - "Default Settings"
    - "Hub Atom"
    - "Atom/Content Role: Plan/Type: Plan/Decomposition"
    - "Atom/Content Role: Plan/Type: Plan/Carrier"
atom_id: "CA-M-295"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Resolve implementation retry limits by source precedence

## Scope

an effective Implementation Retry Limit resolved from direct Operator input, a Plan, the nearest Hub, Framework Instance Settings, **or** Default Settings.

## Claim

**to** resolve an effective Implementation Retry Limit, select the first applicable explicit source **in** this precedence:

1. direct Operator input for the current execution context.
2. the current Plan's explicit Implementation Retry Limit.
3. the nearest Hub with an explicit limit, walking `IS_DECOMPOSITION_OF` from nearest **to** farthest **and** reading its own current Plan File Carrier under CA-D-447-CORE_META_MODEL-DELIVERY--serialize-the-implementation-retry-limit-setting.
4. Framework Instance Settings, resolving an omitted instance parameter through Default Settings under CA-M-279-CORE_META_MODEL-GENERAL-METHOD--resolve-missing-framework-parameters-from-default-settings.

### resolution constraints

- an omitted optional retry override preserves inheritance; another explicit field does **not** stop this lookup. a missing mandatory Plan file is invalid, **not** an inherited-setting selection.
- determine presence, **not** truthiness: **`=0`** is an explicit limit.
- an invalid **or** ambiguous reached source requires Operator disposition **without** silent fallback; an absent effective value stops the affected retry decision.
- direct Operator input applies **only** within its stated context.
- do **not** copy inherited values **or** create separate Objective/settings files. retain explicit overrides even **when** equal **to** the inherited value.
- use the same Plan identity for a Hub's file **and** folder.
- resolution does **not** reset the consumed retry count governed by CA-O-024-CORE_META_MODEL-ACTION--control-implementation-retries.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-297-CORE_META_MODEL-METHOD--compare-by-priority-order.md

SHA-256: e217fde189c3c466446ed69929a43747cde86c1b0ac535d092bfd67cef11cbd5

```markdown
---
version: 4
updated_at: "2026-10-01 21:40:53 +0400"
relations:
  child_of:
    - CA-R-1487
  method_for:
    - CA-R-1487
subjects:
  governs: "Project/lexicographic selection"
  depends_on:
    - "Operator"
    - "Project/priority model application"
    - "Atom/Content Role: Method"
atom_id: "CA-M-297"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Compare by priority order

## Scope

priority-order comparison of admissible alternatives.

## Claim

**when** the Operator selects comparison by priority order, the comparison of admissible alternatives **must** use the resolved order of active, applicable criteria as follows:

- an earlier criterion takes precedence over a later criterion.
- for alternatives tied on **all** earlier criteria, the first criterion that distinguishes them determines their relative preference.
- later criteria **must not** override a preference established by an earlier criterion.
- alternatives tied on **all** applicable criteria remain tied.
- an incomplete criterion order **or** an incomparable result at the current deciding criterion leaves the comparison unresolved; a later criterion **must not** bypass that gap.

this Method defines the comparison technique, **not** priority activation, alternative-selection execution, **or** escalation.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-298-CORE_META_MODEL-GENERAL-METHOD--describe-methodology-expansion-mappings.md

SHA-256: bff7275f00c0dd59032ad72aa017ed209dbb9cb8250e203a8863fb05d2963886

```markdown
---
subjects:
  governs: "Methodology Source/expansion mapping"
  depends_on:
    - "Methodology Source"
    - "Extension"
    - "Project Configuration"
    - "Core Meta-Model"
version: 5
updated_at: "2026-10-01 21:40:53 +0400"
relations: {child_of: [CA-M-006], method_for: [CA-R-1375]}
atom_id: "CA-M-298"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Describe methodology expansion mappings

## Scope

Methodology Source expansion mappings.

## Claim

**to** describe a Methodology Source expansion mapping, use **`=1`** explicit mapping description that identifies:

- the source element **and** its provenance;
- the exact canonical target;
- the mapping rule;
- the intended scope of application;
- the applicable Core Meta-Model distinctions at **any** Local Tier.

apply this same mapping convention **to** Extension **and** Project Configuration sources regardless of provenance. the convention supports CA-R-1375-CORE_META_MODEL-CORE-REQUIREMENT--restrict-methodology-source-expansion-to-core-permission's expansion boundary; it does **not** admit activation **or** reliance. CA-O-054-CORE_META_MODEL-ACTION--admit-methodology-expansion-mappings owns that admission Action **and** re-evaluation following material changes.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-299-CORE_META_MODEL--distinguish-scope-unit-names-from-ordinary-english.md

SHA-256: bd094829b8aaf2e5bc69ea104346c8c7578a46002c1746ae7b1f22f1263dd9ba

```markdown
---
subjects:
  governs: "Scope Unit/Name"
  depends_on:
    - "Scope Unit"
    - "CCE"
version: 4
updated_at: "2026-10-02 20:35:16 +0400"
relations: {}
atom_id: "CA-M-299"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Distinguish Scope Unit Names from Ordinary English

## Scope

Scope Unit references in CAPRMEDIO content.

## Claim

**to** distinguish a Scope Unit reference from ordinary English, use its exact uppercase Scope Unit Name **to** denote the Scope Unit. an **otherwise** identical lowercase word retains its ordinary English meaning.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-301-CORE_META_MODEL--make-atom-claims-easy-to-understand.md

SHA-256: 5b5d8a498e87e2f377eea0593235af7fd642d21006e9a34ab6358787a8769a41

```markdown
---
subjects:
  governs: "Atom/Claim"
  depends_on:
    - "Term"
    - "Workflow/Relation Kind: On Result"
    - "Step"
    - "Atom"
    - "Author"
    - "CCE"
    - "Action"
    - "Workflow"
version: 6
updated_at: "2026-10-04 15:08:16 +0000"
relations:
  child_of:
    - CA-M-113
  relates_to:
    - CA-M-229
    - CA-M-294
    - CA-R-1270
    - CA-R-1508
atom_id: "CA-M-301"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Make Atom Claims easy to understand

## Scope

Atom Claims.

## Claim

**to** make an Atom Claim easy **to** understand, the Author **must** express **and** organize its content so the intended reader can identify what is claimed, what it concerns, **and** how its conditions **and** consequences fit together **without** guessing unstated connections.

## Details

### Meaning and context

- provide the context needed **to** interpret the Claim. reference existing governing definitions **and** authority rather than independently restating them.
- render **every** prose Atom citation as the referenced Atom's complete filename **without** its `.md` extension **or** directory path, preserving **all** filename tokens **and** their exact spelling. direct machine references remain exact Atom IDs rather than citation labels, **and** `CA-R-366-CORE_META_MODEL-REQUIREMENT--reference-exact-atom-revisions-by-version-and-time` continues **to** govern exact-revision metadata.
- choose familiar wording under `CA-M-294-CORE_META_MODEL-METHOD--use-simpler-words-without-losing-meaning` **without** losing precision, necessary distinctions, **or** exact canonical Terms.
- state conditions, alternatives, **and** relationships explicitly. preserve whether **all** conditions apply **or** **any** alternative suffices, including nested logical groups.

### Structure

- use short, direct statements. a simple Claim **may** remain a short paragraph; do **not** compress several points, conditions, **or** steps into one dense sentence.
- use bullets for unordered points, conditions, **or** alternatives.
- use a numbered list for sequential steps **only** **when** the content establishes that sequence. numbering **must not** invent execution order **or** priority.
- use a flow table for a Workflow with branches **or** loops. identify **every** Step, its **`=1`** Action reference **and** parameter/input bindings, **and** the typed Relation, result condition, **and** next Step **or** terminal outcome for **every** transition under `CA-R-1508-CORE_META_MODEL-CORE-REQUIREMENT--define-workflow`.

### Preservation

- preserve the complete Claim **and** its qualifications; easier wording **or** layout **must not** change its meaning.
- retain the Atom boundary under `CA-R-1270-CORE_META_MODEL-CORE-REQUIREMENT--permit-one-composite-claim-as-one-authority-unit`. one Claim does **not** require one sentence; paragraphs, bullets, **and** table rows do **not** determine the number of independently governed Claims.
- express authoritative content once rather than repeating the same Claim **in** prose **and** a list **or** table.
- apply the Term **and** CCE Operator rendering Method under `CA-M-229-CORE_META_MODEL-METHOD--render-governed-terms-and-cce-operators-distinctly` throughout.

readable layout alone is insufficient **when** the Claim still requires the reader **to** reconstruct missing context **or** logical connections.
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-303-CORE_META_MODEL--declare-update-routing-in-the-calling-workflow.md

SHA-256: 2f4c60f6dfc4a019614c0e04a185fc53cf06b88a3a6ddbd580497ff4bb7cf7db

```markdown
---
subjects:
  governs: "Workflow"
  depends_on:
    - "Author"
    - "Action"
    - "Step"
    - "Workflow Run"
    - "Atom"
    - "Atom/Summary"
    - "Artifact/Revision"
    - "Assess Atom Update Identity"
version: 4
updated_at: "2026-10-01 21:40:53 +0400"
relations: {"relates_to": ["CA-M-301", "CA-O-067", "CA-R-1432", "CA-R-1464", "CA-R-1520"]}
atom_id: "CA-M-303"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Declare update routing **in** the calling Workflow

## Scope

Atom update routing for a calling Workflow.

## Claim

**to** author an Atom update Workflow, declare its response **to** identity assessment **in** the Workflow graph rather than **in** the assessment Action **or** executor code.

- reference CA-O-067-CORE_META_MODEL-ACTION--assess-atom-update-identity for the assessment; bind the target Revision, proposed result, applicable authority, **and** evidence **to** that Step. the Action returns its assessment **without** selecting the caller's next Step **or** continuation Workflow.
- map identity-preserving results **to** the caller's declared update path **and** remaining authorization **and** checks; the assessment alone does **not** perform the update.
- map replacement-required results **to** a terminal handoff under CA-R-1520-CORE_META_MODEL-GENERAL-REQUIREMENT--return-workflow-handoffs-through-terminal-results. keep the admitted replacement-continuation binding **in** the Workflow definition, **not** as an assessment Action input. the ending Run does **not** call **or** wait for replacement **or** persist an intermediate update merely **to** replace it.
- map unresolved results **to** the caller's declared evidence-gathering **or** escalation path; an unresolved result **must not** be treated as approval.
- include reassessment **when** the proposal changes **or** its evidence becomes stale **before** persistence. a changed Summary remains a replacement under CA-R-1464-CORE_META_MODEL-REQUIREMENT--keep-summary-fixed-for-atom-identity even **when** the request began as an update.

this Method constrains how an Author expresses the caller's graph. it is **not** another Workflow, executable routing service, **or** requirement **to** build the executor through a particular Workflow.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-304-CORE_META_MODEL--write-self-contained-agentic-action-instructions.md

SHA-256: 42bac0554e085881c7902a8477792c052a4abda9c8538efc0751410f71044aac

```markdown
---
subjects:
  governs: "Step Run/Invocation"
  depends_on:
    - "Action"
    - "Step"
    - "Workflow"
    - "Operator"
    - "Tool"
    - "Action/Execution Kind: Agentic"
    - "Step Run/Tool Call"
version: 4
updated_at: "2026-09-30 15:26:58 +0400"
relations: {"method_for": ["CA-R-1789", "CA-R-1790", "CA-R-1791", "CA-R-1792", "CA-R-1793"]}
atom_id: "CA-M-304"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary
Write self-contained agentic Action instructions

## Scope
derived instructions that present an Agentic Action for execution.

## Claim

**to** present an Agentic Action for execution, organize its derived instruction around the declared responsibility rather than assumed session memory.

- state the requested outcome, relevant context, exact targets, inputs, available evidence, **and** governing references.
- distinguish already performed effects from proposed changes, **and** existing permissions from decisions still needed.
- state the expected result **and** how **to** report uncertainty, failures, partial effects, **or** a request for Operator input. do **not** treat a suggested correction as permission **to** apply it.
- keep the instruction limited **to** the bound Action. leave next-Step selection **and** cross-Workflow handoff coordination **to** the executor using the governing Workflow.
- use understandable wording **and** structured points under CA-M-301-CORE_META_MODEL-METHOD--make-atom-claims-easy-to-understand **and** CA-M-294-CORE_META_MODEL-METHOD--use-simpler-words-without-losing-meaning; reference governing definitions rather than copying another authoritative procedure into the prompt.
- keep internal Tool calls as execution detail under CA-R-1528-CORE_META_MODEL-GENERAL-REQUIREMENT--record-tool-calls-within-step-runs. **when** an operation needs independently governed routing, checks, **or** approval boundaries, express it as an explicit Step during Workflow authoring rather than inventing Workflow nodes from runtime calls.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-305-CORE_META_MODEL--write-workflow-schemes-using-step-references.md

SHA-256: 7bfa882f4b769654eaba1c267fe179ff83019fd6fd76a022fc12065a93fdd4e5

```markdown
---
subjects:
  governs: "Workflow"
  depends_on:
    - "Step"
    - "Action"
    - "Atom/Content Role: Operations/Type: Step"
    - "Workflow/Relation Kind: On Result"
version: 4
updated_at: "2026-10-02 20:35:16 +0400"
relations: {"method_for": ["CA-R-1570"]}
atom_id: "CA-M-305"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Write Workflow schemes using Step references

## Scope

Workflow schemes using Step references.

## Claim

**to** write a Workflow scheme, express the graph through references **to** its Step Atoms:

- use **`=1`** unambiguous reference for **every** graph node; readable node labels **may** accompany those references.
- state the entry, typed directed transitions, result conditions, **and** terminal outcomes against those nodes.
- place Action references **and** parameter/input bindings **in** the referenced Step Atoms rather than reproducing them **in** the scheme.
- reference reusable Action behavior from the Steps; do **not** paste it into either the Step **or** graph Claim.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-306-CORE_META_MODEL-GENERAL--author-plan-atoms.md

SHA-256: b20340474959f2b3e19417b6d7de7398e62bd6d556c341edec7d3ae64011092d

```markdown
---
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Claim"
    - "Atom/Summary"
    - "Atom/Author"
    - "Atom/Content Role: Plan/Type: Plan/Assignee"
    - "Atom/Content Role: Plan/Type: Plan/Label"
    - "Atom/Content Role: Plan/Type: Plan/Subtype"
    - "Atom/Content Role: Plan/Type: Plan/Definition of Done"
    - "Atom/Content Role: Plan/Type: Plan/Decomposition"
    - "Atom/Content Role: Plan/Type: Plan/Blocking"
    - "Autonomous Confidence Threshold"
    - "Implementation Retry Limit"
    - "Scope Unit"
    - "File Carrier"
version: 7
updated_at: "2026-10-02 20:35:16 +0400"
relations: {"relates_to": ["CA-R-1574", "CA-R-1575", "CA-R-1576", "CA-R-1577", "CA-R-1599", "CA-R-1584", "CA-R-1588", "CA-R-1589", "CA-R-1591", "CA-R-1418", "CA-M-123", "CA-M-271", "CA-M-295", "CA-D-470", "CA-D-471", "CA-D-481"]}
atom_id: "CA-M-306"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Author Plan Atoms

## Scope

Plan Atoms.

## Claim

**to** author a Plan Atom, apply the common Plan authoring rules independently of Label:

1. resolve **`=1`** effective Author.
2. state **`=1`** intended work **or** outcome **in** Objective, supported by own work, direct decomposition, **or** both under CA-R-1575.
3. resolve its Claim Target Scope Unit under CA-R-1588; keep narrower **or** composite work restrictions **in** Objective, **and** do **not** target an ancestor Scope Unit.
4. **if** it has own work, resolve **`=1`** effective Assignee **and** assign that work **to** that Assignee. retain the leaf-work bound under CA-R-1589.
5. write **`=1`** Definition of Done under CA-M-123, carried inside Details under CA-D-470; include decomposed completion obligations **when** applicable.
6. use a Label **only** for navigation; apply an authoring Subtype **only when** explicitly governed.
7. express required start dependencies with `BLOCKS`; declare `IS_DECOMPOSITION_OF` **only** on the decomposing Plan under CA-D-481. derive the inverse; do **not** infer execution dependencies from leading numbers **or** folder placement.
8. resolve confidence **and** retry values from their applicable sources; store **only** explicitly selected overrides on this Plan.
9. keep supporting Details within Objective **and** its restrictions **without** another intended outcome. review Objective against the completed Details **and** Definition of Done; explicitly revise Objective **if** needed **and** recheck their agreement.
10. **only after** that review, derive Summary from the finalized Objective under CA-R-1418 **and** CA-R-1465. retain the established Summary across Revisions; **if** it needs changing, replace the Atom identity under CA-R-1464.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-307-CORE_META_MODEL-CORE--define-content-role-specific-cce-profiles.md

SHA-256: 158b7e802ce470f95564bcc9a32644c4f501d4c14c5b278b0573c3e7b3f56b77

```markdown
---
subjects:
  governs: "CCE/Role Profile"
  depends_on:
    - "CCE"
    - "CCE Operator"
    - "Atom/Claim"
    - "Atom/Content Role"
    - "Type"
version: 4
updated_at: "2026-10-02 20:35:16 +0400"
relations:
  child_of:
    - CA-M-113
    - CA-M-230
    - CA-M-234
  relates_to:
    - CA-R-1283
    - CA-R-1530
atom_id: "CA-M-307"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Define Content-role-specific CCE Profiles

## Scope

CCE Role Profiles.

## Claim

a CCE Role Profile **means** one restriction of shared CCE that identifies the permitted primary Claim contribution, permitted CCE Operator uses, permitted subordinate content slots, **and** prohibited primary contributions for one Content Role **or** one narrower Type **or** content slot.

the current role-specific profiles apply **only** **to** Plan, Requirement, Method, Evaluation, Delivery, **and** Operations Atoms.

Concern **and** Analysis Claims remain subject **to** shared CCE **without** an additional CCE Role Profile. this absence does **not** exempt them from shared CCE **or** authorize normative authority outside their Content Role meanings.

no CCE Role Profile is currently registered for Implementation because the current source set contains no Implementation Atoms. an absent Implementation profile **must not** be replaced by another role's profile **or** treated as role-profile conformance.

a narrower Type **or** content-slot profile **may** restrict its parent role profile **and** define permitted subordinate operator use, but it **must not** change the primary contribution of the Content Role.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-308-CORE_META_MODEL-CORE--resolve-the-effective-cce-role-profile.md

SHA-256: c0f47bd447cde321bc74e49045b16c8bfcdaac54709d5dd2c362f218d93aa0f0

```markdown
---
subjects:
  governs: "CCE/Role Profile/resolution"
  depends_on:
    - "CCE/Role Profile"
    - "Atom/Content Role"
    - "Type"
    - "Atom/Claim"
version: 4
updated_at: "2026-10-02 20:35:16 +0400"
relations:
  child_of:
    - CA-M-307
  relates_to:
    - CA-M-309
    - CA-M-310
    - CA-M-311
    - CA-M-312
    - CA-M-313
    - CA-M-314
atom_id: "CA-M-308"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Resolve the Effective CCE Role Profile

## Scope

effective CCE Role Profiles for Atom Claims.

## Claim

**to** resolve one effective CCE Role Profile for one Atom Claim, the Author **must** perform **all** of:

1. resolve the Atom's Content Role **before** selecting a profile.
2. **if** the Content Role is Plan, Requirement, Method, Evaluation, Delivery, **or** Operations, select the corresponding profile under CA-M-309 through CA-M-314.
3. apply an admitted Type profile **and** content-slot profile **after** the role profile; treat each narrower profile as a restriction **or** declared subordinate use, **not** as permission **to** change the role's primary contribution.
4. distinguish operators that express the primary Claim contribution from operators inside a condition, Definition of Done, input, result, failure, transition, representation, **or** another governed subordinate slot.
5. **if** the Content Role is Concern **or** Analysis, apply shared CCE **without** a role-specific profile.
6. **if** the Content Role is Implementation, return no registered CCE Role Profile **without** selecting a fallback profile **or** reporting role-profile conformance.
7. **if** the Content Role, Type, content slot, **or** applicable profile is unresolved, report the exact unresolved selection **and** do **not** report role-profile conformance.

## Details

the effective profile is derived from governed content classification. it is **not** another required Atom property.
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-309-CORE_META_MODEL-METHOD--write-plan-claims-with-the-plan-cce-profile.md

SHA-256: 0ccf013b3aa5e388853f9b0a8acd98e73180fd4d4e0028684a472f2566e46f61

```markdown
---
subjects:
  governs: "CCE/Role Profile: Plan"
  depends_on:
    - "Atom/Content Role: Plan"
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Content Role: Plan/Type: Plan/Definition of Done"
    - "CCE Operator"
version: 4
updated_at: "2026-10-01 21:41:08 +0400"
relations:
  child_of:
    - CA-M-307
  relates_to:
    - CA-M-123
    - CA-M-306
    - CA-R-1575
    - CA-R-1581
atom_id: "CA-M-309"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Write Plan Claims with the Plan CCE Profile

## Scope

Plan Claims written with the Plan CCE Role Profile.

## Claim

**to** write a Plan Claim with the Plan CCE Role Profile, the Author **must** perform **all** of:

1. state the Plan's primary contribution as intended work, an intended outcome, **or** their governed composition under CA-M-306-CORE_META_MODEL-GENERAL-METHOD--author-plan-atoms.
2. **if** the Plan has own work, identify the action, its object, intended result, Assignee, **and** applicable boundary explicitly. modality, condition, temporal, quantification, logical, restriction, predicate, **and** comparison Operators **may** qualify that intended work.
3. **if** the Plan is supported **only** by decomposition, state its intended outcome **without** inventing own work.
4. keep reusable procedure authority, normative product boundaries, current realization facts, **and** reusable operational behavior outside the Plan's primary contribution.
5. write the Definition of Done as the subordinate falsifying Condition Expression under CA-M-123-CORE_META_MODEL-METHOD--write-definitions-of-done. condition, temporal, quantification, logical, predicate, restriction, **and** comparison Operators **may** occur **in** that slot **only** to determine whether the Plan remains **not** Done.
6. keep optional Details subordinate **to** the same intended work **or** outcome; Details **must not** introduce another intended outcome **or** a second Definition of Done.

## Details

an action word **in** a Plan identifies intended work. it does **not** define a reusable Operations Action.
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-310-CORE_META_MODEL--write-requirement-claims-with-the-requirement-cce-profile.md

SHA-256: b41cd2dfe70813a227d0253e717c5d39ac6d5cb842ea72524ce0582476ed0db6

```markdown
---
subjects:
  governs: "CCE/Role Profile: Requirement"
  depends_on:
    - "Atom/Content Role: Requirement"
    - "CCE Operator"
    - "Atom/Claim"
version: 5
updated_at: "2026-10-04 04:27:08 +0400"
relations:
  child_of:
    - CA-M-307
  relates_to:
    - CA-R-1339
    - CA-M-233
    - CA-M-235
atom_id: "CA-M-310"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Write Requirement Claims with the Requirement CCE Profile

## Scope

Requirement Claims with the Requirement CCE Role Profile.

## Claim

**to** write a Requirement Claim with the Requirement CCE Role Profile, the Author **must** perform **all** of:

1. state the primary contribution as one Entity model **or** required result by its meaning **and** value under CA-R-1339. express required properties **and** observable boundaries within that model **or** result; an obligation, permission, **or** prohibition alone does **not** select Requirement.
2. use **must**, **must not**, **may**, **only**, quantification, predicates, comparisons, **and** explicit conditions as applicable **to** state what is required, permitted, prohibited, **or** bounded.
3. use **means** **only** **when** the Claim defines the governed Requirement subject rather than merely describing it.
4. express temporal Operators **only** as observable timing boundaries **or** conditions on the required result.
5. keep procedural selection, ordered execution steps, implementation instructions, **and** reusable operational behavior outside the primary contribution. reference applicable Method **or** Operations authority rather than reproducing it.

## Details

the Requirement profile governs the required model **or** result. an observed test result remains execution evidence; it is **not** the required-result specification.
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-311-CORE_META_MODEL--write-method-claims-with-the-method-cce-profile.md

SHA-256: e269327a60f09d386b1857772c57f35f2135bce174be8e85f6ab34bcf0b3f1bc

```markdown
---
subjects:
  governs: "CCE/Role Profile: Method"
  depends_on:
    - "Atom/Content Role: Method"
    - "CCE Operator"
    - "Atom/Claim"
version: 5
updated_at: "2026-10-04 04:27:08 +0400"
relations:
  child_of:
    - CA-M-307
  relates_to:
    - CA-R-1340
    - CA-M-113
    - CA-M-301
atom_id: "CA-M-311"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Write Method Claims with the Method CCE Profile

## Scope

Method Claims with the Method CCE Role Profile.

## Claim

**to** write a Method Claim with the Method CCE Role Profile, the Author **must** perform **all** of:

1. state the primary contribution as one reusable authorship, construction, **or** Implementation choice **or** convention for satisfying accepted Spec authority under CA-R-1340.
2. use **to** for the governed method purpose. identify the applicable inputs, construction **or** selection choices, dependencies, produced result, **and** unresolved-choice handling necessary for reuse. include a performer, order, repetition, **or** stopping condition **only when** the convention requires it; do **not** invent an operational Action **or** Workflow **to** fill a Method template.
3. use condition, temporal, quantification, logical, restriction, predicate, **and** comparison Operators **only** with explicit scope over the affected method content.
4. use modality **only** to constrain correct performance of the Method; the Method **must not** create an independently governed product outcome **or** permission that belongs **in** Requirement authority.
5. use **means** **only** **when** defining the governed Method subject **or** one necessary Method-local term.
6. reference applicable Requirement, Evaluation, Delivery, **and** Operations authority rather than reproducing their independently governed contributions as method steps.
7. **when** the Method concerns tests, govern how their implementation is constructed **or** selected. the test's checked behavior, fixture, acceptance policy, expected result, **and** disposition remain Evaluation authority; its executable test code is Implementation.

## Details

the Method profile governs how accepted authority is satisfied. it does **not** turn one intended Plan action **or** one reusable Operations Action into a Method.
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-312-CORE_META_MODEL--write-evaluation-claims-with-the-evaluation-cce-profile.md

SHA-256: f89d277d5a08c3c9c33129fe95b91e9a735335ed103f50fd37f1c7c41e48ff9e

```markdown
---
subjects:
  governs: "CCE/Role Profile: Evaluation"
  depends_on:
    - "Atom/Content Role: Evaluation"
    - "CCE Operator"
    - "Condition Expression"
version: 5
updated_at: "2026-10-04 04:27:08 +0400"
relations:
  child_of:
    - CA-M-307
  relates_to:
    - CA-R-1341
    - CA-M-122
    - CA-M-264
atom_id: "CA-M-312"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Write Evaluation Claims with the Evaluation CCE Profile

## Scope

Evaluation Claims with the Evaluation CCE Role Profile.

## Claim

**to** write an Evaluation Claim with the Evaluation CCE Role Profile, the Author **must** perform **all** of:

1. state the primary contribution as one falsifiable check, acceptance criterion, **or** disposition rule against identified checked authority **and** Scope.
2. state recoverable inputs, the evaluated subject, observable evidence, **and** the condition that yields each result necessary for reproducibility under CA-M-264-CORE_META_MODEL-METHOD--write-evaluations-with-reproducible-falsification.
3. use condition, temporal, quantification, logical, restriction, predicate, **and** comparison Operators with explicit scope over the checked evidence **and** result.
4. use modality **only** to constrain correct evaluation **or** disposition. an Evaluation **must not** create the Requirement that it checks.
5. specify the checked behavior, case inputs **or** fixture, expected observations, acceptance policy, **and** result disposition required by the check. include a checking procedure **only** as subordinate Evaluation content. reusable test-construction **or** selection conventions belong **in** Method authority; executable test code belongs **in** Implementation; a separately reusable test-running Action **or** Workflow belongs **in** Operations.
6. report unresolved, unavailable, **or** contradictory evidence as its governed result rather than silently converting it **to** pass **or** fail.

## Details

classification follows the primary contribution. quality-assurance policies **and**
test cases are Evaluation contributions; product outcome policy remains Requirement
authority, **and** tool **or** technique selection remains Method authority.
apply CA-R-794 for the Evaluation's Local Tier.
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-313-CORE_META_MODEL-METHOD--write-delivery-claims-with-the-delivery-cce-profile.md

SHA-256: 570884157745cc3016065c683188b6b80ad0376bba2f76948c279562edc0f947

```markdown
---
subjects:
  governs: "CCE/Role Profile: Delivery"
  depends_on:
    - "Atom/Content Role: Delivery"
    - "CCE Operator"
    - "Carrier"
    - "Entity/Carrier"
    - "Atom/Claim"
    - "Atom/Subjects"
    - "Relation Type"
version: 5
updated_at: "2026-09-28 22:47:05 +0000"
relations:
  child_of:
    - CA-M-307
  relates_to:
    - CA-R-1342
atom_id: "CA-M-313"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Write Delivery Claims with the Delivery CCE Profile

## Scope

authoring Delivery Claims with the Delivery CCE Role Profile.

## Claim

a Delivery Claim **must** use the Delivery CCE Role Profile **to** express its Carrier contribution with the following authoring conventions:

1. name the governed Carrier **or** Entity/Carrier binding **and** state its definition, classification, **or** constraint directly.
2. include format, content, address, placement, **or** lifecycle conditions **when** they are relevant **to** that contribution.
3. choose CCE Operators **to** express the applicable modality, conditions, quantities, **and** comparisons.
4. use **means** for a definition; express a classification **or** binding through its admitted Relation Type.
5. keep the Claim about the governed Subject; use references for separately governed contributions.

## Details

Carrier definitions **and** classifications need **only** the details relevant **to** their own contribution. they do **not** require an invented filename, format, **or** lifecycle condition.
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-314-CORE_META_MODEL-METHOD--write-operations-claims-with-type-specific-cce-profiles.md

SHA-256: a3f8c559979f66d1130dc199f1a842fff3e77e1e589fca77ff32e3276d61bbbc

```markdown
---
subjects:
  governs: "CCE/Role Profile: Operations"
  depends_on:
    - "Atom/Content Role: Operations"
    - "Atom/Content Role: Operations/Type: Action"
    - "Atom/Content Role: Operations/Type: Workflow"
    - "Atom/Content Role: Operations/Type: Step"
    - "Atom/Content Role: Operations/Type: Actor"
    - "CCE Operator"
version: 4
updated_at: "2026-10-01 21:41:08 +0400"
relations:
  child_of:
    - CA-M-307
  relates_to:
    - CA-R-1452
    - CA-R-1530
    - CA-R-1563
    - CA-R-1565
    - CA-R-1569
    - CA-M-304
    - CA-M-305
atom_id: "CA-M-314"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Write Operations Claims with Type-specific CCE Profiles

## Scope

Operations Claims written with their admitted Operations Type-specific CCE Profiles.

## Claim

**to** write an Operations Claim, the Author **must** first resolve its admitted Operations Type **and** **then** apply **`=1`** primary Type profile:

1. for Action, use **means** to define the named reusable operational behavior. state its required inputs, preconditions, operational contribution, returned results, observable effects, **and** failure results. modality, condition, temporal, quantification, logical, restriction, predicate, **and** comparison Operators **may** constrain that behavior.
2. for Workflow, use **means** to define the reusable graph through Step references, entry, typed transitions, result conditions, **and** terminal outcomes. use condition, temporal, logical, restriction, predicate, **and** comparison Operators **only** with explicit transition scope under CA-M-305-CORE_META_MODEL-METHOD--write-workflow-schemes-using-step-references.
3. for Step, define the invocation binding of **`=1`** referenced Action with its parameters **and** inputs. do **not** copy the Action behavior **or** define another Workflow.
4. for Actor, define participation, responsibility, capability, authorization, **or** prohibition using **must**, **may**, **must not**, **only**, conditions, **and** explicit boundaries as applicable. do **not** encode one particular execution as reusable Actor authority.

## Details

an Operations Claim **must not** combine more than one primary type profile. subordinate inputs, conditions, results, failures, transitions, **and** effects remain part of the selected type's single operational contribution.
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-315-CORE_META_MODEL-CORE--validate-claims-against-effective-cce-role-profiles.md

SHA-256: e086c85c7b1a25ed6ebe7930e854b1f57fbeec09814e7f372789bb0fe51f8c90

```markdown
---
subjects:
  governs: "CCE/Role Profile/validation"
  depends_on:
    - "CCE/Role Profile"
    - "CCE Operator"
    - "Atom/Claim"
    - "Atom/Content Role"
    - "Type"
version: 4
updated_at: "2026-10-02 20:35:16 +0400"
relations:
  child_of:
    - CA-M-307
    - CA-M-308
  relates_to:
    - CA-M-113
    - CA-M-229
    - CA-M-234
atom_id: "CA-M-315"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Validate Claims against Effective CCE Role Profiles

## Scope

Atom Claims against effective CCE Role Profiles.

## Claim

**to** validate one Atom Claim against its effective CCE Role Profile, the Validator **must** perform **all** of:

1. resolve the effective profile under CA-M-308 **without** inferring a different Content Role from the wording under review.
2. identify the Claim's primary contribution, every subordinate content slot, **and** every registered CCE Operator occurrence.
3. verify that the primary contribution matches the resolved role profile **and** that every narrower Type **or** content-slot contribution remains within its admitted boundary.
4. verify that every CCE Operator use is permitted for its exact primary **or** subordinate context **and** has explicit logical scope.
5. reject a primary contribution owned by another Content Role even **when** every individual CCE Operator is present **in** the global registry.
6. for Concern **or** Analysis, validate shared CCE **and** their governed Content Role meaning **without** requiring a role-specific profile.
7. for Implementation content, report that no CCE Role Profile is registered; do **not** apply another role's profile **or** report role-profile conformance.
8. report every mismatch by Content Role, Type, content slot, primary contribution, **and** Operator occurrence. do **not** rewrite the source Claim **or** report conformance while one required classification remains unresolved.

## Details

global CCE Operator registration is necessary but insufficient for role-profile conformance.
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/05_method/CA-M-300-PROJECT_CONFIGURATION-METHOD--use-constraint-only-for-external-limitations.md

SHA-256: 075eaea69c97d76f97da70a03161ed683220f5fb22698ac50308ea20286b662e

```markdown
---
subjects:
  governs: "Atom/Content Role: Requirement/Type: Constraint"
  depends_on:
    - "Atom/Content Role: Requirement/Type"
    - "Project"
    - "Author"
version: 5
updated_at: "2026-09-29 22:20:38 +0000"
relations: {"method_for":["CA-R-1673"]}
atom_id: "CA-M-300"
content_role: "Method"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary
Use Constraint only for external limitations

## Scope
selection of a Requirement Type.

## Claim

**to** select a Requirement Type, the Author **must** use Constraint **only** for a limitation imposed from outside the Project choice boundary.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-111-CORE_META_MODEL--author-one-cce-claim-and-derived-summary.md

SHA-256: 3f03aaa946145fbd555a66a5af52b3668000227067d4920550358166e46f4e2c

```markdown
---
subjects:
  governs: "Atom Claim Authoring"
  depends_on:
    - "Atom/Claim"
    - "CCE"
    - "Atom/Summary"
version: 25
updated_at: "2026-10-02 20:25:13 +0400"
relations: {"relates_to": ["CA-R-1624", "CA-O-103", "CA-D-479", "CA-R-1465"]}
atom_id: "CA-M-111"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-111-CORE_META_MODEL--author-one-cce-claim-and-derived-summary.md
---
# Summary

Author one CCE Claim and derived Summary

## Scope

authoring an Atom's primary contribution, its applicability, **and** its derived Summary.

## Claim

**to** author one CCE Claim **and** its derived Summary, an Author **must** use these authoring constraints:

- express **`=1`** independently replaceable contribution using the applicable CCE Content Role profile. carry it under the primary contribution heading registered **in** CA-D-479 rather than imposing the literal heading Claim on **every** role.
- resolve **`=1`** Claim Target Scope Unit independently of ownership. select the current Scope Unit as the authoring default **or** an explicitly permitted different target; carry the resolved value under CA-D-482. express applicability under CA-D-495. for RMED, describe what the Claim applies **to**, including applicable conditions **and** exclusions, **in** Scope; do **not** merely repeat the carried current **or** target Scope Unit; those restrictions alone do **not** make the Atom Relational.
- keep Details within the primary contribution under CA-R-1624. for RMED, read the Claim within its Scope; Details **must not** change either. **if** supporting content reveals an incomplete **or** inaccurate contribution **or** applicability, revise the affected Scope **or** primary contribution explicitly **and** recheck agreement; do **not** hide the change **in** Details.
- write Summary **only after** the other body sections **and** the contribution review are complete. shorten the finalized primary contribution under CA-R-1465 **and** CA-R-1273. for RMED, summarize the Claim within its finalized Scope, **not** the Scope alone; do **not** substitute supporting Results **or** TLDR as the source.
- for an existing Atom, retain the established Summary **and** check its faithfulness; **if** the Summary needs changing, use a new Atom identity under CA-R-1464.
- derive **every** Translation from the full corresponding source content, **not** the Summary.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-112-CORE_META_MODEL-METHOD--use-english-as-the-project-language.md

SHA-256: 559f6984b7db2f27dd94cdda92eaf84e6edd574149a75103331c6942a2e37cc5

```markdown
---
subjects:
  governs: "language"
  depends_on:
    - "CCE"
version: 14
updated_at: "2026-09-29 22:20:38 +0000"
relations:
  child_of:
    - CA-R-940
atom_id: "CA-M-112"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-112-CORE_META_MODEL-METHOD--use-english-as-the-project-language.md
---
# Summary
Use English as the Project language

## Scope
expressing CAPRMEDIO Project meaning.

## Claim

**to** express CAPRMEDIO Project meaning, the Author **must** use English as the base language.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-113-CORE_META_MODEL--write-claims-in-caprmedio-controlled-english.md

SHA-256: 11c46b7ef3c9c8fc987b334ce75f66d11521d7ccd236d32767004f4d770d49bd

```markdown
---
subjects:
  governs: "language"
  depends_on:
    - "artifact-model"
    - "CCE"
    - "Author"
    - "Atom/Claim"
version: 17
updated_at: "2026-10-02 20:25:13 +0400"
relations:
  child_of:
    - CA-M-111
    - CA-M-112
    - CA-R-941
  relates_to:
    - CA-M-229
    - CA-M-301
    - CA-M-294
    - CA-M-307
    - CA-M-308
    - CA-M-315
atom_id: "CA-M-113"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-113-CORE_META_MODEL--write-claims-in-caprmedio-controlled-english.md
---
# Summary

Write Claims in CAPRMEDIO Controlled English

## Scope

Claim authoring **in** CAPRMEDIO Controlled English.

## Claim

**to** write one Claim **in** CAPRMEDIO Controlled English, the Author **must** satisfy **all** of the following:

- use the controlled English subset of the identified CCE version.
- name **every** necessary participant **and** relation explicitly.
- state **every** necessary modality, quantity, condition, **and** boundary explicitly.
- use exact canonical Terms owned by active Definition Atoms.
- resolve the effective CCE Role Profile under CA-M-308-CORE_META_MODEL-CORE-METHOD--resolve-the-effective-cce-role-profile **and** satisfy that profile under CA-M-315-CORE_META_MODEL-CORE-METHOD--validate-claims-against-effective-cce-role-profiles.
- choose wording under CA-M-294-CORE_META_MODEL-METHOD--use-simpler-words-without-losing-meaning.
- exclude ambiguous pronouns, anaphora, ellipsis, unstated defaults, **and** mixed logical groupings.
- make the content understandable under CA-M-301-CORE_META_MODEL-METHOD--make-atom-claims-easy-to-understand **and** render Terms **and** CCE Operators under CA-M-229-CORE_META_MODEL--render-governed-terms-and-cce-operators-distinctly.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-114-CORE_META_MODEL--derive-terminology-projection-from-definition-atoms.md

SHA-256: 2723d0e67e441b29718e6725e88c3a026fc934f2980ec66ee0094b73cd2ad4d6

```markdown
---
subjects:
  governs: "Terminology Projection Derivation"
  depends_on:
    - "Projection/Type: Catalog"
    - "Generator"
    - "Definition Atom"
    - "Governed Term"
    - "Project"
    - "Atom/Claim"
    - "Subject"
    - "Subject Path"
    - "Entity"
    - "Term"
    - "Action"
    - "Workflow"
version: 20
updated_at: "2026-10-01 21:33:03 +0400"
relations: {}
atom_id: "CA-M-114"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-114-CORE_META_MODEL--derive-terminology-projection-from-definition-atoms.md
---
# Summary

Derive Terminology Projection from Definition Atoms

## Scope

derivation of a terminology Projection from active Definition Atoms.

## Claim

**to** build a terminology list using the Catalog Type, the Generator **must** derive **every** Governed Term's name **and** Project-specific meaning from its active Definition Atom. read the Term named by the defining Claim **and** verify that the Definition Atom's GOVERNS Subject Relation identifies its defined target under CA-R-1279-CORE_META_MODEL-CORE-REQUIREMENT--govern-every-defined-term. extract Term references from **every** named component of a Subject Path, **not** **only** its terminal component; obtain **every** referenced Term's meaning from that Term's own defining Claim, **not** by treating **all** path components as definitions supplied by the referencing Atom. include an entry **only** **when** the defining Claim establishes a Project-specific meaning; consistent use, capitalization, **or** occurrence **in** a Subject Path alone does **not** supply defining authority. an unresolved named component is a Term-reference gap **to** report, **not** permission **to** invent a definition **or** silently treat that component as ordinary vocabulary. exclude words **and** phrases used **only** with their ordinary English meanings. retain the source reference **without** classifying the direct Subject reference **or** a complete composite Subject Path as a Term **or** creating independent vocabulary authority.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-115-CORE_META_MODEL--author-one-cce-claim-per-atom.md

SHA-256: 2464267db6c3239df60e5da076748b6a776f79683921a7ad784dc3af1b2b83ef

```markdown
---
subjects:
  governs: "Atom Claim Boundary Authoring"
  depends_on:
    - "Atom"
    - "Claim"
    - "Atom/Claim"
    - "CCE"
    - "Author"
    - "Scope Unit"
    - "Atom/Claim/Target Scope Unit"
    - "Relational Atom"
version: 23
updated_at: "2026-09-28 15:12:22 +0400"
relations: {}
atom_id: "CA-M-115"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-115-CORE_META_MODEL--author-one-cce-claim-per-atom.md
---
# Summary

Author one CCE Claim per Atom

## Scope

authoring the boundary of **`=1`** independently replaceable Atom contribution.

## Claim

**to** author an Atom, the Author **must** perform **all** of:

1. identify one statement whose complete effect **must** be accepted, replaced, **and** retired together.
2. split **every** independently replaceable component into another Atom.
3. resolve **`=1`** Claim Target Scope Unit independently of ownership. select the current Scope Unit **as** the default during authoring **or** select an explicitly permitted different target; carry the resolved value under CA-D-482-CORE_META_MODEL-DELIVERY--carry-the-resolved-claim-target-scope-unit. express applicability **in** the registered body sections under CA-D-495-CORE_META_MODEL-CORE-DELIVERY--carry-applicability-in-the-registered-body-sections; for RMED, use Scope **and** write the Claim within that applicability; those restrictions alone do **not** make the Atom Relational.
4. write the complete Claim **in** the current CCE version.
5. remove **every** duplicate alternate authoritative statement.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-116-CORE_META_MODEL-CORE--derive-navigation-projections-from-the-cce-claim.md

SHA-256: 83522ad2e023e2cbbb14c05df6df90a94b352aa1bcd5a60bfe84bca48f640c5d

```markdown
---
subjects:
  governs: "Atom Claim Projection"
  depends_on:
    - "Atom/Claim"
    - "Atom/Summary"
    - "Translation"
version: 14
updated_at: "2026-10-02 20:25:13 +0400"
relations:
  relates_to:
    - CA-M-294
atom_id: "CA-M-116"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-116-CORE_META_MODEL-CORE--derive-navigation-projections-from-the-cce-claim.md
---
# Summary

Derive navigation Projections from the CCE Claim

## Scope

navigation values derived from an Atom Claim.

## Claim

**to** derive navigation values from an Atom Claim, the Generator **must** derive the concise human-readable Summary **when** creating the Atom **and** derive requested Translations directly from the Claim, **without** adding authoritative meaning. choose wording under CA-M-294-CORE_META_MODEL-METHOD--use-simpler-words-without-losing-meaning. for an existing Atom identity, retain **and** check the Summary under CA-R-1273-CORE_META_MODEL-CORE-REQUIREMENT--keep-summary-source-faithful **and** CA-R-1464-CORE_META_MODEL-REQUIREMENT--keep-summary-fixed-for-atom-identity rather than regenerating it as an independent Projection.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-120-CORE_META_MODEL-CORE--compile-the-direct-relation-registry.md

SHA-256: b9fabdd91e81d8df1213490b85d8fea8ad61497e0a98004589c52bf040846d6f

```markdown
---
subjects:
  governs: "Relation Kind/registry compilation"
  depends_on:
    - "Relation Kind"
    - "Relation Kind/Metadata"
    - "CAPRMEDIO Graph"
    - "Applicable Methodology"
    - "Relation/authority"
    - "Atom/Content Role: Requirement"
    - "Projection"
    - "Generator"
    - "Relation"
    - "Single Source of Truth"
version: 14
updated_at: "2026-10-02 20:25:13 +0400"
relations:
  child_of:
    - CA-R-295
    - CA-R-326
  method_for:
    - CA-R-806
    - CA-R-1246
    - CA-R-1437
    - CA-R-1472
atom_id: "CA-M-120"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-120-CORE_META_MODEL-CORE--compile-the-direct-relation-registry.md
---
# Summary

Compile the direct-relation registry

## Scope

direct-relation registry compilation.

## Claim

**to** compile the direct-relation registry, the Generator **must** perform **all** of:

1. derive the metadata required by CA-R-806-CORE_META_MODEL-GENERAL-REQUIREMENT--register-complete-relation-kind-metadata for **every** declared Relation Kind from its active governing Requirement authority. report missing **or** conflicting metadata **without** inventing a graph owner, meaning, endpoint class, **or** constraint.
2. group Relation Kinds by their owning kind of CAPRMEDIO Graph **and** resolve **every** lookup by graph kind **and** canonical name. reuse the same source authority across instances of the same graph kind governed by the same Applicable Methodology; do **not** merge registrations from different graph kinds because their names match.
3. derive inverse navigation from its declared owning direction **without** independently authoring an inverse Relation fact. distinguish **`=1`** authoritative declaration for an independently authored Relation fact from the governing derivation authority **and** input facts of a derived Relation under CA-R-1437-CORE_META_MODEL-CORE-REQUIREMENT--keep-one-source-for-each-relation-fact; do **not** invent a direct source declaration for a computed result.
4. retain source traceability for the compiled registry as a non-authoritative Projection. resolve cross-graph **and** authoritative-source endpoints against their admitted graph contexts under CA-R-806-CORE_META_MODEL-GENERAL-REQUIREMENT--register-complete-relation-kind-metadata **and** CA-R-1472-CORE_META_MODEL-GENERAL-REQUIREMENT--admit-typed-secondary-graph-connections. cross-graph references **or** views **must not** register a foreign Relation Kind as native **or** reclassify an external endpoint as a native node of the receiving graph.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-121-CORE_META_MODEL-METHOD--evaluate-scope-expressions.md

SHA-256: 4a79dc8d21ac47b99e29c0621cfc41cd31b53593c0a35e26bcd800a6f40e5f38

```markdown
---
subjects:
  governs: "Scope Expression Evaluation"
  depends_on:
    - "Scope Expression"
version: 17
updated_at: "2026-09-29 22:34:56 +0000"
relations: {}
atom_id: "CA-M-121"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-121-CORE_META_MODEL-METHOD--evaluate-scope-expressions.md
---
# Summary
Evaluate Scope Expressions

## Scope
evaluation of a Scope Expression.

## Claim
**to** evaluate one Scope Expression, the Resolver **must** perform **all** of:

1. resolve **every** exact Atom ID **or** other atomic identity **to** **`=1`** Governed Entity.
2. interpret **all** `<ENTITY_KIND>` as **every** Governed Entity of that kind within Atom Scope.
3. interpret **or** as set union.
4. interpret **and** as set intersection.
5. interpret **without** as left-side set exclusion.
6. interpret **where** as retention of **only** members whose field predicate evaluates **to** true according **to** `CA-M-122-CORE_META_MODEL-METHOD--evaluate-condition-expressions`.
7. evaluate the innermost parenthesized set function **before** its containing set function.
8. use another Scope function **only** **when** an active CCE Method gives that function **`=1`** set meaning.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-122-CORE_META_MODEL-METHOD--evaluate-condition-expressions.md

SHA-256: fb2819f1f14617ba1f5c8933adc9fed2fabdea33d11ca43a9879fa4a4536f97f

```markdown
---
subjects:
  governs: "CCE Condition Expression Evaluation"
  depends_on:
    - "CCE Condition Expression"
    - "CCE Operator"
version: 16
updated_at: "2026-10-01 21:33:03 +0400"
relations:
  child_of:
    - CA-M-113
atom_id: "CA-M-122"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-122-CORE_META_MODEL-METHOD--evaluate-condition-expressions.md
---
# Summary

Evaluate Condition Expressions

## Scope

evaluation of CCE Condition Expressions.

## Claim

**to** evaluate one CCE condition expression, the Resolver **must** perform **all** of:

1. evaluate the innermost parenthesized function **before** its containing function.
2. evaluate **`=`** **and** **`!=`** as exact equality **and** inequality between one governed property **and** one canonical value.
3. evaluate **`<`**, **`<=`**, **`>`**, **and** **`>=`** **only** for properties with one governed comparison order.
4. evaluate **in** **and** **not in** as scalar membership **and** non-membership **in** one explicitly parenthesized value list, **or** according **to** CA-M-127-CORE_META_MODEL-METHOD--evaluate-set-valued-property-membership **when** the governed property is set-valued.
5. evaluate **is empty** **and** **is not empty** as absence **and** presence of a governed property value.
6. evaluate **contains**, **starts with**, **and** **ends with** **only** for governed textual property values.
7. evaluate **and** as true **only** **when** **every** argument is true.
8. evaluate **or** as true **when** **`>=1`** argument is true.
9. evaluate **not** as the inverse truth value of its argument.
10. evaluate **if** ... **then** as false **only** **when** its antecedent is true **and** its consequent is false.
11. evaluate **every** as true **only** **when** its predicate is true for **every** member of its population.
12. evaluate **any** as true **when** its predicate is true for **`>=1`** member of its population.
13. evaluate **none** as true **only** **when** its predicate is false for **every** member of its population.
14. evaluate **where** as restriction of one population **to** members whose predicate is true.
15. use another logical function **only** **when** an active CCE Method gives that function **`=1`** logical meaning.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-123-CORE_META_MODEL-METHOD--write-definitions-of-done.md

SHA-256: 7dacab3c9ae5c6412e31fe4a4dbad0af0e9ef278e0bc89b9c3a461853d5dbc71

```markdown
---
subjects:
  governs: "semantics"
  depends_on:
    - "CCE"
version: 17
updated_at: "2026-10-01 21:38:15 +0400"
relations:
  child_of:
    - CA-M-113
    - CA-M-122
    - CA-R-1581
    - CA-R-1583
atom_id: "CA-M-123"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-123-CORE_META_MODEL-METHOD--write-definitions-of-done.md
---
# Summary

Write Definitions of Done

## Scope

authoring one Definition of Done.

## Claim

**to** write one Definition of Done, the Author **must** perform **all** of:

1. begin the falsification condition expression with: the Plan is **not** Done **if**.
2. make **every** atomic condition observable **and** decidable.
3. enclose **every** composite condition **and** **every** function argument **in** explicit parentheses.
4. evaluate the condition expression according **to** CA-M-122-CORE_META_MODEL-METHOD--evaluate-condition-expressions.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-125-CORE_META_MODEL--assign-subjects-from-the-claim.md

SHA-256: f0159d5c05bac7f9161c02f3d48b8de8cc0644f0ca74f9552d75734f070f1e37

```markdown
---
subjects:
  governs: "Subject Assignment"
  depends_on:
    - "Atom/Claim"
    - "Atom/Summary"
    - "Atom/Subjects"
    - "Subject Path"
    - "Author"
    - "Subject"
    - "Term"
    - "Atom/Content Role: Evaluation"
    - "Evaluation For Relation"
    - "Entity"
    - "Dependent Entity"
version: 25
updated_at: "2026-10-02 20:25:13 +0400"
relations: {}
atom_id: "CA-M-125"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-125-CORE_META_MODEL--assign-subjects-from-the-claim.md
---
# Summary

Assign Subjects from the Claim

## Scope

Subject assignment for an Atom from its Claim **and** complete Markdown Main Content.

## Claim

**to** assign an Atom's Subjects, the Author **must** perform **all** of:

1. read the entire Markdown Main Content, including Summary, Scope, Claim, Details, other registered sections, nested headings, tables, examples, **and** reference labels. build an inventory of canonical Entity mentions with exact locations **and** full resolved paths. treat an Atom citation label rendered under `CA-M-301-CORE_META_MODEL-METHOD--make-atom-claims-easy-to-understand` as the referenced Atom's complete filename **without** its `.md` extension **or** directory path. under `CA-R-1280-CORE_META_MODEL-CORE-REQUIREMENT--reference-every-prerequisite-subject-through-depends-on`, the label is readable reference evidence, **not** an Entity mention **or** Subject target, including **when** it occurs **in** the same sentence as Entity language; inventory an Entity **only** **when** surrounding prose independently uses it.

   recognize Terms through their existing definitions, including `Term` itself under `CA-R-1318-CORE_META_MODEL-CORE-REQUIREMENT--define-term`. `Evaluation` remains a Term **when** used inside an Evaluation Atom under `CA-R-1341-CORE_META_MODEL-CORE-REQUIREMENT--define-evaluation-content-role`. resolve its referenced Entity from that definition **and** the usage context. self-reference alone does **not** (remove a mentioned Entity from the inventory **or** establish a new Entity); a Term's spelling alone does **not** establish its Subject target. retain unresolved meaning as an explicit gap rather than treating it as ordinary wording.
2. select the **`=1`** canonical Entity that the Claim governs **and** reference its narrowest exact Subject Path directly through GOVERNS.

   - for a Claim about entry **or** exit criteria of a Dependent Entity, apply this same narrowest-target rule rather than substituting its wider bearer.
   - **when** the Atom has Content Role Evaluation **and** its Claim defines a conformance check, select the canonical target whose conformance is checked; do **not** select a generic Evaluation label **or** the execution of the check merely from its Content Role. bind the checked authority separately with `evaluation_for` under `CA-R-1018-CORE_META_MODEL-CORE-REQUIREMENT--register-evaluation-targets`.
3. connect **every** other Entity **in** the mention inventory through DEPENDS_ON using its narrowest exact full Subject Path. include mentions outside Claim; do **not** repeat GOVERNS **or** add unmentioned Entities. unresolved mentions block completion rather than disappearing from the inventory.
4. for a definition Claim, use its defined Term **in** the Subject Path that identifies the target being defined, under `CA-R-1279-CORE_META_MODEL-CORE-REQUIREMENT--govern-every-defined-term`. resolve **every** named path component as a Term reference; the path identifies the target **and** the GOVERNS link is the Subject Relation. the path does **not** define its component Terms.
5. split the Atom **before** assignment **when** the Claim governs **`>1`** canonical targets.
6. verify that the distinct GOVERNS **and** DEPENDS_ON targets equal the mention inventory. record **every** reference once **without** creating an intermediate Subject object, repeating definitions, **or** treating path components **and** implicit bearer prefixes as separate Entity mentions.
7. serialize the direct references under `CA-D-269-CORE_META_MODEL-DELIVERY--serialize-atom-subjects-in-frontmatter`. its migration-limited legacy compatibility preserves existing temporal carrier evidence; it does **not** add temporal nesting **to** a migrated flat Carrier.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-127-CORE_META_MODEL-METHOD--evaluate-set-valued-property-membership.md

SHA-256: 869ddf637c7d7e7b302a6a8f218d9971b15899dd8337eabd7e3cc50de6bd7bf2

```markdown
---
subjects:
  governs: "Set-valued Property Membership Evaluation"
  depends_on:
    - "CCE Condition Expression Evaluation"
    - "Set-valued Property"
version: 15
updated_at: "2026-10-01 21:38:15 +0400"
relations:
  child_of:
    - CA-M-122
atom_id: "CA-M-127"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-127-CORE_META_MODEL-METHOD--evaluate-set-valued-property-membership.md
---
# Summary

Evaluate Set-valued Property Membership

## Scope

evaluation of **in** **or** **not in** for one set-valued governed property.

## Claim

**to** evaluate **in** **or** **not in** for one set-valued governed property, the Resolver **must** evaluate **in** as true exactly **when** **`>=1`** property member **`=`** one listed value **and** **must** evaluate **not in** as true exactly **when** no property member **`=`** **any** listed value.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-135-CORE_META_MODEL-METHOD--exclude-generated-only-implementation-edges.md

SHA-256: 53d3574f95dd27c6763d7831471ce5689496fdf9621bfab7abdc86dbe7e3d2ab

```markdown
---
subjects:
  governs: "provenance"
  depends_on: []
version: 18
updated_at: "2026-10-01 21:38:15 +0400"
relations: {}
atom_id: "CA-M-135"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-135-CORE_META_MODEL-METHOD--exclude-generated-only-implementation-edges.md
---
# Summary

Exclude generated-only implementation edges

## Scope

provenance validation of recorded changes in the governed selection.

## Claim

provenance validation inspects **every** recorded change **in** the governed selection. a change contributes an Implementation Relation, implementation coverage, **or** semantic traceability edge **only** **when** it changes **`>=1`** non-generated governed source.

an update **only** **to** generated Projections remains an auditable refresh. it retains its required Journal provenance but cannot become an implementation input **to** the semantic graph that produced the generated Carrier. a mixed change participates **only** through its substantive non-generated governed source changes.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-225-CORE_META_MODEL--retrieve-applicable-methodology-mechanically.md

SHA-256: 331bebb4ba36da94db528c1e7a005332759989c02a0de578666c30025cf48573

```markdown
---
subjects:
  governs: "Applicable Methodology Retrieval"
  depends_on:
    - "Applicable Methodology"
    - "Atom/Subjects"
version: 15
updated_at: "2026-10-02 20:25:13 +0400"
relations: {}
atom_id: "CA-M-225"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-225-CORE_META_MODEL--retrieve-applicable-methodology-mechanically.md
---
# Summary

Retrieve Applicable Methodology Mechanically

## Scope

Applicable Methodology retrieval for one Subject **or** Workflow query.

## Claim

**to** retrieve Applicable Methodology for one Subject **or** Workflow query, the Retriever **must** derive GOVERNS **and** DEPENDS_ON indexes on demand from projected Atom Subjects, select matching GOVERNS paths, add DEPENDS_ON authority **only** through transitive prerequisite closure, retain Applicable Methodology membership order, make no inference, **and** return no Atom **if** no matching GOVERNS path exists.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-228-CORE_META_MODEL-METHOD--write-subject-expressions-with-bearer-and-value-qualification.md

SHA-256: 340bef13eb116227c397231ba6f8bf7fd103221943f75fec48c3dbff6ba5d3cc

```markdown
---
subjects:
  governs: "Subject Expression Writing"
  depends_on:
    - "Subject Path"
    - "Entity"
    - "Relation"
    - "Term"
    - "Subject"
    - "GOVERNS"
    - "DEPENDS_ON"
version: 14
updated_at: "2026-10-01 21:38:15 +0400"
relations: {}
atom_id: "CA-M-228"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-228-CORE_META_MODEL-METHOD--write-subject-expressions-with-bearer-and-value-qualification.md
---
# Summary

Write Subject Expressions with Bearer and Value Qualification

## Scope

authoring one Subject Expression.

## Claim

**to** write a Subject Expression, start with a canonical Entity reference **and** apply `/` **or** `:` qualification **only** **where** the registered relation admits the exact endpoints. `/` retains bearer qualification **and** `:` retains allowed-value qualification; resolve **every** named component, including names **before** **and** **after** the separators, as a Term reference under CA-R-1321. the resulting qualified path identifies its existing canonical target **without** copying it; connecting the Atom **to** that target through GOVERNS **or** DEPENDS_ON creates the Subject Relation, **not** another target Entity.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-229-CORE_META_MODEL--render-governed-terms-and-cce-operators-distinctly.md

SHA-256: 2cbd7347fd35d5f13db953b9a1b5157a155cce9d37ceaa02ee22a3f8a8bcead0

```markdown
---
subjects:
  governs: "Governed Term Rendering"
  depends_on:
    - "CCE Operator"
    - "General Term"
    - "Governed Term"
    - "Scope Unit/Name"
    - "Author"
    - "Markdown Atom Carrier/Main Content/CCE Operator"
version: 12
updated_at: "2026-10-02 20:25:13 +0400"
relations:
  relates_to:
    - CA-D-280
    - CA-M-299
atom_id: "CA-M-229"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-229-CORE_META_MODEL--render-governed-terms-and-cce-operators-distinctly.md
---
# Summary

Render Governed Terms and CCE Operators Distinctly

## Scope

CAPRMEDIO content lexical-case rendering.

## Claim

**to** render CAPRMEDIO content, the Author **must** apply the following lexical-case rules:

- start **every** Governed Term with a capital letter.
- start **every** General Term with a lowercase letter.
- preserve the lowercase spelling of **every** ordinary English word at the start of a sentence **or** list item **unless** an active rule requires an exact-case token.
- preserve the required case of canonical Terms, Scope Unit Names, **and** exact registered references, including at sentence **and** list-item starts.
- preserve the canonical spelling of **every** registered CCE Operator. use CA-D-280 for its representation **in** Markdown Atom Carrier Main Content.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-230-CORE_META_MODEL-METHOD--define-registered-cce-operators-through-cce-methods.md

SHA-256: 4c090008c3e1216f092a433498ab4f2fa3f1172b90f7f3f51fa9e7078e4dde6e

```markdown
---
subjects:
  governs: "CCE Operator"
  depends_on:
    - "CCE Method"
version: 12
updated_at: "2026-10-01 21:38:15 +0400"
relations: {}
atom_id: "CA-M-230"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-230-CORE_META_MODEL-METHOD--define-registered-cce-operators-through-cce-methods.md
---
# Summary

Define Registered CCE Operators through CCE Methods

## Scope

registered CCE Operators in CCE.

## Claim

within CCE, a CCE Operator **means** one canonical lowercase word-form token **or** token sequence **or** one canonical symbolic token that one active CCE Method assigns one syntactic **or** logical function.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-231-CORE_META_MODEL--derive-navigation-projections-from-the-cce-claim.md

SHA-256: 58569ecf2939c7576971b708a291ed0fd7eef9663a9b5cd38a60f90e287124e5

```markdown
---
subjects:
  governs: "Navigation Projection Derivation"
  depends_on:
    - "Atom/Claim"
    - "Atom/Summary"
version: 18
updated_at: "2026-10-02 20:25:13 +0400"
relations: {}
atom_id: "CA-M-231"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-231-CORE_META_MODEL--derive-navigation-projections-from-the-cce-claim.md
---
# Summary

Derive Navigation Projections from the CCE Claim

## Scope

derivation of an Atom's navigation values from its authoritative content.

## Claim

**to** derive an Atom's navigation values, derive them from authoritative content rather than another navigation value:

- derive a new Atom's Summary from its finalized primary contribution within its applicability under CA-R-1465 **and** CA-M-111. for RMED, use Claim read within Scope, **not** Scope alone.
- derive **every** requested Projection from its applicable complete source content, including relevant textual applicability restrictions, **not** from the Summary.
- for an existing Atom identity, retain its Summary **and** check source faithfulness. a needed Summary change follows CA-R-1464 **and** **must not** be applied as a same-identity refresh.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-232-CORE_META_MODEL-CORE--derive-atom-subjects-graph-from-current-atom-subjects.md

SHA-256: c919f93f1ff23638be3797af928c0341db481fe034337b7c0b291c63a4871a9b

```markdown
---
subjects:
  governs: "Subject Projection Derivation"
  depends_on:
    - "Projection/Type: Atom Subjects Graph"
    - "Atom/Subjects"
    - "Subject Path"
    - "Subject"
    - "Atom"
    - "GOVERNS"
    - "DEPENDS_ON"
version: 12
updated_at: "2026-10-02 20:25:13 +0400"
relations: {}
atom_id: "CA-M-232"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-232-CORE_META_MODEL-CORE--derive-atom-subjects-graph-from-current-atom-subjects.md
---
# Summary

Derive Atom Subjects Graph from Current Atom Subjects

## Scope

Atom Subjects Graph derivation from current Atom Subjects.

## Claim

**to** derive an Atom Subjects Graph, the Generator **must** reproduce **every** selected Subject as a direct GOVERNS **or** DEPENDS_ON graph link from its source Atom **to** its target with its exact canonical target, Subject Path, **and** Relation Kind **without** adding authority, requiring a duplicate target-kind field **in** the Atom's Subjects, **or** creating a separately identified Subject object. a Projection **may** derive a target's kind from its canonical authority **when** the Projection's own Spec calls for that classification; it **must not** independently reauthor that kind **or** require it as duplicated source Subjects metadata. an unmigrated temporal Carrier admitted temporarily by CA-D-269 retains its source classification as migration evidence **without** changing the direct reference **or** requiring that classification **in** the canonical flat representation.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-233-CORE_META_MODEL--prefer-positive-normative-statements.md

SHA-256: dd4f7a1a7ffa2f0399c14995f04510c8f23c33751e2d1c6403e78f7a94738a40

```markdown
---
subjects:
  governs: "Normative Atom Prose Authoring"
  depends_on:
    - "Atom"
    - "Atom/Claim"
    - "CCE"
version: 12
updated_at: "2026-10-02 20:25:13 +0400"
relations: {}
atom_id: "CA-M-233"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-233-CORE_META_MODEL--prefer-positive-normative-statements.md
---
# Summary

Prefer Positive Normative Statements

## Scope

normative Atom prose authored **in** CCE.

## Claim

**to** author normative Atom prose, state applicable conditions **and** required behavior positively **when** this preserves the complete Claim; an explicit prohibition is warranted **only** **when** it prevents a real ambiguity **or** protects an important boundary.

## Details

- use the positive statement **when** it already makes the required behavior clear.
- make a necessary prohibition explicit **when** the positive statement alone leaves a materially different interpretation **or** fails **to** protect the boundary.
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-234-CORE_META_MODEL--register-expandable-canonical-cce-operator-list.md

SHA-256: 51ccafdcd78490efa4d387d203901dd58151063016c6cb80fe197a3f901f6dc5

```markdown
---
subjects:
  governs: "CCE Operator Registry"
  depends_on:
    - "CCE Operator"
    - "CCE Method"
version: 12
updated_at: "2026-10-02 20:25:13 +0400"
relations: {}
atom_id: "CA-M-234"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-234-CORE_META_MODEL--register-expandable-canonical-cce-operator-list.md
---
# Summary

Register Expandable Canonical CCE Operator List

## Scope

the canonical CCE Operator Registry.

## Claim

the current canonical CCE Operator Registry **must** contain this expandable set:

1. statement form: **to**, **means**.
2. modality: **must**, **must not**, **may**.
3. condition: **if**, **then**, **when**, **otherwise**.
4. temporal condition: **before**, **after**, **until**, **unless**.
5. quantification: **all**, **every**, **any**, **none**.
6. logical/set: **and**, **or**, **not**, **without**, **where**.
7. restriction: **only**.
8. predicate: **in**, **not in**, **is empty**, **is not empty**, **contains**, **starts with**, **ends with**.
9. comparison: **`=`**, **`!=`**, **`<`**, **`<=`**, **`>`**, **`>=`**.

## Details

another token **may** enter the CCE Operator Registry **when** one active CCE Method assigns the token one syntactic **or** logical function.
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-235-CORE_META_MODEL--express-cardinality-with-comparison-operators-and-integer-literals.md

SHA-256: 71d6a9c1edd3e6d6f679274929db91f1a513bffc63c3cf345ed730771fb7fe78

```markdown
---
subjects:
  governs: "Cardinality Constraint Authoring"
  depends_on:
    - "Cardinality Constraint"
    - "CCE Operator Registry"
    - "Nonnegative Integer Literal"
version: 11
updated_at: "2026-10-02 20:25:13 +0400"
relations: {}
atom_id: "CA-M-235"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-235-CORE_META_MODEL--express-cardinality-with-comparison-operators-and-integer-literals.md
---
# Summary

Express Cardinality with Comparison Operators **and** Integer Literals

## Scope

numeric Cardinality Constraint authoring.

## Claim

**to** author one numeric Cardinality Constraint, the Author **must** serialize one canonical comparison CCE Operator immediately followed by one Nonnegative Integer Literal as a prefix immediately **before** the counted Entity **or** expression; examples: **`=1`** Author, **`>=1`** Requirement Atom, **`<=1`** Type, **`>=0`** Property.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-236-CORE_META_MODEL--normalize-noncanonical-cce-operator-expressions.md

SHA-256: a6adb30a7a77963d6ae72ee3cd46daf38792ab08f92a22c9d85927d56d654aed

```markdown
---
subjects:
  governs: "CCE Operator Expression Normalization"
  depends_on:
    - "CCE Operator Expression"
    - "CCE Operator Registry"
version: 12
updated_at: "2026-10-02 20:25:13 +0400"
relations: {}
atom_id: "CA-M-236"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-236-CORE_META_MODEL--normalize-noncanonical-cce-operator-expressions.md
---
# Summary

Normalize Noncanonical CCE Operator Expressions

## Scope

noncanonical CCE Operator Expressions.

## Claim

**to** normalize one noncanonical CCE Operator Expression, the Author **must** apply **all** applicable rewrites:

- `each` **to** **every**.
- `equals` **to** **`=`**.
- `does not equal` **to** **`!=`**.
- `both <A> and <B>` **to** `(<A>` **and** `<B>)`.
- `either <A> or <B>` **to** `(<A>` **or** `<B>)`.
- `neither <A> nor <B>` **to** **not** `(<A>` **or** `<B>)`.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-237-CORE_META_MODEL--author-claim-value-sets.md

SHA-256: df29e7212946501440f940523a8367aa06d02321e7da08ad0313caf66504bef9

```markdown
---
subjects:
  governs: "Claim Value Set Authoring"
  depends_on:
    - "Atom/Claim"
    - "Author"
    - "Claim Value Set"
    - "Property"
    - "Subject Expression"
    - "IS_ALLOWED_VALUE_OF"
version: 10
updated_at: "2026-10-02 20:25:13 +0400"
relations:
  child_of:
    - CA-M-115
atom_id: "CA-M-237"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-237-CORE_META_MODEL--author-claim-value-sets.md
---
# Summary

Author Claim Value Sets

## Scope

Claim Value Set authoring.

## Claim

**to** author one Claim Value Set, the Author **must**:

1. identify **`=1`** Property X within **`=1`** Claim;
2. write its finite allowed-value set as `X: (A, B, C)`;
3. include **`>=1`** unique canonical values **and** treat their order as non-authoritative;
4. retain the complete set as **`=1`** Claim **only** **if** **all** values **must** be accepted, replaced, **and** retired together;
5. interpret `:` as Claim Value-Set syntax inside that Claim **and** as **`=1`** IS_ALLOWED_VALUE_OF relation **only** inside a Subject Expression.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-239-CORE_META_MODEL--derive-dependency-order-from-explicit-edges.md

SHA-256: 1b02d58e3d7915ed2a089ee3527059e22059549f6ea831ab7b442eec2419d78b

```markdown
---
subjects:
  governs: "Dependency Order Derivation"
  depends_on:
    - "DEPENDS_ON"
    - "DERIVED_FROM"
    - "Atom/Direct Relation Serialization"
    - "Artifact/Revision"
    - "Artifact"
    - "Atom/Content Role: Plan/Type: Plan"
version: 11
updated_at: "2026-10-02 20:25:13 +0400"
relations:
  child_of:
    - CA-M-120
atom_id: "CA-M-239"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-239-CORE_META_MODEL--derive-dependency-order-from-explicit-edges.md
---
# Summary

Derive Dependency Order from Explicit Edges

## Scope

non-Plan Artifact dependency order derivation from explicit edges.

## Claim

**to** derive one non-Plan Artifact dependency order, the resolver **must**:

1. construct one directed graph from direct `relations.depends_on` edges from **every** dependent Artifact **to** **every** prerequisite Artifact;
2. derive its `required_by` inverse view **without** authoring inverse edges;
3. calculate one deterministic prerequisite-first topological order with canonical identity **only** as a tie-breaker; **and**
4. reject a cycle.

the resolver **must not** use target-list position, Local Order, **or** `relations.derived_from` as a dependency edge.

## Details

Plan readiness follows `BLOCKS` under CA-R-1580: **all** blockers **must** be Done, **and** independent ready Plans **may** execute concurrently subject **to** their permissions; navigation order **must not** add blocking.
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-240-CORE_META_MODEL-METHOD--derive-restricted-cce-canonical-signatures-without-source-rewrite.md

SHA-256: 28efd9bb18d9a0c1638ec827eb985407e7acd8b5ae1fb5574a8312325d77cfb3

```markdown
---
subjects:
  governs: "Canonical Signature Derivation"
  depends_on:
    - "Atom/Claim"
    - "Atom/Claim/Canonical Signature"
    - "CCE Operator"
version: 9
updated_at: "2026-10-01 21:38:15 +0400"
relations:
  child_of:
    - CA-M-115
atom_id: "CA-M-240"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-240-CORE_META_MODEL-METHOD--derive-restricted-cce-canonical-signatures-without-source-rewrite.md
---
# Summary

Derive Restricted CCE Canonical Signatures **without** Source Rewrite

## Scope

derivation of Canonical Signatures from one selected Atom Carrier folder.

## Claim

**to** derive Canonical Signatures from one selected Atom Carrier folder, the Tool **must** inspect **only** active single-statement Atom Claims, identify **every** outermost parenthesized expression that **contains** the **and** Operator **or** the **or** Operator, derive a Canonical Signature **only** **if** the expression satisfies the Restricted Boolean Expression grammar, emit source-identity evidence **and** **every** exclusion diagnostic, **and** make no source-Carrier rewrite, lifecycle change, Claim merge, **or** authority decision.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-241-CORE_META_MODEL--derive-canonical-scope-signatures-without-source-rewrite.md

SHA-256: f5d5edb002a405d0f20269a6a92ce43391c00a8e3014434d69636cdd3461a4c6

```markdown
---
subjects:
  governs: "Canonical Scope Signature Derivation"
  depends_on:
    - "Scope Expression"
    - "Scope Expression/Canonical Scope Signature"
    - "Atom/Carrier"
version: 9
updated_at: "2026-10-01 21:38:15 +0400"
relations:
  child_of:
    - CA-M-121
atom_id: "CA-M-241"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-241-CORE_META_MODEL--derive-canonical-scope-signatures-without-source-rewrite.md
---
# Summary

Derive Canonical Scope Signatures **without** Source Rewrite

## Scope

derivation of Canonical Scope Signatures from one caller-selected Atom Carrier folder.

## Claim

**to** derive Canonical Scope Signatures from one caller-selected Atom Carrier folder, the Tool **must** inspect **only** active Carriers with **`=1`** unwrapped Scope Expression **in** one `## Scope` section, resolve **every** atomic identity against active Atom IDs **in** that selected folder, derive a signature **only** **if** the Scope Expression satisfies the restricted Canonical Scope Signature grammar, emit source identity, source revision, source Carrier digest, source frontier digest, source expression, signature, **and** exclusion diagnostic, **and** make no source-Carrier rewrite, lifecycle change, Claim merge, authority decision, **or** dependency relation.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-264-CORE_META_MODEL-METHOD--write-evaluations-with-reproducible-falsification.md

SHA-256: d8b61e6baf4d04cfa1ecf4eeea501e476357c2b1d2be008e72efc024f569f4bb

```markdown
---
subjects:
  governs: "Atom/Content Role: Evaluation/authoring"
  depends_on:
    - "Atom/Content Role: Evaluation"
    - "Atom/Content Role: Method"
    - "Atom/Scope"
    - "Atom/Local Tier"
    - "Evaluation For Relation"
version: 8
updated_at: "2026-10-01 21:38:15 +0400"
relations: {}
atom_id: "CA-M-264"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-264-CORE_META_MODEL-METHOD--write-evaluations-with-reproducible-falsification.md
---
# Summary

Write evaluations with reproducible falsification

## Scope

authoring or maintaining an Evaluation.

## Claim

**to** write **or** maintain an Evaluation, identify its checked authority **and** Scope, select a suitable test technique, specify recoverable inputs, procedure, **and** observable falsifying conditions, **and** preserve the distinction between Core foundations, independent General evaluation criteria **where** General is admitted, **and** the default Standard tier; keep writing techniques, test frameworks, **and** authoring conventions **in** Method authority rather than treating them as test results.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-265-CORE_META_MODEL-GENERAL-METHOD--derive-evaluation-groups-from-checked-authority.md

SHA-256: 9671bdbce08ff36fa425d0715ec70e752b9b27574025828c12bb92d8908fc15b

```markdown
---
subjects:
  governs: "Atom/Content Role: Evaluation/grouping"
  depends_on:
    - "Atom/Content Role"
    - "Evaluation For Relation"
version: 9
updated_at: "2026-10-01 21:38:15 +0400"
relations: {}
atom_id: "CA-M-265"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-265-CORE_META_MODEL-GENERAL-METHOD--derive-evaluation-groups-from-checked-authority.md
---
# Summary

Derive evaluation groups from checked authority

## Scope

derivation of Er, Em, and Ed groups from checked authority.

## Claim

**to** derive Er, Em, **and** Ed groups, resolve the Content Role of **every** `evaluation_for` target **and** include the Evaluation **in** the corresponding Requirement, Method, **or** Delivery group; **if** targets span multiple roles, **then** include it **in** **every** applicable group **without** assigning a new Content Role **or** persisting a duplicate target-role field. absence of individual targets on a Core **or** General Evaluation policy admitted by CA-R-1018-CORE_META_MODEL-CORE-REQUIREMENT--register-evaluation-targets **must not** require an invented classification.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-271-CORE_META_MODEL-METHOD--resolve-confidence-thresholds-by-source-precedence.md

SHA-256: 7988f7d01120126c071f1033991c06994a2cab874612a29c90e54d521b5ed0ab

```markdown
---
subjects:
  governs: "Confidence Threshold/resolution"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Confidence Threshold"
    - "Operator"
    - "Hub Atom"
    - "Framework Instance Settings"
    - "Property"
    - "AI Agent"
version: 8
updated_at: "2026-09-29 22:34:37 +0000"
relations:
  child_of:
    - "CA-R-1428"
atom_id: "CA-M-271"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-271-CORE_META_MODEL-METHOD--resolve-confidence-thresholds-by-source-precedence.md
---
# Summary
Resolve confidence thresholds by source precedence

## Scope
resolution of a Confidence Threshold.

## Claim
**to** resolve an effective Confidence Threshold, select the first applicable explicit source **in** this precedence:

1. direct Operator input for the current decision context.
2. an explicit value on the current Plan.
3. the nearest Hub with an explicit value, walking `IS_DECOMPOSITION_OF` from nearest **to** farthest; read its own current Plan File Carrier under `CA-D-472-CORE_META_MODEL-DELIVERY--serialize-explicit-plan-confidence-overrides`, **not** a separate Objective targeting a folder.
4. the Framework Instance Settings default.

### resolution constraints

- an omitted optional override preserves inheritance; another explicit field does **not** stop lookup for the omitted field. a missing mandatory Plan file is invalid, **not** an inherited-setting selection.
- use current Plan Revisions, **not** historical Carrier copies **or** unrelated nearby files; a Label is **not** an override source.
- **if** a reached source is invalid **or** ambiguous, **or** no source supplies a value, request Operator disposition **before** the affected autonomous action; do **not** invent a value **or** silently fall through past invalid authority.
- direct Operator input applies **only** within its stated context.
- do **not** copy inherited values into Plan overrides. preserve an explicit selection even **when** it **`=`** the inherited value; a later upstream change **must not** overwrite it.
- this resolution **must not** create another Atom, settings file, **or** execution permission.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-272-CORE_META_MODEL-METHOD--classify-an-atom-local-tier-from-its-complete-claim.md

SHA-256: 92560c8c303d5d2646dbb612dd343cca65cab92123e1f211c82d863f8a42fe0d

```markdown
---
subjects:
  governs: "Atom/Local Tier/classification"
  depends_on:
    - "Atom/Claim"
    - "Atom/Scope"
    - "Atom/Content Role"
    - "Atom/Local Tier"
    - "Atom/Global Tier"
    - "Scope Unit"
    - "Type"
    - "Methodology Source"
    - "Autonomous Confidence Threshold"
version: 12
updated_at: "2026-10-01 21:38:15 +0400"
relations: {"method_for": ["CA-R-1566", "CA-R-659", "CA-R-1431", "CA-R-1573"]}
atom_id: "CA-M-272"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-272-CORE_META_MODEL-METHOD--classify-an-atom-local-tier-from-its-complete-claim.md
---
# Summary

Classify an Atom Local Tier from its complete Claim

## Scope

classification of an Atom's Local Tier against the tiers admitted **in** its current Scope Unit.

## Claim

**to** classify one Atom's Local Tier, the Author **must** perform **all** of:

1. resolve the exact current Atom identity **and** Revision, complete independently replaceable Claim, governed Subject, authority owner, Atom Scope, Claim Target Scope Unit **and** textual Claim Scope, Content Role, Type, **and** governing boundary; resolve the Local Tiers admitted **in** its current Scope Unit under CA-R-680-CORE_META_MODEL-GENERAL-REQUIREMENT--order-project-local-tiers **or** CA-R-1442-CORE_META_MODEL-GENERAL-REQUIREMENT--order-non-project-local-tiers **and** apply the existing Project Principle **and** Goal exceptions **and** Type restrictions **before** classifying an ordinary Claim. CAPO **and** I content resolves **to** Standard under CA-R-1566-CORE_META_MODEL-GENERAL-REQUIREMENT--keep-change-and-implementation-content-at-standard **and** proceeds directly **to** the preservation check; this explicit role-tier rule is **not** an inference from the governed Subject. resolve ownership **and** targeting under CA-M-273-CORE_META_MODEL-METHOD--derive-ownership-and-claim-target-atom-sets **and** read applicability restrictions from the body sections registered by CA-D-495-CORE_META_MODEL-CORE-DELIVERY--carry-applicability-in-the-registered-body-sections, including Scope for RMED, **when** deriving local applicability is required. an unresolved referent, contradictory boundary, unadmitted Type, unexplained source change, **or** independently replaceable mixed contribution stops that Atom's classification for the existing admission **or** Atom-boundary review.
2. test the complete Claim against CA-R-659-CORE_META_MODEL-CORE-REQUIREMENT--define-core-local-tier. identify the Core foundation it establishes for **all** Atoms at greater Global Tiers **in** the Scope Unit under CA-R-1573-CORE_META_MODEL-CORE-REQUIREMENT--govern-greater-global-tiers-within-each-scope-unit, including General **and** Standard, **and** explain which identity, purpose, owner, fundamental separation, **or** conservation boundary would cease **to** hold **if** the Claim were negated. **if** the dependency is established, **then** assign Core **and** proceed **to** the preservation check; usefulness, scope-wide occurrence, importance, precision, **and** reuse alone establish no constitutive dependency.
3. **if** the Core test is false **and** General is admitted **in** the current Scope Unit, **then** test the complete Claim against CA-R-1431-CORE_META_MODEL-CORE-REQUIREMENT--define-general-local-tier. identify **all** Standard Atoms **in** the Scope Unit governed under CA-R-1573-CORE_META_MODEL-CORE-REQUIREMENT--govern-greater-global-tiers-within-each-scope-unit; do **not** filter them by matching Content Role **or** Subject. record **`=2`** materially different realizations that preserve its complete contract **and** a changed shared contract that preserves its Core boundaries while changing its conformance. explain how this independently replaceable specification can be accepted, revised, **or** retired **without** duplicating a Core premise **or** concrete realization. assign General **only** **when** both witnesses **and** the independent authority unit are established. **if** General is **not** admitted, **then** skip this test.
4. **if** no applicable higher Local Tier **or** explicit tier rule applies, **then** use Standard as the default lowest Local Tier under CA-R-660-CORE_META_MODEL-CORE--define-standard-local-tier. no concrete Carrier field, path, token, format, realization procedure, test specimen, **or** representation-change witness is required for Standard. an omitted Local Tier token resolves **to** Standard under CA-D-285-CORE_META_MODEL-DELIVERY--serialize-local-tier-filename-tokens, subject **to** its Project Goal exception; that Carrier default does **not** override an applicable higher-tier requirement **or** resolve missing classification evidence.
5. perform the preservation check **before** accepting the classification: record the exact source identity, Revision, Claim contribution, clause-based test evidence, witnesses required by the tests actually applied, previous **and** proposed tier **and** structural rank, Scope **and** relation impacts, **and** disposition. classify a definition by its own complete Claim rather than by the value it defines. preserve identity, ownership, unchanged Claim meaning, Scope binding, **and** necessary direct relations; remove **or** correct an invalid tier-parent edge **only** with its explicit authority rationale. return an identified unresolved result **if** the applicable tiers **or** classification evidence are unresolved, the evidence conflicts, **or** independently replaceable contributions require different tiers; do **not** use Standard **to** conceal an unresolved decision, invent a General Atom, **or** average the tiers. consult applicable Project Principles **and** request **`=1`** exact Operator disposition **only** **when** a material unresolved proposition remains below the effective Autonomous Confidence Threshold.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-273-CORE_META_MODEL--derive-ownership-and-claim-target-atom-sets.md

SHA-256: 43cf73127ffbc418ff0479c45001f05129cf3ca78d981dfa5faf57eeee744dfa

```markdown
---
subjects:
  governs: "Atom selection"
  depends_on:
    - "Atom/Revision/Author"
    - "Owned Atoms"
    - "Targeting Atoms"
    - "Subtree-owned Atoms"
    - "Subtree-targeting Atoms"
    - "Scope Unit"
    - "Atom Collection"
    - "Atom/Claim/Target Scope Unit"
    - "Atom/Content Role"
    - "Atom/Status"
    - "Artifact/Revision"
    - "Directory Carrier"
version: 13
updated_at: "2026-10-01 21:40:53 +0400"
relations: {}
atom_id: "CA-M-273"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-273-CORE_META_MODEL--derive-ownership-and-claim-target-atom-sets.md
---
# Summary

Derive Ownership **and** Claim-target Atom Sets

## Scope

selection of Owned Atoms, Targeting Atoms, Subtree-owned Atoms, **and** Subtree-targeting Atoms for a Scope Unit.

## Claim

**to** derive the four Atom sets for a selected Scope Unit, the resolver **must** perform **all** of:

1. establish the complete authoritative source frontier, including Atoms outside the selected subtree that can target a Scope Unit inside it; scanning **only** locally stored Atoms is insufficient for Targeting Atoms **or** Subtree-targeting Atoms.
2. read **every** candidate Atom's carried current Scope Unit **and** check it against its nearest containing Scope Unit, passing through Atom Collections **and** Plan Hub Carriers **without** treating their nesting as additional Scope Unit ownership. preserve the carried external-Atom Author fallback under CA-D-276-CORE_META_MODEL-DELIVERY--use-economical-yaml-frontmatter **when** no containing Scope Unit exists; do **not** invent a Scope Unit owner.
3. resolve **every** candidate's Claim Target Scope Unit independently of ownership. read the internally carried target; absence of a required value is invalid, **not** permission **to** infer it from placement; apply CA-R-1588-CORE_META_MODEL-CORE-REQUIREMENT--default-plan-target-to-the-enclosing-scope-unit for Plans within Hub decomposition. an unresolved required target remains unresolved. a reference **to** another Scope Unit **must not** transfer ownership, **and** the target **must** resolve **to** a Scope Unit, **not** a Hub Atom **or** another non-Scope-Unit object. Claim Scope restrictions remain **in** the body sections registered by CA-D-495, including Scope for RMED, **and** do **not** create extra targets.
4. derive Owned Atoms, Targeting Atoms, Subtree-owned Atoms, **and** Subtree-targeting Atoms under CA-R-1447-CORE_META_MODEL-GENERAL-REQUIREMENT--define-owned-atoms, CA-R-1448-CORE_META_MODEL-GENERAL-REQUIREMENT--define-targeting-atoms, CA-R-942-CORE_META_MODEL-GENERAL-REQUIREMENT--define-subtree-owned-atoms, **and** CA-R-1449-CORE_META_MODEL-GENERAL-REQUIREMENT--define-subtree-targeting-atoms respectively. use the Scope Unit tree for descendant coverage; do **not** substitute physical subtree membership for Claim targeting **or** inferred inherited applicability for an explicit **or** default Claim target.
5. retain source Atom **and** Revision references **without** creating additional authoritative Atom copies. apply Content Role, Status, **and** other requested filters **after** resolving the selected set; the alias `spec` selects the Active RMED subset under CA-M-288-CORE_META_MODEL-METHOD--use-spec-as-an-alias-for-active-rmed-subtree-targeting-atoms, independently of Local Tier.
6. report the exact missing source, owner, target, ancestry, **or** required filter value **and** withhold a complete affected result **when** it is unresolved **or** contradictory. a complete empty set remains empty; an incomplete frontier **must not** be reported as a complete empty set.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-275-CORE_META_MODEL-METHOD--format-scope-unit-names.md

SHA-256: d7579c6270371ce4a2e9802e93451c466dfb8034083e28f2906398448605251a

```markdown
---
subjects:
  governs: "Scope Unit/Name"
  depends_on:
    - "Scope Unit"
version: 7
updated_at: "2026-10-01 21:40:53 +0400"
relations:
  method_for:
    - "CA-R-962"
atom_id: "CA-M-275"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-275-CORE_META_MODEL-METHOD--format-scope-unit-names.md
---
# Summary

Format Scope Unit Names

## Scope

Scope Unit Names.

## Claim

**to** write a Scope Unit Name, join nonempty uppercase letter-or-digit word tokens with single underscores.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-276-CORE_META_MODEL-METHOD--repair-accidental-atom-id-reuse.md

SHA-256: 4d525fb2a37384a43214576fae9fc9b5e554a1ba096b72fdc252991376c0d74f

```markdown
---
subjects:
  governs: "Atom/Identity/collision repair"
  depends_on:
    - "Atom/Identity"
    - "Atom/Content Role"
    - "Atom/Claim"
    - "Atom/Scope"
    - "Artifact/Revision"
    - "Carrier/Canonical Address"
    - "Project"
    - "Operator"
    - "AI Agent"
    - "Confidence Threshold"
    - "Work Journal"
version: 9
updated_at: "2026-10-01 21:40:53 +0400"
relations: {"method_for":["CA-R-728"]}
atom_id: "CA-M-276"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-276-CORE_META_MODEL-METHOD--repair-accidental-atom-id-reuse.md
---
# Summary

Repair accidental Atom ID reuse

## Scope

repair of accidental reuse of assigned Project Atom IDs.

## Claim

**to** repair accidental reuse of an assigned Project Atom ID, an AI Agent **must** perform **all** of:

1. identify the distinct source Atoms by exact Carrier address, Revision, **and** recorded history. distinguish accidental reuse from legitimate Revisions of the same Atom **and** derived copies of its Carrier.
2. establish the original valid owner from recorded assignment history. **if** the original owner cannot be established at the effective Confidence Threshold, request an Operator decision for that collision **before** changing its identities **or** references. filename order, discovery order, current filesystem timestamps, **or** the highest Version **must not** select the owner.
3. preserve the original owner's Atom ID. give **every** later accidental reuse the next unreused Project-wide number for its own Content Role under CA-D-450-CORE_META_MODEL-DELIVERY--number-project-owned-atoms-within-each-content-role, using the encoding under CA-D-378-CORE_META_MODEL-DELIVERY--serialize-assigned-atom-identities. this corrects invalid reuse **and** does **not** authorize changing a valid owner's immutable identity.
4. preserve **every** affected Atom's Claim, Content Role, Atom Scope, Claim Target Scope Unit, **and** textual Claim Scope. preserve its immutable prior Revisions **and** recorded history; record the exact predecessor-to-corrected-identity mapping **in** the existing Work Journal **without** rewriting historical Carriers **or** Records.
5. resolve **every** affected current reference against its intended Atom using the reference's context **and** recorded history. update references **only** **when** their intended targets are established; request an Operator decision for unresolved references. do **not** replace the ambiguous ID indiscriminately.
6. verify that the repaired active identities resolve uniquely **and** **every** affected current reference still identifies its intended Claim **before** declaring the collision repaired. keep unrelated Claims **and** identities unchanged.
7. perform repair as an explicitly authorized source change, **not** as an automatic side effect of lookup **or** compilation. preserve CA-D-336-CORE_META_MODEL-DELIVERY--resolve-active-atoms-from-canonical-carrier-identities's failure on ambiguous lookup **until** source repair is complete, **and** regenerate affected Projections from their corrected sources through their existing governed workflows.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-277-CORE_META_MODEL-METHOD--report-in-silent-mode.md

SHA-256: f923b99df9e1b3c9f5434e3ada5de1a958e29d12cf15c889a31ca9c5bd7c5058

```markdown
---
subjects:
  governs: "Framework Instance Settings/interaction/reporting mode: silent"
  depends_on:
    - "Framework Instance Settings/interaction/reporting mode"
    - "Framework Instance Settings/interaction/reporting mode/effects"
    - "Framework Instance Settings/interaction/reporting mode/mandatory information"
    - "Artifact"
    - "Skill"
    - "Project"
version: 11
updated_at: "2026-10-01 21:40:53 +0400"
relations: {"relates_to":["CA-R-1628","CA-R-1439","CA-R-1440","CA-R-1558","CA-O-052","CA-R-1750"]}
atom_id: "CA-M-277"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-277-CORE_META_MODEL-METHOD--report-in-silent-mode.md
---
# Summary

Report **in** silent mode

## Scope

silent-mode reporting.

## Claim

**to** report **in** `silent` mode, answer exploratory input normally **and**, apart from the mandatory information governed by CA-R-1440-CORE_META_MODEL-GENERAL-REQUIREMENT--preserve-mandatory-information-in-every-reporting-mode, report **only** durable Artifacts **or** Project state that CAPRMEDIO created, updated, archived, committed, **or** **otherwise** changed; omit ordinary announcements of mode selection, workflow routing, Skill chaining, **and** gate transitions.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-278-CORE_META_MODEL--report-in-verbose-mode.md

SHA-256: 83268166eb114056680a614852a1a3812947ec20706766c1e2ec0a0d2677e282

```markdown
---
subjects:
  governs: "Framework Instance Settings/interaction/reporting mode: verbose"
  depends_on:
    - "Framework Instance Settings/interaction/reporting mode"
    - "Framework Instance Settings/interaction/reporting mode/effects"
    - "Framework Instance Settings/interaction/reporting mode/mandatory information"
    - "Artifact"
    - "Skill"
version: 9
updated_at: "2026-10-02 20:25:13 +0400"
relations: {"relates_to":["CA-R-1628","CA-R-1439","CA-R-1440","CA-O-052","CA-R-1750"]}
atom_id: "CA-M-278"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-278-CORE_META_MODEL--report-in-verbose-mode.md
---
# Summary

Report **in** verbose mode

## Scope

reporting **in** `verbose` mode.

## Claim

**to** report **in** `verbose` mode, explicitly report relevant workflow modes, mode transitions, selected Skill chains, entry **and** exit gates, **and** planned **or** completed Artifact operations, together with the mandatory information governed by CA-R-1440-CORE_META_MODEL-GENERAL-REQUIREMENT--preserve-mandatory-information-in-every-reporting-mode.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-279-CORE_META_MODEL-GENERAL-METHOD--resolve-missing-framework-parameters-from-default-settings.md

SHA-256: c2e860f2bde6f00870a04b8641e652f0d354ad3d22b66011068cb67cf423a2b0

```markdown
---
subjects:
  governs: "Framework Instance Settings/parameter resolution"
  depends_on:
    - "Framework Instance Settings"
    - "Default Settings"
    - "Project"
    - "Operator"
version: 8
updated_at: "2026-09-29 22:34:37 +0000"
relations:
  relates_to:
    - "CA-R-1402"
    - "CA-R-1441"
    - "CA-R-1750"
    - "CA-D-407"
    - "CA-D-408"
atom_id: "CA-M-279"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-279-CORE_META_MODEL-GENERAL-METHOD--resolve-missing-framework-parameters-from-default-settings.md
---
# Summary
Resolve missing framework parameters from Default Settings

## Scope
resolution of a Framework Instance Settings parameter.

## Claim
**to** resolve a Framework Instance Settings parameter, use its explicit value **if** that parameter is present **in** the current Project's Framework Instance Settings; **otherwise**, use the corresponding value from Default Settings. determine presence for the individual parameter, **not** its containing section **or** the truthiness of its value, so valid `false`, `0`, **and** empty values remain explicit selections. validate the selected value against its governing parameter authority **and** reject an invalid explicit value **without** falling back. **if** neither source supplies a required parameter, report that parameter as unresolved **and** stop the operation that requires it; an optional parameter **may** remain absent. do **not** copy inherited values into Framework Instance Settings as explicit selections.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-287-CORE_META_MODEL-METHOD--exclude-activity-labels-from-content-role-names.md

SHA-256: 099c91d3ca92f46ecbf27c2492b761965e97725a42b2aeed83b964f0ccf32f46

```markdown
---
subjects:
  governs: "Content Role Naming"
  depends_on:
    - "Atom/Content Role/Name"
    - "Author"
    - "Status"
version: 10
updated_at: "2026-10-01 21:40:53 +0400"
relations: {}
atom_id: "CA-M-287"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-287-CORE_META_MODEL-METHOD--exclude-activity-labels-from-content-role-names.md
---
# Summary

Exclude Activity Labels from Content Role Names

## Scope

Content Role names.

## Claim

**to** name a Content Role, the Author **must not** use a verb, imperative, workflow instruction, Status, **or** activity label.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-288-CORE_META_MODEL-METHOD--use-spec-as-an-alias-for-active-rmed-subtree-targeting-atoms.md

SHA-256: b71c8ce5127d89f83c76b00944735dbaa6dac3e01384196e2e0169ed7da94f3a

```markdown
---
subjects:
  governs: "Subtree-targeting Atoms"
  depends_on:
    - "Atom/Content Role"
    - "Atom/Status"
    - "Author"
version: 7
updated_at: "2026-10-01 21:40:53 +0400"
relations: {}
atom_id: "CA-M-288"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-288-CORE_META_MODEL-METHOD--use-spec-as-an-alias-for-active-rmed-subtree-targeting-atoms.md
---
# Summary

Use spec as an Alias for Active RMED Subtree-targeting Atoms

## Scope

Active RMED Subtree-targeting Atom references.

## Claim

**to** refer **to** Subtree-targeting Atoms filtered **to** Active Revisions **and** Content Role **in** (Requirement, Method, Evaluation, Delivery), an Author **may** use `spec` as a non-authoritative alias for that same filtered set.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-291-CORE_META_MODEL-GENERAL--author-project-structure-without-competing-declarations.md

SHA-256: 0c8da5e8f320adcf41f9258c77a926b77208cc7de28df68d3184567e3d0cb0f2

```markdown
---
subjects:
  governs: "Project Structure"
  depends_on:
    - "Scope Unit"
    - "Scope Unit/Name"
    - "Scope Unit/Type"
    - "Scope Unit/Label"
    - "Scope Unit/Local Order"
    - "Scope Unit/Navigational Order Number"
    - "Goal"
    - "Framework Instance Settings"
    - "Carrier"
version: 5
updated_at: "2026-10-01 21:40:53 +0400"
relations:
  relates_to:
    - "CA-R-1483"
    - "CA-R-1484"
    - "CA-R-1485"
    - "CA-R-1430"
atom_id: "CA-M-291"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-291-CORE_META_MODEL-GENERAL--author-project-structure-without-competing-declarations.md
---
# Summary

Author Project Structure **without** competing declarations

## Scope

Project Structure declarations.

## Claim

**to** express Project Structure, use one declaration for **every** non-root Scope Unit, reference its parent by the reserved Project-root reference **or** the parent's unique Name, **and** keep structural Local Order distinct from Navigational Order Number. retain an explicit Label independently of Ordered/Unordered Type. retain readable Structural Level **and** authority path **only** with their checked derivation from declared parentage **and** applicable Carrier conventions; physical nesting **must not** silently replace logical parentage. use concrete Carrier bindings as declared values rather than repeating them **in** Goal, Requirement, **or** Delivery Atoms. write an Authority Mode override **only** **when** explicitly selected for that unit; an omitted override remains inherited rather than copied as an explicit value. references **and** observations **must** distinguish the declared unit from its existing Carrier **and** Goal coverage.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-294-CORE_META_MODEL--use-simpler-words-without-losing-meaning.md

SHA-256: c0efb3ac9832f3bc7501c4a4ad3b54c5a51d125dbba29da5600817c78c53b47d

```markdown
---
version: 4
updated_at: "2026-10-02 20:35:16 +0400"
relations:
  child_of:
    - CA-R-940
    - CA-R-941
  method_for:
    - CA-R-940
    - CA-R-941
  relates_to:
    - CA-M-229
    - CA-R-1273
subjects:
  governs: "language"
  depends_on:
    - "Author"
    - "Atom/Claim"
    - "Atom/Summary"
    - "CCE"
    - "Governed Term"
    - "CCE Operator"
atom_id: "CA-M-294"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-294-CORE_META_MODEL--use-simpler-words-without-losing-meaning.md
---
# Summary

Use simpler words without losing meaning

## Scope

CAPRMEDIO content wording.

## Claim

**when** choosing wording for CAPRMEDIO content, the Author **must** choose words **and** phrases that are simpler **and** more familiar **to** the intended reader **when** they preserve the intended meaning **without** adding ambiguity.

## Details

- prefer clear everyday wording over unnecessary jargon **or** specialized wording.
- preserve who **or** what the statement concerns, its obligations **or** permissions, quantities, conditions, boundaries, **and** logical distinctions.
- prefer a clear longer phrase over a shorter obscure expression; fewer words do **not** necessarily make the content simpler.
- retain specialized wording **when** replacing it would lose a necessary distinction **or** make the meaning less precise.
- retain exact canonical Terms, CCE Operators, **and** references. simpler wording does **not** authorize an unregistered synonym **or** a silent Term rename.

for a Summary, simplify its wording while preserving its source faithfulness under CA-R-1273; this does **not** require restating the complete Claim.
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-295-CORE_META_MODEL--resolve-implementation-retry-limits-by-source-precedence.md

SHA-256: 5627d9a55942dba36d0d58b83b250b4c8f3e2aa88f16b2da71409987ff8fbcd8

```markdown
---
version: 9
updated_at: "2026-09-28 15:12:22 +0400"
relations:
  child_of:
    - CA-R-1489
  depends_on:
    - CA-M-279
subjects:
  governs: "Implementation Retry Limit/resolution"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Implementation Retry Limit"
    - "Operator"
    - "Framework Instance Settings"
    - "Default Settings"
    - "Hub Atom"
    - "Atom/Content Role: Plan/Type: Plan/Decomposition"
    - "Atom/Content Role: Plan/Type: Plan/Carrier"
atom_id: "CA-M-295"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-295-CORE_META_MODEL--resolve-implementation-retry-limits-by-source-precedence.md
---
# Summary

Resolve implementation retry limits by source precedence

## Scope

an effective Implementation Retry Limit resolved from direct Operator input, a Plan, the nearest Hub, Framework Instance Settings, **or** Default Settings.

## Claim

**to** resolve an effective Implementation Retry Limit, select the first applicable explicit source **in** this precedence:

1. direct Operator input for the current execution context.
2. the current Plan's explicit Implementation Retry Limit.
3. the nearest Hub with an explicit limit, walking `IS_DECOMPOSITION_OF` from nearest **to** farthest **and** reading its own current Plan File Carrier under CA-D-447-CORE_META_MODEL-DELIVERY--serialize-the-implementation-retry-limit-setting.
4. Framework Instance Settings, resolving an omitted instance parameter through Default Settings under CA-M-279-CORE_META_MODEL-GENERAL-METHOD--resolve-missing-framework-parameters-from-default-settings.

### resolution constraints

- an omitted optional retry override preserves inheritance; another explicit field does **not** stop this lookup. a missing mandatory Plan file is invalid, **not** an inherited-setting selection.
- determine presence, **not** truthiness: **`=0`** is an explicit limit.
- an invalid **or** ambiguous reached source requires Operator disposition **without** silent fallback; an absent effective value stops the affected retry decision.
- direct Operator input applies **only** within its stated context.
- do **not** copy inherited values **or** create separate Objective/settings files. retain explicit overrides even **when** equal **to** the inherited value.
- use the same Plan identity for a Hub's file **and** folder.
- resolution does **not** reset the consumed retry count governed by CA-O-024-CORE_META_MODEL-ACTION--control-implementation-retries.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-297-CORE_META_MODEL-METHOD--compare-by-priority-order.md

SHA-256: 71f3408c5344717f598f90fddf5381c05d5622ca0fb89f60f70f9beea58b4330

```markdown
---
version: 4
updated_at: "2026-10-01 21:40:53 +0400"
relations:
  child_of:
    - CA-R-1487
  method_for:
    - CA-R-1487
subjects:
  governs: "Project/lexicographic selection"
  depends_on:
    - "Operator"
    - "Project/priority model application"
    - "Atom/Content Role: Method"
atom_id: "CA-M-297"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-297-CORE_META_MODEL-METHOD--compare-by-priority-order.md
---
# Compare by priority order

## Scope

priority-order comparison of admissible alternatives.

## Claim

**when** the Operator selects comparison by priority order, the comparison of admissible alternatives **must** use the resolved order of active, applicable criteria as follows:

- an earlier criterion takes precedence over a later criterion.
- for alternatives tied on **all** earlier criteria, the first criterion that distinguishes them determines their relative preference.
- later criteria **must not** override a preference established by an earlier criterion.
- alternatives tied on **all** applicable criteria remain tied.
- an incomplete criterion order **or** an incomparable result at the current deciding criterion leaves the comparison unresolved; a later criterion **must not** bypass that gap.

this Method defines the comparison technique, **not** priority activation, alternative-selection execution, **or** escalation.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-298-CORE_META_MODEL-GENERAL-METHOD--describe-methodology-expansion-mappings.md

SHA-256: ad330a79ba6cc3bc04995aae6a3c04f6b6ad105e7a4bad64829f2d34566626c4

```markdown
---
subjects:
  governs: "Methodology Source/expansion mapping"
  depends_on:
    - "Methodology Source"
    - "Extension"
    - "Project Configuration"
    - "Core Meta-Model"
version: 5
updated_at: "2026-10-01 21:40:53 +0400"
relations: {child_of: [CA-M-006], method_for: [CA-R-1375]}
atom_id: "CA-M-298"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-298-CORE_META_MODEL-GENERAL-METHOD--describe-methodology-expansion-mappings.md
---
# Summary

Describe methodology expansion mappings

## Scope

Methodology Source expansion mappings.

## Claim

**to** describe a Methodology Source expansion mapping, use **`=1`** explicit mapping description that identifies:

- the source element **and** its provenance;
- the exact canonical target;
- the mapping rule;
- the intended scope of application;
- the applicable Core Meta-Model distinctions at **any** Local Tier.

apply this same mapping convention **to** Extension **and** Project Configuration sources regardless of provenance. the convention supports CA-R-1375-CORE_META_MODEL-CORE-REQUIREMENT--restrict-methodology-source-expansion-to-core-permission's expansion boundary; it does **not** admit activation **or** reliance. CA-O-054-CORE_META_MODEL-ACTION--admit-methodology-expansion-mappings owns that admission Action **and** re-evaluation following material changes.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-299-CORE_META_MODEL--distinguish-scope-unit-names-from-ordinary-english.md

SHA-256: 0b82ea293a95d8f02090a55926d2995d076c549a9d979fa2f556fc618b9e15f9

```markdown
---
subjects:
  governs: "Scope Unit/Name"
  depends_on:
    - "Scope Unit"
    - "CCE"
version: 4
updated_at: "2026-10-02 20:35:16 +0400"
relations: {}
atom_id: "CA-M-299"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-299-CORE_META_MODEL--distinguish-scope-unit-names-from-ordinary-english.md
---
# Summary

Distinguish Scope Unit Names from Ordinary English

## Scope

Scope Unit references in CAPRMEDIO content.

## Claim

**to** distinguish a Scope Unit reference from ordinary English, use its exact uppercase Scope Unit Name **to** denote the Scope Unit. an **otherwise** identical lowercase word retains its ordinary English meaning.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-300-PROJECT_CONFIGURATION-METHOD--use-constraint-only-for-external-limitations.md

SHA-256: ca5226d1b6a44e873ecfff4e54dc373e68b2664edf9a85f2872f66fbf85880ee

```markdown
---
subjects:
  governs: "Atom/Content Role: Requirement/Type: Constraint"
  depends_on:
    - "Atom/Content Role: Requirement/Type"
    - "Project"
    - "Author"
version: 5
updated_at: "2026-09-29 22:20:38 +0000"
relations: {"method_for":["CA-R-1673"]}
atom_id: "CA-M-300"
content_role: "Method"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/05_method/CA-M-300-PROJECT_CONFIGURATION-METHOD--use-constraint-only-for-external-limitations.md
---
# Summary
Use Constraint only for external limitations

## Scope
selection of a Requirement Type.

## Claim

**to** select a Requirement Type, the Author **must** use Constraint **only** for a limitation imposed from outside the Project choice boundary.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-301-CORE_META_MODEL--make-atom-claims-easy-to-understand.md

SHA-256: 9ce29da00e12e8530cf6faa4f18518f9e9217448ad9fec2cf314f9ba7468c6a9

```markdown
---
subjects:
  governs: "Atom/Claim"
  depends_on:
    - "Term"
    - "Workflow/Relation Kind: On Result"
    - "Step"
    - "Atom"
    - "Author"
    - "CCE"
    - "Action"
    - "Workflow"
version: 6
updated_at: "2026-10-02 20:35:16 +0400"
relations:
  child_of:
    - CA-M-113
  relates_to:
    - CA-M-229
    - CA-M-294
    - CA-R-1270
    - CA-R-1508
atom_id: "CA-M-301"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-301-CORE_META_MODEL--make-atom-claims-easy-to-understand.md
---
# Summary

Make Atom Claims easy to understand

## Scope

Atom Claims.

## Claim

**to** make an Atom Claim easy **to** understand, the Author **must** express **and** organize its content so the intended reader can identify what is claimed, what it concerns, **and** how its conditions **and** consequences fit together **without** guessing unstated connections.

## Details

## Meaning and context

- provide the context needed **to** interpret the Claim. reference existing governing definitions **and** authority rather than independently restating them.
- render **every** prose Atom citation as the referenced Atom's complete filename **without** its `.md` extension **or** directory path, preserving **all** filename tokens **and** their exact spelling. direct machine references remain exact Atom IDs rather than citation labels, **and** `CA-R-366-CORE_META_MODEL-REQUIREMENT--reference-exact-atom-revisions-by-version-and-time` continues **to** govern exact-revision metadata.
- choose familiar wording under `CA-M-294-CORE_META_MODEL-METHOD--use-simpler-words-without-losing-meaning` **without** losing precision, necessary distinctions, **or** exact canonical Terms.
- state conditions, alternatives, **and** relationships explicitly. preserve whether **all** conditions apply **or** **any** alternative suffices, including nested logical groups.

## Structure

- use short, direct statements. a simple Claim **may** remain a short paragraph; do **not** compress several points, conditions, **or** steps into one dense sentence.
- use bullets for unordered points, conditions, **or** alternatives.
- use a numbered list for sequential steps **only** **when** the content establishes that sequence. numbering **must not** invent execution order **or** priority.
- use a flow table for a Workflow with branches **or** loops. identify **every** Step, its **`=1`** Action reference **and** parameter/input bindings, **and** the typed Relation, result condition, **and** next Step **or** terminal outcome for **every** transition under `CA-R-1508-CORE_META_MODEL-CORE-REQUIREMENT--define-workflow`.

## Preservation

- preserve the complete Claim **and** its qualifications; easier wording **or** layout **must not** change its meaning.
- retain the Atom boundary under `CA-R-1270-CORE_META_MODEL-CORE-REQUIREMENT--permit-one-composite-claim-as-one-authority-unit`. one Claim does **not** require one sentence; paragraphs, bullets, **and** table rows do **not** determine the number of independently governed Claims.
- express authoritative content once rather than repeating the same Claim **in** prose **and** a list **or** table.
- apply the Term **and** CCE Operator rendering Method under `CA-M-229-CORE_META_MODEL-METHOD--render-governed-terms-and-cce-operators-distinctly` throughout.

readable layout alone is insufficient **when** the Claim still requires the reader **to** reconstruct missing context **or** logical connections.
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-303-CORE_META_MODEL--declare-update-routing-in-the-calling-workflow.md

SHA-256: 6cbbea9c891aafa3871e95e06199df1da6fc435c83a981129a9596f2853eaa34

```markdown
---
subjects:
  governs: "Workflow"
  depends_on:
    - "Author"
    - "Action"
    - "Step"
    - "Workflow Run"
    - "Atom"
    - "Atom/Summary"
    - "Artifact/Revision"
    - "Assess Atom Update Identity"
version: 4
updated_at: "2026-10-01 21:40:53 +0400"
relations: {"relates_to": ["CA-M-301", "CA-O-067", "CA-R-1432", "CA-R-1464", "CA-R-1520"]}
atom_id: "CA-M-303"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-303-CORE_META_MODEL--declare-update-routing-in-the-calling-workflow.md
---
# Summary

Declare update routing **in** the calling Workflow

## Scope

Atom update routing for a calling Workflow.

## Claim

**to** author an Atom update Workflow, declare its response **to** identity assessment **in** the Workflow graph rather than **in** the assessment Action **or** executor code.

- reference CA-O-067-CORE_META_MODEL-ACTION--assess-atom-update-identity for the assessment; bind the target Revision, proposed result, applicable authority, **and** evidence **to** that Step. the Action returns its assessment **without** selecting the caller's next Step **or** continuation Workflow.
- map identity-preserving results **to** the caller's declared update path **and** remaining authorization **and** checks; the assessment alone does **not** perform the update.
- map replacement-required results **to** a terminal handoff under CA-R-1520-CORE_META_MODEL-GENERAL-REQUIREMENT--return-workflow-handoffs-through-terminal-results. keep the admitted replacement-continuation binding **in** the Workflow definition, **not** as an assessment Action input. the ending Run does **not** call **or** wait for replacement **or** persist an intermediate update merely **to** replace it.
- map unresolved results **to** the caller's declared evidence-gathering **or** escalation path; an unresolved result **must not** be treated as approval.
- include reassessment **when** the proposal changes **or** its evidence becomes stale **before** persistence. a changed Summary remains a replacement under CA-R-1464-CORE_META_MODEL-REQUIREMENT--keep-summary-fixed-for-atom-identity even **when** the request began as an update.

this Method constrains how an Author expresses the caller's graph. it is **not** another Workflow, executable routing service, **or** requirement **to** build the executor through a particular Workflow.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-304-CORE_META_MODEL--write-self-contained-agentic-action-instructions.md

SHA-256: 24548b4d1c17f9c9e1b52bc86e12507e6bf07d547f31a859e4ea9f1fe9f4ad24

```markdown
---
subjects:
  governs: "Step Run/Invocation"
  depends_on:
    - "Action"
    - "Step"
    - "Workflow"
    - "Operator"
    - "Tool"
    - "Action/Execution Kind: Agentic"
    - "Step Run/Tool Call"
version: 4
updated_at: "2026-09-30 15:26:58 +0400"
relations: {"method_for": ["CA-R-1789", "CA-R-1790", "CA-R-1791", "CA-R-1792", "CA-R-1793"]}
atom_id: "CA-M-304"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-304-CORE_META_MODEL--write-self-contained-agentic-action-instructions.md
---
# Summary
Write self-contained agentic Action instructions

## Scope
derived instructions that present an Agentic Action for execution.

## Claim

**to** present an Agentic Action for execution, organize its derived instruction around the declared responsibility rather than assumed session memory.

- state the requested outcome, relevant context, exact targets, inputs, available evidence, **and** governing references.
- distinguish already performed effects from proposed changes, **and** existing permissions from decisions still needed.
- state the expected result **and** how **to** report uncertainty, failures, partial effects, **or** a request for Operator input. do **not** treat a suggested correction as permission **to** apply it.
- keep the instruction limited **to** the bound Action. leave next-Step selection **and** cross-Workflow handoff coordination **to** the executor using the governing Workflow.
- use understandable wording **and** structured points under CA-M-301-CORE_META_MODEL-METHOD--make-atom-claims-easy-to-understand **and** CA-M-294-CORE_META_MODEL-METHOD--use-simpler-words-without-losing-meaning; reference governing definitions rather than copying another authoritative procedure into the prompt.
- keep internal Tool calls as execution detail under CA-R-1528-CORE_META_MODEL-GENERAL-REQUIREMENT--record-tool-calls-within-step-runs. **when** an operation needs independently governed routing, checks, **or** approval boundaries, express it as an explicit Step during Workflow authoring rather than inventing Workflow nodes from runtime calls.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-305-CORE_META_MODEL--write-workflow-schemes-using-step-references.md

SHA-256: 4a9f3cfd879a7a10fadb20816a3f5ab360ffa6d9e25d7dbe1921bcdfd5d35bc4

```markdown
---
subjects:
  governs: "Workflow"
  depends_on:
    - "Step"
    - "Action"
    - "Atom/Content Role: Operations/Type: Step"
    - "Workflow/Relation Kind: On Result"
version: 4
updated_at: "2026-10-02 20:35:16 +0400"
relations: {"method_for": ["CA-R-1570"]}
atom_id: "CA-M-305"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-305-CORE_META_MODEL--write-workflow-schemes-using-step-references.md
---
# Summary

Write Workflow schemes using Step references

## Scope

Workflow schemes using Step references.

## Claim

**to** write a Workflow scheme, express the graph through references **to** its Step Atoms:

- use **`=1`** unambiguous reference for **every** graph node; readable node labels **may** accompany those references.
- state the entry, typed directed transitions, result conditions, **and** terminal outcomes against those nodes.
- place Action references **and** parameter/input bindings **in** the referenced Step Atoms rather than reproducing them **in** the scheme.
- reference reusable Action behavior from the Steps; do **not** paste it into either the Step **or** graph Claim.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-306-CORE_META_MODEL-GENERAL--author-plan-atoms.md

SHA-256: 38800095948285729edf22193b736d1f5b496032688b3559e8aaa826e11e1445

```markdown
---
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Claim"
    - "Atom/Summary"
    - "Atom/Author"
    - "Atom/Content Role: Plan/Type: Plan/Assignee"
    - "Atom/Content Role: Plan/Type: Plan/Label"
    - "Atom/Content Role: Plan/Type: Plan/Subtype"
    - "Atom/Content Role: Plan/Type: Plan/Definition of Done"
    - "Atom/Content Role: Plan/Type: Plan/Decomposition"
    - "Atom/Content Role: Plan/Type: Plan/Blocking"
    - "Autonomous Confidence Threshold"
    - "Implementation Retry Limit"
    - "Scope Unit"
    - "File Carrier"
version: 7
updated_at: "2026-10-02 20:35:16 +0400"
relations: {"relates_to": ["CA-R-1574", "CA-R-1575", "CA-R-1576", "CA-R-1577", "CA-R-1599", "CA-R-1584", "CA-R-1588", "CA-R-1589", "CA-R-1591", "CA-R-1418", "CA-M-123", "CA-M-271", "CA-M-295", "CA-D-470", "CA-D-471", "CA-D-481"]}
atom_id: "CA-M-306"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-306-CORE_META_MODEL-GENERAL--author-plan-atoms.md
---
# Summary

Author Plan Atoms

## Scope

Plan Atoms.

## Claim

**to** author a Plan Atom, apply the common Plan authoring rules independently of Label:

1. resolve **`=1`** effective Author.
2. state **`=1`** intended work **or** outcome **in** Objective, supported by own work, direct decomposition, **or** both under CA-R-1575.
3. resolve its Claim Target Scope Unit under CA-R-1588; keep narrower **or** composite work restrictions **in** Objective, **and** do **not** target an ancestor Scope Unit.
4. **if** it has own work, resolve **`=1`** effective Assignee **and** assign that work **to** that Assignee. retain the leaf-work bound under CA-R-1589.
5. write **`=1`** Definition of Done under CA-M-123, carried inside Details under CA-D-470; include decomposed completion obligations **when** applicable.
6. use a Label **only** for navigation; apply an authoring Subtype **only when** explicitly governed.
7. express required start dependencies with `BLOCKS`; declare `IS_DECOMPOSITION_OF` **only** on the decomposing Plan under CA-D-481. derive the inverse; do **not** infer execution dependencies from leading numbers **or** folder placement.
8. resolve confidence **and** retry values from their applicable sources; store **only** explicitly selected overrides on this Plan.
9. keep supporting Details within Objective **and** its restrictions **without** another intended outcome. review Objective against the completed Details **and** Definition of Done; explicitly revise Objective **if** needed **and** recheck their agreement.
10. **only after** that review, derive Summary from the finalized Objective under CA-R-1418 **and** CA-R-1465. retain the established Summary across Revisions; **if** it needs changing, replace the Atom identity under CA-R-1464.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-307-CORE_META_MODEL-CORE--define-content-role-specific-cce-profiles.md

SHA-256: 2189d14817cfc60a4e6fa6a8ba187f0a91ddace23922079c6a3ae5c19e4bd014

```markdown
---
subjects:
  governs: "CCE/Role Profile"
  depends_on:
    - "CCE"
    - "CCE Operator"
    - "Atom/Claim"
    - "Atom/Content Role"
    - "Type"
version: 4
updated_at: "2026-10-02 20:35:16 +0400"
relations:
  child_of:
    - CA-M-113
    - CA-M-230
    - CA-M-234
  relates_to:
    - CA-R-1283
    - CA-R-1530
atom_id: "CA-M-307"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-307-CORE_META_MODEL-CORE--define-content-role-specific-cce-profiles.md
---
# Summary

Define Content-role-specific CCE Profiles

## Scope

CCE Role Profiles.

## Claim

a CCE Role Profile **means** one restriction of shared CCE that identifies the permitted primary Claim contribution, permitted CCE Operator uses, permitted subordinate content slots, **and** prohibited primary contributions for one Content Role **or** one narrower Type **or** content slot.

the current role-specific profiles apply **only** **to** Plan, Requirement, Method, Evaluation, Delivery, **and** Operations Atoms.

Concern **and** Analysis Claims remain subject **to** shared CCE **without** an additional CCE Role Profile. this absence does **not** exempt them from shared CCE **or** authorize normative authority outside their Content Role meanings.

no CCE Role Profile is currently registered for Implementation because the current source set contains no Implementation Atoms. an absent Implementation profile **must not** be replaced by another role's profile **or** treated as role-profile conformance.

a narrower Type **or** content-slot profile **may** restrict its parent role profile **and** define permitted subordinate operator use, but it **must not** change the primary contribution of the Content Role.

## Details
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-308-CORE_META_MODEL-CORE--resolve-the-effective-cce-role-profile.md

SHA-256: 91c2689e21bccde937c48a1974f8da1dbc85a2653b3f14e6b3ed4d20de841481

```markdown
---
subjects:
  governs: "CCE/Role Profile/resolution"
  depends_on:
    - "CCE/Role Profile"
    - "Atom/Content Role"
    - "Type"
    - "Atom/Claim"
version: 4
updated_at: "2026-10-02 20:35:16 +0400"
relations:
  child_of:
    - CA-M-307
  relates_to:
    - CA-M-309
    - CA-M-310
    - CA-M-311
    - CA-M-312
    - CA-M-313
    - CA-M-314
atom_id: "CA-M-308"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-308-CORE_META_MODEL-CORE--resolve-the-effective-cce-role-profile.md
---
# Summary

Resolve the Effective CCE Role Profile

## Scope

effective CCE Role Profiles for Atom Claims.

## Claim

**to** resolve one effective CCE Role Profile for one Atom Claim, the Author **must** perform **all** of:

1. resolve the Atom's Content Role **before** selecting a profile.
2. **if** the Content Role is Plan, Requirement, Method, Evaluation, Delivery, **or** Operations, select the corresponding profile under CA-M-309 through CA-M-314.
3. apply an admitted Type profile **and** content-slot profile **after** the role profile; treat each narrower profile as a restriction **or** declared subordinate use, **not** as permission **to** change the role's primary contribution.
4. distinguish operators that express the primary Claim contribution from operators inside a condition, Definition of Done, input, result, failure, transition, representation, **or** another governed subordinate slot.
5. **if** the Content Role is Concern **or** Analysis, apply shared CCE **without** a role-specific profile.
6. **if** the Content Role is Implementation, return no registered CCE Role Profile **without** selecting a fallback profile **or** reporting role-profile conformance.
7. **if** the Content Role, Type, content slot, **or** applicable profile is unresolved, report the exact unresolved selection **and** do **not** report role-profile conformance.

## Details

the effective profile is derived from governed content classification. it is **not** another required Atom property.
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-309-CORE_META_MODEL-METHOD--write-plan-claims-with-the-plan-cce-profile.md

SHA-256: 3e4b344d85e967a8b1055996d846cd8b33f91b364eb2ed25512aeaba218a4f6c

```markdown
---
subjects:
  governs: "CCE/Role Profile: Plan"
  depends_on:
    - "Atom/Content Role: Plan"
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Content Role: Plan/Type: Plan/Definition of Done"
    - "CCE Operator"
version: 4
updated_at: "2026-10-01 21:41:08 +0400"
relations:
  child_of:
    - CA-M-307
  relates_to:
    - CA-M-123
    - CA-M-306
    - CA-R-1575
    - CA-R-1581
atom_id: "CA-M-309"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-309-CORE_META_MODEL-METHOD--write-plan-claims-with-the-plan-cce-profile.md
---
# Summary

Write Plan Claims with the Plan CCE Profile

## Scope

Plan Claims written with the Plan CCE Role Profile.

## Claim

**to** write a Plan Claim with the Plan CCE Role Profile, the Author **must** perform **all** of:

1. state the Plan's primary contribution as intended work, an intended outcome, **or** their governed composition under CA-M-306-CORE_META_MODEL-GENERAL-METHOD--author-plan-atoms.
2. **if** the Plan has own work, identify the action, its object, intended result, Assignee, **and** applicable boundary explicitly. modality, condition, temporal, quantification, logical, restriction, predicate, **and** comparison Operators **may** qualify that intended work.
3. **if** the Plan is supported **only** by decomposition, state its intended outcome **without** inventing own work.
4. keep reusable procedure authority, normative product boundaries, current realization facts, **and** reusable operational behavior outside the Plan's primary contribution.
5. write the Definition of Done as the subordinate falsifying Condition Expression under CA-M-123-CORE_META_MODEL-METHOD--write-definitions-of-done. condition, temporal, quantification, logical, predicate, restriction, **and** comparison Operators **may** occur **in** that slot **only** to determine whether the Plan remains **not** Done.
6. keep optional Details subordinate **to** the same intended work **or** outcome; Details **must not** introduce another intended outcome **or** a second Definition of Done.

## Details

an action word **in** a Plan identifies intended work. it does **not** define a reusable Operations Action.
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-310-CORE_META_MODEL--write-requirement-claims-with-the-requirement-cce-profile.md

SHA-256: 6584f7d1aaae67206f46874e40d012af5c1cad225ae2b8db045d3c4a21596967

```markdown
---
subjects:
  governs: "CCE/Role Profile: Requirement"
  depends_on:
    - "Atom/Content Role: Requirement"
    - "CCE Operator"
    - "Atom/Claim"
version: 5
updated_at: "2026-10-04 04:27:08 +0400"
relations:
  child_of:
    - CA-M-307
  relates_to:
    - CA-R-1339
    - CA-M-233
    - CA-M-235
atom_id: "CA-M-310"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-310-CORE_META_MODEL--write-requirement-claims-with-the-requirement-cce-profile.md
---
# Summary

Write Requirement Claims with the Requirement CCE Profile

## Scope

Requirement Claims with the Requirement CCE Role Profile.

## Claim

**to** write a Requirement Claim with the Requirement CCE Role Profile, the Author **must** perform **all** of:

1. state the primary contribution as one Entity model **or** required result by its meaning **and** value under CA-R-1339. express required properties **and** observable boundaries within that model **or** result; an obligation, permission, **or** prohibition alone does **not** select Requirement.
2. use **must**, **must not**, **may**, **only**, quantification, predicates, comparisons, **and** explicit conditions as applicable **to** state what is required, permitted, prohibited, **or** bounded.
3. use **means** **only** **when** the Claim defines the governed Requirement subject rather than merely describing it.
4. express temporal Operators **only** as observable timing boundaries **or** conditions on the required result.
5. keep procedural selection, ordered execution steps, implementation instructions, **and** reusable operational behavior outside the primary contribution. reference applicable Method **or** Operations authority rather than reproducing it.

## Details

the Requirement profile governs the required model **or** result. an observed test result remains execution evidence; it is **not** the required-result specification.
```

## .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/05_method/CA-M-311-CORE_META_MODEL--write-method-claims-with-the-method-cce-profile.md

SHA-256: 645b2c3437366b4217979c0548b31876b65446a4d8e8fd6fc8c09d788ff97677

```markdown
---
subjects:
  governs: "CCE/Role Profile: Method"
  depends_on:
    - "Atom/Content Role: Method"
    - "CCE Operator"
    - "Atom/Claim"
version: 5
updated_at: "2026-10-04 04:27:08 +0400"
relations:
  child_of:
    - CA-M-307
  relates_to:
    - CA-R-1340
    - CA-M-113
    - CA-M-301
atom_id: "CA-M-311"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-311-CORE_META_MODEL--write-method-claims-with-the-method-cce-profile.md
---
# Summary

Write Method Claims with the Method CCE Profile

## Scope

Method Claims with the Method CCE Role Profile.

#…7687 tokens truncated…nd** Delivery constraints; identical source code **or** identical source-file bytes are **not** required. judge fresh reconstruction **and** repeated implementation by this runtime equivalence, **not** by a requirement **to** leave already-conforming code untouched. an authorized RMED change establishes a new comparison baseline **and** **must not** be reported as reconstruction against unchanged RMED.
```

## .caprmedio_caprmedio/05_method/CA-M-263-CORE-METHOD--make-information-clear-to-the-operator.md

SHA-256: 78af762fc6673b584c04a0251330aca64eda0470240ebe9956a65dab06ab7c7a

```markdown
---
cce_version: "cce_1"
cce_form: "method"
subjects:
  governs: "Operator/communication"
  depends_on:
    - "Operator"
    - "CAPRMEDIO Framework Instance"
version: 4
updated_at: "2026-09-17 02:13:04 +0000"
relations: {"child_of":["CA-R-1420"]}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Make information clear to the Operator

**to** expose governed information **to** the Operator, provide an initial **or** adapted representation that the Operator accepts as sufficient for the current governed use **or**, **when** applicable adaptation attempts are exhausted **or** declined, explicitly report the remaining comprehension gap; adapt the representation **without** changing the governed information.
```

## .caprmedio_caprmedio/05_method/CA-M-266-CORE-METHOD--follow-the-operator-selected-implementation-mode.md

SHA-256: f40c7467ac8641663fc20e26ce293d5495da516a80adbfce0637056222c4759f

```markdown
---
cce_version: "cce_1"
cce_form: "method"
version: 5
updated_at: "2026-09-05 23:00:00 +0400"
relations:
  child_of:
    - "CA-M-261"
  relates_to:
    - "CA-M-262"
subjects:
  governs: "Project/Implementation/mode selection"
  depends_on:
    - "Operator"
    - "Spec"
    - "Atom/Content Role: Plan/Type: Task"
    - "Atom/Content Role: Implementation"
    - "Atom/Content Role: Requirement"
    - "Atom/Content Role: Method"
    - "Atom/Content Role: Evaluation"
    - "Atom/Content Role: Delivery"
    - "Project"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Follow the Operator-selected implementation mode

**to** implement within a Task, follow the Operator-selected mode: evaluate **and** fix, full rebuild, refactoring, **or** another authorized approach. keep the selected mode within the Task permissions **and** governing RMED; permission for a full rebuild **must not** be inferred from an evaluation-and-fix request. the reconstruction equivalence governed by CA-M-262 applies regardless of mode **and** does **not** require identical code **or** a no-change rerun.
```

## .caprmedio_caprmedio/05_method/CA-M-270-CORE-METHOD--prepare-verification-before-refactoring.md

SHA-256: b79f91053d3c5165cb542b202adddede084bd6bb30fb0b8b35e06e9a8bf48335

```markdown
---
cce_version: "cce_1"
cce_form: "method"
version: 9
updated_at: "2026-09-21 00:39:50 +0000"
relations: {"child_of":["CA-M-261"],"relates_to":["CA-M-262","CA-O-016","CA-R-1559","CA-O-024"]}
subjects:
  governs: "Project/Implementation/refactoring verification"
  depends_on:
    - "Spec"
    - "Atom/Content Role: Requirement"
    - "Atom/Content Role: Method"
    - "Atom/Content Role: Evaluation"
    - "Atom/Content Role: Delivery"
    - "Atom/Content Role: Implementation"
    - "Project"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Prepare verification before refactoring

**to** refactor existing Implementation, prepare the applicable verification **before** changing the target Implementation:

1. derive regression checks, end-to-end checks, acceptance gates, **and** canary criteria from the applicable Evaluations; select techniques by applicability rather than requiring **every** technique for **every** change. apply the governing Methods within Delivery boundaries while implementing these checks.
2. evaluate the existing Implementation using controlled complete inputs **and** record its outputs **and** existing failures as baseline evidence. expected correctness remains governed by RMED; an existing defect **must not** become a Requirement merely because it appears **in** the baseline.
3. evaluate the refactored candidate against current RMED **and** the recorded baseline under CA-M-262, using the implementation loop **and** retry policy. preserve the applicable checks across the comparison **unless** an authorized RMED change establishes a new baseline under CA-R-1559.
4. apply the required release gates **before** full rollout. **when** canary testing applies, prepare its criteria **before** refactoring **and** execute it on the candidate **after** that Implementation exists during the authorized controlled rollout.

this existing-Implementation baseline is comparison evidence, **not** missing specification recovered from old code, **and** is **not** a prerequisite for a fresh reconstruction with no existing Implementation.
```

## .caprmedio_caprmedio/05_method/CA-M-296-CORE-METHOD--do-not-rely-on-memory-files.md

SHA-256: 81a7cd908ef53de8b6000c72eedaad66ce9fc317c9c5796f1c2e7ff0d558e010

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "Project/information"
  depends_on:
    - "Project"
    - "Artifact"
    - "Atom"
    - "Journal"
    - "Projection"
    - "Applicable Methodology"
    - "Operator"
version: 2
updated_at: "2026-09-16 20:25:40 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
    - "CA-R-1490"
  relates_to:
    - "CA-M-003"
    - "CA-E-002"
---
# Do not rely on memory files

**to** preserve valuable information while developing caprmedio, keep that information recoverable from its proper Project Artifacts **without** depending on Agent memory **or** session continuity.

- do **not** use `MEMORY.md`, similar memory files, conversation summaries, **or** handoff notes as governing authority **or** as the sole preserved copy of valuable information.
- preserve accepted decisions, findings, rationale, **and** necessary evidence **in** their appropriate Artifacts under Applicable Methodology. keep governing Atoms, analysis, **and** factual Journal records distinct; preserving a finding does **not** make it accepted authority.
- secondary summaries **may** help locate sources, but **must not** substitute for reading the relevant current sources **before** relying on their contents **or** claiming that work is complete.
- **before** reducing context **or** handing work over, ensure that valuable information remains recoverable from those Artifacts. a later session **must not** need an earlier Agent's private memory **to** recover it.
- missing, unavailable, **or** conflicting source information remains an explicit gap; do **not** fill it with remembered assertions. request Operator clarification **when** the unresolved gap prevents a sufficiently supported decision.
```

## .caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/05_method/CA-M-141-FRAMEWORK_METHODOLOGY-CORE-METHOD--select-the-least-costly-sufficient-execution-mechanism.md

SHA-256: ce60754335067a1f30e3737834d1fb2acc755406e4d85f7aa1c90bb994a801c3

```markdown
---
subject_scopes:
  - routing
version: 11
updated_at: "2026-09-17 18:05:03 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
    - CA-M-098
    - CA-M-099
---
# Select the least costly sufficient execution mechanism

For one requested operation, first establish the required outcome, applicable
non-negotiable constraints, available source inputs, acceptance conditions,
candidate execution mechanisms, their capability limits, **and** the effective
Operator-selected priority model, its parameters, **and** active criteria. Do **not** select automatically **when** **any** of these inputs
is absent, contradictory, **or** insufficient **to** distinguish the candidates.

Classify a candidate operation as **deterministically specifiable** **only** **when**
its accepted inputs, transformation, decision rules, **and** acceptance conditions
are explicit enough that the same admitted inputs require the same result
**without** interpretation, judgment, **or** open-ended planning. Select a sufficient
deterministic mechanism for that operation whenever one is available. An LLM
**may** prepare **or** interpret work around such an operation, but it **must not** replace
the deterministic execution of the bounded operation itself.

**when** the operation requires interpretation, judgment, **or** open-ended
orchestration, use an LLM **only** for that irreducibly interpretive boundary **and**
keep **every** fully specifiable sub-operation deterministic. From the remaining
sufficient candidates, apply the effective Operator-selected priority model, including
declared human-effort **and** external-expense criteria **when** selected, **to** choose
the least costly acceptable mechanism under that model. apply a declared
tie-breaker **only** **when** the selected model admits it. unresolved ties,
incomparable candidates, an unavailable required mechanism, **or** an unresolved
cost estimate required by that model return the choice **to** the Operator
**without** execution. do **not** substitute comparison by priority order **or**
another algorithm for the selected model.

Stop at that boundary. Record the unresolved input **or** comparison as a
diagnostic; do **not** guess a deterministic rule, silently substitute an LLM, **or**
claim that an LLM result establishes deterministic sufficiency.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-110-PROGRAMMATIC-CORE-IMPL_METHOD--implement-programmatic-components-in-python.md

SHA-256: 25d756476029a4d9860dbcc4062db8de81aefd09309ee043877f3bfa5a600efc

```markdown
---
cce_version: "cce_1"
cce_form: "method"
subjects:
  governs: "programmatic-components"
  depends_on:
    - "Journal/Record"
    - "Atom/Content Role: Operations"
    - "programmatic software"
version: 19
updated_at: "2026-09-17 18:36:38 +0000"
relations: {"derived_from":["CA-A-053"],"child_of":["CA-M-261"]}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Implement PROGRAMMATIC components in Python

use Python for applicable PROGRAMMATIC Tools, App backend services, **and** MCP
components. this Method owns the Python technology selection for that bounded
scope. Configuration **and** Implementation materialize the selected runtime,
dependencies, **and** exceptions; Delivery governs their carrier placement **and**
encoding; Operations defines reusable workflow behavior, **and** Journal Records carry execution evidence. this Method
does **not** govern Skills **or** make Python a discipline-independent CAPRMEDIO
meaning.

## Applicable when

apply **when** a Tool, App backend service, **or** MCP component is added **or** materially
changed, **or** **when** its Python realization, runtime dependency, **or** non-Python
exception is proposed.

## Procedure

1. apply the Python selection established by this Method **and** read its current
   materialization **before** realizing a component.
2. use the standard library **when** it provides the required behavior with
   comparable clarity **and** reliability.
3. add **or** change a runtime, library, workflow tool, **or** non-Python exception
   **only** through an accepted Method that selects it for a bounded scope.
4. materialize **every** accepted selection **in** canonical configuration **and**
   Implementation **without** making either carrier a second authority.
5. place **and** encode **every** materialization through its Delivery, **and** preserve
   evidence of actual execution results **in** Journal Records.

## Outcome

**every** applicable component follows one Method-owned technology selection.
Configuration **and** Implementation reproduce it, Delivery locates its carriers,
**and** the Journal records execution evidence **without** taking over selection authority.

## Failure or stop

stop admission **or** release **when** no accepted Method owns a required selection,
its materialization disagrees with that Method, **or** the Delivery **or** Operations boundary
is absent. do **not** infer a platform-support claim from local execution.

## Sources

- [Python 3.14 documentation](https://docs.python.org/3.14/)
- [Python Packaging User Guide: `pyproject.toml`](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-157-PROGRAMMATIC-CORE-METHOD--allocate-deterministic-transformations-to-functions.md

SHA-256: 65f8c4496c07b9553d47869c421eba310ccc1a223e7fecb50d1b084ba4b95226

```markdown
---
cce_version: "cce_1"
cce_form: "method"
subjects:
  governs: "deterministic-transformation"
  depends_on:
    - "programmatic software"
version: 12
updated_at: "2026-09-05 03:48:00 +0400"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-110"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Allocate deterministic transformations to functions

use a side-effect-free function as the default unit of PROGRAMMATIC behavior.
implement one deterministic transformation as a function **when** its result
follows **only** from its declared inputs **and** the responsibility needs no identity
across calls.

## Applicable when

apply **when** Tools, App backend services, **or** MCP components parse, classify,
validate, plan, project, format, **or** **otherwise** transform explicit input into a
result.

## Procedure

- use a function **unless** the responsibility **must** own mutable state, an
   invariant across calls, a resource, a lifecycle, **or** a replaceable adapter.
- give the function a specific, intention-revealing verb phrase that states
   its one responsibility; prefer clarity over brevity **and** split a function
   whose accurate name requires multiple responsibilities.
- state the function's input, result, **and** failure values explicitly.
- do **not** mutate inputs **or** shared state, perform I/O **or** logging export, **or** read
   the filesystem, process, clock, environment, network, persistence, **or**
   randomness.
- pass **every** required observation **and** setting as explicit input rather than
   obtaining them implicitly.
- group related functions **in** a specifically named module; do **not** create a
   class **only** **to** provide a namespace.

## Outcome

behavior is locally readable, reproducible from declared input, **and** free of
observable side effects. it can be reused, checked, **or** extended **without**
constructing component lifecycle state.

## Failure or stop

stop treating the unit as a deterministic transformation **when** it applies an
external effect. a bounded one-shot effect **may** remain a function under
CA-M-160; allocate an object **only** **when** identity across calls **or** owned state,
invariant, resource, lifecycle, **or** adapter behavior is required.

## Sources

- [Python Functional Programming HOWTO](https://docs.python.org/3.14/howto/functional.html)
- [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-158-PROGRAMMATIC-CORE-METHOD--allocate-owned-state-and-lifecycle-to-objects.md

SHA-256: 30d62f331388ae10d60a1b5ce469303d69cc52ff60f200266ac4f135f9172a17

```markdown
---
cce_version: "cce_1"
cce_form: "method"
subjects:
  governs: "component-lifecycle"
  depends_on:
    - "programmatic software"
version: 13
updated_at: "2026-09-05 03:48:00 +0400"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-110"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Allocate owned state and lifecycle to objects

introduce an object **only** **when** one PROGRAMMATIC responsibility needs identity
across calls because it owns mutable technical state, preserves an invariant,
manages a resource **or** lifecycle, **or** implements a replaceable adapter. do **not**
create an object merely **to** group functions **or** **to** perform a bounded one-shot
effect.

## Applicable when

apply **when** a Tool, App backend service, **or** MCP component **must** retain state,
preserve an invariant across calls, acquire **or** release a resource, transition
through a lifecycle, **or** encapsulate one replaceable technical adapter.

## Procedure

- give the class **or** object a specific, intention-revealing noun phrase that
   states the one state, invariant, resource, lifecycle, **or** adapter
   responsibility it owns; do **not** use an unqualified generic name such as
   `Manager`, `Helper`, **or** `Utils`.
- give **every** effectful method a specific verb phrase that declares the effect
   **or** lifecycle transition it performs.
- keep construction free of I/O **and** start acquisition **or** activation through
   an explicit method.
- make acquisition, use, failure, **and** release **or** recovery boundaries
   explicit.
- keep deterministic transformations outside the object **unless** they require
   its owned responsibility.
- compose the object from explicit collaborators instead of inheriting
   behavior for code reuse.
- use inheritance **only** for one stable, substitutable subtype contract; stop
   **when** a module, function, **or** composed adapter expresses the variation.

## Outcome

**every** object has one clearly named owner responsibility, a visible invariant **or**
lifecycle, explicit collaborators, **and** no unrelated function-grouping role.

## Failure or stop

stop **and** split **or** redesign the object **when** it owns unrelated state **or**
lifecycle concerns, hides an external effect, exists **only** as a namespace **or**
one-shot effect wrapper, **or** uses an ambiguous generic name **or** inheritance
**where** composition provides the same substitution boundary.

## Sources

- [Python Functional Programming HOWTO](https://docs.python.org/3.14/howto/functional.html)
- [Python documentation: data classes](https://docs.python.org/3.14/library/dataclasses.html)
- [PEP 544 — Protocols](https://peps.python.org/pep-0544/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-159-PROGRAMMATIC-CORE-METHOD--define-typed-contracts-at-replaceable-technical-boundaries.md

SHA-256: 21454fcd4f401ce9b49f7a1576744953c66e19eefa2ab1735ffb994dc2b15b20

```markdown
---
cce_version: "cce_1"
cce_form: "method"
subjects:
  governs: "technical-interface"
  depends_on:
    - "programmatic software"
version: 9
updated_at: "2026-09-05 03:48:00 +0400"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-110"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Define typed contracts at replaceable technical boundaries

declare an explicit typed contract wherever a PROGRAMMATIC component depends on
a replaceable technical implementation, adapter, transport, storage mechanism,
**or** host boundary.

## Applicable when

apply **when** a Tool, App backend service, **or** MCP component can substitute one
technical implementation for another **or** crosses a host-owned interface.

## Procedure

1. define the accepted inputs, outcomes, failure values, ownership boundary,
   **and** compatibility expectation at the interface.
2. keep callers dependent on that contract rather than on implementation-only
   state **or** incidental representation.
3. use a structural `Protocol` **when** consumers need one capability contract
   **without** requiring implementations **to** inherit from a framework base class.
4. keep substrate-specific behavior **in** a small adapter **and** keep deterministic
   semantic decisions outside that adapter.
5. record an exception **in** its bounded owner **when** a required external interface
   cannot meet the contract directly.

## Outcome

the component can replace the bounded technical implementation **without**
silently changing its callers' declared expectations.

## Failure or stop

stop substitution **or** host integration **when** the boundary has no explicit
contract, its failures cannot be represented, **or** compatibility cannot be
identified from current authority.

## Sources

- [PEP 544 — Protocols](https://peps.python.org/pep-0544/)
- [Python documentation: `typing.Protocol`](https://docs.python.org/3.14/library/typing.html#typing.Protocol)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-160-PROGRAMMATIC-CORE-METHOD--separate-deterministic-transformations-from-effects-and-lifecycle.md

SHA-256: 35dfd41dd9edc6bf5131ba439b2e3a0670170620381b87b95549fd73dc815ce2

```markdown
---
cce_version: "cce_1"
cce_form: "method"
subjects:
  governs: "effect-boundary"
  depends_on:
    - "programmatic software"
version: 12
updated_at: "2026-09-05 03:48:00 +0400"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-110"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Separate deterministic transformations from effects and lifecycle

keep PROGRAMMATIC decisions **in** a function-based deterministic core. apply
filesystem, process, clock, environment, network, persistence, **or**
logging-export effects through a specifically named bounded one-shot function
**when** no identity **or** ownership is required, **or** through a specifically named
method on an object that owns state, an invariant, a resource, a lifecycle, **or**
a replaceable adapter.

## Applicable when

apply **when** a Tool, App backend service, **or** MCP component combines a decision
with an external effect, asynchronous work, **or** lifecycle transition.

## Procedure

1. form the decision, target, ordering, **and** expected outcome with deterministic
   functions from explicit observations **before** applying an effect.
2. pass the resulting plan **to** one bounded effect boundary.
3. use a function for a one-shot effect **only** **when** its complete target,
   dependency, input, outcome, **and** failure boundary are explicit **and** it owns
   no identity across calls, state, invariant, resource, lifecycle, **or** adapter.
4. use a specifically named object method **when** the effect **must** own **any** of those
   responsibilities across calls.
5. return typed observations **or** completion facts **to** the decision boundary;
   do **not** let the effect owner invent, reorder, **or** suppress a decision.

## Outcome

decision logic is locally readable **and** replayable. **every** effect has a visible,
bounded function **or** object owner, ordered input, **and** recoverable result
boundary. objects exist **only** **where** persistent identity **or** ownership requires
them.

## Failure or stop

stop execution **when** the plan is incomplete, an effect owner would make a new
business decision, a one-shot effect hides a dependency **or** exceeds its declared
boundary, an object exists **without** owned identity **or** ownership, **or** the effect
boundary cannot report a typed result.

## Sources

- [Python Functional Programming HOWTO](https://docs.python.org/3.14/howto/functional.html)
- [Python documentation: data classes](https://docs.python.org/3.14/library/dataclasses.html)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-161-PROGRAMMATIC-CORE-METHOD--bound-file-and-subprocess-effects.md

SHA-256: 7b8ad2dd3cc796e3cbe8b71cd7c4dfbb37bab3da08a42131e427b2fb3b5bb38d

```markdown
---
cce_version: "cce_1"
cce_form: "method"
subjects:
  governs: "external-effect"
  depends_on:
    - "programmatic software"
version: 11
updated_at: "2026-09-05 03:48:00 +0400"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-110"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Bound file and subprocess effects

plan, validate, **and** bound **every** PROGRAMMATIC file mutation **or** subprocess
invocation **before** applying it; make partial failure diagnosable **and** recoverable
**without** guessing.

## Applicable when

apply **when** a Tool, App backend service, **or** MCP component writes, replaces, **or**
removes a file, **or** invokes a subprocess.

## Procedure

1. validate the target **and** preconditions **before** mutation.
2. write replacement content through a secure temporary carrier on the
   destination filesystem, flush required bytes, **and** use an atomic replacement
   **only** **where** the supported boundary provides that guarantee.
3. invoke a subprocess with an argument array, explicit timeout, checked exit
   status, controlled environment input, **and** shell execution disabled by
   default.
4. return the target, inputs, outcome, **and** partial-failure context needed for
   diagnosis **or** recovery.

## Outcome

**every** applicable effect has a declared precondition, bounded execution
surface, observable result, **and** explicit recovery limit.

## Failure or stop

stop the effect **when** preconditions fail, an atomicity guarantee is unavailable
**and** no weaker recovery boundary is accepted, **or** subprocess completion,
timeout, **and** exit status cannot be observed.

## Sources

- [Python documentation: `tempfile`](https://docs.python.org/3.14/library/tempfile.html)
- [Python documentation: `subprocess`](https://docs.python.org/3.14/library/subprocess.html)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-162-PROGRAMMATIC-CORE-METHOD--ratchet-hand-authored-python-source-boundaries.md

SHA-256: c82a351843672678ac6e326448169d7995512ca9f4fc0d39c151932c1c6e2526

```markdown
---
cce_version: "cce_1"
cce_form: "method"
subjects:
  governs: "source-boundary"
  depends_on:
    - "programmatic software"
version: 15
updated_at: "2026-10-04 04:23:29 +0400"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-110"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Ratchet hand-authored Python source boundaries

**to** construct bounded hand-authored PROGRAMMATIC Python source, decompose code
by responsibility under CA-M-157, CA-M-158, **and** CA-M-160; choose smaller coherent
units **and** external data Carriers; **and** use measurements **to** guide the next
construction choice. CA-E-539 owns source-size, complexity, exception, **and**
ratchet acceptance policy.

## Applicable when

apply **to** **every** new **or** materially changed hand-authored Python file **in** Tools, App
backend services, **or** MCP components. generated Runtime **and** Delivery outputs
are outside this source rule.

## Procedure

1. read the applicable Evaluation policy **and** changed-source measurements.
2. separate independently reusable responsibilities **and** move deterministic
   transformations outside effect **and** lifecycle owners.
3. extract related units into specifically named modules **when** that keeps
   dependencies **and** responsibility visible.
4. externalize large static mappings. use TOML by default, JSON for schemas
   **or** machine interchange, **and** YAML **only when** its distinct features are required.
5. submit the resulting source **and** any bounded exception rationale **to** the
   applicable Evaluation. use its result **to** choose the next decomposition.

## Outcome

changed source ratchets toward readable, bounded units **and** externalized static
data. construction choices remain traceable **to** responsibility boundaries
**and** the measurements supplied **to** CA-E-539.

## Failure or stop

return unresolved construction choices **when** the applicable Evaluation policy
**or** required measurement is unavailable. retain a separate responsibility **and**
needed recovery boundary **when** a proposed decomposition would obscure either.
acceptance **and** rejection follow CA-E-539.

## Sources

- [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [Ruff: complex-structure rule](https://docs.astral.sh/ruff/rules/complex-structure/)
- [Python documentation: `tomllib`](https://docs.python.org/3.14/library/tomllib.html)
- [Python documentation: `json`](https://docs.python.org/3.14/library/json.html)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-163-PROGRAMMATIC-CORE-METHOD--emit-structured-operational-diagnostics.md

SHA-256: 05e3d4424b82abd2552b9ea7fe3574a268a1e3e10017432a1d3e9569aa90de43

```markdown
---
cce_version: "cce_1"
cce_form: "method"
subjects:
  governs: "operational-diagnostic"
  depends_on:
    - "Atom/Content Role: Operations"
    - "Carrier"
    - "Journal/Record"
    - "programmatic software"
    - "Logging Policy"
version: 12
updated_at: "2026-09-17 18:36:46 +0000"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-110"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Emit structured operational diagnostics

emit structured operational diagnostics for PROGRAMMATIC work under the active
Logging Policy **in** `CAPRMEDIO-GOV-REQU-315`, including its ERROR, WARNING, INFO,
**and** DEBUG meanings. this Method applies that authority **to** PROGRAMMATIC
diagnosis; it does **not** own the level vocabulary, level meanings, **or** Journal
meaning.

## Applicable when

apply **when** a Tool, App backend service, **or** MCP component reports normal
operation, degraded operation, failure, recovery, **or** diagnostic detail.

## Procedure

1. select ERROR, WARNING, INFO, **or** DEBUG according **to** the active Logging Policy;
   do **not** introduce a fifth shared severity.
2. emit records through one project-owned logging abstraction **and** schema.
   include timestamp, level, component, operation, outcome, **and** the canonical
   action **or** event identity **when** one exists.
3. include actionable, contextual, sanitized fields **and** keep DEBUG bounded **to**
   diagnosable need.
4. materialize sink **and** runtime settings **in** configuration **or** Implementation,
   govern carrier placement **and** encoding through Delivery, **and** preserve actual
   execution evidence through Journal Records **and** diagnostic evidence through
   the applicable production-log Carriers. Operations defines the reusable behavior;
   it does **not** make emitted records O Atoms.
5. declare retention, loss, **and** back-pressure behavior at those bounded
   materialization **and** operational boundaries.
6. make logging failure observable **without** silently breaking primary work.

## Outcome

Operators can diagnose component behavior **without** exposing secrets, confusing
operational diagnostics with governed Journal history, **or** relying on an
undeclared sink behavior.

## Failure or stop

stop emission **or** release of the affected diagnostic path **when** required context
cannot be sanitized, a logging failure is hidden, **or** the component would use
the Journal as a substitute logging sink.

## Sources

- [Python Logging HOWTO](https://docs.python.org/3.14/howto/logging.html)
- [Python Logging Cookbook](https://docs.python.org/3.14/howto/logging-cookbook.html)
- [OpenTelemetry: logs](https://opentelemetry.io/docs/concepts/signals/logs/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-164-PROGRAMMATIC-CORE-METHOD--ratchet-typing-and-automation-adoption.md

SHA-256: 13dcbdfefc3bd15041eca0fefc6d4538539ef8f225448b15f2a31916ea3dab25

```markdown
---
cce_version: "cce_1"
cce_form: "method"
subjects:
  governs: "engineering-ratchet"
  depends_on:
    - "Journal/Record"
    - "programmatic software"
version: 13
updated_at: "2026-10-04 04:23:29 +0400"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-110"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Ratchet typing and automation adoption

advance PROGRAMMATIC typing **and** automation through bounded target selection,
explicit tool configuration, **and** deliberate expansion. Evaluation authority
owns acceptance profiles **and** regression policy under CA-E-539, CA-E-540,
**and** the applicable behavioral Evaluation.

## Applicable when

apply **when** a Tool, App backend service, **or** MCP component adds **or** materially
changes source that falls within an admitted typing, formatting, linting, **or**
behavioral-check capability.

## Procedure

1. resolve **every** selected typing, formatting, linting, **or** behavioral-check
   capability from its accepted Method owner.
2. read its current tool, version, profile, **and** bounded target materialization
   from canonical configuration **or** Implementation; read carrier placement **and**
   encoding from Delivery.
3. keep formatting, linting, typing, **and** behavioral evidence distinct.
4. provide changed **or** new target evidence **and** its current admitted baseline
   **to** the applicable Evaluation for its regression decision.
5. expand **or** replace a selected capability **only** through a Method change;
   materialize that change separately **and** preserve evidence of actual runs **in** Journal Records.

## Outcome

automation **and** typing improve monotonically at an admitted surface **without**
turning an unselected tool, version, **or** strictness level into shared authority.

## Failure or stop

return unresolved selection **when** no accepted Method owns the tool choice **or**
the bounded materialization is unavailable. Evaluation authority determines
whether the supplied baseline **and** execution evidence admit the claimed ratchet.

## Sources

- [Ruff documentation](https://docs.astral.sh/ruff/)
- [Mypy: using Mypy with an existing codebase](https://mypy.readthedocs.io/en/stable/existing_code.html)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-165-PROGRAMMATIC-CORE-METHOD--measure-before-optimizing-programmatic-performance.md

SHA-256: 319c2f8b8e4fd974d63281118c767ead78f7bbbc17808201485b4d12018bb5ee

```markdown
---
cce_version: "cce_1"
cce_form: "method"
subjects:
  governs: "performance-measurement"
  depends_on:
    - "programmatic software"
version: 9
updated_at: "2026-09-05 03:48:00 +0400"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-110"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Measure before optimizing PROGRAMMATIC performance

measure a PROGRAMMATIC performance concern **before** accepting an optimization;
use a representative workload for its Hook, interactive, batch, MCP, App, **or**
background surface rather than treating one surface as universal.

## Applicable when

apply **when** a Tool, App backend service, **or** MCP component proposes **or** assesses
a performance-sensitive change.

## Procedure

1. profile the applicable surface **to** locate the measured bottleneck, **then**
   select its representative workload.
2. preserve the input, environment, baseline, observed distribution, **and**
   comparison threshold with the measurement.
3. compare the change **to** the recorded baseline **before** accepting the claimed
   improvement.
4. leave numeric budgets **to** a later bounded authority **until** current baselines
   **and** Operator priorities establish them.

## Outcome

an accepted performance claim is tied **to** one reproducible workload **and**
measurement boundary instead of a universal **or** unmeasured optimization claim.

## Failure or stop

stop the performance claim **when** no representative workload, preserved
baseline, **or** comparable observation exists; do **not** invent a numeric budget.

## Sources

- [Python documentation: profilers](https://docs.python.org/3.14/library/profile.html)
- [pyperf documentation](https://pyperf.readthedocs.io/en/latest/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-166-PROGRAMMATIC-CORE-METHOD--preserve-declared-interface-compatibility-boundaries.md

SHA-256: 14497a272a2c9c45c2d585603236eabe4d9487c802b000f01f77d65a24ff3a0e

```markdown
---
cce_version: "cce_1"
cce_form: "method"
subjects:
  governs: "compatibility-boundary"
  depends_on:
    - "programmatic software"
version: 11
updated_at: "2026-09-05 03:48:00 +0400"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-110"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Preserve declared interface compatibility boundaries

preserve **or** explicitly replace **every** declared PROGRAMMATIC interface **or** host
compatibility boundary; do **not** infer a broader support claim from
local use, stale workflow configuration, **or** one implementation.

## Applicable when

apply **when** a Tool, App backend service, **or** MCP component changes a declared
technical interface, host integration, transport, **or** dependency-facing
interface boundary.

## Procedure

1. identify the current Requirement, technical contract, **or** pinned external
   origin that declares the affected interface boundary.
2. preserve its declared behavior **or** obtain an accepted bounded replacement
   **before** releasing the change.
3. keep component-specific interface details at the child Scope that owns
   them.
4. **when** no current boundary exists, record the absence rather than claiming
   platform **or** cross-host compatibility.

## Outcome

**every** compatibility claim has one current authority **and** remains limited **to** its
declared interface surface.

## Failure or stop

stop release **or** compatibility claims **when** the affected interface boundary has
no current authority, pinned external origin **where** one is required, **or**
accepted replacement.

## Sources

- [Python documentation: `typing.Protocol`](https://docs.python.org/3.14/library/typing.html#typing.Protocol)
- [Semantic Versioning 2.0.0](https://semver.org/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-191-PROGRAMMATIC-METHOD--bind-one-programmatic-mutation-to-its-initiative.md

SHA-256: 880098eb5e7548e936c2b726745d73e17f40130d387dada2eb002ebba1d33c72

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "programmatic-mutation"
  depends_on:
    - "programmatic software"
version: 11
updated_at: 2026-09-01 02:40:00 +0400
relations:
  method_for:
    - CA-R-1094
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Bind one programmatic mutation to its Initiative

## Applicable when

apply **before** accepting **or** dispatching a programmatic mutation governed by
CA-R-1094.

## Procedure

1. resolve **or** create **=1** sealed Initiative from the accepted human
   instruction. it **may** bind **to** a persisted Plan **or** Task **or** remain an ephemeral
   session task.
2. assign one stable action identity **and** preserve a short instruction-derived
   summary plus enough structured context **to** identify the instruction.
3. attach the Initiative **and** action identities **before** **any** Hook, queue, worker,
   retry, Git, Journal, **or** reconciliation handoff.
4. propagate both identities unchanged through **every** handoff. a process,
   thread, adapter, queue, **or** worker identity **may** be linked as execution
   context but **must not** replace them.
5. return an explicit blocked outcome **before** mutation **when** either identity is
   missing, ambiguous, changed, **or** bound **to** more than one Initiative.

## Outcome

**every** accepted mutation remains attributable **to** one human-origin Initiative
**and** one stable action across asynchronous execution **and** provenance systems.

## Failure or stop

stop **before** mutation **when** the Initiative is unsealed, the action identity is
absent **or** reused for another Initiative, **or** a handoff cannot preserve both
identities.

## Sources

- [CA-A-058 — Validate PROGRAMMATIC Method and Evaluation closure](../02_analysis/CA-A-058-PROGRAMMATIC-ANALYSIS_RPRT--validate-programmatic-method-and-evaluation-closure.md)
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-192-PROGRAMMATIC-METHOD--reconcile-independent-git-and-journal-provenance.md

SHA-256: 5f7f18acf59bf8fccf3198922e510b455b2f4484d70a515362634dd49fed5010

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "provenance"
  depends_on:
    - "programmatic software"
version: 11
updated_at: 2026-09-01 02:40:00 +0400
relations:
  method_for:
    - CA-R-1095
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reconcile independent Git and Journal provenance

## Applicable when

apply **after** a sealed programmatic action changes Git-governed carriers, creates
**or** prepares its Journal record, **or** requires provenance **before** later reliance.

## Procedure

1. preserve one sealed durable action state independently of Git **and** Journal
   writes.
2. record whether the action is `git_complete_journal_pending`,
   `journal_recorded_git_pending`, **or** `reconciled`; do **not** treat either pending
   state as provenance loss.
3. bind **=1** canonical Journal action record **to** **=1** reachable
   real-change commit once that commit SHA is known.
4. commit the Journal carrier later **in** a separate Git commit. derive the
   Journal-carrier binding from its exact revision **and** reachable history; do
   **not** embed the SHA of the commit that **contains** the same record.
5. reconcile missing counterparts, duplicate bindings, revision **or** digest
   mismatches, **and** Journal-carrier watermark lag from sealed durable state.
6. do **not** block the mutation that creates an action on its own reconciliation.
   require `reconciled` **before** a later release, promotion-dependent action, **or**
   other governed reliance on that provenance.
7. return an explicit blocked state **when** deterministic repair cannot establish
   one canonical record **and** one reachable real-change commit.

## Outcome

Git **and** Journal remain independent provenance systems while **every** sealed action
converges **to** one recoverable cross-system binding **without** a digest cycle.

## Failure or stop

stop reliance on the affected provenance **when** the sealed state is absent,
multiple canonical records **or** commits remain, the commit is unreachable, **or**
revision **and** digest mismatches cannot be repaired deterministically.

## Sources

- [Git documentation: commits](https://git-scm.com/docs/git-commit)
- [NDJSON specification](https://github.com/ndjson/ndjson-spec)
- [CA-A-058 — Validate PROGRAMMATIC Method and Evaluation closure](../02_analysis/CA-A-058-PROGRAMMATIC-ANALYSIS_RPRT--validate-programmatic-method-and-evaluation-closure.md)
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-193-PROGRAMMATIC-METHOD--supply-the-active-tool-frontier-to-mcp.md

SHA-256: 0362d22f09b9f2549bd233d337bd8f37c845da61c705df40517b1f20027f1489

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "framework-engine-mcp"
  depends_on:
    - "Projection"
    - "programmatic software"
version: 11
updated_at: "2026-09-17 19:02:58 +0000"
relations:
  method_for:
    - CA-R-1096
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Supply the active Tool frontier to MCP

## Applicable when

apply **when** MCP builds **or** refreshes the callable frontier supplied by TOOLS.

## Procedure

1. enumerate the complete current set of active immediate Tool units from the
   canonical TOOLS frontier.
2. read **and** validate **every** active Tool's machine-invocation contract **without**
   inferring missing meaning from its code **or** runtime state.
3. project **=1** stable callable endpoint for **every** valid active Tool.
4. omit inactive **and** explicitly disabled Tools; report **every** invalid active
   Tool as a diagnostic rather than silently omitting it.
5. delegate **every** admitted call **to** the Tool **without** duplicating **or** changing its
   meaning, inputs, outcomes, **or** mechanics.
6. replace the exposed frontier **only** **after** the complete candidate projection
   validates; preserve the preceding valid frontier **when** refresh fails.

## Outcome

MCP exposes one complete, deterministic projection of valid active Tools **and**
remains a replaceable interface rather than a second Tool authority.
preserving an earlier frontier **after** a failed refresh does **not** make it current;
apply the publication boundary **in** CA-R-1110.

## Failure or stop

stop refresh **and** preserve the preceding valid frontier **when** active Tool
enumeration is incomplete, endpoint identities collide, **or** a machine contract
is missing **or** invalid. reject a call that cannot delegate unchanged.

## Sources

- [Model Context Protocol: lifecycle](https://modelcontextprotocol.io/specification/2025-06-18/basic/lifecycle)
- [Model Context Protocol: tools](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)
- [CA-A-058 — Validate PROGRAMMATIC Method and Evaluation closure](../02_analysis/CA-A-058-PROGRAMMATIC-ANALYSIS_RPRT--validate-programmatic-method-and-evaluation-closure.md)
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-221-PROGRAMMATIC-CORE-METHOD--use-uv-as-the-default-python-workflow-frontend.md

SHA-256: 7f775763961eeba508a3008d51207108150692a6c4378e26d15c1e1315bde6cd

```markdown
---
cce_version: "cce_1"
cce_form: "method"
subjects:
  governs: "python-workflow-frontend"
  depends_on:
    - "Journal/Record"
    - "Atom/Content Role: Operations"
    - "programmatic software"
version: 14
updated_at: "2026-09-17 19:02:49 +0000"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-110"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Use uv as the default Python workflow frontend

use uv as the default frontend for **every** admitted Python workflow capability
that uv provides. this Method owns that tool selection; configuration **and**
Implementation materialize it, Delivery governs its carriers, Operations defines reusable workflow behavior,
**and** Journal Records carry evidence of actual workflow execution.

## Applicable when

apply **when** developing, evaluating, building, **or** packaging PROGRAMMATIC Python
source. installed CAPRMEDIO runtime execution remains outside this Method.

## Procedure

1. resolve the supported Python boundary from its accepted Method **and** canonical
   Project technical-configuration materialization, **then** install **or** select it
   through `uv python`.
2. materialize dependencies selected by accepted Methods **in** `pyproject.toml`;
   change them through `uv add` **or** `uv remove` so the declaration **and** `uv.lock`
   change together.
3. reproduce the project environment with `uv sync --locked` **and** execute
   governed Python commands with `uv run --locked`.
4. run an isolated Python CLI through `uv tool run` **only** with a pinned tool
   version **and** command **when** it is **not** an admitted project dependency.
   unpinned ephemeral execution cannot supply acceptance evidence.
5. use `uv build` **or** `uv publish` **only** **when** an accepted Delivery authorizes a
   package **or** publication target.
6. do **not** mix pip, venv, virtualenv, pipx, Poetry, Conda, **or** another overlapping
   Python workflow manager into the same governed path **unless** uv lacks a
   required capability **or** an external boundary requires the alternative.
7. record an exception with its capability, bounded carriers, exact commands,
   added operational cost, cleanup **or** recovery procedure, **and** Operator
   acceptance.
8. keep uv outside the installed CAPRMEDIO runtime contract. installed Tools
   remain self-contained under `.caprmedio_runtime/tools` **and** execute **without** uv, a
   project virtual environment, **or** another dependency outside that selected
   runtime release. route uv cache, build, **and** staging state into
   `.caprmedio_tmp/`.

## Outcome

one declared Python boundary **and** one reviewed lockfile reproduce the admitted
Python environment **and** commands **without** an undeclared manager **or** dependency
source.

## Failure or stop

stop **when** the supported interpreter cannot be resolved, the lockfile is stale,
a command would update the environment implicitly during evidence collection,
**or** an exception lacks its accepted boundary.

## Sources

- [uv: Features](https://docs.astral.sh/uv/getting-started/features/)
- [uv: Installing and managing Python](https://docs.astral.sh/uv/guides/install-python/)
- [uv: Locking and syncing](https://docs.astral.sh/uv/concepts/projects/sync/)
- [uv: Tools](https://docs.astral.sh/uv/concepts/tools/)
- [uv: Configuring projects](https://docs.astral.sh/uv/concepts/projects/config/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-280-PROGRAMMATIC-CORE-METHOD--adopt-current-python-idioms-only-for-declared-benefit.md

SHA-256: 3334dabc09a3de5637d007394bb6b69bb5459af7b31f35d438226778211bc41f

```markdown
---
cce_version: "cce_1"
cce_form: "method"
subjects:
  governs: "python-idiom-adoption"
  depends_on:
    - "programmatic software"
version: 8
updated_at: "2026-09-11 20:58:34 +0400"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-110"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Adopt current Python idioms only for declared benefit

adopt a stable idiom available **in** the selected Python boundary **only** **when** it
improves a named project quality such as correctness, understandability,
safety, **or** measured performance. preserve the simpler supported idiom **when** a
newer construct adds no useful distinction.

## Applicable when

apply **when** new **or** materially changed PROGRAMMATIC Python source proposes a
runtime-specific language construct **or** concurrency model.

## Procedure

1. state the quality improved **and** the supported Python boundary that admits
   the idiom.
2. prefer the simplest current construct that expresses the required meaning.
3. use f-strings for immediate trusted string construction; use t-strings **only**
   **when** a processor needs structured interpolation data.
4. keep synchronous work synchronous **unless** related concurrent operations
   create a demonstrated need for structured concurrency.
5. record a compatibility exception **when** an admitted host boundary cannot use
   the selected idiom.

## Outcome

current Python capabilities improve the code for an explicit reason **without**
turning novelty into a requirement **or** obscuring the supported boundary.

## Failure or stop

stop adoption **when** the benefit is unnamed, the simpler idiom is equally clear,
**or** the construct exceeds the selected runtime **or** compatibility boundary.

## Sources

- [PEP 750 — Template Strings](https://peps.python.org/pep-0750/)
- [Python documentation: task groups](https://docs.python.org/3.14/library/asyncio-task.html#task-groups)
- [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-281-PROGRAMMATIC-CORE-METHOD--declare-one-python-and-software-configuration-boundary.md

SHA-256: e825a96f745f0b9e73b795c01b076ce8e4a5e7815784f4910e2889595baa6441

```markdown
---
cce_version: "cce_1"
cce_form: "method"
subjects:
  governs: "python-technical-configuration"
  depends_on:
    - "programmatic software"
version: 11
updated_at: "2026-09-11 20:58:34 +0400"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-110"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Declare one Python and software configuration boundary

select the stable CPython `3.14.*` series **and** require one project-owned
technical configuration boundary for interpreter, formatting, linting, typing,
evaluation, **and** packaging. CA-D-250 owns the current carrier placement **and**
encoding **in** the root `pyproject.toml`; configuration **and** Implementation
materialize this Method's selections there. keep that technical configuration
separate from CAPRMEDIO project settings.

## Applicable when

apply **when** Python source **or** a development workflow depends on an interpreter,
dependency, formatter, linter, type checker, evaluator, **or** packager setting.

## Procedure

1. resolve the current Delivery carrier, **then** materialize the selected
   interpreter series **and** admitted development-tool profiles through that
   boundary.
2. keep one value for **every** setting **and** make local **and** automated workflows read
   that value rather than reproduce it.
3. change the interpreter series **or** a selected tool profile **only** through its
   accepted Method **before** changing configuration.
4. verify the selected stable series **before** using version-specific behavior.
5. keep runtime project settings outside `pyproject.toml` **and** expose them **only**
   through the shared Settings Reader.

## Outcome

this Method owns one set of Python workflow selections; Delivery owns its
carrier, **and** configuration **and** Implementation reproduce the selections **without**
becoming another methodological authority.

## Failure or stop

stop **when** two carriers disagree, a moving `latest` label replaces the selected
series, the materialization conflicts with its Delivery, **or** technical **and**
CAPRMEDIO project settings are mixed.

## Sources

- [Python 3.14 release notes](https://docs.python.org/3.14/whatsnew/3.14.html)
- [PyPA: `pyproject.toml` specification](https://packaging.python.org/en/latest/specifications/pyproject-toml/)
- [CA-A-054 — Validate the Python 3.14 contract upgrade](../02_analysis/CA-A-054-PROGRAMMATIC-ANALYSIS_RPRT--validate-the-python-3-14-contract-upgrade.md)
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-282-PROGRAMMATIC-CORE-METHOD--use-ruff-for-python-formatting-linting-and-complexity.md

SHA-256: 334580e46e2d41868af284a9a65b7d78d0cd08b0bf14ad2ad3225947f303dab0

```markdown
---
cce_version: "cce_1"
cce_form: "method"
subjects:
  governs: "python-formatting-and-linting"
  depends_on:
    - "programmatic software"
version: 9
updated_at: "2026-10-04 04:23:29 +0400"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-110"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Use Ruff for Python formatting, linting, and complexity

use Ruff as the selected formatter **and** linter for hand-authored PROGRAMMATIC
Python source, including cyclomatic-complexity lint for changed executable
units.

## Applicable when

apply **to** new **or** materially changed Python source within Tools, App, **or** MCP.

## Procedure

1. materialize one pinned Ruff profile **in** `pyproject.toml`.
2. run Ruff formatting **and** linting through the selected uv workflow.
3. enable the Ruff `C901` rule **and** materialize the applicable Evaluation-owned
   complexity maximum under CA-E-539.
4. provide rule diagnostics, measured values, **and** exception rationale **to**
   CA-E-539 for its acceptance **and** disposition decision.
5. keep Ruff evidence distinct from typing **and** behavioral evidence.

## Outcome

mechanical style, lint, **and** cyclomatic-complexity checks use one reproducible
Method-owned selection **and** one materialized profile.

## Failure or stop

return unavailable configuration **when** Ruff is unpinned **or** the current profile
is absent. changed-source acceptance **and** exception admission follow CA-E-539.

## Sources

- [Ruff documentation](https://docs.astral.sh/ruff/)
- [Ruff: configuration](https://docs.astral.sh/ruff/configuration/)
- [Ruff: complex-structure rule](https://docs.astral.sh/ruff/rules/complex-structure/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-283-PROGRAMMATIC-CORE-METHOD--use-mypy-for-static-python-type-checking.md

SHA-256: 354ab7916329e96171e5809ada0744a0cf05f9751f88ff01f17fac1d7a526b92

```markdown
---
cce_version: "cce_1"
cce_form: "method"
subjects:
  governs: "python-static-typing"
  depends_on:
    - "programmatic software"
version: 9
updated_at: "2026-10-04 04:23:29 +0400"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-110"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Use Mypy for static Python type checking

use Mypy as the selected static type checker for hand-authored PROGRAMMATIC
Python source. CA-E-540 owns strict-profile, baseline, **and** suppression
acceptance policy.

## Applicable when

apply **to** new **or** materially changed Python source within Tools, App, **or** MCP.

## Procedure

1. materialize one pinned Mypy profile **and** bounded target set **in**
   `pyproject.toml`.
2. run Mypy through the selected uv workflow.
3. provide the current diagnostics **and** recorded baseline **to** CA-E-540.
4. bind suppression rationale **to** the affected line **or** symbol for evaluation
   under CA-E-540.
5. keep static typing evidence distinct from runtime validation **and** behavioral
   evidence.

## Outcome

changed Python interfaces become more explicit **without** making untyped legacy
source an unrelated whole-project blocker.

## Failure or stop

return unavailable configuration **when** the profile **or** target set is absent.
typing acceptance, baseline regression, **and** suppression disposition follow
CA-E-540.

## Sources

- [Mypy documentation](https://mypy.readthedocs.io/en/stable/)
- [Mypy: using Mypy with an existing codebase](https://mypy.readthedocs.io/en/stable/existing_code.html)
- [Mypy: strict mode](https://mypy.readthedocs.io/en/stable/command_line.html#cmdoption-mypy-strict)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-284-PROGRAMMATIC-CORE-METHOD--read-engine-settings-through-one-shared-boundary.md

SHA-256: 690b9f8716d649e8d27a7e63ff0129455d6de14f9cf3fd30a7173cf25f9dc049

```markdown
---
cce_version: "cce_1"
cce_form: "method"
subjects:
  governs: "engine-settings-reader"
  depends_on:
    - "Carrier"
    - "Projection"
    - "Artifact/Revision"
    - "Project Settings"
    - "programmatic software"
version: 11
updated_at: "2026-09-17 19:02:53 +0000"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-110"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Read Engine settings through one shared boundary

use one centralized Settings Reader for **every** applicable Tool, App, **and** MCP
component. the Reader reads the authoritative Project Settings Artifact,
validates the complete input, **and** returns an immutable typed snapshot with
source **and** Revision provenance under CA-D-365. the snapshot is derived;
Project Settings is **not** a Projection.

## Applicable when

apply **when** PROGRAMMATIC behavior depends on Project Settings.

## Procedure

1. read the authoritative Project Settings Carrier bound by CA-D-364 through
   the shared Reader; do **not** infer a replacement from a legacy filename.
2. validate the complete carrier at the boundary **and** return structured
   diagnostics for invalid input.
3. pass the immutable snapshot explicitly **to** the consuming deterministic core
   **or** application service.
4. do **not** add component-specific parsers, default chains, environment
   fallbacks, semantic overrides, **or** writes **to** the Reader.
5. make the control panel use the same Reader **and** request changes **to** the
   authoritative Project Settings Artifact through its dedicated Doer, **not**
   through the Reader, its immutable snapshot, **or** a Projection.

## Outcome

**every** component observes one validated settings snapshot **without** duplicating
parsing **or** inventing a second control panel.

## Failure or stop

stop **when** the authoritative Project Settings Carrier is missing **or** invalid, provenance is absent,
**or** a consumer would bypass **or** mutate the shared snapshot.

## Sources

- [Python documentation: `tomllib`](https://docs.python.org/3.14/library/tomllib.html)
- [Pydantic: strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-285-PROGRAMMATIC-CORE-METHOD--select-software-evaluation-techniques-by-failure-mode.md

SHA-256: 703a3fac4c89f3ccf117478bd7a762a92867a3cf6db96b32866561cd2cd0f49d

```markdown
---
atom_id: CA-M-285
content_role: Method
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Core
global_tier: 6
status: Active
author: Anatoly Maslennikov
version: 12
updated_at: "2026-10-04 03:52:53 +0400"
subjects:
  governs: "software-evaluation-selection"
  depends_on:
    - "programmatic software"
    - "Actor"
    - "Spec"
    - "Evaluation"
    - "Implementation"
relations:
  derived_from:
    - CA-A-053
  child_of:
    - CA-M-110
---
# Summary

Select software Evaluation techniques by failure mode

## Scope

selection of behavioral software Evaluation techniques for PROGRAMMATIC components.

## Claim

**to** select behavioral software Evaluation techniques for a PROGRAMMATIC component, the Actor selecting the portfolio **must** take the applicable Spec, declared failure predicates, **and** active Evaluation authority as inputs; identify candidate checks for **every** predicate; evaluate candidate portfolios against the applicable Core Evaluation policy **and** each selected technique's own acceptance **and** disposition rules; select one admitted portfolio; repeat **until** all predicates are covered **or** no candidate remains; produce the selected Evaluation identities **and** selection rationale; **and** return unresolved predicates for authority **or** design clarification **when** no portfolio is admitted.

## Details

1. enumerate the failure predicates established by applicable authority **and** bind each predicate **to** the observable behavior that can distinguish acceptance from rejection.
2. identify applicable Evaluation Atoms across test scopes, purposes, boundary-realism choices, execution environments, **and** release stages **without** treating those labels as a universal ranking.
3. construct candidate portfolios from those Evaluation Atoms. include a specialized technique **only when** its Evaluation applicability **and** evidence preconditions are satisfied.
4. evaluate **every** candidate portfolio under `CA-E-389-PROGRAMMATIC-CORE-EVAL_APPROACH--combine-complementary-software-behavior-evidence` **and** the acceptance **and** disposition rules of **every** selected Evaluation Atom. apply `CA-E-536-PROGRAMMATIC-CORE-EVAL_APPROACH--admit-safe-canary-evaluation` **when** a candidate includes canary evidence.
5. stop with one traceable admitted portfolio **when** all predicates are covered. **when** no candidate passes, return the uncovered predicates, failed policy conditions, **and** missing evidence rather than inventing a test-count ratio **or** silently accepting incomplete coverage.

## Sources

- [CA-E-389-PROGRAMMATIC-CORE-EVAL_APPROACH--combine-complementary-software-behavior-evidence](../06_evaluation/CA-E-389-PROGRAMMATIC-CORE-EVAL_APPROACH--combine-complementary-software-behavior-evidence.md)
- [CA-E-536-PROGRAMMATIC-CORE-EVAL_APPROACH--admit-safe-canary-evaluation](../06_evaluation/CA-E-536-PROGRAMMATIC-CORE-EVAL_APPROACH--admit-safe-canary-evaluation.md)
- [CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-286-PROGRAMMATIC-CORE-METHOD--validate-untrusted-structured-data-with-pydantic.md

SHA-256: 70fd46681fe112c2ce926c38572ccc22b8f41d95644e852a7cf8241433f64a16

```markdown
---
cce_version: "cce_1"
cce_form: "method"
subjects:
  governs: "python-boundary-validation"
  depends_on:
    - "programmatic software"
version: 8
updated_at: "2026-09-11 20:58:34 +0400"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-110"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Validate untrusted structured data with Pydantic

use Pydantic **when** untrusted structured data crosses an admitted Python
boundary. validate once at the boundary **and** pass accepted typed values into
the deterministic core **without** making Pydantic the universal internal model.

## Applicable when

apply **to** an admitted CLI payload, Hook event, configuration carrier, Journal
record, protocol message, **or** external adapter whose invalid structure could
hide a contract defect.

## Procedure

1. define the bounded input model with field types **and** constraints **before**
   custom validators.
2. use strict validation **when** coercion could hide a defect; admit lax conversion
   **only** for a declared interoperability need **and** make it observable.
3. reject undeclared extra fields for closed machine contracts.
4. return structured validation diagnostics **and** pass the accepted typed value
   **to** the deterministic core.
5. add Pydantic as a runtime dependency **only** **where** validation **and** schema value
   justify its dependency cost.

## Outcome

untrusted structured inputs become explicit typed values at one boundary while
the internal model remains independent of the validation library.

## Failure or stop

stop admission **when** the boundary is **not** declared, coercion is silent, extra
fields escape a closed contract, **or** the dependency has no bounded benefit.

## Sources

- [Pydantic: models](https://docs.pydantic.dev/latest/concepts/models/)
- [Pydantic: strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/)
- [Pydantic: model configuration](https://docs.pydantic.dev/latest/concepts/config/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-289-PROGRAMMATIC-CORE-METHOD--route-all-temporary-carriers-through-project-temp.md

SHA-256: 7dce58d61b2a9fb1e5c653bd25715e447b2b9522ae4b13d3e98544ed5dc874e4

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "PROGRAMMATIC/temporary execution state"
  depends_on:
    - "programmatic software"
    - "Project Settings"
llm_session_ids:
  - codex:01a0263a-7510-7672-bce4-58830bc4d184
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 9
updated_at: "2026-10-04 04:23:29 +0400"
relations:
  method_for:
    - CA-R-1473
---
# Route all temporary Carriers through project temp

resolve the configured Project Temporary State root **before** a PROGRAMMATIC
component creates a temporary Carrier **or** invokes a dependency that can create
one. allocate a component-owned **and**, **when** concurrency is possible, run-specific
descendant below `.caprmedio_tmp/`. pass that descendant explicitly **to**
temporary-file APIs **and** configure dependency cache, temporary, staging, build,
**and** Evaluation paths **before** invocation. materialize shared development-tool
cache paths through the root `pyproject.toml`; provide explicit run-specific
paths through launch Carriers for dependencies that do **not** read that file.
do **not** rely on an ambient host
temporary directory **or** the process working directory.

route Python bytecode cache output **to** `.caprmedio_tmp/cache/python/` **before**
importing Project modules, **or** disable bytecode writes for an isolated process.
do **not** create `__pycache__/` **or** `.pyc` Carriers below `.caprmedio_runtime/`.

for an atomic replacement, create its staging Carrier below the Project
Temporary State root **and** verify that the staging **and** destination Carriers satisfy the
required same-filesystem atomicity boundary **before** the first mutation. stop
**without** falling back **to** a destination sibling **or** host temporary location **when**
that precondition is false.

attempt bounded cleanup **when** the owning operation ends. treat interrupted **or**
denied cleanup as retained non-authoritative temporary state, report its owned
path, **and** leave it confined below `.caprmedio_tmp/`. never weaken placement
because cleanup is best-effort.

keep executable releases, shared implementation libraries, registries, stable
launchers, Hook Carriers, runtime logs, sessions, databases, service state,
resumable state, **and** governed Artifacts outside the Temporary State root **in**
their applicable authority **or** runtime places.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-087-TOOLS-CORE-IMPL_METHOD--process-one-project-path-action.md

SHA-256: 6bedb22ca8cf1c404c2b2d9f517e30729cdb9fb15010287ce7126f8ef7dca752

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "provenance"
  depends_on:
    - "Journal"
    - "Journal/Record"
    - "Atom"
    - "Artifact/Carrier"
    - "Project"
    - "Applicable Methodology"
version: 23
updated_at: "2026-09-16 21:24:29 +0000"
relations:
  relates_to:
    - CA-R-1491
  method_for:
    - CA-R-803
    - CA-R-804
    - CA-R-805
    - CA-R-812
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Process one project-path action

use this composite Method for **`=1`** sealed project-path action. its subject is **`=1`** file **or** **`=1`** non-empty folder; a folder action has **`=1`** frozen ordered entry set **and** remains **`=1`** action.

1. COMMIT_TRIGGER atomically accepts **`=1`** immutable source event into the Runtime inbox **and** returns. it performs no repository scan, context gathering, Journal append, staging, Git mutation, retry, **or** worker spawn.
2. the independently supervised COMMIT_AUTOMATION service reconciles inbox events with the current Git-admitted repository frontier. its pure manager defines the fixed action graph **and** its mechanical Scheduler persists **and** advances **only** declared transitions. new events remain durable **and** mark the repository pending while another Git-mutating action is active.
3. a COMMIT_CONTEXT worker produces provisional deterministic context with the Initiative, expected frontier, resolved atomic target **or** frozen folder entry set, **and** provenance facts. Project **or** Git mutation consumers revalidate their mutation preconditions at their effect boundary. Journal recording instead checks event **and** storage integrity under CA-R-1491; it does **not** require observed Project state **to** pass conformance checks **or** remain unchanged.
4. from sealed context, advance two independent branches. an APPEND_CHANGE_RECORDS worker prepares **and** appends the action's canonical Journal record idempotently through the canonical writer; shared-Carrier serialization belongs **to** that writer **or** batcher. preserve intact historical observations **without** silently rebinding them **to** later Project state. independently, a real-change item becomes eligible for the Git gate **without** waiting for the Journal branch.
5. a COMMIT_CHANGE_SET worker alone owns the repository-scoped fenced Git lease. it revalidates the sealed Initiative, action state, expected Git base, target frontier, **and** complete staged target set immediately **before** commit creation. it creates **`=1`** real-change commit containing **all** **and** **only** the action targets **or** **`=1`** separate Journal-only batch commit containing **only** selected Journal Carriers. it never imports **or** invokes its peer Tools **and** rejects **every** non-commit Git operation.
6. persist branch transitions independently through queued, reconciling, context_sealed, journal_pending **or** journaled, real_change_pending **or** real_change_committed, journal_commit_pending **or** journal_committed, **and** completed **or** no_change, with explicit retry_wait, paused, blocked, **and** dead_letter outcomes. resume from the last safe persisted phase **and** reconcile uncertain commit outcomes **before** replay.
7. reconcile at low frequency while enabled so missed Hook delivery **and** external Project edits do **not** make a host callback the correctness boundary.

return the common Tool result envelope. dry run predicts **only** context, queue **and** gate eligibility, message Projection, **and** Journal eligibility. this Method never edits governed subject content, infers Atom meaning beyond the admitted action, **or** performs branch, upstream, remote, synchronization, push, tag, **or** release operations.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-101-TOOLS-CORE-IMPL_METHOD--build-the-as-is-implementation-inventory.md

SHA-256: 886d2ce273bc450a23b08da2ed357068c4d7cd0f712da6c6ef4eb00d9028571e

```markdown
---
subjects:
  governs: "feature-boundary"
  depends_on: []
version: 11
updated_at: "2026-09-10 22:35:50 +0400"
relations:
  method_for:
    - CA-R-1071
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Build the as-is Implementation Inventory

resolve the selected native Implementation frontier **and** bind the observed frontier through exact shared Project Work Journal records **and** source Atom revisions, **then** build a reproducible as-is Implementation Inventory Projection of its directories, files, language-native modules, declared dependencies, **and** detectable realization relations. preserve exactly what is observed **without** interpreting directories as Areas **or** Features, treating files as governed Module scopes, **or** creating project authority.

keep the Inventory as an independently reusable result for navigation, inspection, impact analysis, **and** later reconciliation. structural adoption **may** consume it, but the Inventory remains useful **and** currentable **when** no adoption is requested.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-102-TOOLS-CORE-IMPL_METHOD--derive-structural-crmed-drafts-from-the-inventory.md

SHA-256: 84b507b3467b786b6342f6d534317b33cd0c732f96c7969121cada2575a459fc

```markdown
---
subjects:
  governs: "feature-boundary"
  depends_on: []
version: 9
updated_at: 2026-08-30 16:44:07 +0400
relations:
  method_for:
    - CA-R-1072
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Derive structural CRMED drafts from the Inventory

consume the exact current Implementation Inventory Projection produced by `CA-M-101` **and** apply the structural-adoption heuristic **to** the selected adoption frontier: a folder containing folders proposes an Area draft, a folder containing files proposes a Feature draft, **and** a language-native module **or** source file fallback proposes a Module draft. preserve ambiguity explicitly **when** the observed structure does **not** support one unambiguous proposal.

produce **only** CRMED drafts **and** their draft relations for operator review; do **not** convert Inventory observations directly into authority. the structural CRMED draft set is the primary adoption result, while the consumed Inventory remains an independently useful Step 1 result.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-142-TOOLS-CORE-METHOD--separate-tool-runtime-from-temporary-state.md

SHA-256: a1eb10e0f2d9c6ed231520a49f703c788d21bec056603cfdae2d1be911fb22c2

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "runtime"
  depends_on: []
version: 19
updated_at: 2026-09-15 04:19:10 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a0263a-7510-7672-bce4-58830bc4d184
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  method_for:
    - CA-R-1065
  derived_from:
    - CA-A-057
---

# Separate Tool runtime from temporary state

place CAPRMEDIO-owned persistent operational state under the current Project's
`.caprmedio_runtime/` root. place selected Tool releases **and** stable launchers
under `.caprmedio_runtime/tools/`; keep these carriers reconstructible from
governed source **and** configuration. give **every** Tool-owned log, session, database,
service-state, **and** resumable-state Carrier an owned runtime descendant. these
Carriers **may** preserve a non-reconstructible operational timeline.

allocate a Tool-owned **and**, **when** concurrency is possible, run-specific
descendant below `.caprmedio_tmp/` for **every** temporary, scratch, staging,
cache, Python bytecode cache, build, intermediate Evaluation, atomic-write intermediate, **and**
interrupted-cleanup Carrier. pass that descendant explicitly **to** temporary-file
APIs **and** configure **every** invoked dependency **to** use it. do **not** use the
repository root, process working directory, source tree, Project control root,
Runtime State root, **or** host temporary location as a fallback.

for atomic replacement, stage below `.caprmedio_tmp/` **and** verify the
required same-filesystem atomicity precondition **before** mutation. stop with a
stable boundary diagnostic **when** safe placement cannot be established. attempt
bounded cleanup, but keep **every** cleanup remnant confined **to** temporary state.

keep both trees non-authoritative. deleting `.caprmedio_tmp/` can lose **only**
disposable state. deleting `.caprmedio_runtime/` **may** require reinstallation **or**
lose operational history **and** resumable progress, but cannot lose a governed
Artifact **or** Project Journal history.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-143-TOOLS-CORE-METHOD--allocate-one-runtime-folder-per-script.md

SHA-256: 65c4a9bd346f9c474ca81077801e0b727dcfb1d3ea175fec0246ac9b999618b3

```markdown
---
subjects:
  governs: "runtime"
  depends_on: []
version: 14
updated_at: 2026-08-30 16:44:07 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  method_for:
    - CA-R-1065
  derived_from:
    - CA-A-057
---
# Allocate one runtime folder per script

give **every** CAPRMEDIO script **or** executable tool that persists runtime files one dedicated directory beneath the caprmedio runtime root. keep its runtime files inside that directory; concurrent runs **may** use bounded run-specific descendants.

do **not** scatter runtime files, write into another script's directory, **or** depend on an unowned shared directory. a shared runtime service owns its own directory **and** clients use its service contract rather than its files.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-144-TOOLS-CORE-METHOD--route-and-invoke-tools-through-the-common-cli.md

SHA-256: a79c09fcd404a07105910cdb5a9bbee126c8221b695f422f1c10e787fab0bb9c

```markdown
---
subjects:
  governs: "routing"
  depends_on:
    - "Tool"
    - "Projection"
    - "Artifact"
version: 16
updated_at: "2026-09-17 20:19:59 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  method_for:
    - CA-R-1063
    - CA-R-1064
    - CA-R-1065
    - CA-R-1066
    - CA-R-1067
---
# Route and invoke Tools through the common CLI

use this flow for **every** Tool invocation:

1. the LLM declares the intended capability **without** naming an implementation; the router classifies it as `finder` **or** `doer` **and** **may** refine it **to** a registered subtype such as `checker`.
2. the router resolves as many registered decision steps as required **and** returns **every** applicable Tool with identity, purpose, inputs, preconditions, effects, success checks, failure modes, command shape, **and** representative examples.
3. **after** the LLM selects one Tool, pass either composable structural-unit, Type, **and** subtype filters **or** explicit canonical Atom filenames through the common target selector **and** return the resolved target set **before** execution.
4. execute the selected Tool from its selected immutable release under `.caprmedio_runtime/tools`. use other owned `.caprmedio_runtime/` descendants for persistent logs, sessions, databases, service state, **and** resumable state. use `.caprmedio_tmp/` **only** for disposable scratch, staging, caches, builds, Evaluations, atomic-write intermediates, **and** cleanup remnants. **every** Finder, including **every** Checker, receives no mutation capability **and** **must not** mutate authoritative sources **or** derived outputs, while **every** Doer first returns a complete mutation-free dry run **and** **then** writes **only** its declared authoritative source **or** derived output **after** explicit application.
5. return the common result envelope, stable diagnostics, exit status, resolved targets, observed effects, **and** applicable currentness information.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-145-TOOLS-CORE-METHOD--generate-active-requirement-subject-catalog.md

SHA-256: 3b2f3fbd02f3ca4cb5d7e05eef9056fb23a4346fc661a9ae8a800afcd8008c1e

```markdown
---
subjects:
  governs: "projection-pipeline"
  depends_on: []
version: 16
updated_at: 2026-08-30 16:44:07 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  method_for:
    - CA-R-1059
    - CA-R-1061
    - CA-R-1062
---
# Generate active Requirement Subject Catalog

generate the Subject Catalog through this procedure:

1. resolve **=1** requested structural unit from the common selectors, select **every** active Requirement **in** that unit, exclude inactive Requirements from the displayed rows, **and** bind the output **to** `<selected-structural-unit-root>/stg_requirements_subjects.md`.
2. resolve parent existence, lifecycle, **and** tier against the complete active project Requirement graph **before** restricting displayed rows. treat a Core as structurally valid **only** **when** **every** Requirement parent is a Principle, **and** a Standard as structurally valid **only** **when** **every** Requirement parent is a Core; classify missing, inactive, wrong-tier, cyclic, **or** **otherwise** unplaceable Requirements as Orphans with explicit reasons.
3. require **every** displayed Requirement **to** have one parseable first level-one heading. use its text **after** the `# ` marker verbatim as `Summary`; fail the build **when** that heading is missing **or** ambiguous **and** never substitute filename text.
4. group **every** non-orphan Requirement by its single authored `subject_scopes` value. order Subject groups by the current governed Subject catalog, **then** emit Principle, Core, **and** Standard subsections **in** that order **and** sort rows within **every** tier by numeric Requirement ID.
5. emit exactly three columns: `TYPE + ID`, `Summary`, **and** `Child of`. link `TYPE + ID` as the short identity `REQU-NNN` **to** the canonical Atom; link **every** direct authored `child_of` target **in** `Child of`, sorted by numeric identity **where** multiple targets exist; do **not** replace those targets with ancestors **or** group keys.
6. **after** **all** normal Subject groups, emit **=1** final `Orphans` section. retain the same tier **and** numeric ordering inside it, **and** include the orphan reason **without** adding a fourth table column.
7. bind the selected structural unit, exact complete-graph Atom source frontier, generator version, configuration, source digests, **and** `updated_at`; replace `stg_requirements_subjects.md` atomically **in** that structural-unit root **and** record the completed rebuild through the Work Journal.
8. regenerate from the same frontier **and** configuration **and** require byte-stable semantic output **before** reporting the Subject Catalog current.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-146-TOOLS-CORE-METHOD--generate-active-requirement-lineage-map.md

SHA-256: 55f809e4e2d5503c418eace59351538a955104c4df72033865ff86d88e846964

```markdown
---
subjects:
  governs: "projection-pipeline"
  depends_on: []
version: 16
updated_at: "2026-09-17 20:20:04 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  method_for:
    - CA-R-1061
    - CA-R-1062
    - CA-R-1068
---
# Generate active Requirement Lineage Map

generate the Lineage Map through this procedure:

1. resolve **=1** requested structural unit from the common selectors, bind the output **to** `<selected-structural-unit-root>/stg_requirements_lineage_sections.md`, **and** select **every** active Requirement **in** that unit for displayed rows, but build **and** validate ancestry from the complete active project Requirement graph so a selected Layer **or** Feature retains Principle ancestry declared outside its own scope.
2. treat **every** Principle as its own lineage root. traverse **only** direct authored `child_of` Requirement edges upward; require **every** Core Requirement parent **to** be a Principle **and** **every** Standard Requirement parent **to** be a Core, **and** classify missing, inactive, wrong-tier, cyclic, **or** rootless Requirements as Orphans with explicit reasons.
3. for **every** non-orphan Requirement, compute the sorted unique set of **all** reachable Principle Requirement numbers. name its group by joining those unpadded numbers with `+`, so descendants of **only** `REQU-002` belong **to** `2` **and** descendants shared by `REQU-002` **and** `REQU-003` belong once **to** `2+3` rather than also appearing **in** `2` **or** `3`.
4. sort group names by comparing their numbers from left **to** right; at the first difference, place the smaller number first, **and** place an exhausted prefix **before** **any** extension: `2`, `2+3`, `2+4`, `3`. within **every** group emit Principle, Core, **and** Standard subsections **in** that order **and** sort rows within **every** tier by numeric Requirement ID.
5. require one parseable first level-one heading per displayed Requirement **and** use its text **after** `# ` verbatim as `Summary`; fail the build **when** it is missing **or** ambiguous **and** never use filename text.
6. emit exactly three columns: `TYPE + ID`, `Summary`, **and** `Child of`. link `TYPE + ID` as `REQU-NNN` **to** the canonical Atom; link the direct authored `child_of` targets **in** `Child of`, sorted numerically; never substitute reachable ancestors **or** the lineage group key.
7. **after** **all** normal lineage groups, emit **=1** final `Orphans` section. retain tier **and** numeric ordering inside it, **and** include **every** orphan reason **without** adding a fourth table column.
8. bind the selected structural unit, exact complete-graph Atom source frontier, generator version, configuration, source digests, **and** `updated_at`; replace `stg_requirements_lineage_sections.md` atomically **in** that structural-unit root, record the completed Work Journal event, **and** prove byte-stable semantic output from the same frontier **before** reporting it current.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-147-TOOLS-CORE-METHOD--generate-current-active-atom-snapshot.md

SHA-256: f520c60a8847609640188357973fbe5fc34d6731b4487e5d7443723903a888b9

```markdown
---
subjects:
  governs: "projection-pipeline"
  depends_on: []
version: 12
updated_at: 2026-08-30 16:44:07 +0400
llm_session_ids:
  - codex:019fc24e-24ed-7921-b4db-cf4df3e14bf7
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  method_for:
    - CA-R-1060
    - CA-R-1061
    - CA-R-1062
---
# Generate current active Atom snapshot

generate the current active Atom snapshot through this procedure:

1. resolve the complete current project structural topology **and** canonical Type registry, enumerate Atom carriers through the canonical address resolver, **and** derive active state from **every** Type's registered lifecycle placement rather than from frontmatter, filename text, **or** filesystem timestamps.
2. assign **every** active Atom **=1** canonical Type, one structural level, **and** one structural unit. fail closed on an unknown, ambiguous, malformed, duplicated, **or** topologically unregistered carrier instead of omitting **or** double-counting it.
3. compute one grand total **and** three complete independent rollups: active Atoms by canonical Type, by structural level, **and** by structural unit. emit **every** registered dimension member, including members with a zero count, **and** require **every** rollup **to** sum **to** the grand total.
4. bind the output **to** `<project-control-root>/biz_atoms_current_snapshot.md` **and** emit the declared source frontier **and** as-of timestamp followed by `Total`, `By Type`, `By structural level`, **and** `By structural unit` sections with stably ordered rows **and** integer `active_atom_count` values.
5. bind the exact carrier frontier, lifecycle **and** topology configuration, generator version, source digests, **and** `updated_at`; replace the Projection atomically **and** record the completed rebuild through the Work Journal.
6. regenerate from the same frontier **and** configuration **and** require byte-stable semantic output **before** reporting the snapshot current.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-148-TOOLS-CORE-METHOD--generate-active-atom-history.md

SHA-256: ce95dc9f9ac0317082b5f0bfd734ccc07fe0b139ccfd59f6587ab649f4b2f093

```markdown
---
subjects:
  governs: "projection-pipeline"
  depends_on: []
version: 12
updated_at: 2026-08-30 16:44:07 +0400
llm_session_ids:
  - codex:019fc24e-24ed-7921-b4db-cf4df3e14bf7
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  method_for:
    - CA-R-1062
    - CA-R-1069
---
# Generate active Atom history

generate the active Atom history through this procedure:

1. resolve the configured Artifact timestamp timezone **and** the authoritative first-parent Git revision frontier. use calendar dates **in** that timezone; never use carrier filesystem creation **or** modification times as historical evidence.
2. for **every** calendar date from the first authoritative revision through the requested end date, select the last authoritative revision at **or** **before** that date's end **and** carry the preceding revision forward across dates **without** a new revision.
3. at **every** selected revision, resolve the structural topology, Type registry, canonical Atom addresses, **and** registered lifecycle placement from that revision. count **every** active Atom exactly once **and** fail closed **when** the historical revision cannot be interpreted **without** a declared compatibility rule.
4. for **every** reporting date compute one grand total **and** complete independent rollups by canonical Type, structural level, **and** structural unit. emit registered zero-count members **and** require **every** rollup for that date **to** sum **to** its grand total.
5. bind the output **to** `<project-control-root>/biz_atoms_active_history.md` **and** emit one stably ordered long-form table with `date`, `dimension`, `member`, **and** `active_atom_count`, **where** `dimension` is exactly `total`, `type`, `structural_level`, **or** `structural_unit`.
6. bind the Git frontier, reporting range, timezone, historical compatibility configuration, generator version, **and** source digests; replace the Projection atomically, record the completed rebuild through the Work Journal, **and** require byte-stable semantic output from the same frontier **before** reporting the history current.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-149-TOOLS-CORE-METHOD--generate-the-project-scope-unit-graph-from-configuration-authority.md

SHA-256: 1b0d6fd619efc8d6e45600c83e69ec40dd69807a1a36049929bdd295b92d4cfb

```markdown
---
subjects:
  governs: "Project Scope Unit Graph Projection"
  depends_on:
    - "Project Structure"
    - "Project Settings"
    - "Framework Instance Settings"
    - "Scope Unit"
    - "Atom"
version: 14
updated_at: "2026-09-15 21:31:49 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  method_for:
    - CA-R-1070
---
# Generate the Project Scope Unit Graph from Configuration Authority

**to** generate the Project Scope Unit Graph **and** Sources Projections:

- use the owning Project's authoritative Project Structure Artifact as the sole source of accepted Scope Unit declarations **and** concrete bindings.
- use Project Settings for Project identity **and** Framework Instance Settings for selected framework behavior, under their governing authority.
- preserve the distinction between accepted declarations, Atom Claims, Directory Carrier observations, **and** Journal evidence.
- derive the generated views deterministically from the selected source revisions **without** using previous generated views as authority **or** writing accepted declarations.
- keep Goal coverage, folder materialization, undeclared folders, **and** declaration mismatches visible as separate observations.
- **if** the required authoritative input is missing, invalid, **or** cannot be read completely, report incomplete coverage **and** do **not** claim a complete accepted Project Structure.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-182-TOOLS-METHOD--design-asynchronous-commit-provenance-tool-topology.md

SHA-256: 3b27829f3897e3504647ee70591706bf30f9367608e61e6c6edf7533fb7f4924

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "artifact-operations"
  depends_on: []
version: 10
updated_at: 2026-09-04 03:10:59 +0400
relations:
  method_for:
    - CA-R-802
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Design asynchronous commit-provenance Tool topology

## Applicable when

apply **when** a Tool chain **must** accept work **without** blocking its host **and** **must** survive interruption, backpressure, retry, **or** service replacement.

## Procedure

1. give the chain one deterministic I/O-free manager. supply repository, queue, action, worker-result, settings, lease, circuit, **and** clock facts as explicit typed inputs; return one complete typed execution graph **or** one admissible next command.
2. resolve the current COMMIT_AUTOMATION autonomy envelope **before** admitting work. fail closed **unless** the repository, subject scope, time window, action class, queue **and** resource caps, **and** Work binding are current **and** the action class is a local real-change commit **or** local Journal-only commit.
3. persist the immutable graph, resolved envelope identity, **and** **every** transition under .caprmedio_runtime. give **every** step a stable action **and** step identity, typed input **and** output contracts, declared dependencies, bounded retry routes, **and** terminal outcomes.
4. let a mechanical Scheduler claim **only** ready steps **and** advance **only** manager-declared transitions. a completion **may** make one declared step ready but **may** **not** select, reorder, skip, **or** invent downstream work. enforce pause, resume, narrowing, expiry, **and** circuit state **before** dispatch **and** again **before** **every** effect.
5. give **every** worker one atomic mechanical operation. isolate filesystem, process, clock, environment, logging, **and** persistence effects **in** workers **or** adapters. the actor that authorizes **or** overrides an envelope **must not** be the worker that executes its commit effect.
6. use a direct typed handoff **only** for short synchronous work that needs no independent recovery. use durable scheduling **when** work **must** survive interruption, wait, apply backpressure, **or** retry independently.
7. use idempotency for repeatable effects **and** an exclusive lease **or** compare-and-set boundary for non-repeatable effects. record attempts, leases, input **and** result digests, completion identities, diagnostics, **and** admissible recovery transitions.

## Outcome

the manager owns **every** business decision, the Scheduler advances the accepted graph **without** semantic discretion, workers remain atomic **and** non-deciding, **and** queued work survives manager **or** service termination.

## Failure or stop

reject undeclared cycles **or** transitions. stop autonomous execution **when** state, authority, Work binding, envelope, cap, lease integrity, **or** the next admissible transition is absent, ambiguous, stale, exceeded, **or** invalid. recovery **may** resume **only** under the same still-current envelope **or** a narrower **or** independently authorized replacement.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-200-TOOLS-METHOD--reconcile-git-and-journal-provenance-bidirectionally.md

SHA-256: ef1d3e443a488c0056cdea41ee9ec16142a356eb9f75649920b6c7be46a66f78

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "programmatic-mutation"
  depends_on: []
version: 7
updated_at: 2026-09-01 23:47:24 +0400
relations:
  method_for:
    - CA-R-1120
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reconcile Git and Journal provenance bidirectionally

## Applicable when

use this Method **when** comparing reachable Git change history with Work Journal coverage for the same governed action frontier.

## Procedure

1. seal a reachable Git frontier **and** the corresponding Journal batch frontier.
2. normalize both sides **to** action, Initiative, commit SHA, event ID, subject path, subject revision, digest, batch SHA, **and** ordering facts.
3. match Git real-change commits **to** Journal events **in** both directions **and** classify missing, duplicate, unreachable, digest-mismatched, revision-mismatched, **and** watermark-lag cases.
4. append a recovered Journal event **only** **when** reachable history **and** sealed durable state prove **every** required field; **otherwise** keep the case blocked.
5. re-run the comparison over the same frontier **and** emit a stable reconciliation report whose second unchanged run produces no new events.

## Outcome

Git **and** Journal provenance are either reconciled idempotently **or** separated into explicit evidence-backed discrepancy classes.

## Failure or stop

do **not** infer missing provenance **or** rewrite Git history; stop recovery whenever required identity, digest, reachability, **or** batch evidence is insufficient.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-201-TOOLS-CORE-METHOD--normalize-portable-repository-text-bytes.md

SHA-256: 12a4f0eaec8fa64691f46e87587dfd567f17e46fbb28a34ad461a3912641fdf7

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "artifact-operations"
  depends_on: []
version: 7
updated_at: 2026-09-01 23:47:24 +0400
relations:
  method_for:
    - CA-R-1122
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Normalize portable repository text bytes

## Applicable when

use this Method **when** governed repository text **must** have stable bytes across supported operating systems **and** tools.

## Procedure

1. read the repository-owned normalization policy **and** resolve the selected tracked text files **without** using host defaults as authority.
2. detect encoding, byte-order marks, line endings, final-newline state, **and** disallowed control bytes.
3. produce an exact dry-run of byte changes using the canonical encoding **and** newline rules.
4. on authorized apply, rewrite **only** files whose bytes differ **and** preserve **all** semantic text.
5. re-read **every** changed file **and** prove that a second normalization pass is byte-idempotent.

## Outcome

selected repository text has one policy-derived portable byte representation **and** remains unchanged on repeated normalization.

## Failure or stop

stop on undecodable input, an unsupported file class, missing policy, **or** a transformation that would change semantic text.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-202-TOOLS-METHOD--validate-the-governed-routing-tree.md

SHA-256: ac2969be2b0be78b826dead9940811e7227f4aba21b491343d6f1f6aa8d7ca8b

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "artifact-operations"
  depends_on: []
version: 7
updated_at: 2026-09-01 23:47:24 +0400
relations:
  method_for:
    - CA-R-1123
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Validate the governed routing tree

## Applicable when

use this Method **before** a governed router selects **or** traverses a route **in** the current routing tree.

## Procedure

1. load the current routing-tree authority **and** its declared node, edge, root, leaf, priority, **and** fallback constraints.
2. resolve **every** referenced target against the current active graph **without** following derived inverse relations as authored edges.
3. check root uniqueness, reachability, permitted edge types, cycle rules, selector exclusivity, fallback completeness, **and** terminal-route validity.
4. emit one stable issue per violated constraint with source carrier **and** exact route location.
5. permit routing **only** **when** the selected tree frontier has no blocking issue.

## Outcome

routing receives a deterministic valid verdict **or** an attributable set of structural violations **before** **any** route is used.

## Failure or stop

treat unreadable authority, unresolved targets, ambiguous roots, **and** stale frontiers as blocking validation failures.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-203-TOOLS-METHOD--bind-one-deterministic-script-to-one-tool.md

SHA-256: b3a42fc8731b802ccce0dfaf275fb25b7710944b9ce8326742bd58ca202780fd

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "artifact-operations"
  depends_on: []
version: 10
updated_at: 2026-09-02 00:15:00 +0400
relations:
  method_for:
    - CA-R-1124
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Bind one deterministic script to one Tool

## Applicable when

use this Method **when** admitting **or** reviewing an independently executable deterministic script, including one invoked exclusively by a Skill.

## Procedure

1. select the active Tool Scope Units **and** independently executable deterministic entry scripts within one declared frontier.
2. resolve **every** script's declared Tool identity **and** **every** Tool's canonical entrypoint from their owning authority carriers; include entrypoints invoked **only** through a Skill.
3. compare the two sets **and** require one exact Tool-to-entrypoint binding **in** **every** direction.
4. classify imported modules, workers, **and** shared libraries that are **not** independently executable as implementation support, even **when** several Tools call them.
5. report **every** missing, duplicate, cross-boundary, **or** orphan binding with the Tool identity **and** both relevant paths.

## Outcome

**every** independently executable deterministic script has **=1** Tool owner, **and** **every** Tool has **=1** canonical executable entrypoint.

## Failure or stop

do **not** infer ownership from directory proximity, import topology, **or** invocation by a Skill; treat ambiguous **or** multi-owner bindings as blocking findings.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-204-TOOLS-METHOD--validate-generated-data-stage-pipelines.md

SHA-256: 95cc78ea952c87abe096d10e232c1eb98a46beb2cbb7d55e87f14ad09de51b4c

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "artifact-operations"
  depends_on: []
version: 9
updated_at: 2026-09-02 00:15:00 +0400
relations:
  method_for:
    - CA-R-1125
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Validate generated data-stage pipelines

## Applicable when

use this Method **when** validating a registered generated-data pipeline from source carriers through derived stages.

## Procedure

1. load the registered `src`, `stg`, `mrt`, **and** `biz` stage declarations, their declared dependencies, **and** their materializations.
2. resolve the authoritative source frontier for **every** declared generated output.
3. check that **every** stage uses one registered prefix, **every** dependency advances from `src` toward `biz`, **and** no generated output becomes semantic authority.
4. compare **every** materialization's recorded input frontier with the current declared source frontier.
5. report **every** unregistered prefix, non-forward dependency, missing source frontier, stale materialization, **and** independently authored derived fact with its exact carrier.

## Outcome

the pipeline has an attributable `src → stg → mrt → biz` topology with current source-derived materializations, **or** explicit blocking violations.

## Failure or stop

block acceptance **when** a stage uses an unregistered prefix, lacks a source frontier, depends non-forward, claims semantic authority, **or** cannot prove currentness.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-205-TOOLS-METHOD--reconcile-work-journal-coverage-from-sealed-evidence.md

SHA-256: bb0f06201d20d24192c08e9f007f9ff6ff09b23c1bcfbecb10a4730d9145f50e

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "programmatic-mutation"
  depends_on: []
version: 9
updated_at: 2026-09-02 00:15:00 +0400
relations:
  method_for:
    - CA-R-1127
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reconcile Work Journal coverage from sealed evidence

## Applicable when

use this Method **when** a governed action **may** be missing required Work Journal coverage.

## Procedure

1. seal one governed action frontier **and** collect its action identity, authoritative state, reachable provenance, existing Journal events, **and** the active Journal-event schema.
2. determine whether the existing events provide the coverage required for that exact action.
3. classify absent, duplicate, partial, stale, **or** conflicting coverage **without** editing existing Journal lines.
4. append one `recovered` event **only** **when** sealed durable evidence determines **every** schema-required event field **and** its action binding unambiguously.
5. re-run the same reconciliation on the unchanged frontier **and** confirm that it appends no second recovered event.

## Outcome

**every** selected governed action has an explicit coverage state: covered, recovered from sufficient evidence, **or** blocked for operator resolution.

## Failure or stop

never invent a schema-required event fact, action binding, **or** provenance fact; preserve insufficient cases as blocked.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-206-TOOLS-METHOD--project-bounded-work-journal-ndjson-to-toon.md

SHA-256: 84c3c4fb7ec616be246c9a059709b4d72fe00aca34782121165e09a3084cf742

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "journal-projection"
  depends_on: []
version: 8
updated_at: 2026-09-02 00:25:00 +0400
relations:
  method_for:
    - CA-R-1128
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Project bounded Work Journal NDJSON to TOON

## Applicable when

use this Method **when** a bounded Work Journal frontier **must** be represented as a compact TOON Projection.

## Procedure

1. resolve an exact Journal file, event range, **or** sealed event frontier **and** record its ordered source identities **and** digests.
2. parse **every** NDJSON line strictly **and** reject malformed, duplicate, **or** changed input **before** projection.
3. encode the same ordered event values into TOON **without** adding authority, interpretation, **or** omitted fields.
4. attach the source frontier, encoder identity **and** version, **and** output digest **to** the Projection metadata.
5. decode **or** independently compare the result **to** prove lossless identity, value, **and** order preservation.

## Outcome

one reproducible non-authoritative TOON Projection represents the exact bounded Journal frontier losslessly.

## Failure or stop

produce no Projection **when** the frontier changes during generation, **any** line is malformed, **or** the result cannot be proven lossless.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-207-TOOLS-METHOD--read-generic-artifact-metadata.md

SHA-256: c8ea68907b529a8e007c7df33f586bc8aa467844eeccb6b0739bdcfd378e07b3

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "artifact-operations"
  depends_on: []
version: 9
updated_at: 2026-09-02 00:25:00 +0400
relations:
  method_for:
    - CA-R-1129
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Read generic Artifact metadata

## Applicable when

use this Method **when** framework internals need selected frontmatter **and** derived identity for **=1** generic Artifact.

## Procedure

1. resolve **=1** generic Artifact carrier from the caller-supplied carrier identity **or** path, **without** applying CAPRMEDIO Atom selector semantics.
2. seal its path, filename, **and** source digest, **then** parse **only** its frontmatter **without** loading its body.
3. return the requested registered fields **and** carrier-derived identity; represent **every** absent field **and** **every** parse error explicitly.
4. mark the result as a form-agnostic helper result **and** retain the source identity **and** digest needed **to** attribute it.
5. return no mutation plan **and** do **not** expose this helper as a public substitute for `ATOM_READ`.

## Outcome

callers receive an attributable body-free metadata result for **=1** generic Artifact carrier.

## Failure or stop

return an explicit result for an absent carrier, ambiguous identity, unsupported field, **or** malformed frontmatter **without** mutation.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-208-TOOLS-METHOD--patch-generic-artifact-metadata.md

SHA-256: 90ac8ff3432003f2d0a7ca5fde684b9c03f19402abb664c4c29cd5b2243274d4

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "artifact-operations"
  depends_on: []
version: 9
updated_at: 2026-09-02 00:25:00 +0400
relations:
  method_for:
    - CA-R-1130
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Patch generic Artifact metadata

## Applicable when

use this Method **when** a governed Tool needs the shared mechanics for a field-level frontmatter patch on one generic Artifact.

## Procedure

1. resolve **=1** generic Artifact **and** seal its path, revision, digest, schema, current frontmatter, **and** body digest.
2. apply **only** declared add, replace, **or** remove operations **to** registered frontmatter fields.
3. validate the resulting complete frontmatter document **and** reject unknown fields, failed preconditions, **and** **all** relation-target operations.
4. produce the exact field-level dry-run while preserving the original body bytes **and** carrier identity.
5. on authorized apply, recheck the sealed preconditions, atomically replace the carrier, advance governed revision metadata once, **and** prove the unchanged body digest.

## Outcome

the Artifact receives one schema-valid metadata revision while its body **and** identity remain unchanged.

## Failure or stop

stop **or** roll back on stale preconditions, unknown fields, schema failure, failed body preservation, **or** **any** requested relation patch.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-209-TOOLS-METHOD--create-one-generic-artifact-carrier.md

SHA-256: 9864e9b43452b1317e20dd61dc94e9f71ed558d92f7d673b8f0427326a5abddc

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "artifact-operations"
  depends_on:
    - "Artifact"
    - "Artifact/Carrier"
    - "Atom/Content Role"
version: 8
updated_at: "2026-09-17 20:26:41 +0000"
relations:
  method_for:
    - CA-R-1132
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Create one generic Artifact carrier

## Applicable when

use this Method **when** a canonical Tool delegates generic construction of **=1** non-Atom Artifact Carrier under its admitted schema.

## Procedure

1. accept the structural owner **and** **all** inputs required by the admitted Artifact Carrier schema.
2. derive the canonical identity, filename, **and** owner-relative destination required by that schema **and** its active Carrier rules.
3. preflight the resolved destination **and** identity against existing carriers **and** reject **every** collision **or** implicit overwrite.
4. build the Carrier from the supplied schema-valid inputs, preserving the derivation inputs **in** the dry-run result.
5. on authorized apply, create exactly the derived Carrier **and** verify its required identity, placement, complete schema-valid content, **and** Carrier digest.

## Outcome

**=1** generic Artifact Carrier is created with the identity, placement, **and** content required by its admitted schema, **or** the repository remains unchanged.

## Failure or stop

reject an absent structural owner **or** schema-required input, invalid derivation, collisions, **and** requests that treat this helper as a public alternative **to** `ATOM_CREATE`. Content Role, title, **and** body **must not** be required universally merely because Markdown Atoms use them.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-210-TOOLS-METHOD--plan-one-generic-artifact-migration.md

SHA-256: c84520439a18051d1ab247fae18ae6c6b52ed34428bab41a2398a8c2257cbb4f

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "artifact-migration"
  depends_on: []
version: 8
updated_at: 2026-09-02 00:25:00 +0400
relations:
  method_for:
    - CA-R-1138
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Plan one generic Artifact migration

## Applicable when

use this Method **when** a declared generic Artifact transformation **must** be expanded into a reviewable read-only migration plan.

## Procedure

1. accept one declared transformation rule **and** bounded source frontier **in** read-only mode.
2. resolve **every** source carrier **and** derive its preconditions, old-to-new identity mapping, collision checks, required reference rewrites, affected Projections, **and** expected postconditions.
3. record the source frontier identities, revisions **or** digests, transformation inputs, **and** complete derived effect set **in** a stable order.
4. mark the result as a plan **only**: it grants neither approval nor mutation authority.
5. return explicit unresolved, ambiguous, **and** collision findings rather than omitting affected carriers **or** effects.

## Outcome

one reviewable migration plan describes the complete expected transformation of the declared unchanged source frontier **without** mutating it.

## Failure or stop

do **not** mutate **any** carrier, reference, Projection, **or** Journal; stop on an invalid transformation, unresolved source, ambiguous mapping, **or** collision.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-211-TOOLS-METHOD--generate-one-generic-artifact-catalog.md

SHA-256: 15727881fd9d0f42a9b5ae3ba1003820e51d21a059ac2dd89837320f2243efb6

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "artifact-catalog"
  depends_on: []
version: 8
updated_at: 2026-09-02 00:25:00 +0400
relations:
  method_for:
    - CA-R-1141
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Generate one generic Artifact catalog

## Applicable when

use this Method **when** one registered Artifact catalog **must** be materialized from its declared authoritative source frontier.

## Procedure

1. resolve the registered catalog definition, declared authoritative source frontier, selected fields, ordering rule, **and** output carrier.
2. read **every** declared source contribution **and** materialize the catalog **in** the declared stable order **without** adding independently authored facts.
3. attach the exact source frontier **and** generator identity **to** the derived output.
4. repeat generation against an unchanged frontier **and** require identical derived output.
5. return the materialized catalog as a non-authoritative Projection; do **not** decide **or** repair catalog currentness here.

## Outcome

the catalog is a deterministic non-authoritative Projection of its declared source frontier with stable ordering **and** explicit provenance.

## Failure or stop

do **not** materialize a catalog with unresolved declared sources, missing definition fields, unstable ordering, **or** generator-added meaning.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-212-TOOLS-METHOD--patch-project-settings-with-generated-value-protection.md

SHA-256: 05c8e1169de8035e08fc895912eb17d8bfb6eaf362f061730af0ed38eaac8448

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "project-settings"
  depends_on: []
version: 8
updated_at: 2026-09-02 00:25:00 +0400
relations:
  method_for:
    - CA-R-1143
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Patch Project Settings with generated-value protection

## Applicable when

use this Method **when** a caller supplies a bounded key-level patch for the canonical Project Settings carrier.

## Procedure

1. resolve the single canonical Project Settings carrier, its schema, current digest, **and** the requested key-level patch.
2. classify **every** target key from the settings schema as editable, generated, **or** unknown.
3. reject writes **to** generated **or** unknown values **and** preserve **all** unrelated settings exactly.
4. validate the complete resulting settings document **and** expose the exact key-level **and** byte-level dry-run.
5. on authorized apply, recheck the source digest, replace the carrier atomically, **and** prove that **only** approved keys changed.

## Outcome

Project Settings contain exactly the approved schema-valid changes while generated **and** unrelated values remain untouched.

## Failure or stop

stop on multiple settings carriers, schema failure, stale input, generated **or** unknown targets, **or** **any** undeclared diff.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-213-TOOLS-METHOD--capture-one-external-source.md

SHA-256: f87185fed7c3a0014650114a588d63f2dce40207dffc8c052bd7f7a37998d1ff

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "provenance"
  depends_on: []
version: 9
updated_at: 2026-09-02 00:25:00 +0400
relations:
  method_for:
    - CA-R-1144
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Capture one external source

## Applicable when

use this Method **when** one external page, post, video transcript, **or** supplied text **must** be retained as an immutable source carrier.

## Procedure

1. receive one external page, post, video transcript, **or** supplied text **and** capture the exact retrieved content.
2. record its origin, retrieval time, attribution, content digest, **and** explicit reproducibility result.
3. allocate one immutable source-carrier identity **and** bind the captured bytes **to** that identity **and** digest.
4. **when** reproducibility cannot be established, record that factual outcome explicitly **without** inventing a reproduction claim.
5. return the immutable carrier **and** provenance record **without** importing analysis **or** changing project authority.

## Outcome

one immutable external source carrier preserves exact source bytes **and** declared provenance, including a truthful reproducibility outcome.

## Failure or stop

stop **when** origin, retrieval time, attribution, **or** content digest cannot be recorded; never invent provenance **or** alter captured source bytes.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-214-TOOLS-METHOD--record-one-verified-release-outcome.md

SHA-256: 7cee9ddcca8b90df21d7f4237c0e3c35f4221bcf984fa73eb890526a8b47f934

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "release"
  depends_on:
    - "Journal/Record"
    - "Artifact/Revision"
version: 12
updated_at: "2026-09-17 20:09:12 +0000"
relations:
  method_for:
    - CA-R-1147
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Record one verified release outcome

## Applicable when

use this Method **after** one release attempt has a sealed factual outcome **and** attributable verification evidence.

## Procedure

1. seal one release-attempt identity with its attempted version, release revision **or** commit, manifest, verification results, Work Journal event, actor, **and** completion time.
2. determine success **only** from the declared release acceptance criteria **and** their attributable evidence.
3. for success, record the verified release success **in** one immutable Journal Record binding the version, exact revisions, checks, evidence, Journal, **and** canonical Git identity.
4. for a failed attempt established by its declared acceptance criteria **and** attributable evidence, record the failed non-release attempt **in** Journal Records that bind the same attempted version, exact revision, checks, **and** Work Journal event as the attempt **and** preserves the version as unreleased.
5. reject duplicate **or** conflicting outcomes for the same release-attempt identity.

## Outcome

a successful release has one immutable Journal Record of verified success; an evidenced failed attempt has explicitly bound Journal evidence of a failed non-release attempt **and** never becomes a release claim.

## Failure or stop

do **not** infer success from intent, partial checks, **or** an unsealed manifest; stop on missing evidence **or** conflicting release identity. missing verification **must not** be treated as evidence that the release attempt failed; retain the observed missing-evidence fact **without** inventing an outcome.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-215-TOOLS-METHOD--persist-one-operator-accepted-deferred-plan.md

SHA-256: 82c786a820a430be49b38616d13f25a39ef5995a6b3e4484bd350b8c5911ec68

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "plan-lifecycle"
  depends_on: []
version: 8
updated_at: 2026-09-02 00:25:00 +0400
relations:
  method_for:
    - CA-R-1148
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Persist one operator-accepted deferred Plan

## Applicable when

use this Method **when** the operator explicitly accepts postponing one bounded intended action for later reopening.

## Procedure

1. capture the operator's explicit acceptance, bounded deferred work, current session, owning scope, rationale, dependencies, **and** reopening condition.
2. distinguish the accepted deferral from a suggestion, unrecorded intention, **or** already authorized active Task.
3. validate that the deferred work, scope, dependency, **and** reopening references are complete **and** resolve.
4. create **or** update the deferred Plan Atom with no implementation **or** completion claim.
5. return its stable identity **and** reopening condition **to** the operator **and** relevant queues.

## Outcome

one operator-accepted deferred work item is preserved as an attributable Plan that can be reopened **without** pretending it is active **or** done.

## Failure or stop

do **not** persist a mere suggestion **or** infer acceptance; stop **when** deferred work, scope, rationale, dependency, **or** reopening boundary is ambiguous.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-216-TOOLS-METHOD--extract-one-extension-candidate-from-project-adaptation.md

SHA-256: 7558dfc61d5574559cb6161897a0e7773392eaa356f482231e0af30671e16427

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "extension-promotion"
  depends_on: []
version: 9
updated_at: 2026-09-02 00:25:00 +0400
relations:
  method_for:
    - CA-R-1149
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Extract one Extension candidate from Project Adaptation

## Applicable when

use this Method **when** an operator selects reusable Project Adaptation authority for extraction as one Extension candidate.

## Procedure

1. seal the operator-selected adaptation Atoms **and** resolve their direct dependency closure across current active authority.
2. traverse declared required dependencies **to** the complete closure **and** preserve **every** selected **and** transitively required source Atom reference exactly.
3. reject the extraction **when** **any** required dependency is absent, ambiguous, **or** unresolved; do **not** omit it **or** infer a replacement.
4. assign the candidate its own stable identity **and** preserve the exact selected membership, transitive closure, source revisions, **and** frontier digest.
5. emit the bounded candidate **without** modifying its source Project Adaptation authority.

## Outcome

one independently identified Extension candidate **contains** the selected Project Adaptation authority **and** its complete attributable required dependency closure.

## Failure or stop

stop on unresolved required dependencies, stale source revisions, ambiguous closure, **or** a candidate boundary that cannot be attributed exactly.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-218-TOOLS-METHOD--resolve-github-extension-source.md

SHA-256: ad105a34e3cd819078e73819005ab167ff4bd2f06114445a1b4cff2c2ad602d3

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "extension-packaging"
  depends_on: []
version: 8
updated_at: 2026-09-02 00:25:00 +0400
relations:
  method_for:
    - CA-R-1151
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Resolve GitHub Extension source

## Applicable when

use this Method **when** determining the declared GitHub source boundary for one Extension package.

## Procedure

1. resolve the declared GitHub repository for one Extension **and** determine whether its package root is the complete repository **or** one declared directory.
2. normalize the repository identity **and** optional declared directory **without** inventing an implicit subdirectory **or** alternate source provider.
3. retrieve the source boundary **and** report the declared repository **and** package-root path as attributable source metadata.
4. reject a missing repository, undeclared subdirectory, **or** source boundary that cannot be mapped **to** the Extension package.
5. return source-resolution facts **only**; do **not** choose an installed version **or** change installed Extension state.

## Outcome

one Extension has an exact attributable GitHub repository source boundary **and** either its complete repository **or** one declared package-root directory.

## Failure or stop

stop on an ambiguous repository, undeclared package root, missing source boundary, **or** an attempt **to** manage installed state.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-219-TOOLS-METHOD--resolve-one-target-set.md

SHA-256: 9c511b07b8a02b1486f1a38307e0e689a15d2e1ac36aa00ce4573b6d85fd7635

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "feature-boundary"
  depends_on: []
version: 11
updated_at: 2026-09-04 03:10:59 +0400
relations:
  method_for:
    - CA-R-1153
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Resolve one target set

## Applicable when

use this Method **when** `TARGET_SET` **must** resolve identities **or** governed selectors **before** another Tool checks **or** changes the targets.

## Procedure

1. confirm that `TARGET_SET` is registered as one `unordered_unit` Finder owned immediately by `TOOLS` at Structural level `4`, with prefix `TARGET_SET`, address `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/TARGET_SET`, **and** realization path `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/TARGET_SET/`.
2. resolve the supplied explicit identities **and** composable governed selectors against the current project frontier.
3. deduplicate the resolved members **and** order them by the registered stable ordering rule.
4. seal membership, source frontier, **and** content digest together as one target-set identity.
5. return the sealed set read-only **to** a named downstream Tool **without** evaluating **or** changing **any** target; reject an invalid unit boundary, unresolved selector, ambiguous identity, missing member, **or** changed frontier.

## Outcome

one `TARGET_SET` result **contains** exactly its stable ordered membership, source frontier, **and** content digest for downstream checking **or** change.

## Failure or stop

do **not** mutate targets, execute Evaluations, create change plans, **or** rebuild Projections; return an explicit unresolved **or** stale result instead.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-220-TOOLS-CORE-METHOD--register-executable-tool-folders-as-active-tool-units.md

SHA-256: 4d51bc66cf2c285dce9cb7f4537142bae4488d4b947874d3c8a61b84be638079

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "feature-boundary"
  depends_on:
    - "Project Structure"
    - "Scope Unit"
    - "Operator"
    - "Artifact/Carrier"
version: 7
updated_at: "2026-09-17 20:36:34 +0000"
relations:
  method_for:
    - CA-R-1163
    - CA-R-1164
    - CA-R-1165
    - CA-R-1166
    - CA-R-1167
    - CA-R-1168
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Register executable Tool folders as active Tool units

## Applicable when

apply **when** an immediate native TOOLS folder has a canonical independently executable deterministic Tool candidate **and** its Scope Unit registration needs reconciliation.

## Procedure

1. resolve the owning Project's authoritative Project Structure declarations, the observed immediate native Tool folders, **and** their canonical executable entrypoints. keep accepted declarations separate from observed materialization.
2. exclude shared libraries, caches, tests, migration collections, **and** other folders that do **not** own a canonical independently executable Tool.
3. resolve **=1** accepted immediate TOOLS child declaration for **every** Tool proposed for admission. **if** the declaration is missing **or** requires correction, obtain explicit per-action Operator acceptance **or** valid delegated authority under CA-R-1058 **before** changing Project Structure. preserve the accepted Name, direct parent, Type, Label, applicable order, navigation number, **and** authority/Implementation Folder bindings required by CA-R-1484. a folder observation alone **must not** authorize those values.
4. verify the declaration against the canonical executable **and** matching authority/Implementation Folder bindings under CA-R-1163. resolve the filename token required by applicable Carrier authority **without** independently redefining structural facts **in** an Atom **or** generated graph. a declared but unmaterialized Tool remains declared; do **not** report it as executable **or** available for MCP exposure.
5. treat an admitted Tool as active **unless** current Project authority **or** Configuration explicitly disables it. allow MCP **to** derive exposure **only** from the current valid Tool frontier.

## Outcome

**every** admitted immediate executable Tool folder has **=1** accepted Tool Scope Unit declaration **and** **=1** deterministic MCP-discoverable identity **without** turning infrastructure folders **or** observed files into structural authority.

## Failure or stop

stop admission on unreadable **or** invalid Project Structure, absent required authorization, a missing **or** ambiguous declaration, no unique canonical executable entrypoint, conflicting Tool identity, invalid authority/Implementation Folder binding, **or** ambiguous enablement. report missing materialization separately; do **not** silently invent a declaration **or** publish an incomplete frontier as current.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-223-TOOLS-CORE-METHOD--bind-tool-effect-results-to-the-canonical-operation.md

SHA-256: 1bcc3b53e738dbad582122fa9137e78738214c068be67fb93adb6500f6bb6251

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "tool-effect-result"
  depends_on:
    - "TOOLS"
version: 10
updated_at: 2026-08-27 14:52:39 +0400
relations:
  method_for:
    - CA-R-1186
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Bind Tool effect results to the canonical operation

bind **every** Tool effect request **and** result **to** the canonical operation that
authorized it.

## Applicable when

apply **after** the shared PROGRAMMATIC file-and-subprocess Method (`CA-M-161`)
admits an effect for one Tool operation.

## Procedure

1. resolve the canonical operation identity **and** its sealed target **or** explicit
   argument contract **before** applying an effect.
2. bind **every** admitted effect request **and** returned receipt **to** that operation.
3. preserve the operation identity through failure, recovery, **and** retry.
4. return the Tool's declared structured outcome **without** selecting a separate
   file, subprocess, platform, **or** MCP policy.

## Outcome

**every** Tool effect **and** receipt remains attributable **to** one canonical operation
**and** recoverable **without** reconstructing authority from incidental runtime state.

## Failure or stop

stop **when** the operation identity, sealed target, argument contract, **or** effect
receipt is missing, ambiguous, stale, **or** inconsistent with the Tool outcome.

## Sources

- [Python documentation: subprocess security considerations](https://docs.python.org/3.14/library/subprocess.html#security-considerations)
- [Python documentation: tempfile](https://docs.python.org/3.14/library/tempfile.html)
- [Python documentation: os.replace](https://docs.python.org/3.14/library/os.html#os.replace)
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-253-TOOLS-METHOD--check-one-target-set-against-registered-evaluations.md

SHA-256: 50099f91e7f87b77c6b0b974fef44c4cb174a49104a88b4832c35da63f39ef04

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "feature-boundary"
  depends_on: []
version: 9
updated_at: 2026-09-04 03:10:59 +0400
relations:
  method_for:
    - CA-R-1154
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Check one target set against registered Evaluations

## Applicable when

use this Method **when** `GRAPH_CHECK` **must** apply selected registered Evaluation criteria **to** one previously sealed target set.

## Procedure

1. confirm that `GRAPH_CHECK` is registered as one `unordered_unit` Checker owned immediately by `TOOLS` at Structural level `4`, with prefix `GRAPH_CHECK`, address `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GRAPH_CHECK`, **and** realization path `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GRAPH_CHECK/`.
2. resolve one sealed target-set identity **and** selected registered Evaluation criteria.
3. confirm that the target set retains its recorded membership, source frontier, **and** digest **before** beginning evaluation.
4. apply **every** selected criterion **to** **every** applicable target **and** retain attributable issue, evidence, **and** verdict records **in** deterministic target-and-criterion order.
5. distinguish satisfied, unsatisfied, inapplicable, blocked, **and** error verdicts, **and** return the complete result **without** changing governed Atoms, Journals, native Implementation, **or** derived outputs.

## Outcome

one read-only `GRAPH_CHECK` result provides stable attributable issues, evidence, **and** verdicts for the selected registered criteria over one sealed target set.

## Failure or stop

do **not** evaluate a stale **or** unresolved target set **and** do **not** mutate **any** governed carrier; return explicit blocked **or** error verdicts instead.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-254-TOOLS-METHOD--change-one-sealed-target-set.md

SHA-256: 807d73be11abdb0069a0f0fcfcc8396ecf377a61db4f47291725dd4e0b28ca0f

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "feature-boundary"
  depends_on: []
version: 9
updated_at: 2026-09-04 03:10:59 +0400
relations:
  method_for:
    - CA-R-1155
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Change one sealed target set

## Applicable when

use this Method **when** `BULK_CHANGE` **must** compose registered carrier operations over one sealed target set.

## Procedure

1. confirm that `BULK_CHANGE` is registered as one `unordered_unit` Doer owned immediately by `TOOLS` at Structural level `4`, with prefix `BULK_CHANGE`, address `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/BULK_CHANGE`, **and** realization path `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/BULK_CHANGE/`.
2. resolve one sealed target set **and** declared registered create, structured patch, relation change, rename, move, lifecycle, **or** replacement operations.
3. derive a complete mutation-free change plan that identifies **every** target, effect, precondition, collision, reference rewrite, **and** rollback action.
4. require explicit approval of the exact plan digest **and** recheck the target set frontier **and** **every** effect precondition **before** apply.
5. apply **only** the unchanged approved effects as one validated rollbackable transaction, verify **every** declared effect, **and** return the transaction identity, final target frontier, **and** **any** rollback evidence.

## Outcome

one explicitly approved unchanged `BULK_CHANGE` plan changes one sealed target set as a complete validated rollbackable transaction.

## Failure or stop

do **not** mutate **before** an approved complete plan; stop **or** roll back on a stale target set, failed precondition, unplanned effect, collision, **or** failed verification.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-255-TOOLS-METHOD--rebuild-affected-projections.md

SHA-256: d8746dc3e83a33d1150b427edc6758c745dd376e6b20bc1aca21232d5e8c71cf

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "feature-boundary"
  depends_on: []
version: 8
updated_at: 2026-09-04 03:10:59 +0400
relations:
  method_for:
    - CA-R-1156
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Rebuild affected Projections

## Applicable when

use this Method **when** `PROJECTION_REBUILD` **must** refresh Projections affected by declared changed source frontiers.

## Procedure

1. confirm that `PROJECTION_REBUILD` is registered as one `unordered_unit` Doer owned immediately by `TOOLS` at Structural level `4`, with prefix `PROJECTION_REBUILD`, address `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/PROJECTION_REBUILD`, **and** realization path `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/PROJECTION_REBUILD/`.
2. resolve the changed source frontiers **and** derive the complete affected Projection set using declared Projection dependencies.
3. order affected Projections by those dependencies **and** reject an unresolved **or** cyclic dependency order.
4. preview **every** derived output effect, including output identity, source frontier, **and** expected currentness state.
5. materialize **only** the explicitly approved preview outputs **and** attach their source frontier **and** generator provenance; verify currentness **and** idempotence **after** publication by rebuilding against the unchanged frontier **and** comparing the resulting outputs.

## Outcome

one `PROJECTION_REBUILD` operation materializes **every** **and** **only** affected approved Projection **in** dependency order **and** verifies its currentness **and** idempotence.

## Failure or stop

do **not** publish on an unresolved dependency, incomplete affected set, unapproved output, changed source frontier, failed currentness check, **or** failed idempotence check.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-316-TOOLS-METHOD--implement-atom-validation-checks-from-source-authority.md

SHA-256: 7c2c69384283b7bbe2e7345b53d5f6abfc8729f2a67887f37cf529448b1e42c0

```markdown
---
atom_id: CA-M-316
content_role: Method
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Tool/VALIDATE_ATOMS"
  depends_on:
    - "Tool"
    - "Atom"
    - "Atom/Property"
    - "Evaluation"
    - "Workflow"
    - "Step"
    - "Action"
    - "Single Source of Truth"
version: 6
updated_at: "2026-10-01 21:46:55 +0400"
relations:
  method_for:
    - CA-R-1622
    - CA-R-1623
  relates_to:
    - CA-E-506
    - CA-O-087
---
# Summary

Implement Atom validation checks from source authority

## Scope

implementation of Atom validation checks from source authority for `VALIDATE_ATOMS`.

## Claim

**to** implement `VALIDATE_ATOMS`, use source-bound deterministic check adapters rather than an independently maintained methodology dictionary.

- reuse compatible canonical Carrier readers, safe parsers, section extractors, **and** Relation resolvers; repair their limitations under the Tool's tests rather than fork competing interpretations.
- make each check identify the exact governing Atom Revisions **and** supported condition; resolve applicable expansions through declared model inputs rather than a fixed list of this Project's names.
- generate **or** derive reusable machine-readable constraints from source declarations **where** supported. a hand-written adapter **must** retain its authority binding **and** tests; changed **or** unsupported authority is a visible coverage gap, **not** permission **to** guess natural-language meaning.
- keep Action implementation **and** interface rendering separable. executable behavior traces **to** CA-O-087-CORE_META_MODEL-ACTION--check-atoms; Workflow routing **and** Step bindings remain executor concerns, **not** another procedure inside this Tool.
- use deterministic ordering of diagnostic records **and** preserve source spans; never reorder **or** normalize source bytes **to** hide a failed fidelity check.

### Property contract and coverage

- resolve the selected applicable authority **before** constructing the check inventory. derive a Property contract containing admitted field/section locations, value types, cardinalities, applicability conditions, defaults/override rules, **and** exact source bindings. this contract is a Projection, **not** independently maintained Property authority.
- inventory governing obligations independently of the available adapters. identify mechanically supported checks, semantic-review exclusions, unresolved obligations, **and** missing adapters explicitly; an absent adapter **must not** remove its obligation from the coverage denominator.
- bind source-dependent checks **to** canonical identity, Version, **and** a content digest. a digest mismatch, incomplete source set, contradictory Property declarations, **or** unresolved admission prevents complete coverage; no caller-supplied rule bundle **may** override source authority **or** supply executable code.
- **if** applicable Delivery authority does **not** settle a field spelling, value type, location, **or** required cardinality, report the exact schema gap. do **not** silently infer it from current fixtures, filenames, widespread usage, **or** the implementation.
- do **not** require `cce_version`, `cce_form`, **or** `llm_session_ids` on Atoms. apply the retired-field rule under CA-D-478; CCE authority resolves from the applicable methodology **and** the admitted Claim classification, **not** from those removed fields.

### Boundary libraries

- use Pydantic for strict closed JSON request/result models under CA-M-286-PROGRAMMATIC-CORE-METHOD--validate-untrusted-structured-data-with-pydantic, **and** PyYAML for bounded safe YAML parsing **in** `VALIDATE_ATOMS`. reuse compatible shared Carrier splitting rather than recreate it.
- use a safe YAML loader with duplicate-key rejection **and** bounded nesting, aliases, **and** input size. do **not** construct arbitrary objects, execute tags, **or** silently discard unsupported syntax. distinguish malformed input from an unsupported check.
- pin the selected dependencies **in** the root Python configuration under CA-D-250-PROGRAMMATIC-CORE-DELIVERY--provide-programmatic-software-carriers. dependency adoption does **not** relax read-only execution, protected-input handling, source-bound rule coverage, **or** golden-corpus acceptance.

### Body and Actor adapters

- select the body contract by the carried Content Role under CA-D-479-CORE_META_MODEL-DELIVERY--use-stable-headings-for-atom-body-properties; reuse **`=1`** section parser across section, Property-location, **and** Plan-model checks. use the current CA-D-470-CORE_META_MODEL-DELIVERY--serialize-plan-file-sections nesting for the Plan Definition of Done, **not** its retired sibling-section layout.
- parse actual heading boundaries outside fenced examples. check required cardinality, order, content, **and** nesting independently; an empty admitted Details section is **not** a missing section. retain an explicit gap for an unresolved role **or** extension contract.
- check Author by exact membership **in** the selected Operator registry under CA-D-274-CORE_META_MODEL-DELIVERY--serialize-explicit-atom-revision-author **and** CA-D-494-CORE_META_MODEL-DELIVERY--store-operator-registry-in-project-root. read the registry through the bounded, fingerprinted file reader; fail unlisted names **only after** its schema is valid. do **not** infer aliases, Actor records, **or** permissions. retain malformed, stale, unavailable, **or** absent registry context as incomplete coverage.
- omit effective Plan Assignee resolution for now; retain its deferred coverage explicitly **without** inferring an Assignee from Author **or** from the registry. this does **not** change the optional carried `assignee` encoding.
- refresh an adapter's source binding **only after** reconciling its behavior **and** positive/negative tests with the changed governing Claim. a pin refresh alone is **not** an implementation fix.

## Details
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-318-TOOLS--derive-and-search-the-capability-catalog.md

SHA-256: 3093ec02447c1a3ca47759b42bcca6f6528b6d12f66b078bfbb99ba1c0585810

```markdown
---
atom_id: CA-M-318
content_role: Method
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-03 14:55:01 +0000"
subjects:
  governs: "Capability Catalog"
  depends_on:
    - "Tool"
    - "Action"
    - "Workflow"
    - "Atom"
    - "Scope Unit"
    - "Implementation"
    - "Workflow Run"
    - "Journal"
relations:
  relates_to: [CA-R-1810, CA-D-520]
---
# Summary

Derive and search the capability catalog

## Scope

the TOOLS capability for Capability Catalog.

## Claim

**to** derive **and** search the Capability Catalog, the Implementation **must** apply the following method.

## Details

1. read authoritative Project Structure **and** current source Atoms within the configured Project boundary; omit delivered methodology copies **and** historical or draft Carriers.
2. reuse the safe Atom parser; read identity, Content Role, Type, Status **and** Scope Unit from carried Properties.
3. resolve D-owned Tool Binding tables **and** observe admitted entrypoint files without executing them. bind implemented Action Prompts from their existing source manifests.
4. keep duplicate identities **and** unresolved bindings explicit; an observed script with no declaration remains an Implementation candidate.
5. rank matching query words deterministically, apply the requested filters **and** paginate compact results. load full source content only for a selected context.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-319-TOOLS--observe-and-continue-saved-execution-evidence.md

SHA-256: 9cf6342d6d90860c0470b08f475d3e07c8912d1efc18b9b8294ff9fdcd868786

```markdown
---
atom_id: CA-M-319
content_role: Method
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-03 14:55:01 +0000"
subjects:
  governs: "Execution observation"
  depends_on:
    - "Tool"
    - "Action"
    - "Workflow"
    - "Atom"
    - "Scope Unit"
    - "Implementation"
    - "Workflow Run"
    - "Journal"
relations:
  relates_to: [CA-R-1807, CA-R-1808, CA-R-1809]
---
# Summary

Observe and continue saved execution evidence

## Scope

the TOOLS capability for Execution observation.

## Claim

**to** observe **or** continue a supported Run, the Implementation **must** derive its response from the existing saved evidence.

## Details

1. validate the Run identifier **and** resolve **`=1`** registered backend.
2. read saved status, complete Action reports, source bindings **and** evidence-recording state. preserve initial check outcomes when later fixes are present.
3. derive remaining check **or** fix work from saved coverage **and** dispositions. check current source **and** criteria fingerprints before proposing continuation.
4. bind a notification cursor **to** the Run **and** saved evidence frontier; return later confirmed Events **and** changes **to** status **or** recording state.
5. wait asynchronously **until** evidence changes **or** the bounded timeout expires. an observation timeout does **not** fail the Run.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_MOVE/05_method/CA-M-187-ATOM_MOVE-CORE-METHOD--move-selected-caprmedio-atom-carriers.md

SHA-256: 76f69b2fa0da9554f5d36d2b22ffc82d7658ea59c7a0f343434b289eca2a1e67

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "artifact-operations"
  depends_on: []
version: 9
updated_at: 2026-09-02 01:10:00 +0400
relations:
  method_for:
    - CA-R-867
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Move selected CAPRMEDIO Atom carriers

## Applicable when

use this Method **when** a caller prepares relocation of one exact Atom **or** one frozen bulk set of two **or** more Atom carriers **without** changing their bytes, filenames, **or** identities. actual relocation is permitted **only** **when** an authorized project-local MCP delegation supplies a sealed Initiative action envelope.

## Procedure

1. resolve the exact selector **or** recursive source subtree, retain **only** Atom carriers, **and** capture **every** source path, filename, ID, **and** digest.
2. derive one destination mapping per selected Atom, preserving selected subtree shape by default **and** flattening **only** **when** the sealed Initiative explicitly requests it.
3. validate destination Scope Unit **and** Content-role placement, source membership, path uniqueness, **and** destination collision freedom **without** editing carrier bytes.
4. freeze the complete move map **and** publish a mutation-free dry-run.
5. on explicit authorized `--apply`, recheck source digests **and** destination absence, **then** move the complete atomic **or** bulk set as one rollbackable transaction.
6. verify that **every** source is absent, **every** mapped destination is present, non-Atom files are untouched, **and** **every** moved carrier retains its original bytes, filename, **and** Atom ID.

## Outcome

the selected carriers occupy exactly their approved destinations **and** remain byte-identical governed Atoms.

## Failure or stop

remain **in** dry-run mode **without** delegated apply authority. stop **or** roll back the full move on an invalid destination, collision, stale source, incomplete mapping, changed destination absence, **or** failed post-move verification.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/CLOSE_ATOM/05_method/CA-M-129-CLOSE_ATOM-CORE-IMPL_METHOD--validate-and-describe-one-concern-closure.md

SHA-256: f217b4a98c8419333a20dfcc115ea683a076b067ad6a60362472ec279ff806d5

```markdown
---
subjects:
  governs: "concern-resolution"
  depends_on: []
version: 8
updated_at: 2026-08-30 16:44:07 +0400
relations:
  method_for:
    - CA-R-1042
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Validate and describe one Concern closure

For one closure request, resolve the Concern **and** **every** supplied resolver **or** solution by exact active Atom ID, reject unresolved **or** inactive carriers, require a nonempty terminal disposition, **and** preserve the sealed Initiative action context. Return one closure action targeting `solved` **without** inferring relation kinds, role meanings, **or** participants.

Dry run is mutation-free. `--apply` is accepted **only** through the authorized project-local MCP delegation carried by that sealed Initiative envelope. The authorized effect invokes the canonical Atom lifecycle operation **and** obtains durable `COMMIT_TRIGGER` intake acknowledgement **before** MCP reports success. `CLOSE_ATOM` never appends the Journal, stages files, **or** creates a Git commit.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/COMPILE_APPLICABLE_METHODOLOGY/05_method/CA-M-226-COMPILE_APPLICABLE_METHODOLOGY-CORE-IMPL_METHOD--compile-projected-rmedo-carriers-transactionally.md

SHA-256: de4f89b4f8318e6be5da815d6b6dbd0439ef64611b7b07bbcf394788d76fbcac

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "Applicable Methodology Compilation"
  depends_on:
    - "Tool/COMPILE_APPLICABLE_METHODOLOGY"
    - "Applicable Methodology/Sources"
    - "Applicable Methodology/Compilation Output"
version: 7
updated_at: "2026-10-04 23:02:50 +0400"
relations:
  method_for:
    - CA-R-1842
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Compile Projected RMEDO Carriers Transactionally

**to** compile Applicable Methodology, `COMPILE_APPLICABLE_METHODOLOGY` **must** implement CA-M-224 mechanically, stage the complete projected RMEDO Carrier set under `.caprmedio_runtime`, preserve **and** revalidate **every** selected Source Carrier's repository-relative path, Atom ID, Revision, byte digest, and source Relation, **and** replace **only** files **in** `04_requirement`, `05_method`, `06_evaluation`, `07_delivery`, **and** `09_operations` through atomic file replacement with complete transaction rollback on failure. A deleted derived role tree must be fully regenerated from the same current resolved frontier; the transaction never edits source authority.

## Sources

- CA-R-1842 v1; CA-M-224; CA-O-157 v2.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/DERIVE_CCE_CANONICAL_SIGNATURES/05_method/CA-M-256-DERIVE_CCE_CANONICAL_SIGNATURES-CORE-METHOD--derive-restricted-cce-canonical-signatures.md

SHA-256: c16e844c7ed2c57d17d6528ea7db6957e1e9539e5a34b73ab8bb276798495656

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "Tool/DERIVE_CCE_CANONICAL_SIGNATURES/Canonical Signature Derivation"
  depends_on:
    - "Tool/DERIVE_CCE_CANONICAL_SIGNATURES"
    - "Atom/Claim"
    - "Atom/Claim/Canonical Signature"
version: 5
updated_at: 2026-09-12 04:14:47 +0400
relations:
  child_of:
    - CA-M-240
  method_for:
    - CA-R-1450
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Derive Restricted CCE Canonical Signatures

**to** derive Canonical Signatures, the `DERIVE_CCE_CANONICAL_SIGNATURES` Tool **must** apply CA-M-240 **to** one caller-selected active Atom Carrier frontier **without** changing Source Atoms.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/DERIVE_SCOPE_CANONICAL_SIGNATURES/05_method/CA-M-257-DERIVE_SCOPE_CANONICAL_SIGNATURES-CORE-METHOD--derive-scope-expression-canonical-signatures.md

SHA-256: 296600a298f66fd8578e144f0ef561acc2f6a62234e04a5e82cf8507c2e4906c

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "Tool/DERIVE_SCOPE_CANONICAL_SIGNATURES/Canonical Scope Signature Derivation"
  depends_on:
    - "Tool/DERIVE_SCOPE_CANONICAL_SIGNATURES"
    - "Scope Expression"
    - "Scope Expression/Canonical Scope Signature"
version: 5
updated_at: 2026-09-12 04:14:47 +0400
relations:
  child_of:
    - CA-M-241
  method_for:
    - CA-R-1451
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Derive Scope Expression Canonical Signatures

**to** derive Canonical Scope Signatures, the `DERIVE_SCOPE_CANONICAL_SIGNATURES` Tool **must** apply CA-M-241 **to** one caller-selected active Atom Carrier frontier **without** changing Source Atoms.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/DETECT_CLAIM_VALUE_SET_CANDIDATES/05_method/CA-M-238-DETECT_CLAIM_VALUE_SET_CANDIDATES-CORE-METHOD--detect-exact-claim-value-set-consolidation-candidates.md

SHA-256: 1c75021126223b15ca08df6512399cc5da11a382614368e4eca307e4ce2b3d51

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "Claim Value Set Consolidation Candidate Detection"
  depends_on:
    - "Claim Value Set Consolidation Candidate Evaluation"
    - "Tool/DETECT_CLAIM_VALUE_SET_CANDIDATES"
    - "Atom/Current Scope/Owner"
    - "Atom/Current Scope/Governed Subject Set"
    - "Atom/Claim Scope"
    - "Property"
    - "Entity Graph Projection"
    - "IS_ALLOWED_VALUE_OF"
version: 5
updated_at: 2026-09-02 01:12:00 +0400
relations:
  method_for:
    - CA-R-1358
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Detect Exact Claim Value-Set Consolidation Candidates

**to** detect Claim Value Set consolidation candidates, the `DETECT_CLAIM_VALUE_SET_CANDIDATES` Tool **must** inspect one Scope Unit's local active Atom frontier **without** its child Scope Unit frontiers, derive **every** Atom's Governed Subject Set from its GOVERNS Subjects, derive its Claim Scope from the Property **in** one exact `<Property>: <Value>[ **if** <Qualifier>].` Claim, accept a value **only** **if** one supplied Entity Graph Projection proves its IS_ALLOWED_VALUE_OF relation for that Property, group **only** identical Current Scope Owner, Governed Subject Set, Claim Scope, Property, **and** qualifier coordinates, report **every** contributing Atom ID **and** one proposed `Property: (A, B, C)` Claim, **and** report no candidate for unparseable, unproven, **or** semantically similar prose.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/GENERATE_ENTITY_GRAPH/05_method/CA-M-259-GENERATE_ENTITY_GRAPH-CORE-METHOD--derive-one-entity-and-term-graph-projection.md

SHA-256: 86cc628f83be9151a1b3b40ddd028e2149908cbbb08b5e3032c5ac9d9609b3d7

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "projection-pipeline"
  depends_on: []
version: 7
updated_at: 2026-09-23 04:25:00 +0400
relations:
  method_for:
    - CA-R-1387
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Derive one Entity and Term graph Projection

## Procedure

1. Resolve exactly one caller-selected folder **or** equivalent source frontier, its settings, **and** its Carrier digests. Reject an absent, ambiguous, escaping, **or** unreadable frontier.
2. Parse each readable Carrier **without** mutation. Record **every** unknown **or** unparseable region with its path **and** diagnostic instead of dropping it.
3. Extract declared Terms, direct-parent declarations, **and** direct dependency declarations with source lineage. Preserve unresolved references explicitly.
4. Build the direct-parent tree, direct dependency graph, **and** complete dependency-Term closure. Detect cycles, multiple-parent **or** other declared cardinality violations, **and** unreachable **or** unresolved nodes.
5. Sort **every** node, edge, diagnostic, **and** lineage entry by stable canonical keys. Mark the result non-authoritative **and** bind it **to** the complete source-frontier identity **and** settings digest.
6. Return the Projection **without** mutation **unless** an explicit output path **or** one registered unambiguous destination was supplied. On persistence, reject an authority destination **and** replace exactly one Projection Carrier atomically.

## Outcome

the result is reproducible as-is graph data that `GRAPH_SERVER` **may** consume read-only **and** `GRAPH_UI` **may** present; it is neither an Atom nor an analysis **and** has no authority.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/INSTALL_TOOLS/05_method/CA-M-103-INSTALL_TOOLS-CORE-IMPL_METHOD--install-one-verified-tool-release.md

SHA-256: ed9a447bc38e59328bac3cb5ccd7979434091e7a50a2a4ac68a0072b78de3003

```markdown
---
subjects:
  governs: "feature-boundary"
  depends_on: []
version: 15
updated_at: 2026-09-15 03:15:32 +0400
relations:
  method_for:
    - CA-R-856
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Install one verified Tool release

Inventory **every** eligible regular file below the canonical Tool source, excluding tests, caches, bytecode, **and** host metadata; bind its relative path, content digest, **and** executable mode into one release digest; stage the complete release below `.caprmedio_tmp/install_tools/`; verify its manifest **and** **every** copied byte; publish it below `.caprmedio_runtime/tools/releases/`; **then** atomically select it through `.caprmedio_runtime/tools/current.toml`.

**before** apply, retain the current selection manifest **and** canonical Codex Hook fragment **in** memory. After selection, register the enabled Codex adapter; set repository-local Git configuration caprmedio.codex-hooks = v1; merge exactly one asynchronous PostToolUse command group with matcher .* **and** async: true into the user-level Codex Hook carrier; register the independent Git pre-commit, commit-msg, **and** post-commit Evaluation Hooks; install stable Tool launchers; **and** register enabled background services. Do **not** install automatic-commit PreToolUse, SessionStart, **or** Stop groups.

Each generic Codex command resolves the current Git root, requires the exact activation marker, exits **without** effect **when** the marker **or** executable installed commit-trigger launcher is absent, **and** **otherwise** delegates **to** that launcher. The command performs **only** durable event intake. Remove recognized managed groups from former CAPRMEDIO Hook carriers **without** changing unrelated groups. Reinstallation reuses an identical release **or** selects a new digest **and** preserves an unchanged generic Hook definition byte-for-byte.

**if** a required Hook Carrier, launcher, Git Hook, service registration, **or** release verification fails, restore the retained selection, Hook fragment, Git Hook registration, activation marker, **and** service registry selection; report one stable diagnostic; **and** leave no partially selected runtime. Report Codex host activation as Operator-reviewed external state rather than infer it from Carrier presence. Remove the recognized legacy `.caprmedio_install/` tree **only** **after** the new runtime selection **and** Hook references succeed.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/MIGRATE_ATOM_IDENTITY/05_method/CA-M-155-MIGRATE_ATOM_IDENTITY-CORE-IMPL_METHOD--plan-one-sealed-atom-identity-migration.md

SHA-256: 328998faa90cc0ac893c08ab5ee99332155a2cec8fbc3bca000d84dd765e704d

```markdown
---
subjects:
  governs: "artifact-operations"
  depends_on: []
version: 8
updated_at: 2026-09-06 01:45:12 +0400
relations:
  method_for:
    - CA-R-1048
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Plan one sealed Atom identity migration

For one sealed migration request, resolve the exact active source **and** destination carriers, collect filesystem facts **and** canonical-ID collision candidates, **and** pass **only** those facts **to** a pure planner. The planner validates **every** sealed precondition, applies **only** the named frontmatter **and** relation changes **in** memory, derives the exact result digest, **and** returns one `UPDATE` **or** `MOVE+UPDATE` receipt.

Dry run is mutation-free. `--apply` is accepted **only** through authorized project-local MCP delegation with the sealed Initiative action envelope. The authorized effect atomically writes the planned destination, removes the source **only** **when** paths differ, **and** obtains durable `COMMIT_TRIGGER` intake acknowledgement **before** MCP reports success. It never infers identity mappings, relation meanings, timestamps, Journal events, **or** Git actions beyond the sealed request.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/REBIND_ATOM_RELATIONS/05_method/CA-M-156-REBIND_ATOM_RELATIONS-CORE-IMPL_METHOD--plan-one-sealed-atom-relation-rebinding.md

SHA-256: af474efa5c28bc40544dfc88b96fcb0eaa90016562d6c75d3c188101f84d4afa

```markdown
---
subjects:
  governs: "artifact-operations"
  depends_on: []
version: 8
updated_at: 2026-09-06 01:45:12 +0400
relations:
  method_for:
    - CA-R-1049
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Plan one sealed Atom relation rebinding

For one sealed request, resolve the exact active source carrier, verify its digest **and** version, validate **only** the explicitly named direct relation rewrites **or** removals, **and** pass the observed bytes **and** sealed request **to** a pure planner. The planner preserves filename, body, **and** undeclared frontmatter, advances version once, sets the supplied timestamp, derives the result digest, **and** returns one `UPDATE` receipt.

Dry run is mutation-free. `--apply` is accepted **only** through authorized project-local MCP delegation with the sealed Initiative action envelope. The authorized effect atomically replaces **only** the source carrier **and** obtains durable `COMMIT_TRIGGER` intake acknowledgement **before** MCP reports success. It never infers a relation meaning, target mapping, backup, Journal event, staging change, **or** Git action.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/RETRIEVE_APPLICABLE_METHODOLOGY/05_method/CA-M-227-RETRIEVE_APPLICABLE_METHODOLOGY-CORE-IMPL_METHOD--retrieve-subject-authority-without-persistent-indexes.md

SHA-256: a951d78d8a0cac469e5ce60e70e00c5e495aac55e225d6a4598caf962e270a7d

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "Applicable Methodology Retrieval Tool/Execution"
  depends_on:
    - "Applicable Methodology Retrieval Tool"
    - "Applicable Methodology Retrieval"
version: 4
updated_at: "2026-09-15 19:28:04 +0400"
relations:
  method_for:
    - CA-R-1241
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Retrieve Subject Authority Without Persistent Indexes

**to** retrieve applicable authority, the Tool **must** perform **all** of the following:

1. resolve **every** projected Atom's authoritative source from the selected source frontier using its retained Atom ID **and** Revision; fail closed **if** that binding is missing **or** ambiguous, the source is no longer current, **or** the projected Carrier bytes differ from the source. do **not** require **or** insert embedded Projection metadata.
2. derive GOVERNS **and** DEPENDS_ON indexes **in** memory.
3. seed exact matching governed Subject Paths **and** close **every** prerequisite transitively; fail closed on an unresolved prerequisite.
4. emit ordered source-backed Carrier records with their resolved source bindings.
5. write no persistent Subject Index Carrier **or** cache.


## Sources

- [CA-R-1241 — Require Source-Backed Subject Retrieval](../04_requirement/CA-R-1241-RETRIEVE_APPLICABLE_METHODOLOGY-CORE-REQUIREMENT--require-source-backed-subject-retrieval.md)
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/START_BACKGROUND_SERVICES/05_method/CA-M-104-START_BACKGROUND_SERVICES-CORE-IMPL_METHOD--control-registered-background-services.md

SHA-256: b047d676a5e05cd0c6e46448757a92cbd07005fa8037d11e3b49d8ecb5c6d961

```markdown
---
subjects:
  governs: "feature-boundary"
  depends_on: []
version: 9
updated_at: 2026-09-15 03:15:32 +0400
relations:
  method_for:
    - CA-R-857
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Control registered background services

Verify the selected runtime release, parse **and** validate its `background_services.toml`, expand **only** registered repository, runtime, temporary-state, Tool-root, **and** interpreter placeholders, **and** reject executable Framework Carriers outside `.caprmedio_runtime/tools`.

For status, report admission, queue count **and** bytes, active action **and** phase, process identity, selected release, leases, last success **and** failure, budget usage, circuit state, **and** dead letters **without** mutation. For pause, stop new dispatch **and** preserve intake **and** action state. For resume **or** start, verify health **and** declared budgets, restore admission, **and** drain accepted work **without** starting a duplicate process. For stop, stop admission, request cooperative bounded shutdown, **and** wait for a declared recoverable boundary. For reload, stop at that boundary, re-resolve the selected release, restart, **and** reconcile preserved work.

Use atomic PID **and** lifecycle-state records below each Runtime service directory, with their atomic-write intermediates below `.caprmedio_tmp`. Start processes **without** a shell, route output **to** Runtime logs, route bytecode **and** disposable cache state **to** Project Temporary State, **and** verify the declared startup grace interval. Automatically restart **or** resume **only** a classified transient pre-mutation failure within its measured budget **and** **after** cooldown **and** health checks. Open the circuit **and** require explicit Operator recovery for exhausted budgets **or** governance, Journal, staging, ambiguous Git, **and** lease-integrity failures.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/05_method/CA-M-196-APPS-CORE-METHOD--register-the-application-scope-unit-topology.md

SHA-256: 866020fb7e243c1aadfa6bbe6b87da092b9658879ceef8db19b952352b212f99

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "feature-boundary"
  depends_on: []
version: 8
updated_at: 2026-09-23 04:20:00 +0400
relations:
  method_for:
    - CA-R-1100
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Register the APPS Scope Unit topology

## Applicable when

Use this Method **when** registering **or** changing an immediate APPS Scope Unit.

## Procedure

1. Resolve the active APPS authority **and** the current immediate-child Scope Unit declarations.
2. Register `GRAPH_SERVER`, `GRAPH_UI`, `WORKFLOW_ORCHESTRATOR`, **and** `AGENT_HOST_PLUGINS` as distinct immediate unordered APPS children.
3. Assign the headless read model **and** service to `GRAPH_SERVER`; assign the optional human interface to `GRAPH_UI`; assign Workflow Run state **and** continuation to `WORKFLOW_ORCHESTRATOR`; **and** retain host-specific packaging in `AGENT_HOST_PLUGINS`.
4. Verify that `GRAPH_SERVER` exposes the complete headless boundary required by Tools **and** MCP without depending on `GRAPH_UI`.
5. State that every read model, interface, **and** Projection is derived support **and** does **not** become project authority.
6. Confirm that each declaration has one immediate typed owner, one identity, **and** no conflicting owner **or** responsibility claim.

## Outcome

APPS has four identifiable immediate unordered children with separated server, optional UI, orchestration, **and** host-plugin responsibilities.

## Failure or stop

Stop **when** a required child is missing, duplicated, non-immediate, ordered, assigned a conflicting boundary, **or** given project authority; also stop when headless behavior depends on `GRAPH_UI`.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/05_method/CA-M-222-APPS-CORE-METHOD--bind-an-app-interface-to-declared-backend-services.md

SHA-256: 973bba46ab38aa7ec21bd27231fb5bcace34d67810e2fffaaa8f99989953c9b8

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "app-service-interface"
  depends_on:
    - "APPS"
version: 8
updated_at: 2026-08-27 14:52:39 +0400
relations:
  method_for:
    - CA-R-1187
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Bind an App interface to declared backend services

Bind an App interface **to** one declared backend-service contract **without** making
the interface an authority **or** effect owner.

## Applicable when

Apply at an App interface that presents a declared backend service **to** an
Operator.

## Procedure

1. Resolve the declared service contract **and** its admitted commands, queries,
   results, **and** failures.
2. Render **only** admitted results **and** submit **only** declared commands **or** queries.
3. Preserve visible request, cancellation, stale-result, **and** error states.
4. Consume the service contract **without** bypassing it **to** mutate project
   authority.
5. Do **not** impose Tool scheduling, Hook, file-mutation, **or** MCP protocol behavior
   on another component.

## Outcome

the App interface remains replaceable, reports its service state visibly, **and**
cannot become a second authority **or** effect owner.

## Failure or stop

Stop **when** the service contract is absent **or** stale, a result cannot be rendered
safely, an interface action would bypass the declared service, **or** the interface
would assume Tool, MCP, **or** project-authority behavior.

## Sources

- [Web Content Accessibility Guidelines 2.2](https://www.w3.org/TR/WCAG22/)
- [OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/stable-en/02-checklist/05-checklist)
- [OWASP Cross Site Scripting Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- [Python documentation: task groups](https://docs.python.org/3/library/asyncio-task.html#task-groups)
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/05_method/CA-M-242-APPS-CORE-METHOD--register-the-agent-host-plugins-unit.md

SHA-256: a540577bf002df90c1c6d708e336d96d2d3e52503116d184b90056ea2644f548

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "feature-boundary"
  depends_on: []
version: 4
updated_at: 2026-09-02 00:21:00 +0400
relations:
  method_for:
    - CA-R-1101
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Register the AGENT_HOST_PLUGINS unit

## Applicable when

Use this Method **when** registering **or** changing the AGENT_HOST_PLUGINS Scope Unit owned immediately by APPS.

## Procedure

1. Resolve the active APPS authority **and** the current immediate-child Scope Unit declarations.
2. Register exactly one unordered immediate child with prefix `AGENT_HOST_PLUGINS`, Structural level `4`, address `002_FRAMEWORK_ENGINE/PROGRAMMATIC/APPS/AGENT_HOST_PLUGINS`, **and** the corresponding source path.
3. Assign the unit ownership of installable agent-host-specific plugin packages **and** their host wiring.
4. Require **every** provider-neutral CAPRMEDIO Skill, Tool, **and** Methodology behavior used by a host package **to** remain referenced from its existing owner rather than copied into this unit.
5. Confirm that the declaration has one immediate typed owner, one identity, **and** no duplicated provider-neutral responsibility.

## Outcome

AGENT_HOST_PLUGINS is one identifiable immediate APPS unit with the required boundary, address, realization path, **and** host-specific-only responsibilities.

## Failure or stop

Stop **when** AGENT_HOST_PLUGINS is missing, duplicated, non-immediate, ordered, assigned a conflicting address **or** path, **or** made an owner of provider-neutral behavior.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/AGENT_HOST_PLUGINS/05_method/CA-M-197-AGENT_HOST_PLUGINS-CORE-METHOD--register-the-codex-plugin-unit.md

SHA-256: 7688665b56c889da7f9eaa613efd6f15d84394a6f5d5ee47066f235161bb6002

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "feature-boundary"
  depends_on: []
version: 8
updated_at: "2026-09-23 04:27:00 +0400"
relations:
  method_for:
    - CA-R-1102
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Register the CODEX_PLUGIN unit

## Applicable when

Use this Method **when** adding the Codex-specific plugin boundary under AGENT_HOST_PLUGINS.

## Procedure

1. Register CODEX_PLUGIN as one immediate child Scope Unit of AGENT_HOST_PLUGINS with its stable address, scope token, source path, **and** structural level.
2. Place **only** Codex package metadata, supported host wiring, **and** Codex-specific adapters inside the unit.
3. Reference GRAPH_UI **and** **every** provider-neutral CAPRMEDIO Skill, Tool, **and** Methodology behavior from its existing owner instead of copying **or** redefining it.
4. Rebuild the Project Scope Unit Graph **and** verify the immediate typed ownership edge from AGENT_HOST_PLUGINS **to** CODEX_PLUGIN.

## Outcome

the Codex integration has one explicit host-specific structural owner **without** duplicated provider-neutral behavior.

## Failure or stop

Stop on a duplicate CODEX_PLUGIN unit, an invalid address **or** source path, a non-immediate parent, **or** copied provider-neutral CAPRMEDIO behavior.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/AGENT_HOST_PLUGINS/CODEX_PLUGIN/05_method/CA-M-150-CODEX_PLUGIN-CORE-METHOD--select-the-minimal-codex-plugin-shape.md

SHA-256: 62d60841baa21b33d0dee077bc2af3f0b4d901534df23218acb069869ed8fd76

```markdown
---
subjects:
  governs: "plugin-architecture"
  depends_on: []
version: 11
updated_at: 2026-08-30 16:44:07 +0400
relations:
  method_for:
    - CA-R-1073
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Select the minimal Codex plugin shape

Select the Codex plugin shape through this procedure:

1. Start from the bounded CAPRMEDIO workflows that the plugin **must** make available **in** Codex **and** identify the provider-neutral authority that each workflow references.
2. Package a workflow as a skill **when** instructions **and** capabilities already available **to** Codex are sufficient; add an MCP server **only** **when** the workflow requires controlled tools, an external service, authentication, **or** independently operated infrastructure.
3. Combine skills with an MCP server **only** **when** reusable workflow guidance **must** govern use of those tools, **and** add UI **only** **when** inspecting, comparing, editing, confirming, **or** navigating structured information materially improves the workflow.
4. Keep **every** MCP tool useful **without** UI so Codex can complete the same supported workflow headlessly.
5. Keep Codex-only host wiring, including optional hooks, inside `CODEX_PLUGIN`; reference rather than duplicate provider-neutral CAPRMEDIO behavior.
6. Record the selected skills, MCP connection **or** server, optional UI, optional hooks, excluded capabilities, **and** the evidence that each included component is necessary **before** packaging begins.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/AGENT_HOST_PLUGINS/CODEX_PLUGIN/05_method/CA-M-151-CODEX_PLUGIN-CORE-METHOD--package-the-codex-plugin.md

SHA-256: 65cecb37a660ce0b423c4893da7cac0a6f80b9bc55f63ee895f41d1ce85cd8b0

```markdown
---
subjects:
  governs: "plugin-packaging"
  depends_on: []
version: 10
updated_at: 2026-08-30 16:44:07 +0400
relations:
  method_for:
    - CA-R-1074
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Package the Codex plugin

Package the Codex plugin through this procedure:

1. Create one plugin root with a stable kebab-case identity **and** a required `.codex-plugin/plugin.json` manifest containing the current plugin version, description, **and** relative paths **to** its packaged capabilities.
2. Place reusable workflows under `skills/`; add `.app.json` **only** for a registered MCP server connection, `.mcp.json` **only** for an MCP server distributed with the plugin, **and** assets **or** lifecycle hooks **only** **when** selected by the plugin-shape decision.
3. Keep manifest references relative **to** **and** contained by the plugin root, keep credentials **and** mutable runtime state outside the package, **and** ensure **every** declared file **or** directory exists.
4. Add **or** update one repository marketplace entry at `.agents/plugins/marketplace.json`, point its `source.path` **to** the plugin root with a `./`-prefixed path relative **to** the marketplace root, **and** declare installation policy, authentication policy, **and** category.
5. Verify that the marketplace plugin name matches the manifest identity, the advertised version **and** description match the packaged content, **and** optional MCP, UI, asset, **and** hook references match the selected plugin shape.
6. Produce a distributable package **without** redefining the provider-neutral CAPRMEDIO authority referenced by its skills **or** tools.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/AGENT_HOST_PLUGINS/CODEX_PLUGIN/05_method/CA-M-152-CODEX_PLUGIN-CORE-METHOD--verify-the-installed-codex-plugin.md

SHA-256: 7499899d739fb4af865f9c457cd0e37d02a7b92e9969b15d2007ff06fed2dd5d

```markdown
---
subjects:
  governs: "installed-plugin-validation"
  depends_on: []
version: 11
updated_at: 2026-08-30 16:44:07 +0400
relations:
  method_for:
    - CA-R-1075
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify the installed Codex plugin

Verify the installed Codex plugin through this procedure:

1. Validate each packaged skill, MCP tool, UI resource, **and** hook independently **before** testing the complete plugin; **when** an MCP server is present, exercise representative inputs, edge cases, invalid inputs, empty results, authorization behavior, schemas, **and** model-readable results.
2. Add the repository marketplace as a local source, install the packaged plugin from that source, restart the host **when** required **to** refresh local package files, **and** begin a fresh Codex conversation with the plugin enabled.
3. Run a versioned evaluation set containing direct requests, indirect requests with the same goal, follow-ups that depend on earlier results, unsupported requests, **and** declared boundary cases.
4. For **every** request, record whether the expected skill **or** tool activated, whether arguments **and** results were correct, whether bundled resources resolved from the installed package, whether required steps completed, **and** whether authorization **or** confirmation behavior matched the requested action.
5. **when** MCP **or** UI is present, also verify tool discovery, skill-to-tool routing, authentication **after** installation, model-readable fallback behavior, UI rendering, **and** completion of the combined workflow from start **to** finish.
6. Treat source-package validity, marketplace availability, successful installation, **and** proved runtime invocation as separate outcomes; accept the plugin **only** **when** the fresh installed path supplies replayable evidence for each claimed outcome.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/AGENT_HOST_PLUGINS/CODEX_PLUGIN/05_method/CA-M-198-CODEX_PLUGIN-CORE-METHOD--expose-the-current-graph-ui-through-codex.md

SHA-256: c5c86451a6a65df4a72d57eb8dcf98cead42b4257009cc2f1fc1394fd1352fe9

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "graph-app-access"
  depends_on: []
version: 8
updated_at: "2026-09-23 04:27:00 +0400"
relations:
  method_for:
    - CA-R-1103
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Expose the current GRAPH_UI through Codex

## Applicable when

Use this Method **when** a Codex operator needs **to** inspect the current Project Graph through the installed plugin.

## Procedure

1. Connect the plugin **to** the read-only GRAPH_UI interface **and** obtain its current source frontier **and** rebuild status.
2. Expose graph navigation, filtering, node selection, **and** node inspection **without** copying graph authority into the plugin.
3. For **every** selected node, show its source path, current digest, source content, **and** available provenance.
4. Preserve explicit stale, unavailable, missing-source, **and** rebuild-in-progress states **in** the Codex-facing response.
5. Reject **all** graph mutations through this interface **and** route **any** requested change **to** separately governed Skills **or** Tools.

## Outcome

Codex presents an attributable read-only view of the current GRAPH_UI state **and** its source carriers.

## Failure or stop

Return the precise stale **or** unavailable state **when** GRAPH_UI cannot prove currentness; never synthesize current graph content **or** mutate sources.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/AGENT_HOST_PLUGINS/CODEX_PLUGIN/05_method/CA-M-199-CODEX_PLUGIN-CORE-METHOD--route-selected-graph-context-into-governed-codex-work.md

SHA-256: 6012323d78894c965b4f0f9a1249922e5575ddf1b5099b22faf89c64e1363351

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "graph-app-access"
  depends_on: []
version: 7
updated_at: 2026-09-02 00:25:00 +0400
relations:
  method_for:
    - CA-R-1104
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Route selected graph context into governed Codex work

## Applicable when

Use this Method **when** an operator selects graph nodes as the bounded context for a Codex question **or** governed action.

## Procedure

1. Seal the operator-selected node set with node IDs, source paths, current digests, **and** the selection frontier.
2. Transfer **only** that context **and** its provenance **to** the selected provider-neutral Skill **or** MCP operation.
3. Preserve the meaning, input contract, **and** diagnostic vocabulary of **every** invoked Tool across the Codex adapter.
4. Return answers **and** proposed actions with their source-node attribution **and** unmodified failure states.
5. Require the host's required operator confirmation **before** **any** irreversible action **and** prohibit implicit scope widening, source mutation, secret disclosure, Tool-validation bypass, **or** host-permission bypass.

## Outcome

Codex work remains bounded **to** the selected current graph context **and** attributable **to** its exact source frontier.

## Failure or stop

Stop **when** selection digests are stale, the boundary cannot be sealed, a route would widen authority, host permission denies it, **or** an irreversible action lacks required confirmation.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/GRAPH_SERVER/05_method/CA-M-154-GRAPH_SERVER-CORE-METHOD--serve-live-graph-sources-without-mutation.md

SHA-256: c082d2dd28fdc663de3eb906c66c4f294ea80dece7581e0462d9486b1ab6b866

```markdown
---
subjects:
  governs: "artifact-query"
  depends_on: []
version: 13
updated_at: 2026-09-23 04:20:00 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  method_for:
    - CA-R-1077
  derived_from:
    - CA-A-057
---
# Serve live graph sources without mutation

Serve current graph inputs through this procedure:

1. Start the headless local service through the shared Tool environment without requiring `GRAPH_UI`, **and** keep logs **and** service state beneath its owned `.caprmedio_runtime` directory.
2. Accept **only** a canonical path supplied by the MRT source-lineage manifest **and** resolve it as either a registered `stg_requirements_subjects.md` **or** `stg_requirements_lineage_sections.md` **in** an active structural-unit root **or** a regular active Atom Markdown file below `.caprmedio`.
3. Reject absolute external paths, traversal, symlink escape, inactive lifecycle directories, unregistered STG files, unregistered Markdown, non-Markdown source content, write verbs, **and** **every** mutation request.
4. Read the current source bytes once **and** return the source kind, raw UTF-8 content, SHA-256 digest, canonical repository-relative path, **and** active **or** current status **without** removing frontmatter, rewriting STG content, **or** generating source-specific HTML.
5. Keep **every** request strictly read-only; stopping the service **or** deleting `.caprmedio_runtime` **must not** change an Atom, STG Projection, MRT Projection, **or** Journal.
6. Return explicit not-found, not-active, not-current, invalid-path, invalid-encoding, **and** digest-mismatch results so any Tool, MCP client, **or** optional UI can distinguish stale projections, changed Atoms, **and** unavailable sources.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/GRAPH_UI/05_method/CA-M-153-GRAPH_UI-CORE-METHOD--render-and-navigate-active-graph-html.md

SHA-256: fc70ec74441e5cf47c58076b7720b60091d4c77dae1b772f3ff17ec5eb799b9a

```markdown
---
subjects:
  governs: "projection-pipeline"
  depends_on: []
version: 14
updated_at: 2026-09-23 04:25:00 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  method_for:
    - CA-R-1076
  derived_from:
    - CA-A-057
---
# Render and navigate active graph HTML

Render **and** use the active graph views through this procedure:

1. Discover the applicable active structural units from current project topology **and** require one current `stg_requirements_subjects.md` **and** one current `stg_requirements_lineage_sections.md` **in** each selected structural-unit root.
2. Use the Subject STG files for Subject, tier, **and** orphan placement; use the lineage-section STG files for Principle-root sections **and** direct Requirement relations; **and** read the actual active Atom Markdown for canonical identity, first-H1 Summary, body, frontmatter, path, **and** current digest. Reject a missing STG, inconsistent STG pair, unresolved Atom, **or** STG-to-Atom digest mismatch.
3. Materialize exactly one `.caprmedio/mrt_atoms.html` file by atomic replacement. Embed **all** JavaScript **and** presentation assets **in** that file, generate no sibling JavaScript, CSS, data, index, view, **or** per-Atom HTML files, **and** keep service state **only** under `.caprmedio_runtime`.
4. Embed a machine-readable source-lineage manifest covering **every** consumed STG file, **every** underlying Atom, their source-frontier relation, canonical paths, **and** digests. The embedded JavaScript **must** use `GRAPH_SERVER` **to** retrieve current STG **and** Atom content rather than treating embedded HTML text as authority.
5. Derive the structural-unit filter tree from current registered scope paths **and** expose tier, structural-unit, **and** Requirement-subtype filters plus a show-or-hide control for RMED orphans. Preserve complete-graph orphan classification **when** a display filter hides a neighbor.
6. Let the HTML setting select `short` **or** `detailed` initial node display. A short node shows `<scope>-<number> <Summary>` from the exact first H1; its first click shows the actual current body **without** frontmatter **in** a panel above the node **and** its second click shows complete raw Markdown including frontmatter. A detailed node initially shows that body above the label **and** one click shows complete raw Markdown.
7. Compare **every** live STG **and** Atom digest with the lineage manifest, visibly identify stale STG, stale MRT, **and** unavailable-source states, preserve filters **and** focused-node state **in** the URL, **and** keep each identity linked **to** its canonical source path. Treat the UI as optional: removing it leaves `GRAPH_SERVER`, Tools, **and** MCP operable.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/WORKFLOW_ORCHESTRATOR/05_method/CA-M-302-WORKFLOW_ORCHESTRATOR-METHOD--separate-workflow-coordination-from-action-execution.md

SHA-256: d8e1f7eed8bc1d9c3b2f72ff7f14d1a84be21246210634a0e23be0048d41a313

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "Workflow Run"
  depends_on:
    - "Workflow"
    - "Action"
    - "Tool"
    - "Operator"
    - "Journal"
    - "Projection"
    - "Implementation"
version: 1
updated_at: "2026-09-18 21:23:47 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"method_for": ["CA-R-1522", "CA-R-1523", "CA-R-1524"], "relates_to": ["CA-M-158", "CA-M-222"]}
---
# Separate Workflow coordination from Action execution

**to** implement WORKFLOW_ORCHESTRATOR, separate responsive coordination from long-running Action execution.

- use an on-demand local background service for coordination. an HTTP server, remote deployment, **or** graphical interface is **not** required by this Method.
- execute long-running **or** blocking Actions through bounded workers **or** subprocesses; waiting for external results **or** Operator input **must not** block the coordination interface.
- keep Workflow selection, transition, handoff, retry, **and** approval behavior driven by applicable methodology inputs rather than independently authored application branches.
- use stable request, Run, **and** dispatch identities with durable handoff recording, duplicate suppression, **and** the declared effect-safety mechanism. separate transient worker state from canonical Journal history **and** rebuildable views.
- keep client transport **and** worker adapters replaceable. select concrete libraries, wire formats, persistence Carriers, **and** resource limits through their applicable authority rather than assuming an unapproved default.

asynchronous coordination does **not** require **every** Action implementation **to** use asynchronous programming **or** execute concurrently. this Method does **not** install hooks **or** migrate the existing commit-automation service.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/WORKFLOW_ORCHESTRATOR/05_method/CA-M-320-WORKFLOW_ORCHESTRATOR--coordinate-local-runs-with-dbos.md

SHA-256: 7c3c81a072ca3f3e4c52589bcf4c88f207dc98a84a033386ec457f823e879890

```markdown
---
atom_id: CA-M-320
content_role: Method
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-03 20:12:24 +0400"
subjects:
  governs: "Workflow Run/coordination"
  depends_on: [Workflow, Action, Atom, Operator, Journal, Implementation, Tool]
relations:
  relates_to: [CA-R-1522, CA-R-1523, CA-R-1524, CA-O-104]
---
# Summary

Coordinate local Runs with DBOS

## Scope

WORKFLOW_ORCHESTRATOR's initial local execution capability.

## Claim

implement independent execution through DBOS durable queues **and** a separately started local worker.

## Details

1. validate **and** freeze the submitted request before queue admission; duplicate Run IDs accept **only** the same frozen request.
2. register **=1** Project queue with concurrency **=1** initially, preventing competing source edits.
3. use durable Steps for gather, Agent dispatch, admitted report recording **and** finalization; workflow ordering is gather, check, fix, with no recheck.
4. expose queue state through a client adapter; keep DBOS checkpoints operational, with confirmed Workflow events **in** the shared Journal.
5. start the worker explicitly. installation **or** discovery starts no Run **and** installs no hook.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/WORKFLOW_ORCHESTRATOR/05_method/CA-M-321-WORKFLOW_ORCHESTRATOR--execute-actions-through-a-replaceable-codex-adapter.md

SHA-256: e9ea368589d1285079d4cddcc881f5807002a269ed54fe4dafa401c6c74a7811

```markdown
---
atom_id: CA-M-321
content_role: Method
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-04 04:10:07 +0400"
subjects:
  governs: "Action/execution"
  depends_on: [Workflow, Action, Atom, Operator, Journal, Implementation, Tool]
relations:
  relates_to: [CA-R-1522, CA-R-1523, CA-R-1524, CA-O-104]
---
# Summary

Execute Actions through a replaceable Codex adapter

## Scope

WORKFLOW_ORCHESTRATOR's initial local execution capability.

## Claim

implement Agentic execution through a replaceable Codex CLI adapter with structured output admission.

## Details

1. invoke codex exec with argument arrays, stdin prompts, a JSON output schema **and** an explicit isolated working directory. native execution uses a read-only CLI sandbox; the dedicated Docker Agent service uses its container boundary **without** Project mounts. use existing authentication through runtime credential admission, never through an image layer.
2. give the Agent the selected Atom, current rules, the Action prompt **and** phase report, with no other Atom reports.
3. require a structured report plus optional proposed replacement content. validate identity, source hashes, confidence **and** saved check evidence before admission.
4. retain reports **and** candidate content under the dispatch identity before applying changes.
5. bound subprocess duration **and** output reads. timeouts, invalid output **or** missing credentials block execution rather than inventing a pass.
6. keep the executor interface independent of Codex so other harnesses can be added later.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/WORKFLOW_ORCHESTRATOR/05_method/CA-M-323-WORKFLOW_ORCHESTRATOR--compute-coverage-from-saved-step-evidence.md

SHA-256: 1d468b8ddc36092ebadaf28c334a2dc458375c1582e3e1bd0a5a9c059adb58ba

```markdown
---
atom_id: CA-M-323
content_role: Method
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 01:12:38 +0400"
subjects:
  governs: "Workflow Run/coverage"
  depends_on: [Workflow, Step, Action, Atom, Operator, Journal]
---
# Summary

Compute coverage from saved Step evidence

## Scope

RMED Atoms Base Revise execution in WORKFLOW_ORCHESTRATOR.

## Claim

the Coverage Gate **must** derive its accounting from the frozen request **and** saved results without another semantic Atom evaluation.

## Details

- compare gather identities, ordered paths **and** frozen source/rule observations.
- check every required slot for concluded status **and** evidence; retain coverage gaps **and** blockers.
- use existing finding-disposition **and** completion predicates for fix coverage.
- record the gate once per phase in the existing Run state, Journal **and** full report; recovery reuses the same evidence rather than replaying completed effects.
- run gates as durable DBOS Steps; keep coverage interruption distinct from scheduler failure.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/WORKFLOW_ORCHESTRATOR/05_method/CA-M-324-WORKFLOW_ORCHESTRATOR--manage-the-runtime-with-docker-compose.md

SHA-256: f554e171ffece6f92f7c7873b24fac31262926f963efb39bb0dbacfac0e4036f

```markdown
---
atom_id: CA-M-324
content_role: Method
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 04:10:07 +0400"
subjects:
  governs: "Workflow Orchestrator/Docker runtime/method"
  depends_on: [Implementation, Operator, Workflow Run, AI Agent, Action, Atom, Carrier, Journal, Tool]
relations:
  relates_to: [CA-R-1818, CA-R-1819, CA-M-320]
---
# Summary

manage the runtime **with** Docker Compose

## Scope

the Docker runtime's implementation **and** lifecycle management.

## Claim

implement runtime management through Docker Compose using **=1** image **and** separate MCP, worker **and** Agent services with explicit persistent-state boundaries.

## Details

1. build from admitted Engine sources **and** pinned runtime dependencies; exclude Project data, credentials **and** generated state from the build context.
2. use non-root services, a read-only image filesystem **and** **only** the mounts required by their responsibilities.
3. give the worker a separate Docker scheduler namespace. keep the shared Journal **and** report locations unchanged.
4. publish Docker routing **only** **after** worker readiness. queue calls **must** fail visibly **if** the selected runtime is unavailable; they **must not** fall back **to** another queue.
5. preserve saved dispatch evidence across restart. after uncertain dispatch, require reconciliation rather than another Agent call.
6. keep automatic restart disabled. provide explicit restart **and** a stdio MCP launcher; lifecycle commands do **not** create Workflow requests.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/WORKFLOW_ORCHESTRATOR/05_method/CA-M-325-WORKFLOW_ORCHESTRATOR--execute-agent-proposals-in-an-isolated-service.md

SHA-256: c13373e97862c53e2e87ed0709fd0da5031206ba026e40a54000cdc2310bff8f

```markdown
---
atom_id: CA-M-325
content_role: Method
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 04:10:07 +0400"
subjects:
  governs: "Action/execution/Docker adapter"
  depends_on: [AI Agent, Action, Atom, Workflow Run, Implementation, Operator, Carrier]
relations:
  relates_to: [CA-R-1819, CA-M-321]
---
# Summary

execute Agent proposals **in** an isolated service

## Scope

the worker's replaceable Agent adapter **in** the Docker runtime.

## Claim

execute an Agentic Action by sending its bound context **to** the private Agent service **and** admitting the returned proposal through the existing worker boundary.

## Details

- use a bounded JSON request carrying context, check **or** fix phase **and** timeout; admit the existing AgentOutput schema.
- provide **only** the compiled context, not Project mounts. run Codex CLI **in** a fresh dispatch directory with no inherited user configuration **or** MCP registrations.
- the dedicated Agent container provides outer isolation; the CLI can use external isolation there. native execution retains its read-only CLI sandbox.
- allow **<=1** active Agent request initially. bound request bytes, response bytes **and** execution duration.
- preserve accepted output before effects. transport loss, timeout, invalid output **or** authentication failure interrupts rather than silently retrying.
- seed an absent private runtime authentication cache from an explicitly mounted credential file. do **not** overwrite an existing refreshed cache **or** print its contents.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/05_method/CA-M-167-MCP-CORE-METHOD--delegate-one-initiative-bound-atom-mutation.md

SHA-256: b0ea3396d33a7147f8d3ce079ac5aaa5367c6a7a033c45f41207eaf228bff8a8

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "framework-engine-mcp"
  depends_on: []
version: 5
updated_at: 2026-08-30 16:44:07 +0400
relations:
  method_for:
    - CA-R-1105
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Delegate one Initiative-bound Atom mutation

## Applicable when

Apply **when** an authorized project-local MCP operation requests an Atom mutation.

## Procedure

1. Preserve the human-origin Initiative **and** select the one canonical Atom Tool **without** resolving its target **or** lifecycle meaning.
2. Forward the sealed request **to** that Tool **and** return its structured outcome unchanged.
3. Report success **only** **after** the canonical Tool returns its acknowledged outcome; preserve a rejection, conflict, partial result, **or** blocked result as such.

## Outcome

MCP transports one authorized mutation request **without** becoming the target, mutation, recovery, **or** success-state owner.

## Failure or stop

Stop **and** return an explicit failure **when** authorization, Initiative, canonical Tool selection, **or** the Tool outcome is absent **or** invalid.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/05_method/CA-M-168-MCP-CORE-METHOD--discover-current-immediate-tool-units.md

SHA-256: 1cd3169ff7afedc6b7144bf513ebd89688db777a7a3d0ea1442e05329c5c8e2a

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "framework-engine-mcp"
  depends_on: []
version: 5
updated_at: 2026-08-30 16:44:07 +0400
relations:
  method_for:
    - CA-R-1106
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Discover current immediate Tool units

## Applicable when

Apply **when** MCP **must** refresh the project-local exposed Tool set.

## Procedure

1. Resolve the current project graph **and** its immediate Tool units owned by `TOOLS`.
2. Match each unit **to** its canonical Tool folder **and** current enablement decision.
3. Exclude nested helpers **and** non-Tool folders from the resulting source set.

## Outcome

MCP has one current, authority-derived source set for Tool exposure.

## Failure or stop

Stop discovery **when** the graph, unit identity, enablement decision, **or** canonical Tool folder is unresolved.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/05_method/CA-M-169-MCP-CORE-METHOD--validate-one-complete-tool-invocation-contract.md

SHA-256: c958fdadf31a6ee14feb3689d06505cadd970101301baecb0c21e81d0be5b538

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "framework-engine-mcp"
  depends_on: []
version: 6
updated_at: 2026-08-30 16:44:07 +0400
relations:
  method_for:
    - CA-R-1107
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Validate one complete Tool invocation contract

## Applicable when

Apply **before** MCP exposes one active Tool.

## Procedure

1. Read the Tool's canonical identity, capability kind, input schema, result envelope, diagnostic **and** failure contract, **and** executable binding.
2. Validate that each field is present, coherent, **and** bound **to** the same current Tool identity.
3. Return the validated contract **or** explicit field-level diagnostics **without** repairing **or** reinterpreting it.

## Outcome

**only** one complete canonical Tool contract is eligible for MCP projection.

## Failure or stop

Stop **when** **any** contract field is missing, conflicting, ambiguous, **or** unresolved.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/05_method/CA-M-170-MCP-CORE-METHOD--project-one-callable-mcp-tool-from-one-tool-unit.md

SHA-256: 19826a31cceafe0c2c34f0031a78974b470cc7ae44669233df11de4f77ab895c

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "framework-engine-mcp"
  depends_on: []
version: 5
updated_at: 2026-08-30 16:44:07 +0400
relations:
  method_for:
    - CA-R-1108
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Project one callable MCP Tool from one Tool unit

## Applicable when

Apply **when** a validated active immediate Tool unit is selected for MCP exposure.

## Procedure

1. Derive one stable MCP identity from the canonical Tool identity.
2. Project the validated Tool contract **without** splitting, aliasing, **or** aggregating it.
3. Verify that no other source Tool projects **to** the same callable MCP identity.

## Outcome

One valid active Tool unit has exactly one unambiguous callable MCP projection.

## Failure or stop

Stop publication on a missing source, duplicate identity, alias, **or** attempted aggregation.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/05_method/CA-M-171-MCP-CORE-METHOD--reconcile-disabled-and-removed-tool-projections.md

SHA-256: c796e582973d4a99c7c5f6f5e4942070fa16a638fcb720ba44e7fe65fbace9bc

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "framework-engine-mcp"
  depends_on: []
version: 5
updated_at: 2026-08-30 16:44:07 +0400
relations:
  method_for:
    - CA-R-1109
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reconcile disabled and removed Tool projections

## Applicable when

Apply **when** the current Tool source set **or** its enablement decisions change.

## Procedure

1. Resolve the complete current source set **before** changing the registry.
2. Add newly eligible Tools, exclude explicitly disabled Tools, **and** remove projections **without** current sources.
3. Publish **only** the resulting complete set rather than retaining a separate allowlist.

## Outcome

the registry has no stale, disabled, **or** independently configured Tool projection.

## Failure or stop

Stop **when** source discovery is incomplete **or** **any** resulting projection cannot be classified.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/05_method/CA-M-172-MCP-CORE-METHOD--fail-closed-on-one-invalid-tool-projection.md

SHA-256: d30b8fc05452daa763c137c424897da5c2016739764998fb6d94b8544abb04eb

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "framework-engine-mcp"
  depends_on: []
version: 5
updated_at: 2026-08-30 16:44:07 +0400
relations:
  method_for:
    - CA-R-1110
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Fail closed on one invalid Tool projection

## Applicable when

Apply **when** registry generation detects an invalid selected Tool contract **or** projection.

## Procedure

1. Retain the complete candidate frontier **and** identify the first invalid source **or** projection field.
2. Emit explicit diagnostics for that defect **without** publishing a partial **or** misrepresented current registry.
3. Require a complete valid frontier **before** a later publication attempt.

## Outcome

MCP never presents a partial, silently skipped, **or** stale registry as current.

## Failure or stop

Stop publication **until** the invalid source **or** ambiguity is resolved.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/05_method/CA-M-173-MCP-CORE-METHOD--delegate-one-mcp-call-to-its-canonical-tool.md

SHA-256: c1a1d051105a02d8a74e32ae7b7c0555aed7102db540563b9c8864d3e8b6d540

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "framework-engine-mcp"
  depends_on: []
version: 5
updated_at: 2026-08-30 16:44:07 +0400
relations:
  method_for:
    - CA-R-1111
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Delegate one MCP call to its canonical Tool

## Applicable when

Apply **when** MCP receives one validated request for an exposed Tool.

## Procedure

1. Select the canonical Tool executable from the current registry.
2. Forward the admitted request **without** reimplementing target resolution, project meaning, validation, mutation, recovery, **or** lifecycle semantics.
3. Transport the Tool result as a Tool result, retaining **every** failure **and** side-effect boundary.

## Outcome

MCP is a transport boundary **and** the canonical Tool remains the sole operation owner.

## Failure or stop

Stop **when** canonical selection, request validation, **or** delegated execution fails; do **not** substitute MCP behavior.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/05_method/CA-M-174-MCP-CORE-METHOD--preserve-one-tool-contract-and-authority-boundary.md

SHA-256: ee20ff0a82e6749899cdd6556d42857b0c0a30248149b39fb52c8ce858d02a07

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "framework-engine-mcp"
  depends_on: []
version: 6
updated_at: 2026-09-01 01:55:00 +0400
relations:
  method_for:
    - CA-R-1112
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Preserve one Tool contract and authority boundary

## Applicable when

Apply while MCP adapts one canonical Tool request **or** result **to** protocol transport.

## Procedure

1. Implement MCP as a replaceable protocol adapter **and** keep project meaning
   **and** business decisions outside the carrier.
2. Preserve accepted inputs, results, diagnostics, failures, target-set identity, **and** side-effect controls exactly.
3. Pass a CAPRMEDIO Markdown Atom Doer's sealed target set, expected revision **or** digest, Initiative action, **and** receipt through unchanged.
4. Keep Finder, Checker, **and** Doer boundaries intact; do **not** infer approval **or** turn a failed **or** partial result into success.

## Outcome

Transport changes representation **only**, never Tool authority **or** semantics.

## Failure or stop

Stop whenever protocol adaptation would broaden authority, alter cardinality, **or** obscure a Tool failure.

## Sources

- [Model Context Protocol: base protocol](https://modelcontextprotocol.io/specification/2025-06-18/basic/index)
- [PEP 544 — Protocols](https://peps.python.org/pep-0544/)
- [CA-A-057 — Reconcile PROGRAMMATIC specialization authority](../../02_analysis/CA-A-057-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-programmatic-specialization-authority.md)
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/05_method/CA-M-175-MCP-CORE-METHOD--operate-one-project-local-provider-neutral-mcp-service.md

SHA-256: 1e898d7e3f427cb853da8c6dd04018771e08680e800fc60fa13ec972ee893367

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "framework-engine-mcp"
  depends_on: []
version: 5
updated_at: 2026-08-30 16:44:07 +0400
relations:
  method_for:
    - CA-R-1113
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Operate one project-local provider-neutral MCP service

## Applicable when

Apply **when** a project exposes its generated Tool surface through MCP.

## Procedure

1. Bind one provider-neutral project-local service **to** the current registry.
2. Expose each eligible Tool through that service **without** requiring a user interface **or** agent-host plugin.
3. Permit a plugin **to** package **or** connect **to** the service **without** moving provider-neutral MCP **or** Tool ownership into the plugin.

## Outcome

the complete MCP Tool surface remains headless, project-local, **and** provider-neutral.

## Failure or stop

Stop **when** an additional service becomes a competing authority **or** a capability depends on App presentation.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/05_method/CA-M-176-MCP-CORE-METHOD--regenerate-one-mcp-registry-deterministically.md

SHA-256: 0136615f852199b16e354f812194d115d5b9461f3bd9b2c294d6daf3fef32ff7

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "framework-engine-mcp"
  depends_on: []
version: 6
updated_at: 2026-08-30 16:44:07 +0400
relations:
  method_for:
    - CA-R-1114
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Regenerate one MCP registry deterministically

## Applicable when

Apply **before** publishing the MCP registry for a resolved project frontier.

## Procedure

1. Seal the complete current Tool-contract source frontier.
2. Order equivalent inputs stably **and** generate the registry from those inputs **only**.
3. Repeat generation against an unchanged frontier **and** compare semantic registry content while excluding volatile execution metadata.

## Outcome

the same current Tool contracts **and** project state produce the same MCP capability registry.

## Failure or stop

Stop **when** source sealing, ordering, identity, **or** repeated semantic output is **not** deterministic.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/05_method/CA-M-177-MCP-CORE-METHOD--bind-one-mcp-invocation-to-its-current-project-frontier.md

SHA-256: 8331b34517680b49b121372e4d8767576beff882584adc94c9a959a6e3007560

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "framework-engine-mcp"
  depends_on: []
version: 6
updated_at: 2026-08-30 16:44:07 +0400
relations:
  method_for:
    - CA-R-1115
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Bind one MCP invocation to its current project frontier

## Applicable when

Apply **when** an MCP service instance discovers **or** invokes an exposed Tool.

## Procedure

1. Resolve exactly one project root, selected installed Tool release, project-graph frontier, **and** MCP registry revision.
2. Include sufficient source **and** revision provenance **in** discovery **and** result records.
3. Reject cross-project path escape, unresolved identity, **or** a stale registry **before** Tool invocation.

## Outcome

**every** MCP operation is attributable **to** one current project **and** Tool frontier.

## Failure or stop

Stop at an unresolved **or** stale frontier; do **not** guess a project **or** release.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/05_method/CA-M-178-MCP-CORE-METHOD--negotiate-declared-mcp-protocol-capabilities.md

SHA-256: 50fefc88793d1af1e2891406217aefd862903b02792e04d1f687935e09197253

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "framework-engine-mcp"
  depends_on: []
version: 6
updated_at: 2026-09-01 01:55:00 +0400
relations:
  method_for:
    - CA-R-1116
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Negotiate declared MCP protocol capabilities

## Applicable when

Apply during MCP service initialization.

## Procedure

1. Declare the supported protocol revision **and** capability set.
2. Compare the peer's required revision **and** capabilities with that declaration.
3. Accept **only** a defined compatible mode **and** return machine-readable diagnostics for unsupported **or** invalid lifecycle states.

## Outcome

MCP initialization selects one explicit compatible protocol boundary.

## Failure or stop

Stop on an unsupported revision, incompatible required capability, **or** invalid lifecycle transition.

## Sources

- [Model Context Protocol: lifecycle](https://modelcontextprotocol.io/specification/2025-06-18/basic/lifecycle)
- [CA-A-057 — Reconcile PROGRAMMATIC specialization authority](../../02_analysis/CA-A-057-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-programmatic-specialization-authority.md)
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/05_method/CA-M-179-MCP-CORE-METHOD--bound-one-admitted-mcp-request.md

SHA-256: 01ce8f240c71f59d8c34f705fcb944b9e58bedaf09beb972a1e6e316aef247ef

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "framework-engine-mcp"
  depends_on: []
version: 7
updated_at: 2026-09-01 01:55:00 +0400
relations:
  method_for:
    - CA-R-1117
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Bound one admitted MCP request

## Applicable when

Apply **when** MCP receives one protocol message **before** Tool dispatch.

## Procedure

1. Validate the message against the admitted schema **and** assign its declared
   time **and** resource bounds.
2. Expose progress **only** for an admitted long-running operation.
3. On cancellation, expiry, invalid input, **or** resource exhaustion, stop with a structured outcome **and** preserve Tool **and** project state.

## Outcome

**every** MCP request has an explicit admission **and** completion boundary.

## Failure or stop

Stop **before** dispatch on an invalid **or** expired request **and** never leave an ungoverned background operation.

## Sources

- [Model Context Protocol: base protocol](https://modelcontextprotocol.io/specification/2025-06-18/basic/index)
- [Model Context Protocol: tasks](https://modelcontextprotocol.io/specification/2025-11-25/basic/utilities/tasks)
- [CA-A-057 — Reconcile PROGRAMMATIC specialization authority](../../02_analysis/CA-A-057-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-programmatic-specialization-authority.md)
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/05_method/CA-M-180-MCP-CORE-METHOD--preserve-least-authority-and-secret-boundaries.md

SHA-256: 4693da60a105830dbc7fdc94da17920999e5b9a546f3f6c01fe17050f9d87f85

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "framework-engine-mcp"
  depends_on: []
version: 6
updated_at: 2026-09-01 01:55:00 +0400
relations:
  method_for:
    - CA-R-1118
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Preserve least-authority and secret boundaries

## Applicable when

Apply **when** MCP projects a capability, forwards an invocation, **or** forms a result.

## Procedure

1. Grant no more authority than the source Tool requires **and** preserve its authorization checks.
2. Bind credentials **only** **to** their admitted transport **and** resource boundary.
3. Exclude secrets from discovery, results, diagnostics, logs, progress, **and** generated registries.

## Outcome

MCP exposes **only** the Tool's admitted authority **without** leaking credentials.

## Failure or stop

Stop the affected projection **or** invocation **when** authority is broadened **or** a secret-bearing representation would be emitted.

## Sources

- [Model Context Protocol: authorization](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)
- [CA-A-057 — Reconcile PROGRAMMATIC specialization authority](../../02_analysis/CA-A-057-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-programmatic-specialization-authority.md)
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/05_method/CA-M-181-MCP-CORE-METHOD--return-one-stable-model-readable-mcp-result.md

SHA-256: 288b626e386b56c63e9ad4307b63480b6fd85a0db83e2d8dda3ea5a2386ec6f5

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "framework-engine-mcp"
  depends_on: []
version: 5
updated_at: 2026-08-30 16:44:07 +0400
relations:
  method_for:
    - CA-R-1119
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Return one stable model-readable MCP result

## Applicable when

Apply **after** one canonical Tool returns an admitted outcome.

## Procedure

1. Map the Tool result, diagnostic, empty result, partial result, **or** failure **to** the declared protocol result form.
2. Preserve the original governed meaning **and** provenance.
3. Distinguish a protocol failure from a Tool failure **and** omit internal implementation details from the public response.

## Outcome

the model receives a stable, headless-readable result that retains the Tool outcome's meaning.

## Failure or stop

Stop **and** return an explicit protocol failure **when** the result cannot be represented **without** semantic loss **or** boundary leakage.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/05_method/CA-M-322-MCP--reload-through-isolated-implementation-generations.md

SHA-256: 02cd053bee4ab77671f3f1027d0330ed12c99a53c744c3ae8dd1431df211daba

```markdown
---
atom_id: CA-M-322
content_role: Method
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-03 20:41:31 +0400"
subjects:
  governs: "MCP/implementation"
  depends_on: [MCP, Tool, Operator, Project, Implementation, Workflow, Atom]
---
# Summary

Reload through isolated implementation generations

## Scope

server-side hot reload for the Project-local MCP gateway.

## Claim

the MCP implementation **must** prepare reload candidates in isolated generations **and** atomically select a validated generation for new dispatch.

## Details

1. keep the stdio gateway, protocol session, reload control **and** fixed Project binding stable.
2. load candidate code **and** dependencies in a separate local implementation process, rather than mutating live imported modules with importlib.reload.
3. initialize the candidate without starting Workflows, workers **or** source mutations; obtain its complete Tool contracts **and** validate names, schemas **and** the fixed Project binding.
4. switch new dispatch to the candidate **only** after validation succeeds; preserve the old generation for admitted calls.
5. drain retired generations **after** their admitted calls finish; expose a bounded drain failure rather than silently terminating uncertain effects.
6. when preparation fails, discard the candidate **and** keep the current generation. when a published generation later fails, report affected calls honestly; never replay a mutating call automatically.
7. serialize reload requests **and** suppress duplicate request IDs; an unchanged implementation frontier is a no-op.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/202_FEATURE_PROMPTS/05_method/CA-M-317-PROMPTS--separate-content-assessment-from-heading-recognition.md

SHA-256: b54377eb27c0b9d41dafb9918c512f6f21bf733c3689ce3041c39e74f8ee0dea

```markdown
---
atom_id: "CA-M-317"
content_role: "Method"
current_scope_unit: "PROMPTS"
claim_target_scope_unit: "PROMPTS"
local_tier: "Standard"
global_tier: 11
status: "Active"
author: "Anatoly Maslennikov"
version: 1
updated_at: "2026-10-03 06:25:11 +0400"
subjects:
  governs: "Prompt"
  depends_on:
    - "Atom"
    - "Property"
    - "Carrier"
    - "Scope"
    - "Atom/Claim"
    - "Atom/Details"
    - "Atom/Summary"
    - "Evaluation"
relations:
  relates_to:
    - CA-E-520
    - CA-R-1801
---
# Summary

Separate content assessment from heading recognition

## Scope

authoring the content-review instructions of the RMED review prompts.

## Claim

**to** implement local content assessment, use semantic reading of the complete carried text for content judgments **and** structural parsing for Property conformance, keeping the two judgments separate.

## Details

- instructions request actual quoted passages **and** an explanation of their semantic function, including applicability, contribution, supporting detail, **or** Summary.
- a missing heading is evidence of a Carrier defect; it is **not** evidence that readable content cannot be assessed. a semantic interpretation does **not** declare a missing Property section present.
- instructions distinguish independently replaceable Claims from clauses, examples, **or** conditions of the same Claim. they preserve useful content **when** proposing a correction.
- unresolved meaning **or** genuinely unavailable evidence is stated precisely for the affected check. a generic layout failure is insufficient justification for skipping readable content.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/202_FEATURE_PROMPTS/05_method/CA-M-326-PROMPTS--compose-short-current-implementation-step-prompts.md

SHA-256: 9d0e869f520e3a4ec086a25526fbaa1179e0c45547496319f8173f3f09b8133b

```markdown
---
atom_id: "CA-M-326"
content_role: "Method"
type: "Method"
current_scope_unit: "PROMPTS"
claim_target_scope_unit: "PROMPTS"
local_tier: "Standard"
global_tier: 11
status: "Active"
author: "Anatoly Maslennikov"
version: 1
updated_at: "2026-10-04 18:26:33 +0000"
subjects:
  governs: "Implementation step prompt construction"
  depends_on: ["Prompt", "Step", "Action"]
relations:
  relates_to: [CA-R-1843, CA-R-1845]
---
# Summary

Compose short current implementation Step prompts

## Scope

one self-contained prompt per current CA-O-016 Step.

## Claim

**to** implement one Step prompt, state its exact Step, Action, and context; name required inputs, permitted work, output artifacts, admitted result labels, and blocking conditions without restating methodology authority.

## Details

Keep each prompt concise, pin-aware, and scoped to its own Step. The caller owns transitions and dispatch; a prompt does not route future Steps or infer a pass.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/202_FEATURE_PROMPTS/05_method/CA-M-327-PROMPTS--stage-golden-e2e-tests-before-implementation-work.md

SHA-256: a0341d4f4193f54ac0729e21d8e5aa5651ab4126656c2b9fd77d72894b443eb2

```markdown
---
atom_id: "CA-M-327"
content_role: "Method"
type: "Method"
current_scope_unit: "PROMPTS"
claim_target_scope_unit: "PROMPTS"
local_tier: "Standard"
global_tier: 11
status: "Active"
author: "Anatoly Maslennikov"
version: 1
updated_at: "2026-10-04 18:26:33 +0000"
subjects:
  governs: "Implementation prompt test-first sequencing"
  depends_on: ["Prompt", "Evaluation", "Implementation"]
relations:
  relates_to: [CA-R-1844, CA-O-018, CA-O-019, CA-O-020]
---
# Summary

Stage golden E2E tests before implementation work

## Scope

the tests-first portion of a selected bounded implementation packet.

## Claim

**to** prepare implementation, first specify executable golden E2E cases from E authority and runnable baselines, then implement only the admitted R/D behavior and run the selected checks.

## Details

Mock external boundaries rather than the behavior under test. A baseline or expected initial failure is evidence for preparation, not a completed test or behavior pass.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/202_FEATURE_PROMPTS/05_method/CA-M-328-PROMPTS--diagnose-admit-and-repair-implementation-failures.md

SHA-256: 7118436c58535d74833897f30dbc15f9b902c947fe6be90f38b13673faabf30a

```markdown
---
atom_id: "CA-M-328"
content_role: "Method"
type: "Method"
current_scope_unit: "PROMPTS"
claim_target_scope_unit: "PROMPTS"
local_tier: "Standard"
global_tier: 11
status: "Active"
author: "Anatoly Maslennikov"
version: 1
updated_at: "2026-10-04 18:26:33 +0000"
subjects:
  governs: "Implementation prompt failure handling"
  depends_on: ["Prompt", "Evaluation", "Retry", "Evidence"]
relations:
  relates_to: [CA-R-1846, CA-O-095, CA-O-096, CA-O-099]
---
# Summary

Diagnose, admit, and repair implementation failures

## Scope

the diagnosed repair path after a selected Implementation Workflow check does not pass.

## Claim

**to** handle a failure, retain the actual failing evidence, diagnose its category, admit retry only through current permission/confidence/retry guards, repair the admitted defect, and return for renewed preparation or checking.

## Details

Changed failures, stale evidence, unavailable authority, or non-progressing work block. Repair preserves issue evidence and does not create or promote an M atom.
```

## .caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/202_FEATURE_PROMPTS/05_method/CA-M-329-PROMPTS--compile-and-reuse-the-active-method-projection.md

SHA-256: 036b3d064a8135ee9226ae325acab8f5eddf28c33917317957ef76ddc4379e9c

```markdown
---
atom_id: "CA-M-329"
content_role: "Method"
type: "Method"
current_scope_unit: "PROMPTS"
claim_target_scope_unit: "PROMPTS"
local_tier: "Standard"
global_tier: 11
status: "Active"
author: "Anatoly Maslennikov"
version: 1
updated_at: "2026-10-04 18:26:33 +0000"
subjects:
  governs: "Implementation prompt method projection"
  depends_on: ["Prompt", "Method", "Projection"]
relations:
  relates_to: [CA-R-1844, CA-O-017]
---
# Summary

Compile and reuse the active Method projection

## Scope

the derived active-M file passed through one selected implementation Run.

## Claim

**to** supply implementation method guidance, compile all active M atoms in the declared universe with full frontmatter, Markdown, identity, revision, path, and digest; verify membership and freshness, then retain the same file binding downstream.

## Details

Refresh only after authorized authority change. The file is not editable M authority and does not make unrelated methods applicable.
```

## .caprmedio_caprmedio/104_LAYER_4_CORE_EXTENSIONS/202_FEATURE_FPF/05_method/CA-M-290-FPF-METHOD--materialize-install-and-activate-the-fpf-extension.md

SHA-256: 9fcca961aafc9ce34b5a4a77043ac3e15cc4a84c648f272a3670235d0bb5ef69

```markdown
---
cce_version: cce_1
cce_form: method
subjects:
  governs: "FPF"
  depends_on:
    - "Extension Candidate"
    - "Installed Extensions Catalog Entry"
    - "Project Configuration"
    - "Tool"
    - "MCP"
    - "Skill"
version: 4
updated_at: "2026-09-15 02:22:01 +0400"
relations:
  method_for:
    - CA-R-1475
    - CA-R-1476
    - CA-R-1477
    - CA-R-1478
    - CA-R-1479
    - CA-R-1480
    - CA-R-1481
    - CA-R-1482
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Materialize, install, and activate the FPF Extension

## Applicable when

Use this Method **when** one accepted FPF overlay is ready **to** become an immutable project-local CAPRMEDIO Extension Candidate **or** **when** an installed Candidate is ready for a separately authorized activation.

## Procedure

1. Resolve **and** seal the current CAPRMEDIO Project, Applicable Methodology, Project Configuration, exact upstream FPF revision, complete upstream inventory, ordered overlay inputs, declared behavior changes, preserved behavior, affected paths, **and** acceptance Evaluations.
2. Materialize the overlay into a new immutable package, generate its exact source **and** result manifest **and** digests, **and** reject mutation of the upstream source, user-global installation, **or** an earlier materialized package.
3. Validate CAPRMEDIO terminology, Atom semantics **and** format, Scope Unit routing, Analysis Report placement, explicit Concern creation, Tool contracts, asynchronous boundaries, independent manual **and** automatic recovery controls, **and** direct `fpf` Skill behavior against the sealed frontier.
4. Install the validated Candidate by exact identity **and** version, record one Installed Extensions Catalog Entry **and** installation receipt, **and** leave its methodology authority inactive.
5. **after** separate Operator authorization, select that exact installed revision **in** Project Configuration, regenerate the active Tool frontier **and** MCP registry, **and** make the thin project-local `fpf` Skill available at the governed host path.
6. Start **or** reload the selected asynchronous service release **only** through its independent recovery entrypoint **and** at a recoverable boundary, **then** verify a fresh Codex session resolves direct `$fpf` invocation **and** preserves queued work, effect gates, **and** rollback boundaries.

## Outcome

One immutable, attributable FPF Extension revision is installed project-locally **and**, **only** **when** separately selected, active through current CAPRMEDIO authority **without** a `ca` wrapper.

## Failure or stop

Stop **before** installation **or** activation on an unresolved source, incomplete manifest, nondeterministic result, invalid CAPRMEDIO Atom **or** placement behavior, stale Tool **or** MCP frontier, blocking Hook path, unsafe lifecycle control, project/global collision, failed fresh-session selection, **or** unverifiable rollback.
```

