"""Binance Futures Trading Bot — CLI entry point.

Parses command-line arguments, validates inputs, and places futures orders
on the Binance Testnet via the OrderManager.
"""

from __future__ import annotations

import argparse
import sys

from binance.exceptions import BinanceAPIException, BinanceRequestException

from bot.logging_config import setup_logger
from bot.orders import OrderManager
from bot.validators import validate

logger = setup_logger()

SEPARATOR = "=" * 36


def print_request(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float | None = None,
) -> None:
    """Print a formatted order request summary to the console."""
    print(f"\n========== ORDER REQUEST ==========")
    print(f"")
    print(f"Symbol    : {symbol}")
    print(f"Side      : {side}")
    print(f"Type      : {order_type}")
    print(f"Quantity  : {quantity}")
    if price is not None:
        print(f"Price     : {price}")
    print(f"")
    print(f"==================================")


def print_response(order: dict) -> None:
    """Print a formatted order response summary to the console."""
    print(f"\n========== ORDER RESPONSE ==========")
    print(f"")
    print(f"Order ID      : {order.get('orderId')}")
    print(f"Status        : {order.get('status')}")
    print(f"Executed Qty  : {order.get('executedQty')}")
    print(f"Average Price : {order.get('avgPrice')}")
    print(f"")
    print(f"===================================")
    print(f"\n✅ Order placed successfully.\n")


def main() -> None:
    """Parse CLI arguments, validate inputs, and execute the order."""
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot — Place MARKET and LIMIT orders.",
    )
    parser.add_argument("--symbol", required=True, help="Trading pair (e.g. BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", dest="order_type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", type=float, required=True, help="Order quantity (> 0)")
    parser.add_argument("--price", type=float, default=None, help="Limit price (required for LIMIT orders)")

    args = parser.parse_args()

    symbol: str = args.symbol.upper()
    side: str = args.side.upper()
    order_type: str = args.order_type.upper()
    quantity: float = args.quantity
    price: float | None = args.price

    try:
        validate(symbol, side, order_type, quantity, price)

        print_request(symbol, side, order_type, quantity, price)

        manager = OrderManager()
        response: dict = manager.place_order(symbol, side, order_type, quantity, price)

        print_response(response)

    except ValueError as exc:
        logger.error("Validation error: %s", exc)
        print(f"\n❌ Order failed: {exc}\n")
        sys.exit(1)

    except BinanceAPIException as exc:
        logger.exception("Binance API error")
        print(f"\n❌ Order failed (API Error): {exc.message}\n")
        sys.exit(1)

    except BinanceRequestException as exc:
        logger.exception("Binance request error")
        print(f"\n❌ Order failed (Request Error): {exc}\n")
        sys.exit(1)

    except ConnectionError:
        logger.exception("Connection error")
        print("\n❌ Order failed: Unable to connect to Binance. Check your network.\n")
        sys.exit(1)

    except TimeoutError:
        logger.exception("Request timeout")
        print("\n❌ Order failed: Request timed out. Try again later.\n")
        sys.exit(1)

    except Exception:
        logger.exception("Unexpected error")
        print("\n❌ Order failed: An unexpected error occurred. See logs/app.log for details.\n")
        sys.exit(1)


if __name__ == "__main__":
    main()