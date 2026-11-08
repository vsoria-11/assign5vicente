import streamlit as st
import yfinance as yf

st.title("AAPL 5-Year Average Stock Price")

#5 YEARS AAPL DATA
data = yf.Ticker("AAPL").history(period="5y")

if not data.empty:
    #CALCULATE AVERAGE CLOSING PRICE
    overall_average = data['Close'].mean()
    
    #PRINT RESULT
    st.metric(label="5-Year Average Price", value=f"${overall_average:.2f}")
else:
    st.error("No data found for AAPL.")
