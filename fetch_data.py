import yfinance as yf
import pandas as pd

# Ask the user to enter a stock ticker symbol
ticker_symbol = input("Enter the stock symbol (e.g., AAPL, TSLA, MSFT): ")

# Download historical stock data (past 1 year)
data = yf.download(ticker_symbol, period="1y")

# Reset index to make 'Date' a column
data.reset_index(inplace=True)

# Select only the necessary columns (this prevents ticker headers)
data = data[["Date", "Open", "High", "Low", "Close", "Volume"]]

# Save clean CSV with index=False to avoid extra headers
filename = f"{ticker_symbol}_data.csv"
data.to_csv(filename, index=False)

print("✅ Clean data saved to", filename)
