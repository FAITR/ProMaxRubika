"""Event models."""
from dataclasses import dataclass, field
from typing import Any

@dataclass(slots=True)
class MessageEvent:
    """Normalized incoming message event.

    Fields are optional because different message types may omit metadata.
    `raw` contains the original adapter payload and should be treated as untrusted.
    """
    text: str | None = None
    chat_id: str | None = None
    message_id: str | None = None
    sender_id: str | None = None
    is_outgoing: bool = False
    raw: dict[str, Any] = field(default_factory=dict)
