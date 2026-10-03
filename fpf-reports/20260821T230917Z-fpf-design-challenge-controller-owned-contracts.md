## Task, scope, and boundaries

### Proposal, resolved FPF source, and decision boundary

The proposal is to place each directional Contract Atom inside its controller Scope Unit, derive that controller from structural ownership, and let the Atom state a contract about another sibling Scope Unit. The affected entity is CAPRMEDIO's directional relational-Atom ownership and endpoint model. The receiving use is a possible redesign of Bootstrap Seed authority before CCE migration.

The current model instead places a relational Atom at the narrowest enabled common Structural scope of all endpoints, stores one explicit controller and one or more followers, and validates that common-scope placement. The model also has an unresolved high-priority Concern because the root Bootstrap Seed layers have no registered common parent. Project authority remains with the Operator; this review is read-only and does not accept or implement the proposal.

Project evidence inspected:

- [CA-R-880](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/_01_BSEED_LAYER_1_METAMODEL/04_requirement/CA-R-880-REQUIREMENT-BSEED_METAMODEL--define-contract-as-a-directional-relational-atom-family.md:12) defines Contract as a directional relational-Atom family rather than a role or universal Type.
- [CA-R-873](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/_02_BSEED_LAYER_2_SEMANTICS/04_requirement/CA-R-873-REQUIREMENT-BSEED_SEMANTICS--give-each-relational-atom-one-semantic-controller.md:11) requires one explicit controller and one or more followers.
- [CA-R-877](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/_03_BSEED_LAYER_3_GOVERNANCE/04_requirement/CA-R-877-REQUIREMENT-BSEED_GOVERNANCE--validate-directional-relational-atoms.md:13) requires common-scope ownership and complete endpoint descriptors.
- [CA-R-883](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/_03_BSEED_LAYER_3_GOVERNANCE/04_requirement/CA-R-883-REQUIREMENT-BSEED_GOVERNANCE--register-contract-endpoint-relations.md:11) encodes the controller and followers separately from typed graph relations.
- [CA-E-238](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/_03_BSEED_LAYER_3_GOVERNANCE/06_evaluation/CA-E-238-QA_CASE-BSEED_GOVERNANCE--validate-a-directional-contract-atom.md:15) tests common-scope ownership and multiple followers.
- [CA-C-101](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/_01_BSEED_LAYER_1_METAMODEL/01_concern/CA-C-101-QUESTION-BSEED_METAMODEL--what-scope-owns-relations-among-root-bootstrap-seed-layers.md:14) records the unresolved ownership failure for root Bootstrap Seed peers.
- [CNTR-022](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/04_requirement/CAPRMEDIO-CNTR-022--supply-metamodel-authority-to-semantics.md:9) and [CNTR-023](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio/04_requirement/CAPRMEDIO-CNTR-023--supply-cumulative-authority-to-governance.md:9) show one-target and multi-target current Contracts.

The resolved FPF edition is the locally generated First Principles Framework knowledge graph at source revision `f0b498ddfdf562242984ff7ab7a2557b55af6690`. Four direct patterns were inspected. The review stops after deciding whether controller ownership is structurally preferable and identifying the one unresolved cardinality decision. Runtime validator changes, carrier migration, projection refresh, and full-corpus effects are excluded.

Saved report: `fpf-reports/20260821T230917Z-fpf-design-challenge-controller-owned-contracts.md`

## High-confidence results (>=95%)

### FPF Challenge Findings

#### 1. Controller-owned placement is better for the current directional Contract family

- **Result state:** `no concern found within inspected scope`
- **Confidence:** 98%
- **Project evidence:** Contract is already directional and has exactly one semantic controller, but its carrier is placed at a common scope. That placement fails for the root Bootstrap Seed peers, producing the live unresolved Concern in CA-C-101.
- **Direct FPF basis:** A.6.6 says to recover the actual participants and direct relation first and warns against perspective flips that hide direction. A.6.5 requires exact participant meanings and designations. A.6.C requires contract wording to resolve into atomic claims rather than an undifferentiated contract object.
- **Reviewer inference:** When one endpoint is already the unique semantic controller, making that endpoint's Scope Unit the structural owner removes an otherwise artificial third location. It resolves CA-C-101 without inventing a Structural parent and makes outgoing authority locally discoverable.
- **Consequence:** Keeping common-scope ownership preserves a placement rule that has no valid owner for existing root-layer Contracts.
- **Candidate correction:** A directional Contract Atom belongs directly to its controlling Scope Unit. Its controller Scope Unit and controller Content role are derived from carrier ownership and the Atom's Content role.

#### 2. “One scope in the Atom” must mean one owner, not one relation participant

