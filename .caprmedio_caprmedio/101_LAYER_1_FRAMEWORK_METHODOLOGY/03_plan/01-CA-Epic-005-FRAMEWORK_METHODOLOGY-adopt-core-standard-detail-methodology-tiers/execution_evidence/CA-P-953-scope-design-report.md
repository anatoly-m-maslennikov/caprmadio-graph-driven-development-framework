# CA-P-953 — Scope derivation independent of Local Tier

Non-authoritative design and execution evidence, updated 2026-09-10. The Operator decision below governs this design; this report does not replace active source authority. The worker changed only this report and sibling `CA-P-953-scope-design-cases.py`, without changing Task state, authoritative Atoms, Journals, Git, Tools, or projections.

## Decision record and result

The initial report stopped because the Principles did not uniquely choose a Scope basis. It recommended all active accepted Current-scope Requirements independent of Local Tier and presented an explicitly governed subset as the alternative. The Operator answered that proposal: **“yes, all active RMED atoms”**. This supersedes the R-only recommendation and resolves the material policy choice: include Requirement, Method, Evaluation, and Delivery, with Active as the lifecycle qualification and no tier filter.

The answered proposition's local ownership and Current-scope qualifications remain. The response expands the Content Roles; it does not authorize incoming Claims to acquire ownership, descendant aggregation, or removal of the Current-scope/Relational distinction. These retained boundaries follow CA-R-718, CA-R-923, CA-R-942, and CA-R-943 and require no new choice. No separate `accepted` flag is invented as an additional selector; canonical current Active revision status is used, with existing admission and provenance rules still governing how that status is obtained.

**The narrow CA-P-953 design DoD passes.** The selected policy, authoritative inputs, circularity treatment, and all required cases are specified below. Confidence is at least 99% for these bounded design consequences of the Operator's answer and the cited source rules. This is not a claim that the policy has been installed, every live Claim Scope has been resolved, or the corpus has been migrated.

## Exact Scope rule and authoritative inputs

Proposed replacement meaning for CA-R-931, with CA-R-716 requiring the same derivation:

> The Scope of a Scope Unit means the derived set of all current Active Atoms owned by that Scope Unit whose Content Role is Requirement, Method, Evaluation, or Delivery and whose Claim Scope is bound to that current Scope Unit's Scope, independently of Local Tier.

For review, let `U` be one structurally identified Scope Unit and `F` its verified authoritative source frontier. The derived basis is:

`S(U) = { a in F | owner(a) = U and current_status(a) = Active and role(a) in {R,M,E,D} and claim_scope_binding(a) = current(U) }`.

These symbols are explanatory notation, not new Entities, Properties, serialized fields, or Relations. `current(U)` names the existing current Scope Unit context before its derived set is materialized. The set retains the Atoms' own Content Roles and complete Claims; Methods, Evaluations, and Deliveries are not reinterpreted as Requirements or collapsed into one Claim.

Inputs are exact current authoritative Atom identities/revisions and digests; canonical ownership and structural-parent facts; qualified lifecycle status and Content Role; complete Claims, governed Subjects, explicit Scope constraints and Claim Scope expressions; and the existing default Claim Scope convention. Source completeness and coherence are checked before asserting a complete result. Generated copies and archived revisions are not second inputs. Local Tier, Global Tier, summary text, source-folder labels, and this evidence report cannot select or remove basis members.

## Binding order and circularity

1. Resolve the structural owner independently of Claim Scope. A reference to another Scope Unit does not change ownership (CA-R-718@10; CAPRMEDIO-META-REQU-706@14).
2. Resolve one Atom Scope from that context or the named Operator fallback, governed Entity, and explicit Claim constraints (CA-R-920@11; CA-R-1014@11; CA-R-930@10). Preserve the contextual components; do not equate Atom Scope with a directory address or Claim Scope.
3. Bind an omitted Claim Scope to `current(U)` under CA-D-367@2 and CA-E-240@18. Resolve an explicit expression from its authoring context and establish whether its target differs from current Scope without evaluating `S(U)` to decide its own members. A current-scope value must be omitted in a conforming Carrier; a different relational value must be explicit. A governed Subject or contextual content constraint alone is not a second structural owner or an instruction to widen Claim Scope. Contradictory explicit targeting cannot be discarded by applying the default.
4. Derive `S(U)` from the resulting local Active RMED bindings. CA-R-922@13 remains the semantic equality definition of Current-scope; the default is a contextual binding, not a recursive set-equation solver. Never determine the binding by selecting a highest tier or by testing whether an Atom already appears in the result being derived.
5. If an explicit composite or self-reference cannot be resolved independently, return an identified unresolved Claim Scope and withhold a complete Scope result. Do not choose a fixed point, assume set equality, silently omit the ambiguous Atom, or turn an incomplete frontier into an empty set. This is the specified expected-failure result, not an unresolved design choice.

