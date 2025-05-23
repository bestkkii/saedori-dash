import dash_mantine_components as dmc

def create_chart(title, chart_data):
    return dmc.GridCol([
        dmc.Text(title, fw=700, ta="center", className="font"),
        dmc.Space(h=10),
        dmc.Stack([
            create_chart_row(item["rank"], item["title"], item["artist"])
            for item in chart_data[:5]
        ], className="chart-row", style={"margin-bottom": "30px"})
    ], span=6)

def create_chart_row(rank, title, artist):
    return dmc.Grid([
        dmc.Space(w=20),
        dmc.GridCol(dmc.Text(str(rank), fw="700", className="rank-text"), span="content"),
        dmc.Space(w=20),
        dmc.GridCol(
            dmc.Stack([
                dmc.Text(title, size="sm", className="font", style={"white-space": "nowrap", "overflow": "hidden", "text-overflow": "ellipsis"}),
                dmc.Text(artist, c="dimmed", size="sm", className="font", style={"white-space": "nowrap", "overflow": "hidden", "text-overflow": "ellipsis"}),
            ], gap=0), span="content"
        ),
    ], align="center", gutter="xs")