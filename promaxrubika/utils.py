"""Small internal utilities."""
import logging

def configure_logging(level: int = logging.INFO) -> None:
    """Configure the package logger without exposing credentials."""
    logger = logging.getLogger("promaxrubika")
    logger.setLevel(level)
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        ))
        logger.addHandler(handler)
