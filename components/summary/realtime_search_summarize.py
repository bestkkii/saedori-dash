import dash_mantine_components as dmc


def create_realtime_search_summary(realtime_search_keyword):
    return dmc.GridCol([
            dmc.Grid([
                dmc.GridCol(dmc.Stack([
                    create_realtime_search_chart_row(item["index"], item["value"])
                    for item in realtime_search_keyword]), 
                ),
            ])
    ])

def create_realtime_search_chart_row(rank, realtime_search_keyword):
    return dmc.Box([
        dmc.Grid([
            dmc.GridCol(
                dmc.Flex([
                        dmc.Avatar(str(rank), fw=500, color="green", radius="sm", size="sm", className="font"),
                        dmc.Space(w=3),
                        dmc.Text(realtime_search_keyword, fw=500, size="md", style={"align-self": "center"}, className="font")
                    ], justify="flex-start", gap="xl")
            ,  offset=1),
            dmc.GridCol(dmc.Divider()),
        ])
    ])