"""Subprocess fixture for the Codex CLI adapter; no model access."""
import json
from pathlib import Path
import sys
import time

raw = sys.stdin.read()
value = json.loads(raw[raw.index('{"phase":'):])
context = value['context']
if context.get('fixture_launch_failure'):
    sys.stderr.write('fixture-private-value\nError: failed to initialize in-process app-server client: Operation not permitted (os error 1)\n')
    sys.exit(1)
if context.get('fixture_timeout'):
    time.sleep(10)
report = {key: context[key] for key in ('workflow_run_id', 'atom_id', 'source', 'criteria_sha256')}
report.update(checks={name: {'status': 'passed', 'evidence': 'fixture evidence'}
                      for name in ('properties', 'cce', 'scope', 'claim', 'details', 'summary')},
              findings=[], blockers=[], corrections=[], unresolved_findings=[],
              rejected_findings=[], fix_blockers=[], coverage_gaps=[], result='checked_clean')
destination = Path(sys.argv[sys.argv.index('--output-last-message') + 1])
destination.write_text(json.dumps({'report_json': json.dumps(report),
                                   'candidate_content': None, 'confidence': 99.0}))
