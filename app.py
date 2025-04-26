import dash
import dash_mantine_components as dmc
from layout import create_layout
import callbacks
import requests
import os
from config import DevConfig, ProdConfig

ENV = os.getenv("ENV", "dev")
Config = DevConfig if ENV == "dev" else ProdConfig

app = dash.Dash(
    __name__,
    external_stylesheets=dmc.styles.ALL, 
    requests_pathname_prefix=Config.REQUESTS_PATHNAME_PREFIX,
    suppress_callback_exceptions=True
)

app.title = "새도리"
app.layout = dmc.MantineProvider(
    theme={
        "colorScheme": "light",
        "white": "#FAFBFF",         # 배경색
    },
    children=create_layout(),
)

# Gunicorn을 위한 server 변수 추가
server = app.server

if __name__ == "__main__":
    app.run(debug=True)
