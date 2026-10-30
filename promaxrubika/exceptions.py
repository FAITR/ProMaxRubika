"""Public exception hierarchy."""

class ProMaxRubikaError(Exception):
    """Base exception for this library."""

class UnsupportedFeatureError(ProMaxRubikaError, NotImplementedError):
    """Raised when an operation requires an unavailable protocol adapter."""

class TransportError(ProMaxRubikaError):
    """A transport-level operation failed."""

class ConnectionError(TransportError):
    """Connection or disconnection failed."""

class AuthenticationError(ProMaxRubikaError):
    """Authentication failed."""

class SessionError(ProMaxRubikaError):
    """Session could not be read, written, or validated."""

class RateLimitError(TransportError):
    """The remote service asked the client to slow down."""

class APIError(TransportError):
    """The remote service returned an application-level error."""
