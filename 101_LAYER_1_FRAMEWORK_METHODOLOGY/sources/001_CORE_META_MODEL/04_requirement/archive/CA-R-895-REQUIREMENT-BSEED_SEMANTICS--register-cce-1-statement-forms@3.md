---
subject_scopes:
  - language
relations:
  child_of:
    - CA-R-892
    - CA-R-893
    - CA-R-894
    - CAPRMEDIO-META-REQU-132--define-role-specific-atom-atomicity
version: 3
updated_at: 2026-08-22 02:58:48
---
# Register CCE 1 statement forms

`cce_1` admits only these statement forms for authority-bearing Bootstrap Seed and Principle Claims. Text enclosed by angle brackets names a required typed filling and is not literal CCE text.

| Form identifier | Admitted Content role | Canonical structure | Summary template |
|---|---|---|---|
| `concern_question` | Concern | `THE Project MUST DECIDE WHETHER <typed clause>.` | `decide-whether-<primary predicate and participants>` |
| `definition` | Requirement | `<canonical term> MEANS <typed definition>.` | `define-<canonical term>` |
| `classification` | Requirement | `EVERY <subject kind> IS A <object kind>.` | `classify-<subject kind>-as-<object kind>` |
| `exclusion` | Requirement | `NO <subject kind> IS A <object kind>.` | `exclude-<subject kind>-from-<object kind>` |
| `cardinality` | Requirement | `EVERY <subject kind> <registered predicate> <cardinality> <object kind>.` | `require-<cardinality>-<object kind>-for-<subject kind>` |
| `relation_assertion` | Requirement | `<quantified subject> <registered predicate> <quantified object>.` | `<predicate>-<object>-for-<subject>` |
| `obligation` | Requirement | `<bearer> MUST <registered predicate clause>.` | `<predicate and primary participants>` |
| `prohibition` | Requirement | `<bearer> MUST NOT <registered predicate clause>.` | `prohibit-<predicate and primary participants>` |
| `permission` | Requirement | `<bearer> MAY <registered predicate clause>.` | `permit-<predicate and primary participants>` |
| `invariant` | Requirement | `FOR EVERY <subject kind>, <registered predicate clause> MUST HOLD.` | `require-<predicate>-for-every-<subject kind>` |
| `derivation` | Requirement | `<bearer> MUST DERIVE <Projection> FROM <source> BY <registered Method>.` | `derive-<Projection>-from-<source>` |
| `method` | Method | `TO <outcome>, <performer> MUST PERFORM ALL OF:` followed by one ordered list of registered action clauses. | `achieve-<outcome>` |
| `evaluation` | Evaluation | `THE <Evaluation> PASSES IF ALL OF:` followed by one ordered list of acceptance clauses, then `THE <Evaluation> FAILS IF ANY OF:` followed by one ordered list of refusal clauses. | `validate-<evaluated subject>` |
| `delivery` | Delivery | `<deliverer> MUST DELIVER <deliverable> TO <receiver>` followed by any admitted condition and Applicability tokens. | `deliver-<deliverable>-to-<receiver>` |

The `cardinality` filling must be exactly `AT LEAST ONE`, `AT MOST ONE`, or `EXACTLY ONE`. A quantified subject or object must begin with exactly one admitted quantification or exact-reference token.

A selected form must match the Atom's Content role and role-specific atomicity. An Atom must not concatenate forms, use one form to hide another Content role, or preserve two alternative canonical statements. A missing semantic shape requires a governed extension of this closed form registry before the Claim can be admitted.
