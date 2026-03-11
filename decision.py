def investment_decision(price, rsi, sma):

    if rsi < 30 and price < sma:
        decision = "BUY"
        explanation = "RSI shows the stock is oversold and price is below moving average."

    elif rsi > 70 and price > sma:
        decision = "SELL"
        explanation = "RSI indicates overbought conditions and price is above moving average."

    else:
        decision = "HOLD"
        explanation = "Market momentum is neutral."

    return decision, explanation