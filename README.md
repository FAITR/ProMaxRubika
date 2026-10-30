# ProMaxRubika

**Professional Development for Rubika**  
Async Python framework for building a Rubika self-account client with a pluggable transport.

- Package: `promaxrubika`
- Version: `0.1.0` (initial development release)
- Author: **FAITR** — [@FAITR_PV](https://rubika.ir/FAITR_PV)
- Official Rubika channel: [@promaxrubika](https://rubika.ir/promaxrubika)
- License: MIT
- Python: 3.11+

> **Protocol status:** This release does not implement Rubika's network protocol. No undocumented endpoints, authentication flow, message payloads, or cryptographic signatures are guessed. Network methods require a separately implemented and verified `BaseTransport` adapter. The core event system, filters, session-file handling, packaging, and tests are implemented locally.

## Install

```bash
python -m pip install .
```

## Offline event example

```python
import asyncio
from promaxrubika import Client, MessageEvent, filters

async def main():
    app = Client(session={})

    @app.on_message(filters.text)
    async def on_message(event):
        print(event.text)

    await app.dispatch(MessageEvent(text="Hello", chat_id="demo"))

asyncio.run(main())
```

## Network usage

A real network connection is **not available in the core release**. Supply an adapter implementing `promaxrubika.transport.BaseTransport`, based on authoritative protocol documentation, before calling `start()` or network methods.

```python
from promaxrubika import Client
# from my_verified_adapter import MyVerifiedRubikaTransport
# app = Client(session="my_session.json", transport=MyVerifiedRubikaTransport())
```

Without an adapter, `start()` fails explicitly with `ConnectionError` whose cause is `UnsupportedFeatureError`.

## Implemented in 0.1.0

- Async client lifecycle and async context manager
- Message event model and handler registry
- Composable text/incoming/outgoing/command/regex filters
- Local event dispatch for adapter integration and tests
- JSON session persistence with owner-only permissions where supported
- Dedicated exception hierarchy and package logger
- Packaging metadata, tests, examples, bilingual starter docs

## Not implemented / adapter required

Authentication and OTP, live Rubika connection, send/receive over Rubika, chat listing, contacts, group/channel operations, media upload/download, remote event polling, server-side retries and rate-limit handling. These are not advertised as working features.

## Security

Treat session files as credentials. Do not commit them, share them, or print their contents. File permissions are restricted where the operating system supports it; the JSON file is not encrypted.

## Development

```bash
python -m pip install -e ".[dev]"
python -m unittest discover -s tests -v
```

## Project identity

Created by **FAITR** · Rubika channel: **@promaxrubika**  
Professional Development for Rubika.
