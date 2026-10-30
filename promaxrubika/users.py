"""User and contact operations extension point."""
from .exceptions import UnsupportedFeatureError

class Users:
    """User lookup and contact management require a verified adapter."""
    async def get(self, user_id: str):
        raise UnsupportedFeatureError("User operations require a verified transport adapter.")
