---
subjects:
  governs: "Applicable Methodology"
  depends_on:
    - "Applicable Methodology/Conflict"
    - "Applicable Methodology/Source Frontier Digest"
    - "Operator"
    - "Journal/Record"
    - "Methodology Source/Expansion Boundary"
version: 9
updated_at: "2026-09-16 22:01:42 +0000"
relations:
  relates_to:
    - CA-O-007
    - CA-O-011
---
# Fail Closed on Unresolved Methodology Conflicts

**if** an Applicable Methodology conflict remains unresolved **or** its required Operator approval is missing, stale, partial, ambiguous, **or** mismatched, **then** compilation **must** fail **without** changing Applicable Methodology membership.

qualifying approval **must** be the Operator's actual decision recorded **in** the Journal under CA-O-007 **and** bound **to** the exact conflict **and** source-frontier digest under CA-O-011. a Project Configuration approval Atom, an LLM judgment, **or** the mere presence of a Journal record **must not** substitute for that decision **or** bypass the Core expansion boundary.
