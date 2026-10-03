---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Tool/ATOM_SEARCH"
  depends_on:
    - "Atom"
    - "Artifact/Carrier"
    - "Scope Unit"
    - "Search Atom Carriers"
version: 11
updated_at: "2026-09-17 23:13:10 +0000"
relations: {"evaluation_for":["CA-R-863","CA-O-046"]}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify search caprmedio atom carriers

## Claim checked

CA-O-046 returns **every** **and** **only** matching Atom carrier **in** a deterministic requested view **without** changing project truth.

## Applicable when

apply **to** **any** realization of CA-O-046 **before** it is relied on for read-only Atom discovery.

## Test case

use one fixture with active, draft, archived, malformed, **and** non-Atom Markdown candidates across two Scope Units. within one selected subtree, run an exact Atom selector that yields one result **and** a second conjunction of lifecycle, Content-role, Tier, frontmatter, **and** body-text filters that yields two results; request **every** output view **and** repeat both requests **after** recording **every** fixture digest.

## Additional selection cases

include a valid request matching no Atom, an invalid root, an unsupported filter, an invalid lifecycle selector, an invalid output view **and** an unreadable candidate. a valid non-match returns an empty result, **not** an error **or** a widened selection. reject invalid requests explicitly **before** traversal; an unreadable candidate produces a separate diagnostic **and** **must not** be silently accepted as a match **or** ordinary non-match. repeat applicable requests **to** check deterministic ordering **and** compare **every** fixture digest **to** prove no mutation.

## Acceptance criteria

the exact selector returns one **and** **only** its Atom; the filtered request returns **every** **and** **only** its two matching Atoms **in** stable repository-relative path order; **every** output view **contains** **only** its requested fields; malformed candidates have separate diagnostics; excluded files never appear; repeated results are identical; **and** **every** recorded digest remains unchanged.

## Failure disposition

reject the realization **and** preserve the fixture, requests, unexpected membership **or** ordering, output-view evidence, diagnostics, **and** **any** detected mutation.

## Capability coverage

automated tests **must** prove that search returns deterministic singular **and** bulk results, respects subtree **and** lifecycle filters, excludes non-Atom Markdown, exposes **only** the requested output view, **and** leaves **all** repository bytes unchanged.
