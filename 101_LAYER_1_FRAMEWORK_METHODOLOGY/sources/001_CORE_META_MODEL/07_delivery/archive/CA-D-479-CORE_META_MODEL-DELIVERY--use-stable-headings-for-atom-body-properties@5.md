---
subjects:
  governs: "Markdown Atom Carrier/Main Content"
  depends_on:
    - "Atom/Summary"
    - "Atom/Claim"
    - "Atom/Content Role"
    - "Atom/Details"
    - "Property"
    - "Markdown Atom Carrier/Structure"
version: 5
updated_at: "2026-09-25 11:32:01 +0000"
relations: {"relates_to": ["CA-D-356", "CA-D-478"]}
atom_id: "CA-D-479"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Delivery"
global_tier: 11
---
# Summary

Use stable headings for Atom body Properties

## Claim

a Markdown Atom's Main Content **must** carry its body Properties under the following exact headings **in** the listed order, **after** **`=1`** literal `# Summary` heading with the Summary value below it:

| Content Role | Required level-two headings, **in** order |
|---|---|
| Requirement, Method, Evaluation, Delivery | `## Claim`, `## Details` |
| Analysis | `## Question`, `## Scope`, `## Approach`, `## Results`, `## TLDR` |
| Concern | `## Concern`, `## Evidences`, `## Blast radius` |
| Plan | `## Objective`, `## Details` |
| Operations | `## Operation`, `## Details` |

- carry **`=1`** occurrence of **every** listed heading for the Atom's Content Role. the first listed section is its primary content block; do **not** add a duplicate `## Claim` section **when** another heading is registered for that role.
- carry a Property **only** **in** its registered section, **not** again **in** frontmatter. use CA-D-470 for the Plan Definition of Done inside Details.
- a Property's section ends at the next heading of the same **or** a higher level, **or** at end of Main Content. supporting headings use lower levels; a separately registered nested Property remains independently addressable **without** copying its value.
- heading markers inside fenced code examples are content, **not** Property boundaries.
- do **not** infer a missing, renamed, duplicated, **or** ambiguously nested Property heading from prose, synonyms, **or** position alone.
- a Details section **may** be empty **when** no supporting content **or** required nested Property applies. this does **not** waive the Plan Definition of Done.

## Details
