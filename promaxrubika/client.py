"""Main asynchronous client."""
from __future__ import annotations
import asyncio
import logging
from pathlib import Path
from typing import Any, Callable
from .events import MessageEvent
from .filters import Filter
from .handlers import HandlerRegistry
from .messenger import Messenger
from .session import SessionStore
from .transport import MissingTransport
from .exceptions import ConnectionError

log = logging.getLogger("promaxrubika")

class Client:
    """Async client shell with pluggable, verified transport.

    Args:
        session: Session filename or in-memory session dictionary.
        transport: A BaseTransport-compatible adapter. Omit only for local
            handler/session development; network startup will fail explicitly.
    """
    def __init__(self, session: str | Path | dict[str, Any] = "promaxrubika.session",
                 transport: Any = None) -> None:
        self._session_store = SessionStore(session) if isinstance(session, (str, Path)) else None
        self._session_data = session if isinstance(session, dict) else None
        self.transport = transport if transport is not None else MissingTransport()
        self.handlers = HandlerRegistry()
        self.messenger = Messenger(self.transport)
        self._started = False
        self._stop = asyncio.Event()

    def on_message(self, filter: Filter | None = None):
        """Register an async or sync callback for MessageEvent."""
        def decorator(callback: Callable):
            self.handlers.add(callback, MessageEvent, filter)
            return callback
        return decorator

    async def start(self) -> None:
        """Load session and connect the configured transport."""
        if self._started:
            return
        data = self._session_data if self._session_data is not None else self._session_store.load()
        try:
            await self.transport.connect(data)
        except Exception as exc:
            raise ConnectionError("Could not start ProMaxRubika client") from exc
        self._started = True
        self._stop.clear()
        log.info("Client started")

    async def stop(self) -> None:
        """Stop the client and close transport resources."""
        if self._started:
            try:
                await self.transport.close()
            finally:
                self._started = False
        self._stop.set()
        log.info("Client stopped")

    async def dispatch(self, event: MessageEvent) -> None:
        """Dispatch a normalized event (useful for adapters and tests)."""
        await self.handlers.dispatch(event)

    async def run(self) -> None:
        """Consume normalized events until stop() is called."""
        if not self._started:
            raise RuntimeError("Call start() before run().")
        try:
            async for event in self.transport.listen():
                if self._stop.is_set():
                    break
                await self.dispatch(event)
        finally:
            await self.stop()

    async def send_message(self, chat_id: str, text: str):
        """Send a text message via the configured transport."""
        return await self.messenger.send_message(chat_id, text)

    async def __aenter__(self):
        await self.start()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.stop()
