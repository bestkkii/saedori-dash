from dash import callback, Input, Output, State
import plotly.express as px
import pandas as pd

@callback(Output("interest-modal", "opened"), Input("interest-button", "n_clicks"), State("interest-modal", "opened"), prevent_initial_call=True)
def modal_callback(n_clicks, is_open):
    if n_clicks:
        return not is_open
    return is_open