import dash_mantine_components as dmc
from dash import html

def render_interest_detail():
    return dmc.Collapse(
        id="collapse-detail",
        children=html.Div(id="detail-content"),
        transitionDuration=300,
        transitionTimingFunction="ease",
    )
