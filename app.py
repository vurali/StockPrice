# Import required libraries
import streamlit as st
import yfinance as yf

# Set Streamlit page configuration
st.set_page_config(page_title="Stock Price App", page_icon=":chart_with_upwards_trend:")

# Define a dictionary with ticker symbols for different stocks
stocks = {
    'Google': 'GOOGL',
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Amazon': 'AMZN',
    'Tesla': 'TSLA'
}

# Streamlit app title and description
st.title("Stock Price App")
st.write("""
Select a stock from the dropdown menu to see its **closing price** and ***volume***!
""")

# Create a dropdown menu to select the stock
selected_stock = st.selectbox('***Select a stock Date Range*** : **2010-5-31** To **2021-5-31**', list(stocks.keys()))

# Get the selected ticker symbol
tickerSymbol = stocks[selected_stock]

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical price for this ticker
# Note: The specified date range is from May 31, 2010, to May 31, 2021
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2021-5-31')

# Display closing price and volume charts
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
