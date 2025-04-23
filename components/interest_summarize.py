import dash_mantine_components as dmc
from dash import html

def render_music():
    return dmc.Paper(
        dmc.GridCol("Music summary", ta="center"),
        className="summary-grid"
    )

def render_coin():
    return dmc.Paper(
        dmc.GridCol("Coin summary", ta="center"),
        className="summary-grid"
    )

def render_news():
    return dmc.Paper(
        dmc.GridCol("News summary", ta="center"),
        className="summary-grid"
    )

def render_realtime_search():
    return dmc.Paper(
        dmc.GridCol("Realtime Search Words summary", ta="center"),
        className="summary-grid"
    )

def render_interest_summary():
    return dmc.Grid(
        children=[
            dmc.GridCol(render_music(), span=4),
            dmc.GridCol(render_coin(), span=4),
            dmc.GridCol(render_news(), span=4),
        ]
    )