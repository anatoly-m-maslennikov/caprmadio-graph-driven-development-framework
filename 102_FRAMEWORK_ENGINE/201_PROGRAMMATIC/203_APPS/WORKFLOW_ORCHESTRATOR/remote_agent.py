"""Bounded proposal transport to an Agent container with no Project mounts."""

import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from contracts import AgentOutput

MAX_BYTES = 8 * 1024 * 1024


class RemoteAgent:
    def __init__(self, url="http://agent:8091/execute"):
        self.url = url

    def execute(self, context, phase, directory, timeout):
        body = json.dumps({"context": context, "phase": phase, "timeout": timeout}).encode()
        if len(body) > MAX_BYTES:
            raise ValueError("Agent request exceeds admitted byte limit")
        request = Request(self.url, data=body, headers={"Content-Type": "application/json"})
        try:
            with urlopen(request, timeout=timeout + 5) as response:
                raw = response.read(MAX_BYTES + 1)
        except (HTTPError, URLError, TimeoutError, OSError) as error:
            raise RuntimeError(
                "Isolated Agent transport failed; reconcile the saved dispatch"
            ) from error
        if len(raw) > MAX_BYTES:
            raise ValueError("Agent response exceeds admitted byte limit")
        return AgentOutput.model_validate_json(raw).model_dump()
