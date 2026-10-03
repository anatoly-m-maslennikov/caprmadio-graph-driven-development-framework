"""Canonical discover_operations JSON entrypoint."""
import argparse
import asyncio
import json
from pathlib import Path
import sys

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(TOOLS / 'VALIDATE_ATOMS'))
from capability_discovery.service import Service, Query

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project-root', required=True)
    parser.add_argument('--input', default='-')
    args = parser.parse_args()
    raw = sys.stdin.read() if args.input == '-' else Path(args.input).read_text()
    request = Query.model_validate_json(raw)
    service = Service(args.project_root)
    print(json.dumps(service.discover(request, operations=True), default=str))
