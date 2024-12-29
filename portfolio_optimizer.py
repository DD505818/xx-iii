
import numpy as np
from scipy.optimize import minimize

class PortfolioOptimizer:
    def __init__(self, expected_returns, covariance_matrix, risk_free_rate):
        self.expected_returns = np.array(expected_returns)
        self.covariance_matrix = np.array(covariance_matrix)
        self.risk_free_rate = risk_free_rate

    def calculate_performance(self, weights):
        portfolio_return = np.sum(self.expected_returns * weights)
        portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(self.covariance_matrix, weights)))
        sharpe_ratio = (portfolio_return - self.risk_free_rate) / portfolio_volatility
        return portfolio_return, portfolio_volatility, sharpe_ratio

    def optimize(self):
        num_assets = len(self.expected_returns)
        initial_guess = [1.0 / num_assets] * num_assets
        bounds = [(0, 1) for _ in range(num_assets)]
        constraints = {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}
        result = minimize(lambda weights: -self.calculate_performance(weights)[2], initial_guess, method='SLSQP',
                          bounds=bounds, constraints=constraints)
        return result.x
