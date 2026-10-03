## Task, scope, and boundaries

### Exploration contract and resolved FPF source

The question is which Content roles may carry a contract-typed Atom and which controller-role → subject-role combinations are valid. The clarified Contract distinction is structural-semantic rather than ontological: Contract is a role-local Atom Type used for an Atom owned by the current/controller Scope Unit whose one semantic subject is in exactly one other sibling Scope Unit. :codex-annotation{index="1"}

The decision owner is the Operator. The receiving use is a future revision of Contract Type registration, subject-scope semantics, CCE predicate signatures, validators, and current Contract carriers. This exploration is read-only and excludes authority mutation, carrier migration, validator implementation, and Git work.

Protected constraints:

- Every Atom has exactly one owning Scope Unit and one role-specific atomic unit.
- An ordinary Atom's subject Scope Unit is its owner.
- A contract-typed Atom's owner is the controller Scope Unit, while its subject is exactly one distinct sibling Scope Unit.
- The controller is derived from the carrier's owning Scope Unit.
- The sibling subject and its subject Content role are explicit.
- Every contract-typed Atom has one CCE Claim and one exact registered predicate.
- Content role classifies the Claim's semantic job; Contract Type only marks the sibling-subject exception and discovery class.

The comparison coordinates are semantic completeness, preservation of Content-role boundaries, runtime fidelity, deterministic validation, useful role-pair coverage, and conceptual cost. The baseline is the current Requirement-local `contract` Type plus a cross-role Contract family and explicit controller/follower endpoint structure.

Live methodology evidence:

- [Nine Content roles](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/SEMANTICS/04_requirement/CAPRMEDIO-META-REQU-111--nine-content-roles-with-plan.md:17) defines Requirement, Method, Evaluation, Delivery, Implementation, and Ops as different semantic jobs.
- [Role-specific atomicity](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/METAMODEL/04_requirement/CAPRMEDIO-META-REQU-132--define-role-specific-atom-atomicity.md:17) gives R, M, E, D, and O distinct atomic units.
- [Normative specification](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/SEMANTICS/04_requirement/CAPRMEDIO-META-REQU-091--normative-atoms-are-the-caprmedio-specification.md:15) identifies RMED as the normative specification.
- [Authority and Ops distinction](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/SEMANTICS/04_requirement/CAPRMEDIO-META-REQU-092--authority-evaluation-and-ops-remain-distinct.md:14) separates authority, implementation, enacted facts, evidence, and verification.
- [Evaluation chains](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/SEMANTICS/04_requirement/CAPRMEDIO-META-REQU-094--mechanism-neutral-evaluation-atoms.md:14) separates Evaluation authority, executable test implementations, and factual Ops results.
- [Runtime facts](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/SEMANTICS/04_requirement/CAPRMEDIO-META-REQU-143--classify-enacted-release-and-runtime-facts-as-ops.md:12) explicitly classifies deployment events, environment state, runtime health, and incidents as Ops.
- [Relational role derivation](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/SEMANTICS/04_requirement/CA-R-874-REQUIREMENT-BSEED_SEMANTICS--derive-relational-content-role-from-semantic-control.md:10) says endpoint positions do not determine the Atom's Content role.
- [CCE predicate signatures](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/GOVERNANCE/04_requirement/CA-R-897-REQUIREMENT-BSEED_GOVERNANCE--register-cce-vocabulary-and-predicate-signatures.md:13) can type exact participants, arity, direction, cardinality, and reference mode.

The resolved FPF edition is the local First Principles Framework knowledge graph at source revision `f0b498ddfdf562242984ff7ab7a2557b55af6690`. Creative Abduction with NQD was used to compare real policy mechanisms without treating a role matrix as selected authority. A parity harness was unnecessary because no implementation-method equivalence claim is being made.

Campaign handoff:

- `campaign_id`: `controller-owned-contracts-v2`
- Semantic frontier: Contract is now a role-local discovery and sibling-subject Type, not an independent semantic family; ownership and binary subject cardinality remain fixed.
- Carrier frontier: current live METAMODEL, SEMANTICS, GOVERNANCE, and observed Contract carriers; no authority carrier changed.
- Evaluation profile: carrier Content-role eligibility, controller-role → subject-role combinations, runtime semantics, sibling-subject invariant, and predicate typing; implementation is excluded.
- Predecessors: `fpf-reports/20260821T230917Z-fpf-design-challenge-controller-owned-contracts.md` and `fpf-reports/20260821T231845Z-fpf-options-explore-contract-endpoint-policy.md`.
- Finding states: controller ownership `DECIDED`; exactly one sibling subject `DECIDED`; Contract as discovery Type `DECIDED`; carrier-role set `OPEN`; role-pair admission policy `OPEN`.
- Permitted next transition: Operator selection of the carrier-role and role-pair policy, followed by an authorized authority repair.
- Stop condition: answer the role and runtime questions and return a recommended policy without selecting it for the project.

