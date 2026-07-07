"""bot — Binance Futures Testnet Trading Bot package.

Provides client initialization, order placement, and input validation
for placing MARKET and LIMIT futures orders via the Binance API.
"""

from bot.client import BinanceClient
from bot.orders import OrderManager
from bot.validators import validate

__all__: list[str] = ["BinanceClient", "OrderManager", "validate"]
