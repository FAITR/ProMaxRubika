"""Composable event filters."""
from __future__ import annotations
from collections.abc import Callable
from typing import Any

Predicate = Callable[[Any], bool]

class Filter:
    """A callable predicate supporting &, | and ~ composition."""
    def __init__(self, predicate: Predicate, name: str = "custom") -> None:
        self.predicate, self.name = predicate, name

    def __call__(self, event: Any) -> bool:
        try:
            return bool(self.predicate(event))
        except Exception:
            return False

    def __and__(self, other: "Filter") -> "Filter":
        return Filter(lambda e: self(e) and other(e), f"({self.name}&{other.name})")

    def __or__(self, other: "Filter") -> "Filter":
        return Filter(lambda e: self(e) or other(e), f"({self.name}|{other.name})")

    def __invert__(self) -> "Filter":
        return Filter(lambda e: not self(e), f"~{self.name}")

text = Filter(lambda e: isinstance(getattr(e, "text", None), str), "text")
incoming = Filter(lambda e: not getattr(e, "is_outgoing", False), "incoming")
outgoing = Filter(lambda e: bool(getattr(e, "is_outgoing", False)), "outgoing")
private = Filter(lambda e: bool(getattr(e, "chat_type", None) == "private"), "private")
group = Filter(lambda e: bool(getattr(e, "chat_type", None) == "group"), "group")

def command(value: str) -> Filter:
    """Match a text message beginning with a command such as /start."""
    if not value.startswith("/"):
        raise ValueError("command must begin with '/'")
    return Filter(lambda e: isinstance(getattr(e, "text", None), str)
                  and e.text.split(maxsplit=1)[0] == value, f"command:{value}")

def regex(pattern: str, flags: int = 0) -> Filter:
    """Match message text using a regular expression."""
    import re
    compiled = re.compile(pattern, flags)
    return Filter(lambda e: isinstance(getattr(e, "text", None), str)
                  and compiled.search(e.text) is not None, f"regex:{pattern}")
