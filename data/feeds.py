import ccxt
import asyncio
import aiohttp
import json

binance = ccxt.binance()

async def get_binance_price(symbol="ETH/USDT"):
    ticker = binance.fetch_ticker(symbol)
    return ticker['last']

async def uniswap_ws_listener(pair="ETH/USDC"):
    url = "wss://polygon-mainnet.g.alchemy.com/v2/5LUrmX4ZXiv8h0NxJoRbOhZAiN25D32y"  # Replace with your WebSocket URL

    async with aiohttp.ClientSession() as session:
        async with session.ws_connect(url) as ws:
            # Example subscription to Uniswap pool updates (adjust to actual pair contract)
            payload = {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "eth_subscribe",
                "params": ["logs", {
                    "address": "0x8ad599c3a0ff1de082011efddc58f1908eb6e6d8"  # Uniswap V3 ETH/USDC pool on Ethereum
                }]
            }
            await ws.send_json(payload)

            while True:
                msg = await ws.receive()
                print(msg.data)

# Example testing
if __name__ == "__main__":
    print(asyncio.run(get_binance_price()))
    asyncio.run(uniswap_ws_listener())
