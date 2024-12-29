
class RiskAnalyzer:
    def __init__(self):
        pass

    def calculate_volatility(self, data):
        return data["Close"].pct_change().std()

    def calculate_var(self, data, confidence_level=0.95):
        return data["Close"].pct_change().quantile(1 - confidence_level)
