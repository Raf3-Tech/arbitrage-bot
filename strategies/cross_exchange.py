async def detect_opportunity(prices):
    """
    prices = {
        'binance': {'ETH/USDT': 2500},
        'uniswap': {'ETH/USDT': 2550}
    }
    """
    for pair in prices['binance']:
        if pair in prices['uniswap']:
            price_binance = prices['binance'][pair]
            price_uniswap = prices['uniswap'][pair]
            delta = price_uniswap - price_binance
            perc = delta / price_binance
            if perc >= 0.005:
                print(f"🔍 Arbitrage Opportunity on {pair}: Buy @ Binance (${price_binance}), Sell @ Uniswap (${price_uniswap})")
