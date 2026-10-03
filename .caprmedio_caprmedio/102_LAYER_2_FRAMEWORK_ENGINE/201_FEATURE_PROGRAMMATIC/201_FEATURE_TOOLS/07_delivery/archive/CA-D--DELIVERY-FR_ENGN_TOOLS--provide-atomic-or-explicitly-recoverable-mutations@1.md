---
subject_scopes:
  - failure-recovery
version: 1
updated_at: 2026-08-21 20:35:00
relations: {}
---
# Provide atomic or explicitly recoverable mutations

Deliver each mutation with a declared atomicity boundary. Use secure temporary carriers and atomic replacement where the supported substrate guarantees them. When full atomicity is unavailable, preserve enough durable state and identity to detect interruption, choose the authoritative state, and retry or recover without guessing.

Bound child processes by checked outcomes and timeouts. Do not report success before required bytes, process outcomes, and recovery metadata have crossed their declared durability boundary.

Candidate alignment: CA-R-004, CA-R-827, CA-D-001, CA-E-002, CA-R-861.

## Sources

- [Python documentation: tempfile](https://docs.python.org/3.14/library/tempfile.html)
- [Python documentation: os.replace](https://docs.python.org/3.14/library/os.html#os.replace)
- [Python documentation: subprocess](https://docs.python.org/3.14/library/subprocess.html)
