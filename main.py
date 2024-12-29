
from xxiii_crypto_orchestrator import CryptoOrchestrator
from portfolio_optimizer import PortfolioOptimizer
from automated_trader import AutomatedTrader

crypto_sources = [
    {"exchange": "binance", "api_key": "YOUR_BINANCE_API_KEY", "api_secret": "YOUR_BINANCE_API_SECRET"},
    {"exchange": "kraken", "api_key": "YOUR_KRAKEN_API_KEY", "api_secret": "YOUR_KRAKEN_API_SECRET"}
]

crypto_symbols = ["BTC/USDT", "ETH/USDT", "BNB/USDT"]

expected_returns = [0.1, 0.08, 0.06]
covariance_matrix = [
    [0.01, 0.008, 0.007],
    [0.008, 0.02, 0.01],
    [0.007, 0.01, 0.015]
]
risk_free_rate = 0.02

trader = AutomatedTrader(broker_api="MockAPI")

orchestrator = CryptoOrchestrator(crypto_sources, PortfolioOptimizer, trader)

strategy_results = orchestrator.run_strategy(crypto_symbols, expected_returns, covariance_matrix, risk_free_rate)
print("Crypto Strategy Results:")
print(strategy_results)