- **Result state:** `concern`
- **Confidence:** 99%
- **Project evidence:** Current Contracts state cross-scope relations and typed flows. Moving the carrier does not turn those relations into unary claims.
- **Direct FPF basis:** A.6.5 distinguishes a relation declaration, its participant meanings, and the references that designate actual participants. A.6.6 requires the actual participants and direction to remain recoverable.
- **Reviewer inference:** The controller may be implicit because it is deterministically derived from ownership, but every other endpoint must remain explicit in the CCE Claim or its registered predicate fillings. Otherwise placement silently erases relation arity.
- **Consequence:** Treating the Contract as genuinely one-scope would make the sibling, direction, and predicate truth conditions unrecoverable.
- **Candidate correction:** Say “one owning Scope Unit” rather than “one Scope Unit.” A Contract remains a relational Claim whose controlling participant is implicit and whose other participant designations are explicit.

#### 3. The generic `controller`/`followers` block becomes redundant under controller ownership

- **Result state:** `concern`
- **Confidence:** 96%
- **Project evidence:** CA-R-883 says `relational_endpoints` is not a graph relation, while the same carriers separately declare relation-specific targets such as `authority_input` and `depends_on`. CCE predicate signatures now provide ordered participant slots, kinds, cardinalities, direction, and reference modes.
- **Direct FPF basis:** A.6.6 recommends stating the direct relation first and adding reusable declaration machinery only for a concrete receiving use. A.11 requires composition through existing slots and relations before retaining another durable structural mechanism.
- **Reviewer inference:** Once ownership supplies the controller and the registered CCE predicate supplies the relation signature, a second generic endpoint structure repeats identity and can drift from the Claim and typed relation. Relation-specific participant names such as consumer/source are clearer than controller/follower.
- **Consequence:** Retaining both encodings creates two places that can disagree about endpoints and direction.
- **Candidate correction:** Derive relational shape, the controlling endpoint, and controller Content role. Keep only explicit target designations and any role projections that cannot be derived from the registered predicate signature.

### Strengths within inspected scope

The proposal aligns structural ownership with the unique semantic controller, resolves the current root-peer ownership hole, preserves one Atom and one CCE Claim, and reduces duplicated endpoint metadata. It also makes the existing examples read naturally: SEMANTICS owns the Claim that SEMANTICS consumes authority from METAMODEL, while GOVERNANCE owns its cumulative-authority Claim.

## Open questions (confidence <95%)

### Must every Contract have exactly one sibling target?

- **Best current answer:** Do not make binary cardinality universal yet. Permit one or more explicit sibling targets when the target set is an indivisible semantic filling, but split the Atom when one target relation can be revised, replaced, or terminated independently.
- **Confidence:** 92%.
- **Missing evidence:** An atom-by-atom replaceability review of the active Contract inventory. The live root inventory contains ten relational Contract carriers, seven of which currently have multiple followers; several express cumulative upstream sets rather than accidental bundles.
- **Consequence:** Unconditionally forcing one target would split cumulative contracts into many Atoms and could lose the single invariant that the controller consumes the complete upstream set. Unconditionally permitting lists could retain genuinely independent contracts in one Atom.
- **Exact next action:** The Operator must choose either binary Contracts or role-atomic target-set cardinality. Then test CNTR-017, CNTR-019 through CNTR-021, and CNTR-023 through CNTR-025 individually against the independent-replacement criterion.

### Unchecked claims and insufficient basis

This review did not inspect validator implementation coverage, projection-copy synchronization, every non-root Contract carrier, symmetric relations, parent-child relations, or migration mechanics. It therefore does not establish that controller-owned placement is already executable. Those questions return when implementation is proposed or after the target authority changes.

### Return to project authority

The Operator can safely choose controller-owned placement independently of the binary-versus-multi-target question. The smallest proposed authority statement is:

```text
EVERY directional Contract Atom belongs directly to its controlling Scope Unit.
```

The companion endpoint rule should remain undecided until the Operator chooses between exactly one sibling target and an indivisible target set. No current Atom has been changed by this review.

## Skills used

- `fpf-design-challenge` — challenged controller-owned Contract placement against current CAPRMEDIO authority and bounded FPF relation patterns.

#### FPF sources consulted (4 read; 4 used)

- `FPF-Knowledge-Graph/A_Kernel Architecture Cluster/06_Signature Stack & Boundary Discipline/03_A.06.C - Contract Unpacking for Boundaries.md` — **used**: contract wording must resolve into distinct atomic claims and exact objects.
- `FPF-Knowledge-Graph/A_Kernel Architecture Cluster/06_Signature Stack & Boundary Discipline/16_A.06.05 - Relation-Declaration Slot Discipline - SlotKind, ValueKind, RefKind, and participant-designation discipline.md` — **used**: relation participants and their designations must remain explicit and typed.
- `FPF-Knowledge-Graph/A_Kernel Architecture Cluster/06_Signature Stack & Boundary Discipline/17_A.06.06 - Base Declaration Discipline - Direct relation first; reusable declaration only when needed.md` — **used**: preserve direct relation direction and avoid redundant declaration machinery.
- `FPF-Knowledge-Graph/A_Kernel Architecture Cluster/11_Ontological Parsimony/00_A.11 - Ontological Parsimony.md` — **used**: prefer existing relation signatures and composition over duplicate structural mechanisms.
