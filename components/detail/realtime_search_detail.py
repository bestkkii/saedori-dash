import dash_mantine_components as dmc
from fetch.fetch_realtime_search_keyword_data import parse_realtime_search_keyword_data
from dash import html

def create_realtime_search_chart(country, realtime_search_keyword):
        left_item = realtime_search_keyword[:5]
        right_item = realtime_search_keyword[5:]
        return dmc.GridCol([
            dmc.Grid([
                dmc.GridCol(dmc.Stack([
                    create_realtime_search_chart_row(item["index"], item["value"])
                    for item in left_item]), span=5
                ),
                dmc.GridCol(dmc.Stack([
                    create_realtime_search_chart_row(item["index"], item["value"])
                    for item in right_item]), span=5
                )
            ])
        ], span=6)

def create_realtime_search_chart_row(rank, realtime_search_keyword):
    return dmc.Box([
        dmc.Grid([
            dmc.GridCol(dmc.Text(str(rank), fw=600), span=4),
            dmc.GridCol(dmc.Text(realtime_search_keyword, fw=600), span="content"),
            dmc.GridCol(dmc.Divider()),
                
        ])
    ])