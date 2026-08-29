"""Content screening via the OpenAI moderation endpoint."""

from briefbot.config import get_client


def is_safe(text):
    """Return True when the text passes moderation, False when flagged."""
    client = get_client()
    response = client.moderations.create(input=text)
    return not response.results[0].flagged
