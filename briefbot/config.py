"""OpenAI client configuration for briefbot.

The OpenAI Python SDK v1+ no longer uses module-level globals like
`openai.api_key` / `openai.api_base`. Instead, callers instantiate a client.

This module centralizes that instantiation so the rest of the codebase can
depend on a small helper.
"""

from __future__ import annotations

import os

from openai import OpenAI


def configure() -> None:
    """Backwards-compatible no-op.

    The v0.x SDK used global configuration (e.g. `openai.api_key`). The v1+ SDK
    configures per-client instance, so callers should prefer `get_client()`.

    Tests in this repository call `configure()` as a setup hook after setting
    environment variables; keeping this function preserves that intent.
    """


def get_client() -> OpenAI:
    """Create an OpenAI client from environment variables.

    - OPENAI_API_KEY is required.
    - OPENAI_API_BASE is optional and is used by the offline test suite to
      point the client at the local stub server.
    """
    api_key = os.environ["OPENAI_API_KEY"]
    base_url = os.environ.get("OPENAI_API_BASE")
    return OpenAI(api_key=api_key, base_url=base_url)
