import dash_mantine_components as dmc
from dash import html
from config import Config

def render_title():
    return dmc.Flex(
        className="title-container",
        children=[
            dmc.Image(
                src=f"{Config.ASSETS_PATH}/images/SaeDoRi.png",
                h=50,
                fit="contain"
            ),
            dmc.Text(
                "세상 돌아가는 이야기로 새로운 아이디어를 얻어봐!",
                fw=700,
                className="title-text"
            ),
            html.Div(style={"width": "50px"})
        ]
    )