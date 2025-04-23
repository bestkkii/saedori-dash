import dash
import dash_mantine_components as dmc
from layout import create_layout
import callbacks
import requests

app = dash.Dash(__name__,external_stylesheets=dmc.styles.ALL)

app.title = "새도리"
app.layout = dmc.MantineProvider(
    theme={
        "colorScheme": "light",
        "white": "#FAFBFF",         # 배경색
    },
    children=create_layout(),
)

server = app.server

if __name__ == "__main__":
    app.run(debug=True)
