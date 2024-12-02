# fetch_data.py
import requests
import pandas as pd

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",  # Sort by market cap
        "per_page": 50,  # Get top 50 cryptocurrencies
        "page": 1,
        "sparkline": False,
    }
    response = requests.get(url, params=params)
    data = response.json()

    # Create DataFrame from the fetched data
    df = pd.DataFrame(data)
    df = df[["name", "symbol", "current_price", "market_cap", "total_volume", "price_change_percentage_24h"]]
    df.columns = ["Name", "Symbol", "Current Price (USD)", "Market Cap", "24h Trading Volume", "24h % Change"]
    
    return df

import requests

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 50,
        "page": 1,
        "sparkline": False
    }
    response = requests.get(url, params=params)
    data = response.json()  # Parse the API response
    
    # Debug the response
    print(data)
    print(type(data))
    
    return data

