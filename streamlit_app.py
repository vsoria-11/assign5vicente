import streamlit as st
import yfinance as yf

st.title("AAPL 5-Year Average Stock Price")

data = yf.Ticker("AAPL").history(period="5y")

if not data.empty:
    overall_average = data['Close'].mean()
    
    st.metric(label="5-Year Average Price", value=f"${overall_average:.2f}")
else:
    st.error("No data found for AAPL.")
