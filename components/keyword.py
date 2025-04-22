from dash import html
import dash_bootstrap_components as dbc

def render_keyword_section():
    return html.Div([
        dbc.Row(
            [
                dbc.Col(html.Div("오늘의 단어 1", className="keyword-box text-center"), width=4),
                dbc.Col(html.Div("오늘의 단어 2", className="keyword-box text-center"), width=4),
                dbc.Col(html.Div("오늘의 단어 3", className="keyword-box text-center"), width=4),
            ],
            className="mt-4 mb-4 keyword-background"
        ),
        dbc.Row(
            [
                dbc.Col(html.Div("오늘은", className="text-end fw-bold"), width=2),
                dbc.Col(html.Div("랜덤 단어 1", className="random-box text-center"), width=3),
                dbc.Col(html.Div("그리고", className="text-center fw-bold"), width=2),
                dbc.Col(html.Div("랜덤 단어 2", className="random-box text-center"), width=3),
                dbc.Col(html.Div("조합을 추천해!", className="text-center fw-bold"), width=2),
            ],
            className="mt-4 mb-4 keyword-background",
            align="center"
        ),
    ])
