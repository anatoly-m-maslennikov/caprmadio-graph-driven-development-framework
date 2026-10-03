---
atom_id: CA-A-043
subject_scopes:
  - authority
  - requirement-topology
  - scope-topology
  - carrier-format
version: 1
updated_at: 2026-08-21 01:52:33
---

## Task, scope, and boundaries

Audit target: the current filesystem state of CAPRMEDIO at Git baseline `3730084a`, including the uncommitted identity migration now present in the worktree.

Audit contract:

- Level 0: all 76 active RMED Atoms—75 Requirement Atoms and one Evaluation Atom.
- Level 1 META: all 43 active Core RMED Atoms.
- Level 2 GOV: the one active Core RMED Atom.
- Total governed carriers audited: 120.
- The Project Goal was used only as the required parent of Project Principles; it was excluded from Level 0 because current authority places Goal outside Project Structural level `0`.
- Archived, draft, done, and solved carriers were excluded.
- Level 1–2 Standards and downstream SPEC artifacts were read only where a scoped claim depended on them; they were not independently audited.
- REALIZATION, FIELD, settings carriers, generators, tests, deployment state, and repository acceptance were excluded.
- No tests were run. Evidence came from carrier reads and deterministic, read-only graph/frontmatter scans.

Evaluation question: Are the scoped RMED Atoms coherent, irreducible, correctly owned and classified, mechanically conformant, and aligned with the bounded FPF patterns relevant to authority hierarchy, semantic identity, carrier separation, structural composition, flow, and improvement?

Verdict states: `supported`, `unsupported`, or `insufficient basis` within this boundary. This report is an Analysis artifact only; it changes no CAPRMEDIO authority.

Saved report: `fpf-reports/2026-08-18T175430Z-fpf-alignment-audit-level-0-rmed-level-1-2-cores.md`

## High-confidence results (>=95%)

### Bounded verdict

Overall verdict: **unsupported**.

The scoped authority is substantially more coherent than in prior passes, and its strict graph topology now passes every bounded structural check. Full alignment is nevertheless unsupported because four blocker classes remain: contradictory structural-scope ownership, invalid META Subject values, incomplete Principle navigation metadata, and reducible or duplicated Core meaning.

### Per-claim alignment matrix

| Audited claim family | Verdict | Evidence |
|---|---|---|
| Strict authority topology | supported | Across the 120 scoped Atoms: zero parentless Atoms, zero childless scoped Principles/Cores, zero same-scope same-tier `child_of` edges, zero illegal scoped tier-direction edges, zero missing scoped `child_of` targets, and zero `child_of` cycles. |
| Basic carrier conformance | supported | Every scoped Atom has exactly one `subject_scopes` value, positive integer `version`, readable `updated_at`, non-legacy relation encoding, no explicit default `tier: standard`, and no duplicate active identity. Semantic vocabulary validation is reported separately below. |
| Tier hierarchy and conflict direction | supported | Project tier authority, META derivation, and current parent edges form one acyclic ordered ladder. This is consistent with FPF E.3’s requirement for explicit, acyclic precedence rather than a flat principle list. |
| Semantic-role and carrier separation | supported | META distinguishes Artifact, Carrier, Revision, Content role, Artifact form, authority, applicability, currentness, and realization; GOV Core requires faithful representation. This is consistent with FPF E.10.D2 and C.2.1. |
| Continuous-improvement boundary | supported | Project authority separates observations, proposals, RMED changes, implementation, delivery, and later evaluation, and requires an exact comparison frame before claiming improvement. This is consistent with FPF E.23. |
| Structural-scope ownership | unsupported | Project Standards encode all Layer scopes at Project level while the governing Core assigns each child scope to its immediate parent. |
| META Subject classification | unsupported | Six active META Cores use values outside META’s closed Subject vocabulary. |
| Semantic irreducibility and DRY | unsupported | Four scoped carriers retain independently removable procedure, restatement, or duplicated authority. |
| Principle navigation metadata | unsupported | One of 14 active Project Principles lacks the required contiguous `principle_order`. |

