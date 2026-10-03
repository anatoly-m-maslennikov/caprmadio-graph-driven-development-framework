---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "artifact-operations"
  depends_on: []
version: 9
updated_at: "2026-09-17 02:43:52 +0000"
relations:
  evaluation_for:
    - CA-M-185
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify create sealed caprmedio atom carriers

## Claim checked

CA-M-185 admits one Atom **or** a frozen bulk set atomically **only** **after** complete validation **and** delegated apply authority.

## Applicable when

Apply **to** **any** realization of CA-M-185 **before** it can create governed Atom carriers.

## Test case

Use one fixture containing a valid single-Atom request **and** a frozen two-Atom request with valid role placement **and** unique IDs. Record dry-runs, attempt apply **without** delegated authority, introduce a collision at the second bulk destination **and** attempt delegated apply, **then** remove that collision **and** apply the unchanged single **and** bulk requests through sealed Initiative envelopes.

## Acceptance criteria

Dry-runs **and** the unauthorized apply create nothing; the colliding bulk set creates neither Atom; authorized valid applies create the single carrier **and** both bulk carriers exactly once as canonical first revisions with complete metadata; no target, filename, **or** stable ID collides; **and** no temporary **or** partial carrier remains.

## Failure disposition

Reject the realization **and** preserve the sealed envelopes, authority result, collision evidence, dry-runs, resulting directory state, **and** **any** partial-write residue.

## Post-effect failure coverage

repeat the frozen bulk request from an independent clean fixture with its exact authorized preconditions. **after** **>=1** planned Carrier becomes visible, inject a later publication **or** post-write validation failure. **if** the complete set is published by **=1** atomic effect, inject the failure **after** that publication **and** **before** final validation succeeds; the test **must not** require a weaker publication design.

- observe that the fault occurs **after** the selected effect, **not** during preflight.
- check that the complete requested set returns **to** its pre-action absence state under CA-M-185, unrelated Carriers remain unchanged, **and** no owned staging **or** partial Carrier remains.
- report the failed attempt **and** recovery result; do **not** return a creation-success receipt. retain evidence of the fault, actual effects, **and** restoration **without** deleting accepted Journal history.
- a collision rejected **before** mutation does **not** satisfy this recovery case. failure **to** restore the claimed boundary fails the Evaluation; reporting that failure is **not** a passing rollback result.
