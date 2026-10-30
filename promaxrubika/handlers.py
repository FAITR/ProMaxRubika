"""Handler registration and dispatch."""
from __future__ import annotations
import inspect
import logging
from dataclasses import dataclass
from typing import Any, Awaitable, Callable
from .filters import Filter

log = logging.getLogger("promaxrubika")

@dataclass(slots=True)
class Handler:
    callback: Callable[..., Any]
    event_type: type
    filter: Filter | None = None

class HandlerRegistry:
    """Stores handlers and dispatches matching events in registration order."""
    def __init__(self) -> None:
        self._handlers: list[Handler] = []

    def add(self, callback: Callable[..., Any], event_type: type,
            filter: Filter | None = None) -> Callable[..., Any]:
        if not callable(callback):
            raise TypeError("handler must be callable")
        self._handlers.append(Handler(callback, event_type, filter))
        return callback

    async def dispatch(self, event: Any) -> None:
        for handler in tuple(self._handlers):
            if not isinstance(event, handler.event_type):
                continue
            if handler.filter is not None and not handler.filter(event):
                continue
            result = handler.callback(event)
            if inspect.isawaitable(result):
                await result