### Blocker 1 — Project ownership rules contradict the current scope carriers (99%)

[REQU-032](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/04_requirement/CAPRMEDIO-REQU-032--assign-immediate-child-scope-ownership.md:17>) requires each structural scope to own the definitions of its immediate children. In the current hierarchy, Project’s immediate child is META, META’s is GOV, and GOV’s is SPEC. However [REQU-008](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/04_requirement/CAPRMEDIO-REQU-008--define-project-scope-boundary.md:14>) says Project owns all concrete Layer scopes, and the META, GOV, and SPEC scope definitions are all Project-level Standards: [REQU-015](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/04_requirement/CAPRMEDIO-REQU-015--define-meta-layer-scope.md:16>), [REQU-016](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/04_requirement/CAPRMEDIO-REQU-016--define-gov-layer-scope.md:16>), and [REQU-017](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/04_requirement/CAPRMEDIO-REQU-017--define-spec-layer-scope.md:16>).

The current carriers therefore implement the accepted Project-owned Layer-scope model, while REQU-032 still asserts recursive immediate-parent ownership. FPF C.13 requires a construction account to identify one consistent whole, constituent relation, and ownership rule; both rules cannot govern the same hierarchy simultaneously.

Recommended repair: preserve the latest Project-ownership decision. Replace REQU-032 with the narrower rule actually intended for descendant scope families—most notably SPEC’s ownership of Feature definitions and Feature contracts—and reparent REQU-015 through REQU-017 to the Project scope/structural-level authority that owns them.

### Blocker 2 — Six META Cores violate the closed META Subject vocabulary (100%)

[META-175](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-175--use-canonical-meta-subject-scopes.md:18>) declares a closed ten-value vocabulary. Six scoped Cores use unregistered values:

- `requirement-topology`: [META-156](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-156--govern-tier-preserving-requirement-relations.md:3>), [META-176](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-176--derive-global-tier-number-from-structure-and-applicability.md:3>), and [META-680](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-680--enable-a-local-tier-subset-for-each-structural-level.md:3>).
- `subject-scope`: [META-157](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-157--narrowest-common-scope-ownership.md:3>).
- `extension-model`: [META-160](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-160--govern-extension-semantics.md:3>) and [META-687](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-687--govern-project-adaptation-semantics.md:3>).

These are carrier-level violations, not a reason to expand the vocabulary: META-175 already assigns structural levels, labels, Extensions, Project Adaptations, inheritance, and recursive applicability to `scope-topology`, and precedence to `authority`.

Recommended repair: migrate META-157, META-160, META-176, META-680, and META-687 to `scope-topology`; classify META-156 as `authority` because its primary claim governs Requirement-parent legality and precedence.

### Blocker 3 — the Project Principle order is incomplete (100%)

[GOV-330](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/200_LAYER_2_GOV/04_requirement/CAPRMEDIO-GOV-REQU-330--order-project-principles-for-navigation.md:14>) requires every active Project Principle to carry a unique, contiguous positive `principle_order`. Thirteen Principles carry values `1–6` and `8–14`; [REQU-003](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/04_requirement/CAPRMEDIO-REQU-003--apply-dry-across-caprmedio.md:2>) carries no order. Assigning `principle_order: 7` repairs the only gap without changing authority or conflict precedence.

### Blocker 4 — semantic irreducibility and DRY remain incompletely applied (97–100%)

Four scoped carriers still contain meaning that can be removed or changed independently of their named claim:

