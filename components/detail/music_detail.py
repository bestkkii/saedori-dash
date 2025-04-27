import dash_mantine_components as dmc
from dash import dcc

def create_chart(title, chart_data):
    return dmc.GridCol([
        dmc.Text(title, fw=700, ta="center", className="font"),
        dmc.Space(h=20),
        dmc.Grid([
            dmc.GridCol(dmc.Stack([
                create_chart_row(item["rank"], item["title"], item["artist"], item["url"])
                for item in chart_data[:5]], className="chart-detail-row", style={"margin-bottom": "30px"}), span=6
            ),
            dmc.GridCol(dmc.Stack([
                create_chart_row(item["rank"], item["title"], item["artist"], item["url"])
                for item in chart_data[5:]], className="chart-detail-row", style={"margin-bottom": "30px"}), span=6
            ),
        ]),
    ], span=6)


def create_chart_row(rank, title, artist, url):
    return dmc.Grid([
        dmc.GridCol(dmc.Text(str(rank), fw="700", size="xl", className="font"), span="content", style={"text-align": "center"}),
        dmc.GridCol(
            dmc.Stack([
                dmc.Text(dmc.Anchor(title, href=url, style={"textDecoration": "none", "color": "inherit"}, target="_blank"), fz="h5", ta="center", fw=700),
                dmc.Text(artist, c="dimmed", size="sm", ta="center"),
            ], gap=0, align="center"), span="auto", style={"text-align": "center"}
        ),
    ], align="center", justify="center", gutter="md")