Saved report: `fpf-reports/20260821T232644Z-fpf-options-explore-contract-content-role-matrix.md`

## High-confidence results (>=95%)

### CandidateSet and declared-coordinate evaluation

#### Candidate A — RDO carriers with same-role subjects only

Admit only R–R, D–D, and O–O contracts.

- Benefit: small visible matrix.
- Loss: excludes Method interaction agreements and Evaluation boundaries even though both are first-class, independently governed meanings.
- Disposition in this exploration: dominated on semantic completeness and useful coverage.

#### Candidate B — RMEDO carriers with same-role subjects only

Admit R–R, M–M, E–E, D–D, and O–O, but no cross-role subject.

- Benefit: simple role equality validation.
- Loss: cannot directly represent an Evaluation owned by one tool or scope whose one subject is another scope's Method or Delivery interface.
- Disposition in this exploration: retained only as a simplicity-oriented alternative.

#### Candidate C — Every RMEDO × RMEDO pair is automatically valid

Admit all 25 directed role combinations.

- Benefit: maximum expressiveness.
- Loss: role pairs such as M–O or O–R become admissible without proving that the relation is a Contract rather than realization, evidence, observation, feedback, or ordinary typed-edge meaning.
- Disposition in this exploration: dominated on semantic precision and validation safety.

#### Candidate D — RMEDO carriers with predicate-registered directed role pairs

Admit `contract` as a role-local Type in RMEDO. Require each Contract predicate signature to register one exact controller Content role and one exact subject Content role. Same-role and cross-role pairs are both possible, but no pair is valid merely because both roles exist.

- Benefit: preserves all role distinctions while supporting real cross-role boundaries.
- Cost: every admitted Contract predicate needs a complete role-pair signature.
- Disposition in this exploration: practical front leader across completeness, validation, runtime fidelity, and reopenability.

#### Candidate E — RMED `contract` plus Ops `contract_observation`

Use `contract` only for normative RMED authority and use a separate Ops Type for factual runtime observations concerning a sibling.

- Benefit: makes the authority-versus-fact distinction visible in Type names.
- Cost: repeats a distinction already encoded by the Content role and weakens the simple rule that Contract Type means “subject is a sibling.”
- Disposition in this exploration: retained if human readers repeatedly mistake `ops:contract` for normative authority.

| Candidate | Role completeness | Runtime fidelity | Deterministic validation | Conceptual economy | Cross-role tool cases |
|---|---|---|---|---|---|
| A — RDO same-role | Low | Medium | High | High | Low |
| B — RMEDO same-role | Medium | High | High | High | Low-medium |
| C — all pairs automatic | High | Medium | Low | Medium | High |
| D — registered pairs | High | High | High | Medium-high | High |
| E — RMED plus Ops observation Type | High | High | High | Medium | High |

### Best-supported answer

**The carrier role should be RMEDO, not only RDO. Confidence: 98%.** Method and Evaluation have independent atomic meanings and can govern cross-scope boundaries. Excluding them would contradict the current role model.

**The role subjects should not be restricted to D–D or O–O, and they should not be restricted to same-role pairs. Confidence: 98%.** The best rule is Candidate D: each registered Contract predicate admits one exact directed pair.

The core model is:

```text
Every ordinary Atom has its owning Scope Unit as its subject Scope Unit.
Every contract-typed Atom has exactly one distinct sibling Scope Unit as its subject Scope Unit.
Every contract-typed Atom retains exactly one RMEDO Content role.
Every Contract predicate signature declares exactly one controller Content role and exactly one subject Content role.
```

The Type is role-local, so these are distinct coordinates even if the local Type token is always `contract`:

```text
requirement:contract
method:contract
evaluation:contract
delivery:contract
ops:contract
```

The Content role carries the semantics; `contract` carries only the sibling-subject and discovery meaning.

### Does CAPRMEDIO have runtime semantics?

Yes. Confidence: 99%. Runtime is not one universal Contract class:

- Method specifies how operation or transformation occurs.
- Evaluation specifies how behavior or results are checked.
- Delivery specifies release, target-environment, topology, and runtime-configuration rules without claiming enactment.
- Implementation is the executable mechanism.
- Ops records the actual execution, deployment, runtime state, health, incident, or result.

