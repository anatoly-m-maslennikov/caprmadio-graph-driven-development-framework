---
atom_id: CA-D-388
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Generated Data Stage Prefix"
  depends_on:
    - "Journal"
    - "Projection"
    - "Carrier/Format"
version: 4
updated_at: "2026-09-14 06:21:07 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Serialize Generated Data Stage Prefixes and Formats

Journal input **and** generated Projection Carriers **must** use these ordered stage prefixes: canonical Journal input `src`, deterministic lossless staging Projection `stg`, consumer-ready semantic Projection `mrt`, **and** aggregated metrics Projection `biz`. `src` **must** use canonical NDJSON Journal input; `stg` **must** use TOON. these prefixes classify Journal inputs **and** generated Projections **only**. unregistered stage prefixes remain available for later governed Extension.
