import dash_mantine_components as dmc
from dash import html, dcc, callback, Input, Output
import requests
    
def render_music():
    return dmc.Container(
        dmc.Stack(
            children= [
                dmc.Text("뮤직 차트"),
                dmc.Text("가격은 30초 주기로 갱신됩니다."),
            ]
        ),
        className="summary-grid"
    )

def coin_summary_view():
    return html.Div([
        html.Div([
            html.P('비트코인 BTC', className='coin-left-text'),
            html.P(f'비트코인 가격', className='coin-right-text', id='price-bitcoin')
        ], className='coin-position'),
        html.Hr(className="coin-divide-line"),
        html.Div([
            html.P('이더리움 ETH', className='coin-left-text'),
            html.P('이더리움 가격', className='coin-right-text', id='price-ethereum')
        ], className='coin-position'),
        html.Hr(className="coin-divide-line"),
        html.Div([
            html.P('리플 XRP', className='coin-left-text'),
            html.P('리플 가격', className='coin-right-text', id='price-xrp')
        ], className='coin-position'),
        
        dcc.Interval(
            id='interval-component-bit',
            interval=3*1000,  # 5초
            n_intervals=0
        ),
        dcc.Interval(
            id='interval-component-eth',
            interval=3*1000,  # 5초
            n_intervals=0
        ),
        dcc.Interval(
            id='interval-component-xrp',
            interval=3*1000,  # 5초
            n_intervals=0
        ),
    ], className="coin-summary-view")

@callback(
    Output('price-bitcoin', 'children'), 
    Output('price-ethereum', 'children'), 
    Output('price-xrp', 'children'),
    Input('interval-component-bit', 'n_intervals'), 
    Input('interval-component-eth', 'n_intervals'), 
    Input('interval-component-xrp', 'n_intervals')
)
def update_price(a, b, c):
    krw_usd_flag = 0
    url = "https://api.upbit.com/v1/ticker"
    if krw_usd_flag % 2 == 1:
        querystring = {"markets": "USDT-BTC,USDT-ETH,USDT-XRP"}
    else:
        querystring = {"markets": "KRW-BTC,KRW-ETH,KRW-XRP"}

    # API 호출
    response = requests.get(url, params=querystring)
    data = response.json()

    # 시세 정보 추출
    bit_price = data[0]['trade_price']
    eth_price = data[1]['trade_price']
    xrp_price = data[2]['trade_price']
    krw_usd_flag += 1
    return f'{bit_price:,} USDT', f'{eth_price:,} USDT', f'{xrp_price:,} USDT'
    



def render_coin():
    return dmc.Container(
        dmc.GridCol(coin_summary_view(), ta="center"),
        className="summary-grid"
    )

def render_news():
    return dmc.Container(
        dmc.GridCol("News summary", ta="center"),
        className="summary-grid",
    )

def render_realtime_search():
    return dmc.Container(
        dmc.GridCol("Realtime Search Words summary", ta="center"),
    )

def render_interest_summary():
    return dmc.Grid(
        children=[
            dmc.GridCol(render_music(), span=4),
            dmc.GridCol(render_coin(), span=4,),
            dmc.GridCol(render_news(), span=4,),
        ],
    )