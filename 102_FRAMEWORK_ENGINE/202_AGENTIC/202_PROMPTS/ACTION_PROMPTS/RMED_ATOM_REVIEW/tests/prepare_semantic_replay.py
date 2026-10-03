"""Build blinded, source-bound synthetic inputs; never generate judgments.

Run with an absent output directory. Expected cases stay outside reviewer
packets. This tests semantic behavior, not full real-Project carrier compliance.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import random
import sys

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
from context_builder import body_sections, prepare_context  # noqa: E402
from review_evidence import ReviewContext  # noqa: E402


DEFINITIONS = {
    'Widget': 'a Widget means a display component; Widgets is its plural form.',
    'Widget/Color': 'Widget/Color means the Color Property of a Widget; Color in a Widget context names this Property.',
    'Widget/Size': 'Widget/Size means the Size Property of a Widget; Size in a Widget context names this Property.',
    'Widget/Status': 'Widget/Status means the Status Property of a Widget; Status in a Widget context names this Property.',
    'Widget/Color: Blue': 'Widget/Color: Blue means the allowed Color value named Blue; Blue in a display-color context names this value.',
    'Widget/Size: Large': 'Widget/Size: Large means the allowed Size value named Large; Large in a Widget-size context names this value.',
    'Widget/Status: Active': 'Widget/Status: Active means the allowed Status value named Active; Active in a Widget-status context names this value.',
    'Widget/Status: Queued': 'Widget/Status: Queued means the allowed Status value named Queued; Queued in a Widget-status context names this value.',
    'Operator': 'an Operator means a human viewing or controlling the synthetic Project display.',
}


def digest(raw: str) -> str:
    return hashlib.sha256(raw.encode()).hexdigest()


def bound(path: str, identifier: str, version: int, raw: str) -> dict:
    return {'binding': {'path': path, 'atom_id': identifier, 'version': version,
                        'sha256': digest(raw)}, 'text': raw}


def mock_authority(identifier: str, target: str, claim: str) -> dict:
    raw = ('---\nstatus: Active\ncontent_role: Requirement\nsubjects:\n  governs: '
           + json.dumps(target) + '\n---\n# Summary\nsynthetic authority\n## Scope\n'
           'the synthetic DEMO universe.\n## Claim\n' + claim + '\n## Details\n')
    return bound(f'synthetic/{identifier}.md', identifier, 1, raw)


def build(output: Path) -> None:
    output.mkdir(parents=True, exist_ok=False)
    root = HERE.parents[4]
    manifest = json.loads((HERE / 'source_bindings.json').read_text())
    baseline = []
    selected_ids = set(manifest['evaluators']['coherence'])
    for binding in manifest['sources']:
        if binding['atom_id'] not in selected_ids:
            continue
        raw = (root / binding['path']).read_text()
        if digest(raw) != binding['sha256']:
            raise ValueError(f'Stale baseline: {binding["atom_id"]}')
        baseline.append({'binding': binding, 'text': raw})
    definitions = [mock_authority(f'FIXTURE-R-{n:03}', target, claim)
                   for n, (target, claim) in enumerate(DEFINITIONS.items(), 1)]
    principle = mock_authority('FIXTURE-R-100', 'Synthetic Project',
        'the synthetic DEMO Project must keep display properties explicit and internally coherent.')
    cases = json.loads((HERE / 'tests/fixtures/cases.json').read_text())
    random.Random(260926).shuffle(cases)
    candidates = []
    for index, case in enumerate(cases, 1):
        raw = (HERE / 'tests/fixtures' / case['file']).read_text()
        from context_builder import metadata
        props = metadata(raw)
        candidates.append(bound(f'synthetic/case-{index:04}.md', props['atom_id'], props['version'], raw))
    authority = baseline + definitions + [principle]
    context = prepare_context({'confidence_threshold': .99, 'sources': authority + candidates,
        'authority_bindings': [row['binding'] for row in authority],
        'principle_admissions': [{'binding': principle['binding'],
            'applicable_to': [row['binding']['path'] for row in candidates],
            'reason': 'Synthetic test universe; this is the only applicable Project Principle.',
            'provenance': 'Explicit fixture definition; not a real Project admission.'}],
        'scope_of_review': 'Coherence only. The mock Entity universe is closed to the nine supplied definitions. All other dictionary words are general unless used as that Entity. Baseline rules supply evaluation criteria, not additional Entities in the fixture body.',
        'prompts': {'coherence': (HERE / 'evaluate_coherence.prompt.md').read_text()}})
    sha = ReviewContext(context).sha256
    (output / 'context.json').write_text(json.dumps(context, indent=2))
    (output / 'packets').mkdir()
    (output / 'results').mkdir()
    for index, candidate in enumerate(candidates, 1):
        packet = {'context_sha256': sha, 'source': candidate['binding'],
                  'raw': candidate['text'], 'sections': body_sections(candidate['text'])}
        (output / 'packets' / f'{index:04}.json').write_text(json.dumps(packet, indent=2))
    (output / 'private-expectations.json').write_text(json.dumps(cases, indent=2))
    print(json.dumps({'output': str(output), 'count': len(candidates), 'context_sha256': sha}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', type=Path)
    build(parser.parse_args().output)
