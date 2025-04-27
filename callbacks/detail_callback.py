from dash import callback, Input, Output, State, no_update
from dash.dependencies import ALL
from dash import ctx
from components.interest_detail import render_music_detail, render_realtime_search_detail, render_news_detail, render_coin_detail

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
        return render_coin_detail(), True
    elif name == "news":
        return render_news_detail(), True
    elif name == "realtime":
        return render_realtime_search_detail(), True
    return "", False