"""Group operations extension point."""
from .exceptions import UnsupportedFeatureError

class Groups:
    """Group management requires documented protocol operations."""
    async def get(self, group_id: str):
        raise UnsupportedFeatureError("Group operations require a verified transport adapter.")
