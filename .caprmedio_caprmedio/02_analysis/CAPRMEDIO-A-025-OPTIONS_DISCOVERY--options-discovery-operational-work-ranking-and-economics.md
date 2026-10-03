---
atom_id: CAPRMEDIO-A-025-OPTIONS_DISCOVERY
subject_scopes:
  - development-flow
version: 3
updated_at: 2026-09-06 01:45:12 +0400
---
# Options discovery — Operational work ranking and economics

## Current model

Keep the model small:

| Roles | Coordinate |
|---|---|
| Concern and Plan | Priority; `0` is highest and a missing value is unranked |
| Requirement, Method, Evaluation, and Delivery | Tier |
| Analysis, Implementation, and Ops | No priority or tier; classify them by Type and relations |

Priority orders operational work. Tier structures specification authority. They are different coordinates and neither is inferred from the other.

## Deferred options

Future analysis may consider separate severity and urgency, estimated completion time, estimated human hours and tokens, monetary cost, expected new and saved revenue, and estimated versus actual return.

If economic measures are added later, hours and tokens must remain separate until declared rates convert them into money. `benefit / cost` is conventionally a benefit-cost ratio, while standard ROI is `(benefit - cost) / cost`.

These ideas do not change the current model. No deferred option is accepted by this Analysis.
