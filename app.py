import streamlit as st
import pandas as pd
from agent import decision

st.title("📊 Agentic Financial Analyst")

# --- User Inputs ---
predicted_price = st.number_input("Enter Predicted Price", value=100.0)
current_price = st.number_input("Enter Current Price", value=95.0)
sentiment = st.slider("Market Sentiment (-1 to 1)", -1.0, 1.0, 0.0)

# Convert to Pandas Series (simulate your earlier setup)
predicted_price = pd.Series([predicted_price])
current_price = pd.Series([current_price])
sentiment = pd.Series([sentiment])

# --- Decision ---
if st.button("Get Decision"):
    final_decision = decision(predicted_price, current_price, sentiment)

    st.subheader("📌 Final Decision")
    st.success(final_decision)