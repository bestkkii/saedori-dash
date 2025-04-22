from dash import html
import dash_bootstrap_components as dbc
from components.title import render_title
from components.keyword import render_keyword_section
from components.setting import render_setting_buttons
from components.interest_summarize import render_interest_summary
from components.interest_detail import render_interest_detail
from components.modal import render_modals

def create_layout(app):
    return dbc.Container(
        [
            render_title(),
            render_keyword_section(),
            render_setting_buttons(),
            render_interest_summary(),
            render_interest_detail(),
            render_modals(),
        ],
        fluid=True,
        style={"backgroundColor": "#f9f9fb", "padding": "20px"},
    )