1. [REQU-006](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/04_requirement/CAPRMEDIO-REQU-006--minimal-default-project-model.md:15>) combines the minimum Project model, the absence of an Implementation-Atom obligation, and a general “enable only when necessary” rule. The last clause duplicates [REQU-005](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/04_requirement/CAPRMEDIO-REQU-005--necessary-complexity-only.md:18>), while Requirement’s mandatory status is already owned by [META-124](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-124--make-requirement-the-only-universally-mandatory-atom.md:16>). Retain only the minimum-model boundary and its necessary clarification that real Implementation does not require an Implementation Atom.
2. [META-096](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-096--propagate-caprmedio-change-forward.md:17>) mixes a Requirement outcome with a four-step reconciliation procedure and several downstream accountability rules. FPF E.18 keeps a selected flow structure distinct from a procedure, work plan, performed work, and result. Retain the forward-only impact obligation in the Core; move the numbered traversal/closure procedure to a Method and its conformance checks to Evaluation.
3. [META-156](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-156--govern-tier-preserving-requirement-relations.md:17>) duplicates direct-only relation storage and derived transitive ancestry already owned by [META-121](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-121--store-only-direct-semantic-relations.md:16>). Keep META-156 limited to legal tier/scope direction and the strict-versus-casual legality boundary.
4. [META-118](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-118--let-the-dependent-atom-own-the-relation.md:15>) states dependent-side storage twice and embeds an explanatory Content-role-order example between the two statements. Keep one compact dependent-owner rule; move the explanation to Analysis if it remains useful.

These defects directly violate CAPRMEDIO’s own DRY Principle and [META-154](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-154--semantic-irreducibility.md:15>). They also weaken recoverable FPF separation among claim, method, work, and carrier.

### Confirmed non-blocking strengths

- The 14 Project Principles are mutually distinguishable at their current primary-claim boundaries; no further Principle split or merge is supported by this audit.
- The Goal → Principle → Core → Standard parent topology is complete in the scoped strict areas, but this is only a necessary structural condition and does not prove Principle-set sufficiency.
- The global tier ladder is internally coherent: Goal `-1`; Project `0–2`; META `3–4`; GOV `5–6`; SPEC `7–8`; SPEC Feature `9–10`. No scoped Atom stores a redundant numeric global tier.
- Framework, Extension, and Project Adaptation meanings are separated without making Extensions relational objects; application remains a relation, consistent with FPF distinction discipline.
- Continuous improvement now has the essential E.23 boundaries: operator-requested proposal, distinct stages, narrowest affected owner, exact baseline, evaluation frame, protected trade-offs, and stop/continue condition.
- GOV-345 correctly treats carrier structure as faithful representation rather than a second semantic owner, consistent with FPF E.10.D2 and C.2.1.

### Stop condition

Repeat this bounded audit after the four blocker classes are repaired. A clean rerun requires: one consistent structural-scope owner rule; all scoped META Subject values inside the closed catalog; contiguous Principle navigation order; and no independently removable meaning in REQU-006, META-096, META-118, or META-156.

## Open questions (confidence <95%)

1. **What exactly does `Layer` denote after Structural levels became the authority-bearing abstraction? — 92%.** [REQU-001](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/04_requirement/CAPRMEDIO-REQU-001--ordered-realization-topology.md:15>) and REQU-040 govern “Project Layers,” while META-171 makes labels such as Layer and Feature non-authoritative. If `Layer` means a configured label, these Requirements should use `Structural level`; if it denotes a separate concrete project construct, that construct still needs an explicit boundary.
2. **Is an ordinary unversioned `child_of` edge only a current-topology relation, or also a traceability assertion? — 93%.** [META-107](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/100_LAYER_1_META/04_requirement/CAPRMEDIO-META-REQU-107--bind-traceability-to-exact-claims-and-revisions.md:16>) requires exact revisions for every traceability assertion after revision one, while GOV-327 permits ordinary relation targets as filename stems. The model is coherent if ordinary edges declare current topology and Journals own exact relied-upon revisions; it conflicts if ordinary edges themselves assert historical reliance. The boundary should be stated explicitly.
3. **Does REQU-046 require automatic improvement, or only eventual improvement after an operator-requested proposal? — 92%.** [REQU-046](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/04_requirement/CAPRMEDIO-REQU-046--improve-from-observed-project-outcomes.md:16>) says CAPRMEDIO “must convert” material outcomes into improvement, while [REQU-052](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/04_requirement/CAPRMEDIO-REQU-052--propose-improvement-cycles-only-on-operator-request.md:16>) permits only an operator-requested proposal. The likely intended reading is eventual governed improvement after operator authorization, but the Principle should not imply automatic initiation.

## Skills used

