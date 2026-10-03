## Task, scope, and boundaries

**Recommendation: adopt the narrow model.** A Contract should be only a `requirement:contract` Atom: one controller-owned Requirement claim about one exact Delivery endpoint in one other Scope Unit.

The important correction is ownership. If feature siblings must be independent, an ordinary Feature Scope Unit must not own a Contract about a sibling Feature Scope Unit. The parent or composition controller should own the Contract and target one child feature's Delivery endpoint. If one parent composes two features, it owns two separate Contract Atoms—one per target endpoint—not one feature-to-feature Contract.

Canonical shape:

```text
Contract Atom
  owner: one parent or composition controller Scope Unit
  content_role: requirement
  type: contract
  claim: one required outcome
  subject: one exact Delivery Atom in one directly controlled Scope Unit
```

Here, “Delivery endpoint” means the outward Delivery boundary specified by the target D Atom. It does not mean runtime state, a network endpoint specifically, or the target feature's Method, Evaluation, Implementation, or Ops.

The inspected boundary was the current Contract/relational-Atom authority, CAPRMEDIO role definitions, and the proposed restriction from a cross-role Contract family to R-to-D only. No authority rewrite, validator change, migration, formula deletion, or Git operation was performed.

Campaign handoff: this is a new semantic frontier, `controller-owned-contracts-v3`. Its predecessors are `20260821T230917Z-fpf-design-challenge-controller-owned-contracts.md`, `20260821T231845Z-fpf-options-explore-contract-endpoint-policy.md`, and `20260821T232644Z-fpf-options-explore-contract-content-role-matrix.md`. Controller ownership, one target, and `contract` as a role-local Type remain accepted inputs; R-only carrier and D-only subject are the proposed narrowing.

## High-confidence results (>=95%)

1. **No concern found within inspected scope — adopt `Contract = R -> D` (99%).** The model has a sharp inclusion test: a Contract is one Requirement that constrains one Delivery endpoint outside its owning controller scope. M-to-M, E-to-E, M-to-E, runtime, evidence, and implementation relations are not Contracts. They remain ordinary Methods, Evaluations, Ops, Implementations, or typed edges. This is simpler for authors, LLMs, and validators and already matches the registered role-local Type `requirement:contract` in `CAPRMEDIO-GOV-REQU-747`.

2. **No concern found within inspected scope — treat D as the exposed endpoint specification (98%).** The target D Atom owns how the feature's realized deliverable crosses its boundary. The Contract R states what the composition controller requires from that boundary. This preserves realization-agnostic Requirements: the R may constrain the observable outcome but may not prescribe the target feature's internal Method, code, test, or Ops.

3. **Concern — do not encode ordinary sibling-feature dependence (99%).** A Contract owned by Feature A about sibling Feature B would make A depend on B and contradict the stated independence rule. The clean repair is parent/controller ownership. The target feature publishes its D endpoint without knowing its consumers; the composition controller owns any requirement placed on that endpoint.

4. **No concern found within inspected scope — keep the relation atomic and 1-to-1 (99%).** One Contract Atom should identify exactly one target D Atom and state one required outcome. Multiple target endpoints require multiple Contract Atoms. A target feature may have multiple D Atoms, but each Contract selects exactly one.

5. **Concern — current authority does not yet express this model (99%).** The live atoms still define Contract as a cross-role family, allow one or more followers and multiple follower roles, and require common-scope ownership. The eventual repair must at least reconcile `CA-R-880`, `CA-R-873`, `CA-R-874`, `CA-R-883`, `CA-R-877`, `CA-E-238`, and the explanatory tail of `CAPRMEDIO-GOV-REQU-747`. Parent/controller ownership can remain compatible with the narrowest-common-scope rule when that controller is the common composition scope.

6. **No concern found within inspected scope — keep the model deliberately reopenable (98%).** Reopen only when a real accepted case cannot be represented without material loss as one R-to-D Contract plus ordinary linked M/E/I/O Atoms or typed edges. Repeated creation of fake D Atoms solely to satisfy the shape is also a reopen trigger. Hypothetical flexibility is not a reason to broaden the model now.

Recommended CCE rules:

```text
Every Contract is a Requirement Atom with Type contract.
Every Contract belongs to exactly one parent or composition controller Scope Unit.
Every Contract states exactly one required outcome for exactly one Delivery Atom in one directly controlled Scope Unit.
No Contract targets a Method, Evaluation, Implementation, or Ops Atom.
No Feature Scope Unit owns a Contract about a sibling Feature Scope Unit.
```

FPF supports this disposition without dictating CAPRMEDIO's vocabulary. A.6.C warns against treating “contract” as an undifferentiated object and requires its claims and direct objects to remain atomic. A.11 prefers expression through existing roles, Types, and relations over a broad new Contract family and explicitly supports narrow models with declared reopen conditions.

## Open questions (confidence <95%)

None for the semantic decision above. “D is endpoint” is accepted in the bounded sense defined here: the D Atom specifies the outward Delivery boundary. It does not redefine every use of the Delivery role as a network/API endpoint.

Return to authority: if you accept this exact model, the next action is to rewrite the active and draft Contract/relational BSEED authority and its evaluation fixtures into CCE under the R-to-D rule. Any formula can be deleted only after its corresponding CCE claim is reviewed separately and reaches at least 95% confidence.

## Skills used

- `fpf-design-challenge` — challenged the proposed narrowing against current CAPRMEDIO authority and bounded FPF evidence.
- `FPF A.6.C — Contract Unpacking for Boundaries` — **used** to test atomicity, direct-object precision, and avoidance of “contract soup”.
- `FPF A.11 — Ontological Parsimony` — **used** to test whether a broad cross-role Contract family is justified and to define reopen conditions for the narrower model.
