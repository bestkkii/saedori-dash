import dash_mantine_components as dmc
from dash import html
from .summary.coin_summarize import coin_summary_view
from fetch.fetch_music_data import parse_music_data
from .summary.music_summarize import create_chart
from .interest_detail import render_interest_detail
from .summary.realtime_search_summarize import create_realtime_search_summary
from fetch.fetch_realtime_search_keyword_data import parse_realtime_search_keyword_data
from .summary.news_summarize import create_news_summary
from fetch.fetch_news_data import get_news_summary

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
        ], gap="xs")
    ], className="summary-grid")
    
def render_coin():
    return dmc.Container(
        dmc.Stack([
            dmc.Text("코인 현재가", fw=600, fz="h5"),
            dmc.Text("5초 주기로 갱신됩니다.", c="dimmed", size="sm"),
            coin_summary_view()
        ], gap="xs"),
        className="summary-grid"
    )

def render_news():
    news_companies_summary, news_titles_summary = get_news_summary()
    return dmc.Container(
        dmc.Stack([
            dmc.Text("머리기사", fw=600, fz="h5"),
            dmc.Text("언론사의 머리기사를 모아서 보여드립니다.", c="dimmed", size="sm"),
            dmc.Space(h=5),
            create_news_summary(news_companies_summary, news_titles_summary)
        ], gap="xs"),
        className="summary-grid",
    )

def render_realtime_search():
    realtime_search_keywords = parse_realtime_search_keyword_data()["kr"][:5]
    return dmc.Container(
        dmc.Stack([
            dmc.Text("실시간 검색어 랭킹", fw=600, fz="h5"),
            dmc.Text("대한민국에서의 구글 실시간 검색어 순위입니다.", c="dimmed", size="sm"),
            dmc.Space(h=5),
            dmc.Grid([
                create_realtime_search_summary(realtime_search_keywords)
            ])
        ], gap="xs"),
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