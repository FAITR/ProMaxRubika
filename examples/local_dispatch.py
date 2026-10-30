"""Offline example: demonstrates event handlers without connecting to Rubika."""
import asyncio
from promaxrubika import Client, MessageEvent, filters

async def main():
    app = Client(session={})

    @app.on_message(filters.text)
    async def on_message(event):
        print("Received normalized event:", event.text)

    await app.dispatch(MessageEvent(text="Hello from an offline test", chat_id="demo"))

if __name__ == "__main__":
    asyncio.run(main())
