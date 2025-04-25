import dash_mantine_components as dmc
from dash import html, dcc, callback, Input, Output
from .summary.coin import coin_summary_view
from fetch.fetch_music_data import parse_music_data
from .summary.music import create_chart

def render_music():
    musics = parse_music_data()
    return dmc.Container([
        dmc.Stack([
            dmc.Text("뮤직 차트"),
            dmc.Text("30초 주기로 갱신됩니다."),
            dmc.Grid([
                create_chart(title, chart_data)
                for title, chart_data in musics.items()
            ]),
        ])
    ], className="summary-grid")
    
def render_coin():
    return dmc.Container(
        dmc.Stack(coin_summary_view(), ta="center"),
        className="summary-grid"
    )

def render_news():
    return dmc.Container(
        dmc.Stack("News summary", ta="center"),
        className="summary-grid",
    )

def render_realtime_search():
    return dmc.Container(
        dmc.Stack([
                    dmc.Text("실시간 검색어 랭킹", fw=600, fz="h5"),
                    dmc.Text("대한민국에서의 구글 실시간 검색어 순위입니다.", c="dimmed", size="sm"),
        ]),
        className="summary-grid"
    )

def render_interest_summary():
    return dmc.Carousel(
        children=[
            dmc.CarouselSlide(render_music()),
            dmc.CarouselSlide(render_coin()),
            dmc.CarouselSlide(render_news()),
            dmc.CarouselSlide(render_realtime_search()),
        ],
        id="carousel-responsive",
        withIndicators=True,
        slideSize={"base": "100%", "sm": "50%", "md": "33.333333%"},
        slideGap={"base": 0, "sm": "md"},
        loop=True,
        align="start"
    ),

