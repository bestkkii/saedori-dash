from dash import Dash
from layout import layout
import callbacks
import requests

app = Dash(__name__)

app.layout = layout

if __name__ == "__main__":
    app.run_server(debug=True)