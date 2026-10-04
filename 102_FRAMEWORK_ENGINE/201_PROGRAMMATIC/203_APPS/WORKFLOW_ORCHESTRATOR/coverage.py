"""Execution accounting only: never evaluate or recheck Atom meaning."""
from workflow_progress import CHECKS, report_progress


def assess(request, frozen, state, phase):
    obligations = []
    if phase == 'gather':
        selected = state.get('selection', [])
        for index, row in enumerate(request.selection):
            actual = selected[index] if index < len(selected) else {}
            obligations.append((row.atom_id, actual.get('atom_id') == row.atom_id
                and actual.get('source') == frozen['selection_bindings'][index]))
        obligations.append(('exact selection length', len(selected) == len(request.selection)))
        obligations.append(('bound rules', state.get('criteria') == frozen['rule_bindings']))
        obligations.append(('gather outcome', state.get('gathered') and not state.get('gather_blockers')))
    else:
        reports = state.get('reports', [])
        for index, row in enumerate(request.selection):
            report = reports[index] if index < len(reports) else None
            if phase == 'check':
                for name in CHECKS:
                    check = (report or {}).get('checks', {}).get(name, {})
                    obligations.append((f'{row.atom_id}/{name}',
                        check.get('status') in ('passed', 'failed') and bool(check.get('evidence'))))
                obligations.append((f'{row.atom_id}/check blockers', report_progress(report)['check_complete']))
            elif phase == 'fix':
                obligations.append((f'{row.atom_id}/finding dispositions', report_progress(report)['complete']))
            else:
                raise ValueError('Unknown coverage phase')
    obligations.append(('evidence recording', not state.get('recording_blockers')))
    missing = [name for name, passed in obligations if not passed]
    expected = len(obligations)
    covered = expected - len(missing)
    question = None if not missing else (
        f'{phase} coverage is incomplete ({covered}/{expected}). Missing: '
        + ', '.join(missing) + '. How should we resolve the missing work before a new authorized continuation?')
    return {'phase': phase, 'expected': expected, 'covered': covered, 'missing': missing,
            'coverage_percent': 100 if not missing else covered * 100 / expected,
            'result': 'covered' if not missing else 'ask_operator', 'operator_question': question}
