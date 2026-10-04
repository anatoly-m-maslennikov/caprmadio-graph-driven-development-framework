"""Stable stdio gateway entry point."""
import argparse
import asyncio
from pathlib import Path
from hot_reload import Gateway

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project-root', required=True, type=Path)
    args = parser.parse_args()
    asyncio.run(Gateway(args.project_root).serve())
