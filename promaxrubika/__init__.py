"""ProMaxRubika: async Rubika client framework."""
from .client import Client
from .events import MessageEvent
from .exceptions import (
    ProMaxRubikaError,
    ConnectionError,
    AuthenticationError,
    UnsupportedFeatureError,
    SessionError,
    TransportError,
)
from . import filters

__author__ = "FAITR (@FAITR_PV)"
__version__ = "0.1.0"

__all__ = [
    "Client",
    "MessageEvent",
    "filters",
    "ProMaxRubikaError",
    "ConnectionError",
    "AuthenticationError",
    "UnsupportedFeatureError",
    "SessionError",
    "TransportError",
]