Existing CA-R-1361@3 Canonical Scope Signatures cover only their restricted grammar and are non-authoritative. They do not prove arbitrary expression equivalence. This design does not extend that grammar or define a general CCE parser.

## Required cases and ownership boundaries

| Case | Determined result |
| --- | --- |
| Default | A valid omitted Claim Scope binds to the Atom's current unit. Every current Active local R, M, E, or D with that binding contributes, regardless of tier; P, C, A, I, and O do not. Draft and Archived revisions do not contribute. |
| Empty | With a complete coherent frontier and zero qualifying Atoms, `S(U)` is the empty derived set. The structural unit still exists; required Goals, inherited constraints, and other obligations are checked separately. Empty does not mean universal applicability or unrestricted authority. An unavailable, conflicting, or incomplete frontier instead produces an unresolved result (CAPRMEDIO-META-REQU-620@14 and -627@15). |
| Composite | One deterministic grouped Claim Scope remains one target. Preserve `and`/`or`, selected Entities, and explicit bounds. A resolved target different from the whole current Scope is relational and does not enter this unit's defining set, even when every selected Entity lies within the unit. A set of containing Scope Units is not a substitute for the selected Entities. Ambiguous grouping/equality is the identified failure above (CA-R-1271@4; CA-R-1364@4). |
| Inherited | Applicable ancestor authority remains effective under CAPRMEDIO-META-REQU-672@7 without becoming newly owned by the descendant. It constrains interpretation and permitted specialization separately from the local defining set. An empty child basis does not copy or become the parent's Scope. |
| Incoming Goal / Demand | The reference does not make the incoming Atom locally owned. A parent-owned Goal and a peer-owned Demand remain outside the target's local basis. The Goal states desired result without defining target Scope (CA-R-943@11; CAPRMEDIO-REQU-032@7). Demand obligations retain their exact producer-result boundary (CA-R-932@12; CA-R-933@10; CA-R-934@7). |
| Outgoing relational Atom | It is locally owned but has a different Claim Scope, so it is excluded from its owner's current-scope basis. Its relational authority remains effective at its declared target; exclusion from this defining set does not cancel its Claim. |
| Child / descendant | Atoms owned by a child contribute to that child's basis when qualified, not to the parent's. Aggregating descendants is the separately defined Scope-Tree Atom Set (CA-R-942@10); the Operator did not select that set as Scope. An Epic or lifecycle directory introduces no additional Scope Unit. |
| Task | A Task uses the same Atom Scope and Claim Scope, defaults to current scope, preserves explicit composite targeting, and cannot target an ancestor under the standing Operator instruction. Its Plan Content Role keeps it outside the RMED defining basis. No separate Task Scope entity is created. Existing CA-R-1000@8 / CA-E-245@14 terminology remains in the later authorized reconciliation queue. |

The Project external Goal keeps its named Operator Atom Scope and Project target under CA-R-927@13; it is not a locally owned Scope-defining Atom. Non-Project Goal ownership/target validation remains CA-R-925@13, CA-R-926@12, CA-R-1292@6, and CA-R-947@14. Demand ancestor/descendant prohibitions remain CA-R-935@10. None of these rules is weakened by broader RMED membership.

## Tier invariance and bounded verification

For fixed ownership, current status, Content Role, Claims, contextual components, and resolved Claim Scope bindings, any reassignment of Core / Standard / Detail leaves every predicate in `S(U)` unchanged. Therefore basis membership and the meaning supplied by those unchanged Claims remain unchanged. The proof does not rely on the current numerical tier ranking. Carrier paths, revision numbers, timestamps, and digests may change as migration evidence; that bookkeeping must not be mistaken for a change of semantic membership or Claim meaning.

