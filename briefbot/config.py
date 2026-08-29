"""OpenAI client configuration for briefbot.

The OpenAI Python SDK v1+ prefers instantiating a client instead of configuring
module globals.

The test suite expects a `configure()` function that reads environment variables
and prepares the SDK for subsequent calls. In v1+, we implement this by creating
and caching a client instance.
"""

from __future__ import annotations

import os
from typing import Optional

from openai import OpenAI

_CLIENT: Optional[OpenAI] = None


def configure() -> None:
    """Initialize the cached client from environment variables."""

    global _CLIENT
    _CLIENT = OpenAI(
        api_key=os.environ["OPENAI_API_KEY"],
        base_url=os.environ.get("OPENAI_API_BASE"),
    )


def get_client() -> OpenAI:
    """Return the cached client, creating it from env vars if needed."""

    global _CLIENT
    if _CLIENT is None:
        configure()
    assert _CLIENT is not None
    return _CLIENT
