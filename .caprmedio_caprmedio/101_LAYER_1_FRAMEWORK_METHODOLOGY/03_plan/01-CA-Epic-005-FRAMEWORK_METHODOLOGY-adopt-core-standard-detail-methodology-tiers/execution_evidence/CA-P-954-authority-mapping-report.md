# CA-P-954 — Core / General / Standard authority and Carrier mappings

Non-authoritative specification, updated 2026-09-10 from **CA-P-954@2**. **Mapping DoD: PASS.** The Operator accepted Core → General → Standard, Standard as lowest and omitted default, explicit CORE and GENERAL tokens, and derivation of Global Tiers from the structural hierarchy without a further arithmetic question. This supersedes this report's earlier pending Core / Standard / Detail recommendation. Source authority has not yet been changed; CA-P-955 supplies the independent classifier/admission gate before application.

## Decision interpretation and Scope

| Name in earlier material | Current interpretation |
| --- | --- |
| Proposed Core | Core: foundations and invariants. |
| Proposed middle Standard | General: shared specifications independent of concrete representation or implementation. |
| Proposed lowest Detail | Standard, abbreviated STD: concrete fields, syntax, procedures, and test cases. |
| Pre-change Core or Standard in the 705-Atom inventory | Historical classifications under the full-Scope/proper-part rule. Reclassify each Claim by the accepted meaning; neither old name determines its new tier. |
| Principle | Existing Project-only highest Local Tier. No additional Principle tier or automatic promotion is introduced. |

All 13 Project Principles were reread at their live revisions: CA-P-032@5, CA-P-033@9, CA-R-819@11, CA-R-1407@2, CA-R-1420@2, CA-R-1421@1, CA-R-1423@1, CA-M-001@9, CA-M-002@12, CA-M-005@7, CA-M-006@7, CA-M-261@2, and CA-E-001@9. Operator authority establishes the accepted choices; MECE, DRY, necessary complexity, coherence, reconstructability, and checkability support the bounded consequences below. None requires another question about accepted arithmetic.

Consume CA-P-953's selected rule unchanged: the Scope basis contains all current Active, locally owned, Current-scope RMED Atoms, independently of Local Tier. Ownership and Claim Scope binding precede basis derivation. Incoming and outgoing relational Atoms and descendant-owned Atoms stay outside that local basis; inherited authority remains separately effective. A complete empty basis is valid; incomplete or ambiguous input is unresolved. Reclassification alone does not change Claims, ownership, applicability, binding, or membership.

Replace CA-R-1287@4's breadth definition and CA-R-659/660@9's full-Scope/proper-part tier definitions with the accepted abstraction distinctions; add General. Replace CA-R-716@14 and CA-R-931@8's highest-tier Requirement selection with CA-P-953's RMED basis. Claim Scope remains a separate coordinate: a shared General specification may govern a bounded subject, and a Standard procedure may apply throughout its current Scope. Neither breadth nor reusability alone determines Local Tier.

## Complete structural and Goal mapping

Let d be the actual ancestry depth below the Project, whose Structural Level is 0. Resolve the authoritative parent chain before calculating a tier; names, directory prefixes, Epic containment, and lifecycle folders do not substitute for structural parentage.

| Admitted case | Pre-change mapping | New mapping |
| --- | --- | --- |
| External Project Goal | Global -1; no Local Tier; named human Operator context | Unchanged, including external ownership and the no-Local-Tier exception. |
| Project Principle | Global 0 | Unchanged; Project-only. |
| Project Core | Global 1 | Global 1 when its Claim qualifies as Core. |
| Project ordinary tiers | Core 1, Standard 2 | Core 1, General 2, Standard 3. |
| Non-Project Scope Unit at depth d | Core 2d+1; Standard 2d+2 | Core 3d+1; General 3d+2; Standard 3d+3. |
| Direct child | Core 3, Standard 4 | Core 4, General 5, Standard 6. |
| Grandchild | Core 5, Standard 6 | Core 7, General 8, Standard 9. |
| Non-Project Goal targeting depth d | Owned by direct parent; its Standard rank 2d | Same ownership, target, and Standard classification; rank 3d. |
| Siblings and branches | Same positions at equal depth, distinct ownership | Same rule; no authority edge follows from equal numerical ranks. |
| Unoccupied local tier / empty Scope basis | Tier positions derive structurally, not from occupied Atoms | All three positions remain; no compression or fabricated Atom is required. |
| Unknown owner, missing parent, cycle, or unanchored component | Cannot establish a coherent authoritative coordinate | Explicit unresolved/invalid result; no guessed rank or new Scope Unit. |

