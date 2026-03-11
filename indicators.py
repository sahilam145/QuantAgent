import pandas as pd

def calculate_indicators(data):

    # Simple Moving Average
    data["SMA"] = data["Close"].rolling(window=20).mean()

    # Calculate RSI
    delta = data["Close"].diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()

    rs = avg_gain / avg_loss

    data["RSI"] = 100 - (100 / (1 + rs))

    return data