import streamlit as st
import yfinance as yf
<<<<<<< HEAD
import pandas as pd
from agent import decision
=======
import requests
from transformers import pipeline
import time

# -----------------------------
# 🔹 CONFIG
# -----------------------------
API_KEY = "64e143b304be489ea2adf2ae99cb77a6"   # 🔴 Replace this
>>>>>>> 6fec859 (Updated project files)

st.title("📊 Agentic Financial Analyst") 

<<<<<<< HEAD
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
=======
# -----------------------------
# 🔹 INPUT
# -----------------------------
stock = st.text_input("Enter Stock Symbol", "AAPL")

# -----------------------------
# 🔹 FETCH REAL-TIME STOCK DATA
# -----------------------------
data = yf.download(stock, period="1d", interval="1m")

if data.empty:
    st.error("Invalid stock symbol or no data available")
    st.stop()

st.subheader("📈 Live Stock Price")
st.line_chart(data["Close"])

current_price = data["Close"].iloc[-1]

# -----------------------------
# 🔹 REAL-TIME NEWS SENTIMENT
# -----------------------------
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")

sentiment_model = load_model()

def get_sentiment(stock):
    try:
        url = f"https://newsapi.org/v2/everything?q={stock}&apiKey={API_KEY}"
        response = requests.get(url)
        articles = response.json().get("articles", [])[:5]

        headlines = [a["title"] for a in articles if a["title"]]

        if not headlines:
            return 0

        results = sentiment_model(headlines)

        score = 0
        for r in results:
            if r['label'] == 'POSITIVE':
                score += 1
            else:
                score -= 1

        return float(score) / float(len(results)) if len(results) > 0 else 0.0

    except Exception:
        return 0

sentiment = get_sentiment(stock)

st.subheader("📰 Sentiment Score")
st.write(sentiment)

# -----------------------------
# 🔹 SIMPLE PREDICTION (DUMMY)
# -----------------------------
predicted_price = current_price * 1.02  # simple assumption

st.subheader("📊 Prediction")
current_price = current_price.iloc[-1]
st.write(f"Current Price: {current_price:.2f}")
st.write(f"Predicted Price: {predicted_price[0]:.2f}")
st.write("DEBUG:", predicted_price, current_price, sentiment)

# -----------------------------
# 🔹 AGENT DECISION
# -----------------------------
def decision(predicted, current, sentiment):

    try:
        predicted = float(predicted)
        current = float(current)
        sentiment = float(sentiment)
    except Exception:
        return "HOLD"

    if sentiment > 0.5 and predicted > current:
        return "STRONG BUY"
    elif sentiment < -0.5 and predicted < current:
        return "STRONG SELL"
    elif predicted > current:
        return "BUY"
    elif predicted < current:
        return "SELL"
    else:
        return "HOLD"
# -----------------------------
# 🔹 AUTO REFRESH
# -----------------------------

time.sleep(10)
st.rerun()
>>>>>>> 6fec859 (Updated project files)
