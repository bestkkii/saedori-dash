from dash import callback, Input, Output, State
from dash import dcc
import json
from components.interest_detail import render_music_detail
from dash.dependencies import ALL
from dash import ctx
import dash_mantine_components as dmc

# Summary 클릭 시 Detail 열기
@callback(
    Output("detail-content", "children"), Output("collapse-detail", "opened"),
    Input({"type": "carousel-slide", "name": ALL}, "n_clicks"),
    prevent_initial_call=True
)
def show_detail(n_clicks):
    triggered = ctx.triggered_id

    if not triggered:
        return "", False

    name = triggered["name"]

    if name == "music":
        return render_music_detail(), True
    elif name == "coin":
        return dmc.Text("코인 상세 설명입니다."), True
    elif name == "news":
        return dmc.Text("뉴스 상세 설명입니다."), True
    elif name == "realtime":
        return dmc.Text("실시간 검색어 상세 설명입니다."), True

    return "", False