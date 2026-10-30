"""Media operations extension point."""
from .exceptions import UnsupportedFeatureError

class Media:
    """Upload/download require verified endpoint and file-transfer semantics."""
    async def upload(self, path):
        raise UnsupportedFeatureError("Media upload requires a verified transport adapter.")
    async def download(self, media_id: str, destination):
        raise UnsupportedFeatureError("Media download requires a verified transport adapter.")
