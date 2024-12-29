
import ccxt
from binance.client import Client
import pandas as pd

class CryptoDataCollector:
    def __init__(self, exchange_name, api_key=None, api_secret=None):
        self.exchange_name = exchange_name
        self.api_key = api_key
        self.api_secret = api_secret

        if exchange_name == "binance":
            self.client = Client(api_key, api_secret)
        else:
            self.exchange = getattr(ccxt, exchange_name)({
                "apiKey": api_key,
                "secret": api_secret
            })

    def collect_data(self, symbol, timeframe='1d', limit=500):
        if self.exchange_name == "binance":
            klines = self.client.get_klines(symbol=symbol, interval=timeframe, limit=limit)
            data = pd.DataFrame(klines, columns=[
                "timestamp", "open", "high", "low", "close", "volume", "close_time",
                "quote_asset_volume", "number_of_trades", "taker_buy_base", "taker_buy_quote", "ignore"
            ])
            data["timestamp"] = pd.to_datetime(data["timestamp"], unit="ms")
            data.set_index("timestamp", inplace=True)
            return data[["open", "high", "low", "close", "volume"]]
        else:
            ohlcv = self.exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
            data = pd.DataFrame(ohlcv, columns=["timestamp", "open", "high", "low", "close", "volume"])
            data["timestamp"] = pd.to_datetime(data["timestamp"], unit="ms")
            data.set_index("timestamp", inplace=True)
            return data
