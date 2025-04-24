import dash_mantine_components as dmc
from dash import html, dcc, callback, Input, Output
from .coin import coin_summary_view

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