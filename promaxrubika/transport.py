"""Transport interface. No undocumented Rubika endpoints are implemented here."""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, AsyncIterator
from .exceptions import UnsupportedFeatureError

class BaseTransport(ABC):
    """Adapter contract for a verified Rubika protocol implementation.

    Implementations must normalize incoming updates into MessageEvent instances.
    This project intentionally ships no guessed endpoints, signatures, or payloads.
    """
    @abstractmethod
    async def connect(self, session: dict[str, Any]) -> None:
        """Establish an authenticated connection."""

    @abstractmethod
    async def close(self) -> None:
        """Release network resources."""

    @abstractmethod
    async def send_message(self, chat_id: str, text: str) -> Any:
        """Send a text message and return the adapter's normalized result."""

    @abstractmethod
    def listen(self) -> AsyncIterator[Any]:
        """Yield normalized incoming events."""

class MissingTransport:
    """Default adapter that fails explicitly rather than pretending to connect."""
    async def connect(self, session: dict[str, Any]) -> None:
        raise UnsupportedFeatureError(
            "Rubika connectivity is not included: provide a verified BaseTransport adapter."
        )
    async def close(self) -> None:
        return None
    async def send_message(self, chat_id: str, text: str) -> Any:
        raise UnsupportedFeatureError("Sending messages requires a verified transport adapter.")
    async def listen(self) -> AsyncIterator[Any]:
        raise UnsupportedFeatureError("Receiving updates requires a verified transport adapter.")
        yield None
