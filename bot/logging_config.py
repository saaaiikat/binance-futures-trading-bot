"""Logging configuration for the trading bot.

Configures a dual-handler logger: file handler captures all INFO+ messages
for audit purposes, while the console handler only shows WARNING+ to keep
CLI output clean.
"""

import logging
import os

LOG_DIR: str = "logs"
LOG_FILE: str = os.path.join(LOG_DIR, "app.log")
LOG_FORMAT: str = "%(asctime)s | %(levelname)s | %(message)s"


def setup_logger() -> logging.Logger:
    """Configure and return the application logger.

    Creates the logs directory if it doesn't exist. Attaches a file handler
    (INFO level) and a console handler (WARNING level) on first call.
    Subsequent calls return the already-configured logger.

    Returns:
        The configured ``trading_bot`` logger instance.
    """
    os.makedirs(LOG_DIR, exist_ok=True)

    logger = logging.getLogger("trading_bot")
    logger.setLevel(logging.DEBUG)

    if logger.handlers:
        return logger

    formatter = logging.Formatter(LOG_FORMAT)

    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger