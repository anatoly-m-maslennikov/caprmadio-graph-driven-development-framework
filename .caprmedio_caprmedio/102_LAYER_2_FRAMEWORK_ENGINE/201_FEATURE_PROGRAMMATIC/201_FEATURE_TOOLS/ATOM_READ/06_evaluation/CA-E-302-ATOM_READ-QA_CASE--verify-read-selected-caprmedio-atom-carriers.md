---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Tool/ATOM_READ"
  depends_on:
    - "Atom"
    - "Artifact/Carrier"
    - "Scope Unit"
    - "Read Atom Carriers"
version: 12
updated_at: "2026-09-17 23:13:06 +0000"
relations: {"evaluation_for":["CA-R-864","CA-O-047"]}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify read selected caprmedio atom carriers

## Claim checked

CA-O-047 resolves **every** exact Atom selector independently **and** returns **only** the requested faithful carrier view **without** mutation.

## Applicable when

apply **to** **any** realization of CA-O-047 **before** it is relied on as the canonical Atom reader.

## Test case

use a fixture with two valid Atoms. address the first separately by exact path, full filename, filename stem, **and** stable ID; submit a bulk request that selects both Atoms; **and** include one missing selector **and** one deliberately ambiguous stem. request content-only, metadata-only, **and** combined views while recording source bytes.

## Additional resolution cases

independently request an unreadable Carrier, a selector outside the configured control root **and** an invalid output view. preserve attribution **to** the exact failing request; return an explicit failure **without** guessing, widening selection **or** exposing another Carrier. mix valid **and** unresolved selectors **in** a bulk request **and** require **every** result **to** remain attributable. verify that **every** valid view **contains** **only** its requested fields, **and** compare source bytes **before** **and** **after** **every** rejected request.

## Acceptance criteria

**all** four selectors for the first Atom resolve **to** that same carrier; the bulk request returns both **and** preserves selector-to-result attribution; returned content equals **every** body; metadata **contains** raw frontmatter plus correct derived identity, placement, Content-role, Scope Unit, **and** lifecycle facts; missing **and** ambiguous selectors remain explicit; **and** source bytes do **not** change.

## Failure disposition

reject the realization **and** preserve **every** selector, its observed resolution, returned fields, bulk attribution, **and** source-byte comparison.

## Capability coverage

automated tests **must** prove equivalent resolution by path, filename, filename stem, **and** Atom ID; correct singular **and** bulk results; exact output-view selection; explicit missing **and** ambiguous failures; **and** no repository-byte mutation.
