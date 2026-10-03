"""Compare real coherence outputs with the separate synthetic expectations.

This does not certify additional findings; a human/independent reviewer must
adjudicate them. An absent/invalid report is incomplete, never a passing case.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
from evaluation_contract import GROUPS, validate_part  # noqa: E402
from review_evidence import ReviewContext  # noqa: E402


def compare(run: Path) -> dict:
    context = ReviewContext(json.loads((run / 'context.json').read_text()))
    expected = json.loads((run / 'private-expectations.json').read_text())
    results = []
    owned = set(GROUPS['coherence'])
    for index, case in enumerate(expected, 1):
        path = run / 'results' / f'{index:04}.json'
        row = {'ordinal': index, 'fixture': case['file']}
        try:
            actual = json.loads(path.read_text())
            validate_part(actual, context=context)
        except (OSError, ValueError) as error:
            results.append({**row, 'admission': 'incomplete', 'reason': str(error)})
            continue
        checks = {c['id']: c for c in actual['checks']}
        needed = owned.intersection(case['required_failed_checks'])
        needed_blocks = owned.intersection(case.get('required_blocked_checks', []))
        confirmed = {key for key, check in checks.items() if check['findings']}
        blocked = {key for key, check in checks.items() if check['status'] == 'blocked'}
        passed = all(c['status'] == 'passed' for c in checks.values())
        results.append({**row, 'admission': 'valid', 'result': actual['result'],
            'missed_required_findings': sorted(needed - confirmed),
            'missed_required_blocks': sorted(needed_blocks - blocked),
            'additional_finding_checks_to_adjudicate': sorted(confirmed - needed),
            'unexpected_blocked_checks': sorted(blocked - needed_blocks),
            'positive_case_false_failure': case['file'] in ('valid.md', 'valid-composite.md') and not passed,
            'findings': sum(len(c['findings']) for c in checks.values())})
    return {'cases': len(expected), 'admission_counts': dict(Counter(r['admission'] for r in results)),
            'results': results, 'claim': 'Mechanical comparison only; semantic adjudication remains separate.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('run', type=Path)
    args = parser.parse_args()
    print(json.dumps(compare(args.run), indent=2))
