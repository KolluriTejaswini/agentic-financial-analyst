import streamlit as st
import yfinance as yf
import pandas as pd
from agent import decision

st.title("📊 Agentic Financial Analyst")

# --- User Inputs ---
predicted_price_input = st.number_input("Enter Predicted Price", value=100.0)
current_price_input = st.number_input("Enter Current Price", value=95.0)
sentiment_input = st.slider("Market Sentiment (-1 to 1)", -1.0, 1.0, 0.0)

# Convert to Pandas Series (for compatibility with your agent code)
predicted_price = pd.Series([predicted_price_input])
current_price = pd.Series([current_price_input])
sentiment = pd.Series([sentiment_input])


# --- Button Action ---
if st.button("Get Decision"):
    

    
    final_decision = decision(predicted_price, current_price, sentiment)

    # --- Risk Calculation ---
    sentiment_value = sentiment_input
    if sentiment_value > 0.5:
        risk = "LOW"
    elif sentiment_value < -0.5:
        risk = "HIGH"
    else:
        risk = "MEDIUM"

    st.subheader("📌 Results")

    st.write("💰 Current Price:", current_price_input)
    st.write("📈 Predicted Price:", predicted_price_input)
    st.write("🧠 Sentiment Score:", sentiment_input)
    st.write("⚠️ Risk Level:", risk)

    # Decision color
    if final_decision == "BUY":
        st.success("✅ Decision: BUY")
    elif final_decision == "SELL":
        st.error("❌ Decision: SELL")
    else:
        st.warning("⚠️ Decision: HOLD")

    # --- GRAPH SECTION ---
    st.subheader("📊 Stock Price Trend")

    data = yf.download("AAPL", period="1mo")  # last 1 month data
    st.line_chart(data["Close"])
