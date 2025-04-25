from dash import html
import dash_mantine_components as dmc
from components.title import render_title
from components.keyword import render_random_word
from components.keyword import render_today_word
from components.setting import render_setting_buttons
from components.interest_summarize import render_interest_summary
from components.interest_detail import render_interest_detail
from components.modal import render_modals

def create_layout():
    return html.Div(
        children=[
            dmc.Container(
                render_title(),
                className="small-container"
            ),

            dmc.Container(
                render_today_word(),
                className="small-container"
            ),

            dmc.Container(
                render_random_word(),
                className="small-container"
            ),

            dmc.Container(
                render_setting_buttons(),
                className="setting-container"
            ),

            dmc.Container(
                render_interest_summary(),
                className="big-container",
            ),

            dmc.Container(
                render_interest_detail(),
                className="detail-container",
            ),
            
            render_modals()
        ]
    )
