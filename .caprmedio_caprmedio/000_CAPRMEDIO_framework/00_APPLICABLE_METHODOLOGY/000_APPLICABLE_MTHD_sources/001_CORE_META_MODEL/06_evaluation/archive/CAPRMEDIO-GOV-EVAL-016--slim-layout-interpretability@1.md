---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
priority: medium
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: check_of
    targets:
      - CAPRMEDIO-GOV-REQU-399--slim-project-control-layout
---

# Evaluation Case — Interpret the slim project control layout

Give independent reviewers only the `dset/` tree and artifact filenames. Pass
when they consistently identify the sole settings/manifest carrier, distinguish
project-wide records from Version lifecycle artifacts, assign layer-owned truth
to the correct direct layer root, and do not infer a second manifest or generic
scope owner.

Record ambiguities rather than resolving them by majority vote. Any materially
different authority interpretation keeps this Evaluation inconclusive.

This Evaluation atom is immutable. Later correction requires a successor
Evaluation and append-only lifecycle event.

## Primary claim

A reviewer can identify project-wide, Version-wide, and layer-owned authority plus the sole configuration owner from the schema 1.3 tree without explanatory prose.
