import requests
import os

POLYGON_API_BASE_URL = "https://api.polygon.io/v2/aggs/ticker"

def fetch_stock_data(ticker, date_range):
    url = f"{POLYGON_API_BASE_URL}/{ticker}/range/1/day/{date_range['from']}/{date_range['to']}?apiKey={os.getenv('POLYGON_API_KEY')}"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    return response.json().get('results', [])