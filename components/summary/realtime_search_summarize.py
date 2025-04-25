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
            dmc.GridCol(dmc.Text(str(rank), fw=600), span=4),
            dmc.GridCol(dmc.Text(realtime_search_keyword, fw=600), span=3),
            dmc.GridCol(dmc.Divider()),
                
        ])
    ])