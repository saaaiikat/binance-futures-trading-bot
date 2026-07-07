"""Input validation for order parameters.

Validates side, order type, quantity, price, and symbol format before
any order is submitted to the Binance API.
"""

import logging

logger = logging.getLogger("trading_bot")

VALID_SIDES: list[str] = ["BUY", "SELL"]
VALID_ORDER_TYPES: list[str] = ["MARKET", "LIMIT"]


def validate(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float | None = None,
) -> None:
    """Validate all order parameters before submission.

    Args:
        symbol: Trading pair symbol (e.g. "BTCUSDT").
        side: Order side — must be "BUY" or "SELL".
        order_type: Order type — must be "MARKET" or "LIMIT".
        quantity: Order quantity — must be greater than zero.
        price: Limit price — required for LIMIT orders, must be > 0.

    Raises:
        ValueError: If any parameter fails validation.
    """
    side = side.upper()
    order_type = order_type.upper()

    if side not in VALID_SIDES:
        raise ValueError(
            f"Invalid side '{side}'. Must be one of: {', '.join(VALID_SIDES)}."
        )

    if order_type not in VALID_ORDER_TYPES:
        raise ValueError(
            f"Invalid order type '{order_type}'. "
            f"Must be one of: {', '.join(VALID_ORDER_TYPES)}."
        )

    if quantity <= 0:
        raise ValueError(
            f"Quantity must be greater than zero. Received: {quantity}."
        )

    if order_type == "LIMIT" and price is None:
        raise ValueError("LIMIT orders require a --price argument.")

    if price is not None and price <= 0:
        raise ValueError(
            f"Price must be greater than zero. Received: {price}."
        )

    if symbol != symbol.upper():
        raise ValueError(
            f"Symbol must be uppercase. Received: '{symbol}'. "
            f"Use '{symbol.upper()}' instead."
        )

    if not symbol.endswith("USDT"):
        logger.warning(
            "Symbol '%s' does not end with 'USDT'. "
            "Most Futures pairs use USDT margining.",
            symbol,
        )