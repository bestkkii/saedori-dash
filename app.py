import dash_bootstrap_components as dbc
import dash
import dash_bootstrap_components as dbc
from layout import create_layout
import callbacks
import requests

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "새도리 대시보드"
app.layout = create_layout(app)

if __name__ == "__main__":
    app.run(debug=True)