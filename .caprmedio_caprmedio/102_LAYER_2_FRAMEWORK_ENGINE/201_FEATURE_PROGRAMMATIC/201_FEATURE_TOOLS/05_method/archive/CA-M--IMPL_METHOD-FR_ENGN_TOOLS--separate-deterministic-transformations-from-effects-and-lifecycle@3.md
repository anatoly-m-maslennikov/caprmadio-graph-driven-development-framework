---
subject_scopes:
  - python-engineering
version: 3
updated_at: 2026-08-22 01:50:50
relations: {}
---
# Separate deterministic transformations from effects and lifecycle

Inside the Tool's sole manager, implement deterministic parsing, classification, validation, planning, and projection as transformations whose outputs follow from explicit inputs. Keep every business decision and execution-graph choice in that manager and use immutable data objects for stable values.

Move filesystem, process, clock, environment, network, logging-export, scheduling, and persistence effects to atomic non-deciding workers or adapters. Let the scheduler advance the manager-produced graph without changing it. Use objects when one responsibility owns mutable technical state, a resource, a lifecycle, or a replaceable adapter. Prefer composition over inheritance and do not create a class merely to group unrelated functions.

Candidate alignment: CA-M-002, CA-M-005, CA-D-001, CA-D-002.

## Sources

- [Python Functional Programming HOWTO](https://docs.python.org/3.14/howto/functional.html)
- [Python documentation: dataclasses](https://docs.python.org/3.14/library/dataclasses.html)