Therefore a runtime interaction may have an M contract governing the invocation protocol, an E contract governing its check, a D contract governing the delivered interface, an Implementation realizing them, and an O contract recording a factual sibling-subject observation. `O–O` is only one runtime case, not the definition of runtime.

### Role-pair examples

| Directed pair | Admissible example | Important boundary |
|---|---|---|
| M–M | One tool's Method invokes or composes a sibling tool's Method. | Valid only when the interaction rule needs independent identity and lifecycle. |
| E–E | One evaluation facility cross-checks or delegates to a sibling Evaluation. | Results remain Ops, not Evaluation authority. |
| E–M | An Evaluation owned by one tool checks a sibling tool's Method. | This is the usual classification for “one tool tests another tool's method.” |
| E–D | An Evaluation checks a sibling's delivered interface or availability rule. | The executable test is Implementation; its run result is Ops. |
| M–E | A Method deliberately invokes or consumes a sibling Evaluation capability. | Valid, but it is not the same direction or meaning as E–M. |
| D–D | One delivery boundary hands a deliverable or interface to a sibling delivery boundary. | A simple flow with no independent meaning should remain a typed edge. |
| O–O | One bounded runtime observation has a sibling operational subject. | It records a fact and cannot establish or modify RMED authority. |

Other pairs can be registered when their exact predicate passes the same test. The pair alone never proves Contract status.

### Admission test

A proposed contract-typed Atom is valid only when all are true:

1. Its carrier is owned by the controlling Scope Unit.
2. Its one subject resolves to exactly one distinct sibling Scope Unit.
3. Its Content role matches the Claim's primary semantic job.
4. Its predicate signature admits the exact controller-role → subject-role pair.
5. The cross-scope meaning needs independent identity, revision, and lifecycle.
6. Shared ancestor authority or an ordinary typed edge would lose material meaning.
7. Any Ops Claim remains factual and time-bounded and does not modify RMED authority.

This keeps “Contract” narrow without hard-coding a small role matrix.

### Retained options, exclusions, and evidence gaps

- Retain Candidate E as a naming fallback if `ops:contract` causes persistent human confusion.
- Exclude RDO-only because it removes valid Method and Evaluation contracts.
- Exclude D–D/O–O-only because same-role equality is unrelated to whether a sibling-subject Claim needs independent governance.
- Exclude automatic RMEDO × RMEDO admission because realization, evidence, flow, dependency, and observation relations are not Contracts by default.
- No parity plan/report was needed: these are semantic admission policies, not competing implementations claiming equivalent effect.

## Open questions (confidence <95%)

### Should Ops reuse the local Type token `contract`?

- **Best current answer:** Yes, initially. `(content_role, type)` is the complete role-local classification, so `ops:contract` is semantically distinct from `requirement:contract`.
- **Confidence:** 92%.
- **Missing evidence:** Actual authoring and retrieval experience after CCE migration.
- **Consequence:** Reusing the token keeps the sibling-subject rule uniform; a separate `contract_observation` token may improve human clarity but adds a second Type rule.
- **Next action:** Start with `ops:contract`; reopen only if readers or validators repeatedly conflate factual Ops with normative RMED authority.

### Must every Contract identify one exact target Atom as well as the sibling Scope Unit and role?

- **Best current answer:** Require an exact target Atom when the Claim concerns one independently identified subject; permit a role projection only when the Claim intentionally quantifies over that sibling role's governed set.
- **Confidence:** 93%.
- **Missing evidence:** Concrete CCE predicate fixtures for M–M, E–M, D–D, and O–O.
- **Consequence:** Always requiring an Atom is too narrow for role-wide interface rules; never requiring one can make a Contract subject ambiguous.
- **Next action:** Add `reference_mode` and target cardinality to each Contract predicate signature and test both exact-reference and role-projection fixtures.

### Decision handoff

The current best-supported policy is Candidate D. The Operator must still select it before authority changes. After selection, the next work is to redefine the Contract Type invariant, replace generic controller/follower metadata with one sibling-subject reference, register role-pair predicate signatures, and migrate current carriers atom by atom.

## Skills used

- `fpf-options-explore` — compared carrier-role and subject-role policies while preserving the controller-owned sibling-subject invariant.

#### FPF sources consulted (1 read; 1 used)

- `FPF-Knowledge-Graph/B_Trans-disciplinary Reasoning Cluster/04_05_Canonical Reasoning Cycle/02_Abductive Loop/02_B.05.02.01 - Creative Abduction with NQD.md` — **used**: retained structurally distinct role-policy candidates and compared them across declared semantic and operational coordinates.
