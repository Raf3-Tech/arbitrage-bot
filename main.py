import asyncio
from data.feeds import get_binance_price
from strategies.cross_exchange import detect_opportunity

async def run():
    prices = {
        'binance': {'ETH/USDT': await get_binance_price("ETH/USDT")},
        'uniswap': {'ETH/USDT': 2550}  # Simulated price
    }

    await detect_opportunity(prices)

if __name__ == "__main__":
    asyncio.run(run())
