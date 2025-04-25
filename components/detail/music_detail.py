import dash_mantine_components as dmc
from dash import dcc
def create_chart(title, chart_data):
    return dmc.GridCol([
        dmc.Text(title, fw=700, ta="center"),
        dmc.Space(h=10),
        dmc.Stack([
            create_chart_row(item["rank"], item["title"], item["artist"], item["url"])
            for item in chart_data
        ], className="chart-detail-row"),
    ], span=6)

def create_chart_row(rank, title, artist, url):
    return dmc.Grid([
        dmc.GridCol(dmc.Text(str(rank), fw="700", size="xl"), span="content"),
        dmc.Space(w=180),
        dmc.GridCol(
            dmc.Stack([
                dmc.Text(
                    dcc.Link(title, href=url, style={"textDecoration": "none", "color": "inherit"})
                ),
                dmc.Text(artist, c="dimmed", size="sm"),
            ],), span="content",
        ),
    ], align="center", gutter="xs")