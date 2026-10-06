"""Stable stdio gateway entry point, with an explicit Streamable HTTP mode."""
import argparse
import asyncio
from pathlib import Path
from hot_reload import Gateway

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project-root', required=True, type=Path)
    parser.add_argument('--transport', choices=('stdio', 'streamable-http'), default='stdio')
    args = parser.parse_args()
    if args.transport == 'stdio':
        asyncio.run(Gateway(args.project_root).serve())
    else:
        from http_server import main as serve_http
        import sys
        sys.argv = [sys.argv[0], '--project-root', str(args.project_root)]
        serve_http()
