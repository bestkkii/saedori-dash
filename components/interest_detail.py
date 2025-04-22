from dash import html
import dash_bootstrap_components as dbc

def render_interest_detail(title="관심사", description="관심사 세부 내용"):
    return dbc.Card(
        dbc.CardBody([
            html.H5(title, className="card-title"),
            html.P(description, className="card-text"),
        ]),
        className="interest-card"
    )
