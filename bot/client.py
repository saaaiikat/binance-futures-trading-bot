"""Binance Futures API client initialization.

Isolates API authentication and client setup from all business logic.
"""

import os

from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

BINANCE_API_KEY: str | None = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET: str | None = os.getenv("BINANCE_API_SECRET")


class BinanceClient:
    """Wrapper around the python-binance Client for Futures Testnet.

    Validates that API credentials exist before creating the client
    and configures the Binance Futures Testnet endpoint.
    """

    def __init__(self) -> None:
        """Initialize the Binance Futures Testnet client.

        Raises:
            ValueError: If BINANCE_API_KEY or BINANCE_API_SECRET is missing.
        """
        if not BINANCE_API_KEY:
            raise ValueError(
                "BINANCE_API_KEY is missing. "
                "Set it in your .env file or as an environment variable."
            )
        if not BINANCE_API_SECRET:
            raise ValueError(
                "BINANCE_API_SECRET is missing. "
                "Set it in your .env file or as an environment variable."
            )

        self.client: Client = Client(
            BINANCE_API_KEY,
            BINANCE_API_SECRET,
            testnet=True,
        )
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def get_client(self) -> Client:
        """Return the configured Binance client instance."""
        return self.client