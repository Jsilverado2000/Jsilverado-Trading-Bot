import os
from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv('ALPHA_VANTAGE_API_KEY')

# Initialize the Alpha Vantage TimeSeries
ts = TimeSeries(key=api_key, output_format='pandas')

# Function to fetch stock data
def fetch_stock_data(symbol, interval="daily"):
    if interval == "daily":
        data, meta_data = ts.get_daily(symbol=symbol, outputsize='compact')  # Use "full" for more data
    elif interval == "intraday":
        data, meta_data = ts.get_intraday(symbol=symbol, interval='15min', outputsize='compact')
    else:
        raise ValueError("Unsupported interval. Choose 'daily' or 'intraday'.")
    return data, meta_data

# Fetch and analyze data
try:
    ticker = "AAPL"  # Replace with your preferred stock symbol
    print(f"Fetching data for {ticker}...")
    data, meta_data = fetch_stock_data(ticker, interval="daily")

    # Display the first few rows
    print(data.head())

    # Save to CSV
    data.to_csv(f"{ticker}_daily.csv")
    print(f"Data saved to {ticker}_daily.csv")

    # Plot the closing prices
    data['4. close'].plot(title=f"{ticker} Daily Closing Prices")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.show()

except Exception as e:
    print(f"Error: {e}")