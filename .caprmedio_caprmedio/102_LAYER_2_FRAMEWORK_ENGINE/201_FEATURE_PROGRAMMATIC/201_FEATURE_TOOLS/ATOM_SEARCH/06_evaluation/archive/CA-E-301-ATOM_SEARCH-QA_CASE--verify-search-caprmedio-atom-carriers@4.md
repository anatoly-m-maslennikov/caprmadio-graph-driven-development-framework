---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - artifact-operations
    occurrent:
      - evaluation
version: 4
updated_at: 2026-09-02 01:10:00 +0400
relations:
  evaluation_for:
    - CA-M-183
---
# Verify search caprmedio atom carriers

## Claim checked

CA-M-183 returns every and only matching Atom carrier in a deterministic requested view without changing project truth.

## Applicable when

Apply to any realization of CA-M-183 before it is relied on for read-only Atom discovery.

## Test case

Use one fixture with active, draft, archived, malformed, and non-Atom Markdown candidates across two Scope Units. Within one selected subtree, run an exact Atom selector that yields one result and a second conjunction of lifecycle, Content-role, Tier, frontmatter, and body-text filters that yields two results; request each output view and repeat both requests after recording every fixture digest.

## Acceptance criteria

The exact selector returns one and only its Atom; the filtered request returns every and only its two matching Atoms in stable repository-relative path order; each output view contains only its requested fields; malformed candidates have separate diagnostics; excluded files never appear; repeated results are identical; and every recorded digest remains unchanged.

## Failure disposition

Reject the realization and preserve the fixture, requests, unexpected membership or ordering, output-view evidence, diagnostics, and any detected mutation.
