import streamlit as st
import yfinance as yf
import pandas as pd
from utils.indicators import calculate_indicators
from decision import investment_decision
from agents import QuantAgent, LeadAnalystAgent
from news_agent import NewsAgent




st.set_page_config(page_title="QuantAgent", layout="wide")

st.title("📊 QuantAgent - AI Financial Analyst")

ticker = st.text_input("Enter Stock Ticker (Example: AAPL, NVDA, TSLA)")

if st.button("Analyze"):

    data = yf.download(ticker, period="6mo")

    data.columns = data.columns.get_level_values(0)
    # Fix multi-level columns
    data = calculate_indicators(data)

    # calculate indicators
    latest_price = float(data["Close"].iloc[-1])
    latest_rsi = float(data["RSI"].iloc[-1])
    latest_sma = float(data["SMA"].iloc[-1])

    # run agents
    quant_agent = QuantAgent()
    lead_agent = LeadAnalystAgent()

    analysis = quant_agent.analyze_indicators(latest_rsi, latest_sma)

    decision, explanation = investment_decision(latest_price, latest_rsi, latest_sma)
    
    # News Agent
    news_agent = NewsAgent()
    headlines = news_agent.fetch_news(ticker)
    sentiment = news_agent.analyze_sentiment(headlines)

    # Final Report
    report = f"""
    Investment Recommendation: {decision}

    Technical Analysis:
    RSI = {latest_rsi:.2f}
    SMA = {latest_sma:.2f}

    News Sentiment: {sentiment}

    Explanation:
    {explanation}
    """

    st.subheader("📰 Latest Market News")

    for h in headlines:
        st.write("-", h)

    st.write("### 🧠 News Sentiment:", sentiment)

    # -----------------------------
    # AI Report
    # -----------------------------

    
    st.subheader("🤖 AI Agent Report")

    st.write(report)

    st.subheader("📊 Latest Market Data")

    col1, col2, col3 = st.columns(3)

    col1.metric("Price", f"${latest_price:.2f}")
    col2.metric("RSI", f"{latest_rsi:.2f}")
    col3.metric("SMA (20)", f"{latest_sma:.2f}")

    # -----------------------------
    # Price Chart with SMA
    # -----------------------------

    st.subheader("📈 Price Chart with SMA")

    chart_data = data[["Close", "SMA"]].copy()

    chart_data.columns = ["Price", "SMA"]

    st.line_chart(chart_data)

    # -----------------------------
    # RSI Chart
    # -----------------------------

    st.subheader("📉 RSI Indicator")

    st.line_chart(data["RSI"])

    # -----------------------------
    # Decision Logic
    # -----------------------------

    if latest_rsi < 30:
        decision = "BUY"
        explanation = """
        The RSI indicator is below 30 which suggests the stock is oversold.
        This may indicate a potential buying opportunity as the price could rebound.
        """
    elif latest_rsi > 70:
        decision = "SELL"
        explanation = """
        The RSI indicator is above 70 which suggests the stock is overbought.
        This may indicate that the stock price could decline soon.
        """
    else:
        decision = "HOLD"
        explanation = """
        The RSI value is in the neutral range (30-70).
        The market momentum is neither strongly bullish nor bearish.
        """

    st.subheader("🤖 AI Recommendation")

    if decision == "BUY":
        st.success(decision)
    elif decision == "SELL":
        st.error(decision)
    else:
        st.warning(decision)

    st.write("### 🧠 AI Explanation")
    st.write(explanation)

    # -----------------------------
    # Raw Data Section
    # -----------------------------

    with st.expander("View Raw Data"):
        st.dataframe(data.tail(20))


        # streamlit run app.py