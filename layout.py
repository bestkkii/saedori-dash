from dash import html
import dash_mantine_components as dmc
from components.title import render_title
from components.keyword import render_random_word, render_today_word
from components.setting import render_setting_buttons
from components.interest_detail import render_interest_detail
from components.modal import render_modals
from dash import dcc

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
                html.Div(id="carousel-container"),
                className="big-container",
            ),

            dmc.Container(
                render_interest_detail(),
                className="detail-container",
            ),
            
            render_modals()
        ]
    )
