"""Chat operations extension point."""
from .exceptions import UnsupportedFeatureError

class Chats:
    """Chat listing and lookup require a protocol adapter."""
    async def list(self):
        raise UnsupportedFeatureError("Listing chats requires a verified transport adapter.")
