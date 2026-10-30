"""Template only: implement this contract after obtaining verified protocol docs.

Do not fill this with guessed endpoints, keys, request signatures, or payloads.
"""
from promaxrubika.transport import BaseTransport

class MyVerifiedRubikaTransport(BaseTransport):
    async def connect(self, session):
        raise NotImplementedError("Implement from authoritative protocol documentation.")

    async def close(self):
        raise NotImplementedError

    async def send_message(self, chat_id, text):
        raise NotImplementedError

    async def listen(self):
        raise NotImplementedError
        yield None
