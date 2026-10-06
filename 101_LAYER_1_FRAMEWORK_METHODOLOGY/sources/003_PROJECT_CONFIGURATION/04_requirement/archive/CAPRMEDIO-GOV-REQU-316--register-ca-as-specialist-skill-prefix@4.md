---
subjects:
  - public-interface
version: 4
updated_at: 2026-08-23 11:39:04
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-R-1054
---
# Register ca as the specialist skill prefix

GOVERNANCE registers `caprmedio` as CAPRMEDIO's canonical primary routing skill and
`ca-` as its canonical short prefix for action-specific public skill names. An
action-specific CAPRMEDIO skill uses `ca-<action>` unless a governed external
host contract requires another spelling.

The prefix is an interface abbreviation only. It does not rename the CAPRMEDIO
framework, alter governed artifact IDs, or establish a second project prefix.
Skill descriptions and host metadata still identify CAPRMEDIO explicitly so
discovery does not depend on knowing the abbreviation in advance.

`ca-` is reserved exclusively for public skill names. CLI commands, package
and import names, repository identities, directories, settings, schemas,
artifact identities, and other non-skill interfaces use their governed
CAPRMEDIO names and must not use `ca-`. The unhyphenated `ca` name is not a
public skill identity.

## Rationale

The short prefix is visibly derived from CAPRMEDIO and keeps frequently invoked
specialist skill names readable. Exclusive ownership prevents it from becoming
a second framework, package, command, or artifact namespace, while the full
primary name keeps the main entrypoint explicit and discoverable.
