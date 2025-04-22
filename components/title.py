from dash import html, dcc
import dash_bootstrap_components as dbc

def render_title():
    return dbc.Row(
        [
            # dbc.Col(html.Img(src="/assets/images/logo.png", height="50px"), width="auto"),
            dbc.Col(html.H4("세상 돌아가는 이야기로 새로운 아이디어를 얻어봐!", className="text-center"), width=True),
        ],
        className="my-3 align-items-center",
        justify="center",
    )