The sibling finite model ran successfully with **21 named checks and all 81 independent tier assignments for four representative RMED Atoms**. It checks positive inclusion of each role, status/role exclusions, incoming and outgoing relations, descendants, inheritance, composite target preservation, empty bases, and expected failures for incomplete/contradictory sources, unresolved recursive bindings, and invalid default/explicit representations. It also proves that activation, archival, owner change, and Claim Scope change alter the basis explicitly; the model does not merely return one constant set.

Reproduce from the repository root:

```sh
python3 -B .caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/03_plan/01-CA-Epic-005-FRAMEWORK_METHODOLOGY-adopt-core-standard-detail-methodology-tiers/execution_evidence/CA-P-953-scope-design-cases.py
```

The script consumes pre-resolved fixture bindings and never reads or changes live authority. It verifies the specified membership boundary and tier invariance, not a production parser, general semantic equivalence, or an installed resolver. Migration from the old highest-tier R-only policy to the Operator-selected RMED policy can change the defining set by explicit decision. That authorized policy change is distinct from subsequent tier-only reclassification; this report does not assert old/new corpus-wide extensional equality.

## Live evidence and later authority reconciliation

CA-P-953@1 and its governing sources were reopened on resumption. All 13 active Project Principles were reread: CA-P-032@5, CA-P-033@9, CA-R-819@11, CA-R-1407@2, CA-R-1420@2, CA-R-1421@1, CA-R-1423@1, CA-M-001@9, CA-M-002@12, CA-M-005@7, CA-M-006@7, CA-M-261@2, and CA-E-001@9. CA-P-033 supports the Operator's decision; CA-M-002 and CA-M-005 support using the existing model without a new selector; CA-M-001 and CA-M-006 preserve coherent ownership/applicability distinctions; CA-E-001 and CA-M-261 require explicit checkable semantics. No Principle edit was made.

The frozen CA-P-952 inventory still identifies 705 source revisions with canonical records digest `816aece3b235322241c4107ba83966ddebf9a3723082e4f222fd546942512bc1`. The resumed bounded hash check passed **45 matches, 0 failures**: the original 33 revisions below plus CA-R-1309@5, CA-R-1315@6, CA-R-1395@3, CA-R-1396@3, CA-R-1397@2, CA-R-1398@2, CA-R-1399@2, CA-R-932@12, CA-R-933@10, CA-R-935@10, CAPRMEDIO-META-REQU-620@14, and CAPRMEDIO-META-REQU-627@15. Paths and digests remain in `CA-P-952-methodology-tier-frontier.projection.json`. This is not a semantic audit of all 705 Atoms.

The original 33 are CA-R-931@8, CA-R-716@14, CA-R-922@13, CA-R-1287@4, CA-R-659@9, CA-R-660@9, CA-R-718@10, CA-R-886@15, CA-R-919@11, CA-R-920@11, CA-R-923@14, CA-R-925@13, CA-R-926@12, CA-R-927@13, CA-R-942@10, CA-R-943@11, CA-R-1000@8, CA-R-1014@11, CA-R-1271@4, CA-R-1292@6, CA-R-1361@3, CA-R-1364@4, CA-R-930@10, CA-R-947@14, CA-R-1234@5, CA-R-1274@5, CA-R-1387@2, CAPRMEDIO-META-REQU-672@7, CAPRMEDIO-META-REQU-706@14, CA-D-367@2, CA-E-240@18, CA-E-245@14, and CA-E-428@2.

Later authorized authority work must replace CA-R-931/716's highest-tier R-only selection, make the default binding order explicit around CA-R-922 and CA-D-367/CA-E-240, and reconcile CA-R-1287/659/660 and CA-E-428 with the chosen tier meanings. CA-R-1234@5 continues to separate Core Local Tier from CORE_META_MODEL source ownership. Global Tier/precedence mappings belong to CA-P-954. Local Configuration remains expansion-only under the separately read CA-R-1207@6, CA-R-1218@5, and CA-R-1375@3 and cannot redefine this Core Meta-Model policy through configuration.

**DoD verdict: PASS for the reviewable CA-P-953 specification.** Authoritative inputs are identified; tier-only invariance is explicit and checked; default, empty, composite, inherited, and relational cases have determined outcomes including identified failure states. No material policy choice remains unanswered within this Task. Parent receipt/lifecycle handling and subsequent Tasks remain separate; this worker performed neither.
