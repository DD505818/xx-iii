import json
import os

def setup_wizard():
    print("Welcome to the DDGPT Trading System Setup Wizard!")

    # Configure API Keys
    print("\nStep 1: API Key Configuration")
    binance_api_key = input("Enter your Binance API Key: ")
    binance_api_secret = input("Enter your Binance API Secret: ")
    kraken_api_key = input("Enter your Kraken API Key: ")
    kraken_api_secret = input("Enter your Kraken API Secret: ")
    coinbase_api_key = input("Enter your Coinbase API Key: ")
    coinbase_api_secret = input("Enter your Coinbase API Secret: ")
    paypal_api_key = input("Enter your PayPal API Key: ")
    stripe_api_key = input("Enter your Stripe API Key: ")

    # Save API Keys
    api_config = {
        "binance": {"api_key": binance_api_key, "api_secret": binance_api_secret},
        "kraken": {"api_key": kraken_api_key, "api_secret": kraken_api_secret},
        "coinbase": {"api_key": coinbase_api_key, "api_secret": coinbase_api_secret},
        "payment": {"paypal": paypal_api_key, "stripe": stripe_api_key},
    }
    with open("config/api_keys.json", "w") as f:
        json.dump(api_config, f, indent=4)

    # Configure Strategy Parameters
    print("\nStep 2: Strategy Parameters Configuration")
    low_leverage = input("Enter leverage for low volatility (default: 5): ") or 5
    high_leverage = input("Enter leverage for high volatility (default: 2): ") or 2
    stop_loss = input("Enter stop-loss percentage (default: 20): ") or 20

    # Save Strategy Parameters
    strategy_config = {
        "leverage": {"low_volatility": int(low_leverage), "high_volatility": int(high_leverage)},
        "stop_loss": float(stop_loss) / 100,
    }
    with open("config/trading_parameters.json", "w") as f:
        json.dump(strategy_config, f, indent=4)

    print("\nSetup Complete! You can now start trading.")

if __name__ == "__main__":
    setup_wizard()
