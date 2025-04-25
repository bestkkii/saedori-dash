import dash_mantine_components as dmc
from dash import html, dcc, callback, Input, Output
from .summary.coin import coin_summary_view
from fetch.fetch_music_data import parse_music_data
from .summary.music_summarize import create_chart
from .interest_detail import render_interest_detail

def render_music():
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
    ], className="summary-grid")
    
def render_coin():
    return dmc.Container(
        dmc.Stack([
            dmc.Text("코인 현재가", fw=600, fz="h5"),
            dmc.Text("5초 주기로 갱신됩니다.", c="dimmed", size="sm"),
            coin_summary_view()
            ]),
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

def render_interest_summary(selected_items):

    slides = []

    for item in selected_items:
        if item == "코인":
            slides.append(
                dmc.CarouselSlide(
                    html.Div(
                        dmc.Paper(render_coin()),
                        id={"type": "carousel-slide", "name": "coin"},
                        n_clicks=0,
                        style={"cursor": "pointer"}
                    )
                )
            )
        elif item == "노래":
            slides.append(
                dmc.CarouselSlide(
                    html.Div(
                        dmc.Paper(render_music()),
                        id={"type": "carousel-slide", "name": "music"},
                        n_clicks=0,
                        style={"cursor": "pointer"}
                    )
                )
            )
        elif item == "뉴스":
            slides.append(
                dmc.CarouselSlide(
                    html.Div(
                        dmc.Paper(render_news()),
                        id={"type": "carousel-slide", "name": "news"},
                        n_clicks=0,
                        style={"cursor": "pointer"}
                    )
                )
            )
        elif item == "실시간 검색어":
            slides.append(
                dmc.CarouselSlide(
                    html.Div(
                        dmc.Paper(render_realtime_search()),
                        id={"type": "carousel-slide", "name": "realtime"},
                        n_clicks=0,
                        style={"cursor": "pointer"}
                    )
                )
            )

    return html.Div([ 
        dmc.Carousel(
            children=slides,
            id="carousel-responsive",
            withIndicators=True,
            slideSize={"base": "100%", "sm": "50%", "md": "33.333333%"},
            slideGap={"base": 0, "sm": "md"},
            loop=True,
            align="start",
            controlsOffset="0px",
            controlSize=32,
            className="carousel-container",
        ),
    ])