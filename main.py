import os
import time
import requests
from alpha_vantage.timeseries import TimeSeries
from dotenv import load_dotenv

load_dotenv()

ALPHA_KEY = os.getenv("ALPHA_VANTAGE_KEY")
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

ts = TimeSeries(key=ALPHA_KEY, output_format='json')

# List of stocks to track
stocks = ["AAPL", "TSLA", "GOOGL" "ASTS"]

while True:
    for symbol in stocks:
        try:
            data, _ = ts.get_quote_endpoint(symbol=symbol)
            price = data['05. price']
            payload = {"content": f"{symbol} stock price: ${price}"}
            response = requests.post(WEBHOOK_URL, json=payload)
            response.raise_for_status()
            print(f"{symbol} update sent!")
        except Exception as e:
            print(f"Failed to fetch/send {symbol}: {e}")
    # Wait 5 minutes before sending next update
    time.sleep(60 * 5)
