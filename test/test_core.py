import asyncio
import tempfile
import unittest
from pathlib import Path

from promaxrubika import Client, MessageEvent, filters
from promaxrubika.session import SessionStore
from promaxrubika.exceptions import UnsupportedFeatureError, ConnectionError

class FakeTransport:
    def __init__(self):
        self.connected = False
        self.sent = []
    async def connect(self, session):
        self.connected = True
    async def close(self):
        self.connected = False
    async def send_message(self, chat_id, text):
        self.sent.append((chat_id, text))
        return {"ok": True}
    async def listen(self):
        yield MessageEvent(text="hello", chat_id="c1")

class CoreTests(unittest.TestCase):
    def test_session_roundtrip(self):
        with tempfile.TemporaryDirectory() as tmp:
            store = SessionStore(Path(tmp) / "session.json")
            store.save({"key": "test"})
            self.assertEqual(store.load(), {"key": "test"})

    def test_filter_composition(self):
        event = MessageEvent(text="hello")
        self.assertTrue(filters.text(event))
        self.assertTrue((filters.text & ~filters.outgoing)(event))
        self.assertFalse(filters.command("/start")(event))

    def test_dispatch_and_send(self):
        async def scenario():
            transport = FakeTransport()
            app = Client(session={}, transport=transport)
            received = []
            @app.on_message(filters.text)
            async def handler(event):
                received.append(event.text)
            await app.start()
            await app.dispatch(MessageEvent(text="test"))
            await app.send_message("chat", "hi")
            await app.stop()
            self.assertEqual(received, ["test"])
            self.assertEqual(transport.sent, [("chat", "hi")])
            self.assertFalse(transport.connected)
        asyncio.run(scenario())

    def test_missing_transport_is_explicit(self):
        async def scenario():
            app = Client(session={})
            with self.assertRaises(ConnectionError):
                await app.start()
        asyncio.run(scenario())

if __name__ == "__main__":
    unittest.main()
      
