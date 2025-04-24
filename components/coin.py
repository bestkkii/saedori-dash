from dash import html, dcc

def coin_summary_view():
    coins = [
        ('비트코인 BTC', 'price-bitcoin'),
        ('이더리움 ETH', 'price-ethereum'),
        ('리플 XRP', 'price-xrp')
    ]

    intervals = 5*1000  # 5초
    coin_divs = []
    for name, price_id in coins:
        coin_divs.append(html.Div([
            html.P(name, className='coin-left-text'),
            html.P(f'{name.split()[0]} 가격', className='coin-right-text', id=price_id)
        ], className='coin-position'))
        coin_divs.append(html.Hr(className="coin-divide-line"))

    intervals = [
        dcc.Interval(id='interval-component-bit', interval=intervals, n_intervals=0),
        dcc.Interval(id='interval-component-eth', interval=intervals, n_intervals=0),
        dcc.Interval(id='interval-component-xrp', interval=intervals, n_intervals=0)
    ]

    return html.Div(coin_divs + intervals, className="coin-summary-view")