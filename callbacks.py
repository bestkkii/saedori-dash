from dash import Input, Output, callback
import plotly.express as px
import pandas as pd
import requests


# 코인 시세 콜백 함수
krw_usd_flag = 0

@callback(
    Output('price-bitcoin', 'children'), 
    Output('price-ethereum', 'children'), 
    Output('price-xrp', 'children'),
    Input('interval-component-bit', 'n_intervals'), 
    Input('interval-component-eth', 'n_intervals'), 
    Input('interval-component-xrp', 'n_intervals')
)
def update_price(a, b, c):
    global krw_usd_flag
    url = "https://api.upbit.com/v1/ticker"
    market_type = "USDT" if krw_usd_flag % 2 == 1 else "KRW"
    querystring = {"markets": f"{market_type}-BTC,{market_type}-ETH,{market_type}-XRP"}

    response = requests.get(url, params=querystring)
    data = response.json()

    # 시세 정보와 변동 정보 추출
    prices_changes = [(coin['trade_price'], update_change(coin['change'])) for coin in data]

    krw_usd_flag += 1

    return tuple(
        f'{price:,} {market_type} {change}' for price, change in prices_changes
    )

def update_change(change):
    change_symbols = {
        'RISE': '▲',
        'FALL': '▼'
    }
    return change_symbols.get(change, 'ᐉ')
        