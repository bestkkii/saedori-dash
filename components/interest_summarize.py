from dash import html
import dash_bootstrap_components as dbc

def render_interest_summary(title="관심사", description="관심사 요약 내용"):
    return dbc.Card(
        dbc.CardBody([
            html.H5(title, className="card-title"),
            html.P(description, className="card-text"),
        ]),
        className="interest-card"
    )