import dash_mantine_components as dmc
from dash import html
from fetch.fetch_music_data import parse_music_data
from .detail.music_detail import create_chart

def render_interest_detail():
    return dmc.Collapse(
        id="collapse-detail",
        children=html.Div(id="detail-content"),
        transitionDuration=300,
        transitionTimingFunction="ease",
    )

def render_music_detail():
    musics = parse_music_data()
    return dmc.Container([
        dmc.Stack([
            dmc.Text("뮤직 차트", fw=600, fz="h5"),
            dmc.Text("30초 주기로 갱신됩니다.", c="dimmed", size="sm"),
            dmc.Space(h=5),
            dmc.Grid([
                create_chart(title, chart_data)
                for title, chart_data in musics.items()
            ]),
        ])
    ], className="detail-grid")