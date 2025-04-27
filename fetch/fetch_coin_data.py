import requests

def fetch_coin_data(market):
    url = "https://api.upbit.com/v1/candles/days"
    params = {
        "market": market,
        "count": 180
    }
    response = requests.get(url, params=params)
    return response.json()