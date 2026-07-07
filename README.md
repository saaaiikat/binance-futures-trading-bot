# Binance Futures Trading Bot (Python)

A simple Python CLI application for placing **Market** and **Limit** orders on **Binance USDⓈ-M Futures**. The project demonstrates clean code organization, input validation, logging, and exception handling.

> **Note**
>
> This project was developed as part of a Python Developer assessment. The original assignment specifies using the **Binance Futures Testnet** endpoint (`https://testnet.binancefuture.com`).
>
> However, Binance has since transitioned new Futures API development toward **Demo Trading**. The current Binance documentation recommends creating **Demo Trading API keys** for Futures, and the legacy documentation now directs developers to the Demo Trading setup for new integrations. Existing Testnet endpoints may still function, but new Futures testing should use Demo Trading where available. :contentReference[oaicite:0]{index=0}

---

## Features

- Place **MARKET** orders
- Place **LIMIT** orders
- Supports **BUY** and **SELL**
- Command-line interface using `argparse`
- Input validation
- Structured project architecture
- API request and response logging
- Exception handling for API and network errors
- Environment variable support using `.env`

---

## Project Structure

```text
trading-bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── app.log
│
├── cli.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## Requirements

- Python 3.10+
- Binance account
- Binance Futures **Demo Trading** (recommended) or legacy Testnet API credentials

---

## Installation

Clone the repository:

```bash
git clone https://github.com/saaaiikat/trading-bot.git
cd trading-bot
```

Or download the ZIP and extract it.

Create a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
BINANCE_API_KEY=YOUR_BINANCE_API_KEY
BINANCE_API_SECRET=YOUR_BINANCE_API_SECRET
```

A sample configuration is provided in `.env.example`.

---

## Running the Application

### Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

### Limit Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 120000
```

---

## Example Output

```
========== ORDER REQUEST ==========

Symbol    : BTCUSDT
Side      : BUY
Type      : MARKET
Quantity  : 0.01

==================================

========== ORDER RESPONSE ==========

Order ID      : 123456789
Status        : FILLED
Executed Qty  : 0.01
Average Price : 108925.12

==================================

Order placed successfully.
```

---

## Logging

All API requests, responses, and exceptions are written to:

```
logs/app.log
```

The log file includes:

- Request information
- API responses
- Error messages
- Exception details
- Timestamped log entries

---

## Error Handling

The application handles:

- Invalid CLI inputs
- Invalid order parameters
- Missing limit price
- Binance API exceptions
- Network failures
- Unexpected runtime exceptions

---

## Assumptions

- The assignment originally targets the Binance Futures Testnet endpoint.
- Binance now recommends using **Demo Trading** credentials for new Futures API integrations. Existing Testnet configurations may continue to work, but Demo Trading is the preferred environment for new development. :contentReference[oaicite:1]{index=1}
- The account has sufficient simulated funds.
- Internet connectivity is available.

---

## Dependencies

- python-binance
- python-dotenv

See `requirements.txt` for the complete dependency list.

---

## Author

**Saikat Das**

Python Developer Assessment – Binance Futures Trading Bot
