from dash import html
import dash_bootstrap_components as dbc

def render_setting_buttons():
    return dbc.Row(
        [
            dbc.Col(dbc.Button("다운로드", id="download-button", color="primary"), width="auto"),
            dbc.Col(dbc.Button("관심사 설정", id="interest-button", color="secondary"), width="auto"),
        ],
        className="mb-3",
        justify="end"
    )