The recursive form is **child Core = parent Standard + 1; own General = own Core + 1; own Standard = own General + 1**. Parent Standard remains the last position in the parent block. This preserves CA-R-1390@2's parent boundary while replacing CA-R-1391@2's former two-position recursion and extending CA-R-1389@2. Update CA-R-680@12, CA-R-1385@2, CA-R-155@23, and CA-E-428@2 consistently; preserve CA-R-1386/1388/1393/1413@2 and the Goal ownership rules CA-R-925@13, CA-R-926@12, CA-R-927@13, and CA-R-1392@2.

The current Project contains no admitted negative-level Bootstrap units. CAPRMEDIO-META-REQU-679@12 reserves negative levels for explicitly admitted units outside that Project; that possibility does not create current-project ancestors or a second external Goal exception. An outside context without an applicable admitted authority anchor remains unresolved. Another Project resolves against its own Project anchor. This design neither admits Bootstrap units nor assigns them current-project authority.

For every historical non-Principle Atom, the old tier plus d gives its old rank; its independently established new semantic class plus d gives its new rank from the table. This is the explicit old-to-new mapping, not a fixed rename of old Core or Standard. Inserting General changes authority positions and can change same-scope precedence when old peers are reclassified. Record such semantic tier dispositions and relation impacts; do not present them as filename-only changes.

## Content Role, Type, and parentage dispositions

| Current authority | Required mapped disposition |
| --- | --- |
| CA-R-155@23, CA-R-1233@6, CAPRMEDIO-META-REQU-138@9 and GOV-REQU-685@11 | Keep one Local Tier for every Atom except the external Project Goal, with Principle restricted to Project and Core/General/Standard admitted otherwise. Content Role and Type remain separate coordinates. Extend eligible-tier parsing and checks to General. Keep Concern priority, Plan execution sequence, and Local Tier distinct; do not turn optional wording in the old role-routing rule into an exemption from cardinality. Limit reconciliation to affected tier clauses, without unrelated Epic refactoring. |
| All nine Atom Content Roles | Apply the same semantic tier distinction where the Atom has a Local Tier; an R/M/E/D letter does not force Core or Standard. Concrete Concern, Analysis, Plan, Implementation, or Ops instances ordinarily classify Standard from their Claims, not solely from their role. Native artifacts that are not Atoms acquire no Local Tier merely by being Implementation. Existing Project Principle designations remain separate. |
| CAPRMEDIO-GOV-REQU-756@10: Implementation Method only Core | Replace the exclusive Core gate with the accepted semantic classifier: a foundational realization invariant is Core; a shared representation-independent realization specification is General; a concrete reusable realization procedure is Standard. Retain the Method qualification from META-REQU-744@9. Reusability alone cannot force Core, and a procedure is not automatically an Implementation Decision. |
| CAPRMEDIO-GOV-REQU-757@10: Implementation Decision only Standard | Preserve the Standard restriction: this Type selects one concrete approach for a bounded realization target under META-REQU-744@9. Its numerical rank follows the new Standard block position. |
| CAPRMEDIO-META-REQU-766@7: eliminate all Method Standard and preserve only in Core | Remove the forced-empty-Standard endpoint and mandatory Core absorption target. Both conflict with the accepted place for concrete procedures and meaningful shared General specifications. Retain lossless consolidation only when independently justified by semantic coverage; META-REQU-745@7 already supplies the necessary archival precondition, so do not duplicate it. This is a specified semantic reconciliation, not an automatic retirement of arbitrary Methods or Decisions. |
| META-REQU-744@9, -745@7; GOV-REQU-758/759@9 | Preserve Method versus Decision versus Plan/Implementation distinctions, full preservation before absorption, orphan-permitted Decisions, and terminal-permitted Methods. No parent or intermediate General Atom is fabricated merely to fill a tier. |
| CA-R-794@14: Core evaluation policy / Standard concrete checks | Map foundational evaluation invariants to Core, shared representation-independent evaluation specifications and general case criteria to General, and concrete checks/test cases to Standard. Remove the old full-Scope/proper-part test. |
| CA-R-1429@1; CA-D-361@3 / -366@2; CA-E-446@2 | Settings purpose and foundational boundaries remain Core; independently governable shared settings specifications may be General; concrete sections, fields, and Carrier syntax remain Standard. Concrete TOML obligations do not become General because they are reusable. Preserve the settings-ownership distinctions. |
| CA-R-1231/1232@5, -1380@2, -1405@3, -747@17, -924@11; META-REQU-125@15; CA-E-425@3 | Preserve the qualified Type registries and relational admissions. “Core contribution” denotes source contribution, not a blanket Core-tier restriction on instances. No additional Type, relational Method, or relational Delivery is admitted by a tier change. |
| CA-R-796@11, CA-R-829@11, CA-R-808@11, CA-R-838@10 | Keep Requirement tier-parent links within the same Atom Scope, with the parent above the child in the accepted local order. Same-tier Current-scope Requirements remain peers. Preserve registered direction per relation family and reject cycles. Structural parentage is distinct from Atom tier parentage; neither implies a fabricated direct semantic edge. |

