import dash_mantine_components as dmc

def create_chart(title, chart_data):
    return dmc.GridCol([
        dmc.Text(title, fw=700, ta="center"),
        dmc.Space(h=10),
        dmc.Stack([
            create_chart_row(item["rank"], item["title"], item["artist"])
            for item in chart_data[:5]
        ], className="chart-row"),
    ], span=6)

def create_chart_row(rank, title, artist):
    return dmc.Grid([
        dmc.GridCol(dmc.Text(str(rank), fw="700", size="xl"), span="content"),
        dmc.Space(w=40),
        dmc.GridCol(
            dmc.Stack([
                dmc.Text(title),
                dmc.Text(artist, c="dimmed", size="sm"),
            ],), span="content",
        ),
    ], align="center", gutter="xs")