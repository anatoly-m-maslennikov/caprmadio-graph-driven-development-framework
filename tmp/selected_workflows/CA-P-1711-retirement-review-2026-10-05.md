# CA-P-1711 — exact prior-image retirement review

Result: ACCEPT. Confidence: 96%. Read-only review; no tests, images, containers, source files or permissions changed.

## Exact reviewed inputs

- release_image.py: 14d196bafe451085a3c6f7de4cd5f3fac4cec27a8deac5f1ccd848d06b1eae3c
- test_release_image.py: bac6e8970a65510377ed45c9ac487749673e7432980e3ff043e34a8e77917b29
- D573@2: 5db7045ec34fbd9aea129d63262f6fce1ac5a6bff2b147af90a9fad6e560adad

## Findings

No blocking finding in the pinned P1707 delta.

1. Lines700–722 reopen authoritative settings and check their sealed digest, exact closed retention table, admitted condition and duplicate-free immutable image references.
2. Lines773–824 require independently reopened successful same-candidate promotion, suite, build, canary, package, selector and Skill evidence. Unknown prior identity or candidate-as-prior never permits removal.
3. Lines669–698 inspect every listed running/stopped container by immutable image ID. Incomplete observation blocks removal.
4. Lines825–846 exclusively create and synchronize an immutable removal intent before exactly non-forced docker image rm of the prior digest. No prune, tags, alternate targets or force.
5. Lines725–750 and851–873 require exact disappearance and a complete immutable inventory. Uncertain effects, stale proof and failed recording cannot become success.
6. Existing intents prevent implicit replay; concurrent same-candidate attempts cannot both remove the image.

Tests cover malformed/stale settings, required references, stopped containers, missing identity, forged promotion, uncertain/failed removal, recording failure and concurrent admission. The reviewer did not rerun them because of the reported fixture cleanup denial. Historical51 image/14 promotion passes are not refreshed evidence.

## Separate incomplete gates

- Durable same-intent recording reconciliation is not implemented.
- Actual Docker-image proof, full Release dispatch, public/provider admission and restart recovery remain unfinished.
- The intent is scoped to a candidate/prior-image pair, not a global lock over external Docker/selector changes.

Root saved this report from the assigned subagent result; this is not a Workflow Run or Journal receipt.
