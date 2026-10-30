"""Messaging facade."""
from .exceptions import UnsupportedFeatureError

class Messenger:
    """Message operations delegated to the configured transport."""
    def __init__(self, transport) -> None:
        self._transport = transport

    async def send_message(self, chat_id: str, text: str):
        """Send a text message through the configured transport."""
        if not chat_id or not isinstance(chat_id, str):
            raise ValueError("chat_id must be a non-empty string")
        if not isinstance(text, str) or not text:
            raise ValueError("text must be a non-empty string")
        return await self._transport.send_message(chat_id, text)

    async def reply(self, event, text: str):
        """Reply to an event using its chat identifier.

        Adapter-specific reply threading is not standardized in this core.
        """
        if not getattr(event, "chat_id", None):
            raise ValueError("event has no chat_id")
        return await self.send_message(event.chat_id, text)
