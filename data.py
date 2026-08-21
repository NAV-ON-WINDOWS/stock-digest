import os
import requests
from dotenv import load_dotenv
import time
import sys

load_dotenv()

MOCK_MODE = True

MOCK_PRICES = {
    "AAPL": "309.64999",
    "BA": "216.73000",
    "NKE": "41.86000",
    "SBUX": "105.31000",
    "HD": "332.76001",
    "DIS": "96.33000",
    "BRK.B": "512.21002",
    "GE": "361.35999"
}

def fetch_animation():
    sys.stdout.write("Running script")
    sys.stdout.flush()

    for _ in range(3):
        time.sleep(0.5)
        sys.stdout.write(".")
        sys.stdout.flush()

    print()

def if_fetch_error(api_code):
    if api_code == 200:
        pass
    elif api_code == 429:
        raise Exception("Too many API requests made. Try again after 1 minute.")
    elif api_code != 200:
        raise Exception(f"API request failed with status code {api_code}.")

def fetch_with_headers():
    """
    fetching live stock prices for the stock id's mentioned
    using the twelvedata api
    """

    api_key = os.getenv("api_key")
    url = "https://api.twelvedata.com/time_series"
    params = {
        "symbol": "AAPL,BA,NKE,SBUX,HD,DIS,BRK.B,GE",
        "interval": "1min"
    }
    headers = {
        "Authorization": f"apikey {api_key}"
    }

    response = requests.get(url, params=params, headers=headers)

    api_code = response.status_code
    if_fetch_error(api_code)

    result = response.json()
    return result


def get_prices_open():
    if MOCK_MODE:
        return MOCK_PRICES
        
    prices_data = fetch_with_headers()

    prices_open = {}
    try:
        for symbol in prices_data:
            prices_open[symbol] = prices_data[symbol]["values"][0]["open"]
    except (KeyError, TypeError) as e:
        print(f"Missing expected data for a symbol: {e}")

    return prices_open


if __name__ == "__main__":
    fetch_animation()
    print(get_prices_open())