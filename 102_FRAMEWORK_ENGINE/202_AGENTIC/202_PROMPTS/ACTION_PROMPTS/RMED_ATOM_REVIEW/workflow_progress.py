"""Summarize one-pass reports; never evaluate Atoms or rewrite check results."""
from collections import Counter

CHECKS = ('properties', 'cce', 'scope', 'claim', 'details', 'summary')


def findings_resolved(report):
    """Account for every finding; an empty unresolved list is not evidence."""
    findings = report.get('findings')
    if not isinstance(findings, list) or not findings:
        return False
    ids = {item['id']: i for i, item in enumerate(findings) if 'id' in item}
    if len(ids) != sum('id' in item for item in findings):
        return False
    covered = []
    for field in ('corrections', 'rejected_findings'):
        for item in report.get(field, []):
            if field == 'rejected_findings' and not str(item.get('reason', '')).strip():
                return False
            refs = item.get('finding_indexes', []) + [ids.get(key, -1)
                    for key in item.get('finding_ids', [])]
            if 'finding_index' in item:
                refs.append(item['finding_index'])
            if 'finding_id' in item:
                refs.append(ids.get(item['finding_id'], -1))
            if not refs or any(type(ref) is not int or ref < 0 or ref >= len(findings)
                               for ref in refs):
                return False
            covered.extend(refs)
    return len(covered) == len(set(covered)) and set(covered) == set(range(len(findings)))


def report_progress(report):
    if report is None:
        return {'state': 'pending', 'reported_result': None,
                'check_complete': False, 'complete': False}
    checks = report.get('checks', {})
    statuses = {name: checks.get(name, {}).get('status') for name in CHECKS}
    check_complete = (
        set(checks) == set(CHECKS)
        and all(status in {'passed', 'failed'} for status in statuses.values())
        and report.get('blockers') == []
        and report.get('coverage_gaps', []) == []
    )
    result = report.get('result')
    clean = (result == 'checked_clean' and not report.get('findings')
             and all(status == 'passed' for status in statuses.values()))
    fixed = (result in {'fixed_not_rechecked', 'replaced_not_rechecked'}
             and findings_resolved(report)
             and report.get('unresolved_findings') == [])
    complete = check_complete and not report.get('fix_blockers') and (clean or fixed)
    state = (result if complete else 'needs_fix'
             if check_complete and result in {'issues', 'needs_fix'} else 'blocked')
    return {'state': state, 'reported_result': result,
            'check_complete': check_complete, 'complete': complete}


def summarize_progress(reports):
    rows = [report_progress(report) for report in reports]
    return {'total': len(rows),
            'reported': sum(row['reported_result'] is not None for row in rows),
            'checked': sum(row['check_complete'] for row in rows),
            'completed': sum(row['complete'] for row in rows),
            'complete': all(row['complete'] for row in rows),
            'states': dict(Counter(row['state'] for row in rows))}
