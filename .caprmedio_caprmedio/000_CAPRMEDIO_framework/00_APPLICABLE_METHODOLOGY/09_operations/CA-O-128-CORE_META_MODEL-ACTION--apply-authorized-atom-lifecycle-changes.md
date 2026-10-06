---
atom_id: CA-O-128
content_role: Operations
type: Action
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Atom"
  depends_on: ["Action", "Atom/Summary", "Artifact/Revision", "Status", "Carrier", "Operator", "Journal"]
version: 3
updated_at: "2026-10-05 01:39:17 +0000"
relations:
  relates_to: [CA-O-051, CA-O-067, CA-R-1432, CA-R-1464, CA-R-1521, CA-R-1788, CA-R-807, CA-D-303, CA-D-289]
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-128-CORE_META_MODEL-ACTION--apply-authorized-atom-lifecycle-changes.md
  source_atom_id: CA-O-128
  source_atom_revision: 3
  source_sha256: b5d052e97bae6ada98849380199e5c67cbf090900beb33ca202f7872d56301e8
  original_relations_sha256: 9e0aeb5fc87168c9d060e1c1814d671d43c86b7a2e94c8f5d1279124b3f6d7d2
---
# Summary

Apply authorized Atom lifecycle changes

## Operation

This reusable Agentic Action applies only an exact admitted Create, identity-preserving Update, accepted Replace or model-admitted Change Status request. It returns effect/admission evidence, never selects a Workflow continuation or authorizes its own mutation.

### Inputs

- exact request kind and frozen boundary for exactly one Create target or one existing current target/predecessor, its complete proposed Carrier set or status/replacement mapping, target identity/locator, Revision, digest, destination and historical evidence.
- current applicable models, role/type/status/transition and Carrier/Relation validation authority, immutable Summary and identity rules, permissions and explicit effect admission. Preserve any selected adapter's sealed Initiative/delegated-apply conditions; preview alone grants no apply authority.
- for Update, the exact O067 assessment/result and target/proposal/source evidence for that one target supplied by the assessment Step; for Replace, one active predecessor and its complete accepted set of >=1 distinct already-active successors. Multiple Carriers or successors within that one approved replacement are not additional independent targets.
- admitted effect/recovery and canonical Journal capabilities, definition bindings, Run/parent references, check expectations and prior effect/receipt evidence. Missing capabilities or rules block effects; an executor adapter is not Core authority.

### Behavior and outcomes

1. Reject multiple independent Create/current targets or predecessors as invalid before effects or reuse of an assessment. Bulk callers require separate individually admitted invocations/Runs; one target's O067 result never covers another target. Resolve the one target/predecessor and every required Carrier or replacement successor, and validate the whole selected boundary before effects: required current metadata, Summary, direct Relations, Role/Type placement, status model, destinations, historical references and applicable approval. Reject missing/ambiguous/repeated/self-referential targets, unsupported models, invalid content/status/transitions or collisions. Requested effects outside the frozen permission boundary return unauthorized; default to mutation-free preview until explicit apply admission.
2. Create: prove each destination absent and unique and each assigned identity unused against current allocation plus preserved all-history evidence; absent Active files alone are insufficient. Unassigned Drafts do not acquire invented IDs. Freeze complete content/targets/digests and initial metadata under actual applicable authority; competing admission or changed absence invalidates apply rather than silently reallocating.
3. Update: consume O067's exact identity-preserving result, not a reimplemented classifier. Preserve identity/Summary and admitted placement; an assessment requiring replacement cannot authorize this effect. Changed proposal, target or evidence returns reassessment-required with no mutation; changed definitions require separate revalidation. R1432 carrier_only/equivalent refinement retain Version, semantic_revision uses the next Revision, replacement is not same-ID update. R1788 refreshes Updated At on every actual edit, including formatting; no edit/no-op invents no timestamp change or revision. Retain required prior history.
4. Replace: validate the complete predecessor→successor-set intent without reducing it to a pair. Reuse O051 once for the accepted replacement transition; all named successors must be Active before predecessor archival. Preserve its whole-Carrier/archive/status/time/@version and Journal requirements, including explicit predecessor and every successor ID under R807; do not copy replacement history into Atom frontmatter or invent replacement Relations. A selected persistence capability unable to honor the complete approved boundary returns unsupported rather than truncating it.
5. Change Status: resolve the actual current Atom and complete qualified Content Role/Type status model and transition conditions under R1521/R1308. Its exact bound role model (including R1874 for Operations and R1875 for Analysis) supplies values; a more-specific declared Role/Type model overrides it, otherwise it inherits the role model without duplicated Type lists. Its most-specific Delivery rule supplies placement; only after that may D466's conditional Active/current or lowercase-status fallback apply. A missing, ambiguous or unsupported qualified model blocks unchanged; no role borrows another role's values. A same current value returns no-op. Archive only requests a status the same qualified model explicitly defines as archival; absent archival meaning returns missing-archival-model/unsupported unchanged, never maps Concern resolved/canceled or forces Archived. Preserve required identity/Summary/body/Version/history/references and serialize only the admitted new current status and actual edit time while keeping prior transitions in the shared Journal. Applicable archival uses one whole atomic Carrier transition and canonical @version suffix. Invalid models/transitions/destinations are blocked, never approximated by a universal list.
6. Freeze the complete mutation-free proposal and current preconditions. Immediately before any admitted effect recheck permission, all source/destination/assessment/definition bindings and historical admission. Already satisfied valid state returns no-op with checks and Run evidence, not another effect/history event. Apply only the exact admitted boundary; preserve unrelated data. Partial publication is not successful set application.
7. Verify actual outputs, retained history/references and all required durable change/Run receipts. On effect/postcondition failure use only admitted bounded recovery, retaining actual completed/incomplete effects, immutable accepted events and recoverable evidence; incomplete/unverified recovery remains partial or failed. A pending recording receipt returns recording-blocked with actual effect state, never fake completion or permission to replay effects. Retrying Journal delivery is not another Action execution.

## Details

The calling Workflow owns routing. This Action does not invoke O067, choose Replace, start a successor, reset retry allowance or broaden permission. O067 remains the classifier and O051 the accepted replacement-effect owner. Concrete MCP/Tool/path/seal adapters and implementation remain in their existing Engine/configuration units; legacy always+1 Version/unchanged-formatting-time assertions do not override current R1432/R1788.

Every actual invocation, including standalone and the referenced O051 execution, retains its distinct Action Run identity, exact definition/input binding, parent Action/Step/Workflow lineage where applicable, start/terminal outcome, results/effects and canonical durable evidence. Failed/canceled/no-op invocations are recorded without secrets or fictitious Artifact changes. A well-formed source definition does not prove that any effect or Run occurred.
