from dash import dcc
import plotly.graph_objs as go

def create_coin_chart(data, coin_name):
    dates = [entry['candle_date_time_kst'] for entry in data]
    prices = [entry['trade_price'] for entry in data]

    fig = go.Figure(data=[go.Scatter(x=dates, y=prices, mode='lines', name=f'{coin_name} Price')])
    fig.update_layout(title=f'{coin_name}',
                      xaxis_title='날짜',
                      yaxis_title='가격 (KRW)',
                      plot_bgcolor='white',
                      xaxis=dict(showgrid=True, gridcolor='lightgrey'),
                      yaxis=dict(showgrid=True, gridcolor='lightgrey'),
                      title_font=dict(size=16, color='darkblue'),
                      margin=dict(l=40, r=40, t=40, b=40),
                      height=350)

    return dcc.Graph(figure=fig)