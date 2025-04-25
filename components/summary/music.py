import dash_mantine_components as dmc

def create_chart(title, chart_data):
    return dmc.GridCol([
        dmc.Text(title),
        dmc.Stack([
            create_chart_row(item["rank"], item["title"], item["artist"])
            for item in chart_data
        ]),
    ], span=6)

def create_chart_row(rank, title, artist):
    return dmc.Grid([
        dmc.GridCol(dmc.Text(str(rank)), span="content"),
        dmc.GridCol(
            dmc.Stack([
                dmc.Text(title),
                dmc.Text(artist),
            ]), span="content",
        ),
    ])