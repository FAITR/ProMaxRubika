"""Local session-file handling with restrictive filesystem permissions."""
from __future__ import annotations
import json
import os
from pathlib import Path
from typing import Any
from .exceptions import SessionError

class SessionStore:
    """Read/write a JSON session file.

    The library never logs session contents. The file is created with owner-only
    permissions where supported. This is not encryption: protect the device and
    back up session files securely.
    """
    def __init__(self, path: str | Path) -> None:
        self.path = Path(path).expanduser()

    def load(self) -> dict[str, Any]:
        if not self.path.exists():
            return {}
        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
            if not isinstance(data, dict):
                raise ValueError("session root must be an object")
            return data
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            raise SessionError(f"Could not read session file: {self.path}") from exc

    def save(self, data: dict[str, Any]) -> None:
        if not isinstance(data, dict):
            raise TypeError("session data must be a dictionary")
        self.path.parent.mkdir(parents=True, exist_ok=True)
        temp = self.path.with_suffix(self.path.suffix + ".tmp")
        try:
            temp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
            try:
                os.chmod(temp, 0o600)
            except OSError:
                pass
            temp.replace(self.path)
            try:
                os.chmod(self.path, 0o600)
            except OSError:
                pass
        except OSError as exc:
            try:
                temp.unlink(missing_ok=True)
            except OSError:
                pass
            raise SessionError("Could not securely write session file") from exc
