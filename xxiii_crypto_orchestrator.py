
from crypto_data_collector import CryptoDataCollector
from portfolio_optimizer import PortfolioOptimizer

class CryptoOrchestrator:
    def __init__(self, crypto_sources, portfolio_optimizer, trader):
        self.crypto_sources = crypto_sources
        self.portfolio_optimizer = portfolio_optimizer
        self.trader = trader

    def run_strategy(self, crypto_symbols, expected_returns, covariance_matrix, risk_free_rate):
        historical_data = {}
        for source in self.crypto_sources:
            collector = CryptoDataCollector(source["exchange"], source.get("api_key"), source.get("api_secret"))
            historical_data[source["exchange"]] = {
                symbol: collector.collect_data(symbol)
                for symbol in crypto_symbols
            }

        risk_analysis = {}
        for exchange, symbols_data in historical_data.items():
            risk_analysis[exchange] = {}
            for symbol, data in symbols_data.items():
                returns = data["close"].pct_change()
                risk_analysis[exchange][symbol] = {
                    "volatility": returns.std(),
                    "correlation": returns.corr()
                }

        portfolio_optimizer = PortfolioOptimizer(expected_returns, covariance_matrix, risk_free_rate)
        optimized_weights = portfolio_optimizer.optimize_portfolio()

        trades = [{"exchange": source["exchange"], "symbol": symbol, "allocation": weight}
                  for source, weight in zip(self.crypto_sources, optimized_weights)]
        self.trader.execute_trades(trades)

        return {
            "Historical Data": historical_data,
            "Risk Analysis": risk_analysis,
            "Optimized Weights": optimized_weights
        }
