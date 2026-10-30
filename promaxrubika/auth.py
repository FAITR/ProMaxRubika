"""Authentication extension point.

Authentication flows depend on a documented and verified Rubika protocol adapter.
This module deliberately does not guess OTP, password, or token endpoints.
"""
from .exceptions import UnsupportedFeatureError

class AuthManager:
    """Explicitly unavailable authentication facade until an adapter is supplied."""
    async def login(self, *args, **kwargs):
        """Authenticate using a future verified adapter."""
        raise UnsupportedFeatureError(
            "Authentication is adapter-specific and is not implemented in the core package."
        )