- `fpf-alignment-audit` — bounded the target, fixed the audit contract before reading, separated direct FPF patterns from supporting discovery material, prohibited authority mutation, and required this persisted report.

Direct FPF patterns used, six total:

1. [E.3 — Principle Taxonomy & Precedence Model](</Users/am/Documents/My_Repos/levenchuk-fpf-knowledge-graph-toolkit/FPF-Knowledge-Graph/E_The FPF Constitution and Authoring Guides/02_03_Principle Taxonomy & Precedence Model/00_E.03 - Principle Taxonomy & Precedence Model.md:27>) — explicit hierarchy, deterministic precedence, and acyclicity.
2. [E.10.D2 — EntityOfConcern, Description Episteme, and Specification-Use Discipline](</Users/am/Documents/My_Repos/levenchuk-fpf-knowledge-graph-toolkit/FPF-Knowledge-Graph/E_The FPF Constitution and Authoring Guides/09_10_Unified Lexical Rules for FPF/05_E.10.D2 - EntityOfConcern, Description Episteme, and Specification-Use Discipline.md:32>) — entity/description/specification/carrier/work separation.
3. [C.2.1 — U.Episteme Constitution, Empirical Grounding, and Edition Relations](</Users/am/Documents/My_Repos/levenchuk-fpf-knowledge-graph-toolkit/FPF-Knowledge-Graph/C_Kernel Extension Specifications/00_02_Epistemic holon composition (KD-CAL)/01_C.02.01 - U.Episteme- Constitution, Empirical Grounding, and Edition Relations.md:67>) — exact claim identity, carrier separation, and edition succession.
4. [C.13 — Constructional Mereology](</Users/am/Documents/My_Repos/levenchuk-fpf-knowledge-graph-toolkit/FPF-Knowledge-Graph/C_Kernel Extension Specifications/03_13_Constructional Mereology (Compose-CAL)/00_C.13 - Constructional Mereology (Compose-CAL).md:42>) — consistent whole/constituent/relation/identity construction accounts.
5. [E.18 — Transformation Flow Structure](</Users/am/Documents/My_Repos/levenchuk-fpf-knowledge-graph-toolkit/FPF-Knowledge-Graph/E_The FPF Constitution and Authoring Guides/17_18_Transformation Flow Structure/00_E.18 - Transformation Flow Structure.md:45>) — structure versus procedure, planned work, performed work, and results.
6. [E.23 — Quality Improvement Loop Method](</Users/am/Documents/My_Repos/levenchuk-fpf-knowledge-graph-toolkit/FPF-Knowledge-Graph/E_The FPF Constitution and Authoring Guides/22_23_Quality Improvement Loop Method/00_E.23 - Quality Improvement Loop Method.md:36>) — versioned improvement target, rerunnable evaluation, protected trade-offs, proposal/work separation, and stop conditions.

Supporting FPF discovery material screened:

- [E.11.PUA — Pattern Use in a Working Situation and First Useful Result](</Users/am/Documents/My_Repos/levenchuk-fpf-knowledge-graph-toolkit/FPF-Knowledge-Graph/E_The FPF Constitution and Authoring Guides/10_11_Practical-Use Guidance and Pattern Discovery/01_E.11.PUA - Pattern Use in a Working Situation and First Useful Result.md>) — applicability framing.
- [E.11.PUR — Pattern-Use Applicability, Recommendation, and Coordination](</Users/am/Documents/My_Repos/levenchuk-fpf-knowledge-graph-toolkit/FPF-Knowledge-Graph/E_The FPF Constitution and Authoring Guides/10_11_Practical-Use Guidance and Pattern Discovery/02_E.11.PUR - Pattern-Use Applicability, Recommendation, and Coordination.md>) — bounded pattern selection and coordination.

<oai-mem-citation>
<citation_entries>
MEMORY.md:76-79|note=[Used prior one claim and projection boundary decisions to guide live checks]
MEMORY.md:94-107|note=[Used prior tier settings and live verification cautions]
</citation_entries>
<rollout_ids>
</rollout_ids>
</oai-mem-citation>
