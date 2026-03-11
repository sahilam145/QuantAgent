class QuantAgent:

    def analyze_indicators(self, rsi, sma):
        return f"RSI value is {rsi:.2f} and SMA is {sma:.2f}."


class LeadAnalystAgent:

    def final_report(self, decision, explanation):
        report = f"""
        Investment Recommendation: {decision}

        Analysis Summary:
        {explanation}

        This decision is based on technical indicators such as RSI and SMA.
        """
        return report