Scope exclusion does not erase a relational Claim. Goals keep the specific parent-Standard rule above; other admitted relational Atoms retain their declared target, role/Type restrictions, and semantic classification. Unresolved or mixed classification is an identified failure requiring classification/splitting review under CA-P-955 and subsequent per-Atom Tasks, not permission to use the default as a semantic guess.

## Expansion boundary and Carrier contract

CA-R-1234@5 separates CORE_META_MODEL source ownership from Core Local Tier. CA-R-1207@6, CA-R-1218@5, and CA-R-1375@3 continue to protect **every CORE_META_MODEL source Atom at Core, General, or Standard**. An Extension or Local Configuration may add only at an active source-authorized variation point; no tier permits replacement, shadowing, weakening, deletion, contradiction, reinterpretation, or mutation of source authority. A numerically higher-ranked local Claim does not bypass this prohibition. Inherited applicability remains separately effective under META-REQU-672@7; numerical precedence alone grants no override.

| Local classification | Canonical tier segment | Interpretation |
| --- | --- | --- |
| Principle | PRINCIPLE | Existing Project-only marker. |
| Core | CORE | Explicit marker. |
| General | GENERAL | Explicit marker. |
| Standard (STD) | Omitted | Lowest tier and ordinary default. STD is an abbreviation, not an explicit filename token. |
| External Project Goal | Absent | No Local Tier, rather than default Standard; recognize the Goal exception before ordinary omission. |

Extend CA-D-285@4 with GENERAL and retain the other segments. Explicit STD, STANDARD, DETAIL, or combined tier segments are not canonical. Parse the tier at its registered descriptor position after the Atom identity and current Scope owner; the CORE within CORE_META_MODEL is not a tier marker. Preserve the external Goal filename/reference forms in CA-D-292/342@7. Existing concrete Objective, Goal, and Task instances retain their bounded-target meaning and Standard omission, including the Objective form in CA-D-350@4; their identity, target, and sequence portions remain intact. A shared specification governing those Types is a separate specification Atom using its registered ordinary grammar, not a General token inserted into a concrete Objective, Goal, or Task instance.

A historical unmarked Carrier still decodes as historical Standard; it cannot be treated as proof of the new concrete classification. Record an explicit disposition before reclassifying or changing that Carrier. Preserve Atom identity, complete Claim, Claim Scope, Atom Scope, role/Type, status, provenance, and authored direct relations unless a separately recorded semantic revision requires a change. Compute and record old/new tier, rank, and impacted authority relations. CA-D-304@5 and CA-D-311@4 prohibit semantic change disguised as Carrier-only recoding. Do not manufacture identifiers, Principle designations, middle-tier duplicates, or shadow copies.

## Verification, application boundary, and result

All **705** current frontier Carrier hashes still match CA-P-952, and the current candidate path set under both source roots and the adjacent Goal root matches the recorded set after the same status/history and archive-basename exclusions. Frozen records digest: 816aece3b235322241c4107ba83966ddebf9a3723082e4f222fd546942512bc1. This establishes input freshness, not a semantic classification of the 705 Atoms.

The sibling CA-P-954-authority-mapping-cases.py passes **53 named checks**, **40 recursive depths**, and **81 independent Core/General/Standard assignments** through the reused CA-P-953 Scope model. Cases cover explicit expected ranks, Goal exceptions, sibling ownership, empty tiers, missing/cyclic structure, canonical and invalid tier segments, old-name/source-owner independence, Method/Decision gates, tier-parent boundaries, expansion prohibitions, and empty/incomplete Scope behavior. The model takes pre-resolved semantic qualifications; it does not claim to implement a production parser or independently prove the classifier boundaries. CA-P-955 owns that next gate.

Run from the repository root:

~~~sh
python3 -B .caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/03_plan/01-CA-Epic-005-FRAMEWORK_METHODOLOGY-adopt-core-standard-detail-methodology-tiers/execution_evidence/CA-P-954-authority-mapping-cases.py
~~~

Deferred runtime impact was verified in 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/atom_operations.py: LOCAL_TIERS at line 568 and filename parsing at line 596 admit only the old tiers; the upgrade check at line 607 rejects General. Those consumers and their tests need later governed reconciliation before operational use of GENERAL. No Tool or generated projection was changed.

**Mapping DoD: PASS at the 99% threshold.** Accepted choices, structural derivation, Goal placement, role/Type and parentage restrictions, default/token representation, and expansion limits have explicit dispositions. No further Operator policy choice is needed within this mapping. This is not source application, full classifier admission, corpus migration, or runtime closure. The worker changed only this report and its bounded case script; parent receipt and Task lifecycle handling remain separate.
