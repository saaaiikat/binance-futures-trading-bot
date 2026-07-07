"""Order execution logic for Binance Futures.

Provides a single unified entry point for placing MARKET and LIMIT orders,
with structured logging of requests and responses.
"""

from __future__ import annotations

from binance.client import Client

from bot.client import BinanceClient
from bot.logging_config import setup_logger

logger = setup_logger()


class OrderManager:
    """Manages order placement against the Binance Futures API.

    Wraps the Binance client and provides a single ``place_order`` method
    that handles both MARKET and LIMIT order types.
    """

    def __init__(self) -> None:
        """Initialize the OrderManager with a configured Binance client."""
        self.client: Client = BinanceClient().get_client()

    def place_order(
        self,
        symbol: str,
        side: str,
        order_type: str,
        quantity: float,
        price: float | None = None,
    ) -> dict:
        """Place a MARKET or LIMIT futures order on Binance.

        Constructs request parameters dynamically based on order type.
        For LIMIT orders, ``timeInForce`` is automatically set to GTC.

        Args:
            symbol: Trading pair (e.g. "BTCUSDT").
            side: "BUY" or "SELL".
            order_type: "MARKET" or "LIMIT".
            quantity: Amount to trade.
            price: Limit price (required for LIMIT, ignored for MARKET).

        Returns:
            The Binance API response as a dictionary.

        Raises:
            BinanceAPIException: On Binance-specific API errors.
            BinanceRequestException: On request-level errors.
            ConnectionError: On network connectivity issues.
            TimeoutError: On request timeout.
        """
        params: dict = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        self._log_request(params)

        order: dict = self.client.futures_create_order(**params)

        self._log_response(order)

        return order

    @staticmethod
    def _log_request(params: dict) -> None:
        """Log a structured summary of the outgoing order request."""
        logger.info(
            "Order Request — Symbol: %s | Side: %s | Type: %s | Qty: %s%s",
            params["symbol"],
            params["side"],
            params["type"],
            params["quantity"],
            f" | Price: {params['price']}" if "price" in params else "",
        )

    @staticmethod
    def _log_response(order: dict) -> None:
        """Log a structured summary of the order response."""
        logger.info(
            "Order Response — ID: %s | Status: %s | Executed Qty: %s | Avg Price: %s",
            order.get("orderId"),
            order.get("status"),
            order.get("executedQty"),
            order.get("avgPrice"),
        )