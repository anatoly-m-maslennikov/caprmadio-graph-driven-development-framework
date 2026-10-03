---
subjects:
  governs: "Generated Data Stage Prefix"
  depends_on:
    - "Journal"
    - "Projection"
    - "Carrier/Format"
version: 6
updated_at: "2026-09-14 06:21:07 +0400"
relations: {}
---
# Serialize Generated Data Stage Prefixes and Formats

Journal input **and** generated Projection Carriers **must** use these ordered stage prefixes: canonical Journal input `src`, deterministic lossless staging Projection `stg`, consumer-ready semantic Projection `mrt`, **and** aggregated metrics Projection `biz`. `src` **must** use canonical NDJSON Journal input; `stg` **must** use TOON. these prefixes classify Journal inputs **and** generated Projections **only**. unregistered stage prefixes remain available for later governed Extension.
