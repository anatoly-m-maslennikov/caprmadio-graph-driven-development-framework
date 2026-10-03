---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Tool/ATOM_CREATE"
  depends_on:
    - "Atom"
    - "Atom/Identifier"
    - "Atom/Revision"
    - "Create Sealed Atom Carriers"
    - "Artifact/Carrier"
    - "Journal/Record"
version: 14
updated_at: "2026-09-17 04:46:13 +0000"
relations: {"evaluation_for":["CA-R-865","CA-O-032","CA-D-450"]}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify create sealed caprmedio atom carriers

## Claim checked

CA-O-032 admits one Atom **or** a frozen bulk set atomically **only** **after** complete validation **and** delegated apply authority.

## Applicable when

apply **to** **any** realization of CA-O-032 **before** it can create governed Atom carriers.

## Test case

use one fixture containing a valid single-Atom request **and** a frozen two-Atom request with valid role placement **and** unique IDs. record dry-runs, attempt apply **without** delegated authority, introduce a collision at the second bulk destination **and** attempt delegated apply, **then** remove that collision **and** apply the unchanged single **and** bulk requests through sealed Initiative envelopes.

## Acceptance criteria

dry-runs **and** the unauthorized apply create nothing; the colliding bulk set creates neither Atom; authorized valid applies create the single carrier **and** both bulk carriers exactly once as canonical first revisions with complete metadata; no target, filename, **or** stable ID collides; **and** no temporary **or** partial carrier remains.

## Failure disposition

reject the realization **and** preserve the sealed envelopes, authority result, collision evidence, dry-runs, resulting directory state, **and** **any** partial-write residue.

## Post-effect failure coverage

repeat the frozen bulk request from an independent clean fixture with its exact authorized preconditions. **after** **`>=1`** planned Carrier becomes visible, inject a later publication **or** post-write validation failure. **if** the complete set is published by **`=1`** atomic effect, inject the failure **after** that publication **and** **before** final validation succeeds; the test **must not** require a weaker publication design.

- observe that the fault occurs **after** the selected effect, **not** during preflight.
- check that the complete requested set returns **to** its pre-action absence state under CA-O-032, unrelated Carriers remain unchanged, **and** no owned staging **or** partial Carrier remains.
- report the failed attempt **and** recovery result; do **not** return a creation-success receipt. retain evidence of the fault, actual effects, **and** restoration **without** deleting accepted Journal history.
- a collision rejected **before** mutation does **not** satisfy this recovery case. failure **to** restore the claimed boundary fails the Evaluation; reporting that failure is **not** a passing rollback result.

## Historical identity admission cases

- attempt creation with an assigned ID that exists **only** **in** an archived, replaced, **or** absorbed Atom. reject reuse even **when** no active Carrier owns the ID.
- exercise repeated IDs **in** the requested bulk set, duplicate destinations, **and** a competing identity admission **after** dry run. no invalid request creates a partial set **or** silently selects a different ID during apply.
- provide incomplete **or** conflicting assignment evidence. report unresolved admission rather than interpreting missing evidence as an unused number.
- include a valid unassigned Draft request. validate its Draft Carrier grammar **and** initial Revision metadata **without** requiring **or** assigning a stable Atom ID.
- for accepted identified Atoms, verify the Project-wide next-unreused-number rule for their Content Role, **not** merely active-file uniqueness. keep the existing valid single/bulk, dry-run, authorization, collision, **and** post-effect recovery cases.
