import pandas as pd
import pyupbit


class Finance:
    @staticmethod
    def gen_fibo(limit: int = 200):
        a = b = 1
        while True:
            a, b = b, a + b
            if b >= limit:
                return
            yield b

    def __init__(self):
        period = 72
        self.fibo = list(self.gen_fibo(period))

    cache_price = {}

    def get_price(self, ticker: str, cache: bool = True) -> pd.DataFrame:
        if not cache or ticker not in self.cache_price:
            self.cache_price[ticker] = pyupbit.get_ohlcv(
                ticker=f"KRW-{ticker}", interval="minute60"
            )
        return self.cache_price[ticker]
    
    def get_current_price(self, ticker: str) -> float:
        return pyupbit.get_current_price(f'KRW-{ticker}')

    def get_score(self, ticker: str) -> float:
        price = self.get_price(ticker)
        sum_val = 0
        for f in self.fibo:
            func = lambda x: (x[-1] / x[0] - 1) * 100
            change = price.close.rolling(f).apply(func).iloc[-1]
            sum_val += change
        return sum_val / len(self.fibo)

    def get_aatr(self, ticker: str) -> float:
        price = self.get_price(ticker)
        atr = (price.high - price.low).ewm(max(self.fibo)).mean()
        return (atr / price.close).iloc[-1]

    def signal(self, ticker: str) -> bool:
        return self.get_score(ticker) > 0

    def max_ratio(self, ticker: str) -> float:
        return max(0.01 / self.get_aatr(ticker), 0.01)
