---
subject_scopes:
  - carrier-format
relations:
  child_of:
    - CA-E-001
    - CA-E-206
  evaluation_for:
    - CAPRMEDIO-GOV-REQU-731
    - CAPRMEDIO-GOV-REQU-736
    - CAPRMEDIO-GOV-REQU-764
    - CAPRMEDIO-GOV-REQU-733
    - CAPRMEDIO-R-798
    - CAPRMEDIO-R-799
    - CAPRMEDIO-GOV-REQU-685
    - CA-R-859
    - CA-R-890
  check_of:
    - CA-M-109
version: 1
updated_at: 2026-08-22 04:00:55
---
# Validate canonical Atom filename structure

## Claim checked

Every active or draft role-classified Markdown Atom filename deterministically exposes its identity state, current Scope Unit, effective local tier, Atom Type, Type-governed target Scope Unit, and derived CCE Summary without duplicating or merging those facts.

## Test case

Construct accepted fixtures for a Project-root Principle, a non-Project Core, an unmarked default-tier Atom, and a target-bearing Atom. Construct matching draft fixtures with the visible empty number slot. Parse each filename into Atom ID or draft absence, current Scope Unit, local tier, Atom Type, target Scope Unit when admitted, Summary slug, and extension; render it again and compare bytes.

Independently add a current-scope segment to a Project-root fixture, remove or duplicate a required non-Project current Scope Unit, use an unknown scope name, place `PRINCIPLE` or `CORE` outside the tier position, insert an empty tier segment, spell the default tier, use lowercase in a structured token, use uppercase in the Summary, omit a required target, add a prohibited target, provide two targets, place the target before Type, use an unknown Type, remove one Summary-delimiter hyphen, add a second delimiter, use an unsafe path character, assign a number to a draft, or remove the number from an accepted Atom.

## Acceptance criteria

Every valid fixture round-trips byte-identically and resolves exactly one value for every applicable filename fact. A Project-root fixture resolves Project ownership from the governed omission of `<CURRENT_SCOPE>`. The unmarked fixture resolves the default lower local tier. Every invalid fixture fails and identifies the exact identity, scope, tier, Type, target, delimiter, Summary, extension, safety, or lifecycle violation. No fixture derives semantic Scope Unit meaning from a filename short name inside Atom prose or frontmatter.

## Failure disposition

Record a Concern naming the rejected Carrier and exact filename component, and stop acceptance or migration only for that Carrier.
