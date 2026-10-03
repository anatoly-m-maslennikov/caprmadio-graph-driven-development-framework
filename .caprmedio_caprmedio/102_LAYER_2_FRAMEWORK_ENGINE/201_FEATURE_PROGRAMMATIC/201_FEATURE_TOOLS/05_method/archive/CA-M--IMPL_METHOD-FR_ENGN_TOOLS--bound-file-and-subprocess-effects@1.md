---
subject_scopes:
  - python-engineering
version: 1
updated_at: 2026-08-21 20:35:00
relations: {}
---
# Bound file and subprocess effects

Plan and validate a file mutation before applying it. Write replacement content through a secure temporary carrier on the destination filesystem, flush required bytes, and replace atomically where the supported platform provides that guarantee. Otherwise expose the weaker recovery boundary explicitly.

Invoke subprocesses with argument arrays, explicit timeouts, checked exit status, controlled environment input, and shell execution disabled by default. Return enough context to diagnose or recover from partial failure without guessing.

Candidate alignment: CA-R-004, CA-R-827, CA-R-846, CA-D-001, CA-R-861.

## Sources

- [Python documentation: subprocess security considerations](https://docs.python.org/3.14/library/subprocess.html#security-considerations)
- [Python documentation: tempfile](https://docs.python.org/3.14/library/tempfile.html)
- [Python documentation: os.replace](https://docs.python.org/3.14/library/os.html#os.replace)
