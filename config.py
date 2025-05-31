import os
from dotenv import load_dotenv
load_dotenv()

RPC_URL_POLYGON = os.getenv("RPC_URL_POLYGON")
WALLET_PRIVATE_KEY = os.getenv("PRIVATE_KEY")
PUBLIC_ADDRESS = os.getenv("PUBLIC_ADDRESS")

TOKENS = ["USDT", "USDC", "BNB", "WBNB", "XRP"]
EXCHANGES = ["binance", "uniswap", "pancakeswap", "kraken"]

PROFIT_THRESHOLD = 0.005
SLIPPAGE_TOLERANCE = 0.003
