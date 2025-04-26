import dash_mantine_components as dmc
from fetch.fetch_realtime_search_keyword_data import parse_realtime_search_keyword_data
from dash import html

def create_realtime_search_chart(country, realtime_search_keyword):
        left_item = realtime_search_keyword[:5]
        right_item = realtime_search_keyword[5:]
        return dmc.GridCol([
            dmc.Grid([
                dmc.GridCol(dmc.Stack([
                    create_realtime_search_chart_row(country, item["index"], item["value"])
                    for item in left_item]), span=6
                ),
                dmc.GridCol(dmc.Stack([
                    create_realtime_search_chart_row(country, item["index"], item["value"])
                    for item in right_item]), span=6
                ),
            ]),
        ], span=6)

def create_realtime_search_chart_row(country, rank, realtime_search_keyword):
    rank_color = "red"
    if country == "us":
        rank_color = "blue"
    return dmc.Grid([
            dmc.GridCol(dmc.Avatar(str(rank), radius="sm", fw=500, color=rank_color), span=4,),
            dmc.GridCol(dmc.Text(realtime_search_keyword, fw=500, fz="h5", ta="center"), span="content", offset=1, style={"align-self": "center"}),
            dmc.GridCol(dmc.Divider()),
        ])