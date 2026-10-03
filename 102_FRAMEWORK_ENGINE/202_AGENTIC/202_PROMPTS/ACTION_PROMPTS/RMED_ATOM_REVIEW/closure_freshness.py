"""Read-only freshness gate after report admission and before Run closure.

The caller supplies the already validated admission from batch_admission and
the exact pins used by the Run. This checks bytes, not semantic correctness or
permission. It never refreshes pins, repairs files, or upgrades a failed review.
"""
from __future__ import annotations

import hashlib
import re
from pathlib import Path
from collections.abc import Mapping, Sequence


def audit_bindings(root: Path, bindings: Sequence[Mapping]) -> list[dict]:
    """Report changed/missing pins, including formatting-only authority edits."""
    root = root.resolve()
    if not isinstance(bindings, (list, tuple)) or not bindings:
        return [{'kind': 'missing_bindings'}]
    issues = []
    pins = {}
    for binding in bindings:
        path = binding.get('path') if isinstance(binding, Mapping) else None
        digest = binding.get('sha256') if isinstance(binding, Mapping) else None
        try:
            if (not isinstance(path, str) or not path or Path(path).is_absolute()
                    or '..' in Path(path).parts or not isinstance(digest, str)
                    or not re.fullmatch(r'[a-f0-9]{64}', digest)):
                raise ValueError('malformed pin')
            target = (root / path).resolve()
            if not target.is_relative_to(root):
                raise ValueError('pin escapes repository')
            if path in pins and pins[path] != digest:
                raise ValueError('conflicting pins')
            pins[path] = digest
        except (OSError, ValueError, RuntimeError) as error:
            issues.append({'kind': 'invalid_binding', 'path': path, 'reason': str(error)})
            continue
        try:
            actual = hashlib.sha256(target.read_bytes()).hexdigest()
        except OSError as error:
            issues.append({'kind': 'unreadable_binding', 'path': path, 'reason': str(error)})
            continue
        if actual != digest:
            issues.append({'kind': 'stale_binding', 'path': path,
                           'expected_sha256': digest, 'actual_sha256': actual})
    return issues


def close_batch(root: Path, admission: Mapping, groups: Mapping) -> dict:
    """Check freshness only; this does not itself close or verify a batch.

    Admission must already be validated by batch_admission. Candidate pins
    must match its exact sources, and rule/prompt pins must include its evidence.
    Settings and extra input completeness remain caller responsibilities.
    Authority includes the deployed workflow's source-bindings cache, not only
    the subset quoted by a reviewer. Settings and prompts are pinned at Run
    admission. If they change, preserve the historical reports and admit a new
    Run; changing hashes on old reports is not verification.
    """
    issues = []
    for group in ('candidates', 'authority', 'settings', 'prompts'):
        for issue in audit_bindings(root, groups.get(group, [])):
            issues.append(dict(issue, group=group))
    if admission.get('admission') != 'accepted':
        issues.append({'kind': 'review_not_accepted', 'admission': admission.get('admission')})
    try:
        evaluations = admission.get('evaluations')
        if not isinstance(evaluations, list) or not evaluations:
            raise ValueError('validated admission must include evaluations')

        def pins(rows):
            return {(r['path'], r['sha256']) for r in rows}

        expected = pins([e['source'] for e in evaluations])
        if pins(groups.get('candidates', [])) != expected:
            raise ValueError('candidate pins differ from admitted evaluations')
        rules = pins([r for e in evaluations for r in e['authority_sources']])
        if not rules or not rules <= pins(groups.get('authority', [])):
            raise ValueError('authority pins omit admitted rules')
        prompt_hashes = {part['prompt_sha256'] for e in evaluations for part in e['parts']}
        if not prompt_hashes or not prompt_hashes <= {h for _, h in pins(groups.get('prompts', []))}:
            raise ValueError('prompt pins omit admitted evaluator prompts')
    except (KeyError, TypeError, ValueError) as error:
        issues.append({'kind': 'admission_pin_mismatch', 'reason': str(error)})
    return {'result': 'blocked' if issues else 'fresh', 'issues': issues,
            'scope': 'supplied_run_pins', 'completion_verified': False,
            'source_repair_authorized': False}
