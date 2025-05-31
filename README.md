# arbitrage-bot
Python-based arbitrage bot using flash loans to exploit price differences across DEXs and CEXs (Uniswap, PancakeSwap, Binance, Kraken). Operates on BNB Chain and Polygon with real-time WebSocket feeds and custom smart contracts. Designed for cloud deployment and low-latency execution.

# 🔁 Cross-Exchange Flash Loan Arbitrage Bot

A cloud-based Python bot that performs real-time cross-exchange arbitrage using flash loans. It scans price differences across decentralized (Uniswap, PancakeSwap, SushiSwap) and centralized (Binance, Kraken Pro) exchanges to execute profitable trades with zero upfront capital.

---

## ⚙️ Features

- 🧠 Real-time arbitrage detection (WebSocket feeds)
- 💸 Flash loan execution via Aave
- 🔁 Cross-exchange DEX/CEX arbitrage (Uniswap V3, PancakeSwap, etc.)
- ⛓️ Operates on BNB Chain and Polygon
- 🧾 Public order book monitoring (Kraken, Binance)
- 🪙 Targets: USDT, USDC, SOL, ADA, XRP, CUSD, BNB, and more
- 🧠 Smart slippage & MEV avoidance strategies
- ☁️ Cloud-ready (run on Codespaces, Railway, or Render)

---

## 🛠️ Tech Stack

- Python 3.10+
- `web3.py`, `ccxt`, `aiohttp`, `python-dotenv`
- Solidity (for custom smart contracts)
- Aave Protocol (flash loan provider)
- Uniswap V3 & PancakeSwap Router
- WebSocket + REST APIs

---
