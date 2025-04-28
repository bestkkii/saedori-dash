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
        dmc.Space(w=20),
        dmc.GridCol(dmc.Text(str(rank), fw="700", className="rank-text"), span="content"),
        dmc.Space(w=20),
        dmc.GridCol(
            dmc.Stack([
                dmc.Text(dmc.Anchor(title, href=url, style={"textDecoration": "none", "color": "inherit"}, target="_blank"), size="sm", className="font", style={"white-space": "nowrap", "overflow": "hidden", "text-overflow": "ellipsis"}),
                dmc.Text(artist, c="dimmed", size="sm", className="font", style={"white-space": "nowrap", "overflow": "hidden", "text-overflow": "ellipsis"}),
            ], gap=0), span="content"
        ),
    ], align="center", gutter="xs")