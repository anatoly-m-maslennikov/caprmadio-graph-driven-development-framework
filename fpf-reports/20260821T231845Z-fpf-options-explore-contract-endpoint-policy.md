## Task, scope, and boundaries

### Exploration contract and resolved FPF source

The question is which endpoint-domain policy best complements the now-protected Contract model: one controller-owned RMEDO Atom, one independently governed Claim, and one exact sibling target. :codex-annotation{index="1"}

The decision owner is the Operator. The receiving use is a later repair of the Bootstrap Seed Contract authority and current Contract carriers. This exploration does not decide the policy, edit authority, migrate carriers, implement validators, or perform Git work.

Protected constraints:

- A Contract is directional and binary: one controlling endpoint and one exact target endpoint.
- The controlling Scope Unit owns the Contract Atom.
- The controlling endpoint is derived from the Atom's owner rather than repeated as endpoint metadata.
- The target is a distinct sibling Scope Unit and remains explicit.
- Contract is orthogonal to Content role; any RMEDO Atom may carry a Contract when its primary meaning has that role.
- The registered predicate preserves direction, participant kinds, cardinality, and reference modes.

Declared comparison coordinates are separation of semantic axes, deterministic validation, expressive coverage, conceptual burden, migration cost, and reopenability. Semantic-axis separation, one-Claim atomicity, explicit direction, and exact participants are mandatory. Novelty is telemetry only. The baseline is the current common-scope, one-controller-plus-many-followers model.

Project evidence includes [CA-R-871](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/METAMODEL/04_requirement/CA-R-871-REQUIREMENT-BSEED_METAMODEL--distinguish-shared-authority-edges-and-relational-atoms.md:12), [CA-R-880](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/METAMODEL/04_requirement/CA-R-880-REQUIREMENT-BSEED_METAMODEL--define-contract-as-a-directional-relational-atom-family.md:12), [CA-R-873](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/SEMANTICS/04_requirement/CA-R-873-REQUIREMENT-BSEED_SEMANTICS--give-each-relational-atom-one-semantic-controller.md:11), [CA-R-874](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/SEMANTICS/04_requirement/CA-R-874-REQUIREMENT-BSEED_SEMANTICS--derive-relational-content-role-from-semantic-control.md:10), [CA-R-876](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/SEMANTICS/04_requirement/CA-R-876-REQUIREMENT-BSEED_SEMANTICS--separate-control-dependency-and-result-flow.md:12), and the CCE predicate-signature requirements in [CA-R-897](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/GOVERNANCE/04_requirement/CA-R-897-REQUIREMENT-BSEED_GOVERNANCE--register-cce-vocabulary-and-predicate-signatures.md:13).

The resolved FPF edition is the local First Principles Framework knowledge graph at source revision `f0b498ddfdf562242984ff7ab7a2557b55af6690`. Creative Abduction with NQD was used to retain mechanism-level alternatives without manufacturing a winner. A parity harness was not used because this compares architecture policies, not method implementations under an OEE/QD parity claim.

Campaign handoff:

- `campaign_id`: `controller-owned-contracts`
- Semantic frontier: controller-owned, binary Contract; RMEDO carrier role remains orthogonal; endpoint-domain restriction remains undecided.
- Carrier frontier: current live METAMODEL, SEMANTICS, GOVERNANCE, and twelve observed Contract carriers; no authority carrier changed.
- Evaluation profile: ownership, binary arity, role orthogonality, predicate typing, design/runtime separation, migration effects; runtime implementation and full migration are excluded.
- Predecessor: `fpf-reports/20260821T230917Z-fpf-design-challenge-controller-owned-contracts.md`
- Finding states: controller-owned placement `DECIDED`; binary target cardinality `DECIDED`; RMEDO carrier orthogonality `DECIDED`; global D–D/O–O restriction `OPEN` after the Operator withdrew tentative acceptance.
- Permitted next transition: Operator selection of an endpoint policy, followed by an authorized authority-repair batch.
- Stop condition: return a compared candidate set and recommendation without treating it as the project decision.

Saved report: `fpf-reports/20260821T231845Z-fpf-options-explore-contract-endpoint-policy.md`

## High-confidence results (>=95%)

### CandidateSet and provenance

#### Option A — Global homogeneous-plane restriction

Every Contract must connect two endpoints in the same globally defined plane, such as D–D or O–O. Cross-plane relations can never be Contracts.

- Strength: one simple global admission test.
- Cost: `D`, `O`, design/runtime phase, endpoint kind, and predicate semantics can become one overloaded classification axis.
- Risk: valid future predicates may require exceptions or a new Contract family.
- Provenance: the Operator's tentative D–D/O–O proposal, retained after its acceptance was withdrawn.

#### Option B — Predicate-typed binary Contract

The universal Contract rule governs only controller ownership, binary arity, sibling topology, atomic identity, and explicit direction. Each registered CCE predicate signature governs participant kinds and design/runtime Applicability. A predicate may require homogeneous endpoints; another predicate may reject or explicitly admit a cross-domain relation.

- Strength: keeps topology, Content role, endpoint kinds, phase, and relation meaning independent.
- Cost: every Contract predicate needs a complete signature and applicability rule.
- Risk: weak registries could make the model appear more permissive than it is.
- Provenance: composition of the protected constraints with CA-R-874, CA-R-876, and CA-R-897.

#### Option C — Two explicit Contract subfamilies

Define separate design-time and runtime Contract subfamilies. Both remain controller-owned, binary, and RMEDO-role-neutral, but each has its own endpoint and applicability rules.

