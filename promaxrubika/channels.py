"""Channel operations extension point."""
from .exceptions import UnsupportedFeatureError

class Channels:
    """Channel management requires documented protocol operations."""
    async def get(self, channel_id: str):
        raise UnsupportedFeatureError("Channel operations require a verified transport adapter.")