- Strength: strong discovery and validation boundaries for design versus runtime use.
- Cost: adds taxonomy and forces every Contract through a family classification even when its predicate already supplies the distinction.
- Risk: subfamilies can duplicate predicate-signature semantics or create ambiguous boundary cases.
- Provenance: a structural refinement of the tentative D–D/O–O distinction.

#### Option D — Runtime-only Contract

Reserve Contract for runtime endpoint relations. Represent design-time authority and dependency through ordinary ancestor authority or typed edges.

- Strength: smallest and sharpest Contract concept.
- Cost: independently governed design-time cross-scope agreements lose Contract identity or require another relational family.
- Risk: users may recreate “design contracts” under inconsistent names.
- Provenance: combines CA-R-871's three representations with a strict runtime boundary.

#### Option E — Remove Contract as an authority family

Keep binary relational RMEDO Atoms and registered predicates, but derive “Contract” only as a discovery label or Projection.

- Strength: maximum ontological parsimony; the predicate fully determines meaning.
- Cost: loses an explicit authority-level family used for shared validation and discovery.
- Risk: Contract-specific lifecycle and review rules become scattered across predicates.
- Provenance: a deliberately more radical parsimony candidate.

### Declared-coordinate evaluation and diversity map

| Option | Axis separation | Deterministic validation | Coverage | Conceptual burden | Migration cost | Reopenability |
|---|---|---|---|---|---|---|
| A — global planes | Medium | High after D/O definitions exist | Medium | Medium | Medium | Low |
| B — predicate typed | High | High | High | Medium | Medium | High |
| C — two subfamilies | Medium-high | High | Medium-high | High | High | Medium |
| D — runtime only | High | High | Low-medium | Low | High | Medium |
| E — projection only | High | Medium | High | Medium | Very high | High |

These are separate coordinates, not an opaque score. Option B is the only candidate that remains on the current practical front across axis separation, validation, coverage, and reopenability without the taxonomy cost of C or the expressiveness loss of D. Option E remains an interesting long-horizon alternative but has excessive migration cost for the current frontier.

### Best-supported recommendation

**Option B is the better default for CAPRMEDIO at 97% confidence.** It preserves the user's controller-owned, one-to-one model while avoiding a premature universal D–D/O–O ontology. It also uses machinery already required by CCE: a predicate's arity, direction, participant slots, value kinds, cardinalities, reference modes, and Applicability can determine whether one exact Contract is valid.

The corresponding model is:

```text
Every Contract Atom belongs directly to its controlling Scope Unit.
Every Contract Claim relates its controlling Scope Unit to exactly one distinct sibling Scope Unit.
Every Contract Atom retains exactly one RMEDO Content role.
Every Contract predicate signature determines the admitted endpoint kinds and Applicability.
```

This does not mean “anything can be a Contract.” CA-R-871 still supplies the admission boundary: use shared ancestor authority for shared meaning, a typed edge for a relationship without independent governance, and a Contract Atom only when the relationship itself needs identity, revision, and lifecycle.

### Retained options, exclusions, and migration implications

- Retain Option C as a reopenable alternative if a large stable population of design-time and runtime predicates develops different lifecycle or validation rules.
- Retain Option D only if the Operator later decides that design-time relations never need independently governed Contract identity.
- Exclude role-based restrictions such as Delivery-only or Ops-only: the Operator explicitly clarified that a Contract may live in any RMEDO Atom in the controller.
- Exclude the current common-scope and multi-follower baseline: controller ownership and binary cardinality are already settled for this campaign.
- A live scan found ten root Contract carriers, seven with multiple followers, plus two Framework Engine Contract carriers. Binary migration therefore requires atom-by-atom splitting or reclassification; the endpoint policy should be decided before that work.

## Open questions (confidence <95%)

### What do `D` and `O` denote?

- **Best current answer:** They may denote description/design-side and object/operation-side endpoints, but the repository contains no governed expansion.
- **Confidence:** Below 90%.
- **Missing input:** The Operator's intended terms and boundary tests.
- **Consequence:** The framework cannot safely register D–D or O–O as vocabulary or validation categories.
- **Next action:** Define each term only if the selected predicate signatures actually need it. Option B does not require these global categories.

### Should design-time and runtime become named Contract profiles?

- **Best current answer:** Not initially. Derive them as registry or discovery projections from predicate Applicability; promote them only if they acquire different lifecycle, validation, or routing rules.
- **Confidence:** 92%.
- **Missing evidence:** A classified inventory of intended Contract predicates and their actual rule differences.
- **Consequence:** Premature profiles add taxonomy; delayed profiles may reduce discoverability temporarily.
- **Next action:** During Contract migration, classify predicates by applicability and compare their validation/lifecycle requirements.

### Decision handoff

The Operator can now select Option B without defining D/O globally. If selected, the next authorized work is a bounded authority repair covering CA-R-880, CA-R-873, CA-R-877, CA-R-883, CA-E-238, common-scope ownership authority, and current Contract carriers. This exploration itself authorizes none of those mutations.

## Skills used

- `fpf-options-explore` — generated and compared endpoint-policy alternatives without treating the recommendation as a project decision.

#### FPF sources consulted (1 read; 1 used)

- `FPF-Knowledge-Graph/B_Trans-disciplinary Reasoning Cluster/04_05_Canonical Reasoning Cycle/02_Abductive Loop/02_B.05.02.01 - Creative Abduction with NQD.md` — **used**: preserved mechanism-level alternatives, explicit evaluation coordinates, and a retained candidate set instead of collapsing immediately to one winner.
