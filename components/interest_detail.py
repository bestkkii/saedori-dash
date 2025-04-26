import dash_mantine_components as dmc
from dash import html
from fetch.fetch_music_data import parse_music_data
from fetch.fetch_realtime_search_keyword_data import parse_realtime_search_keyword_data
from fetch.fetch_news_data import get_news_detail
from .detail.music_detail import create_chart
from .detail.realtime_search_detail import create_realtime_search_chart
from .detail.news_detail import create_news_detail

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


def render_realtime_search_detail():
    realtime_search_keywords = parse_realtime_search_keyword_data()
    return dmc.Container([
        dmc.Stack([
            dmc.Grid([
                dmc.GridCol([
                    dmc.Text("실시간 검색어 차트", fw=600, fz="h5"),
                ], span=6),
                dmc.GridCol([
                    dmc.Flex([
                        dmc.Badge(color="green", radius="sm", size="md", variant="light"),
                        dmc.Text("대한민국", size="xs", c="dimmed"),
                        dmc.Badge(color="red", radius="sm", size="md", variant="light"),
                        dmc.Text("미국", size="xs", c="dimmed"),
                    ], justify="flex-end", gap="md")                    
                ], span=3, offset=3)
            ]),
            dmc.Text("30초 주기로 갱신됩니다.", c="dimmed", size="sm"),
            dmc.Space(h=5),
            dmc.Grid([
                create_realtime_search_chart(index, value)
                for index, value in realtime_search_keywords.items()
            ],),
        ])
    ], className="detail-grid")

def render_news_detail():
    companies, titles, leads, urls = get_news_detail()
    return dmc.Container([
        dmc.Stack([
            dmc.Grid([
                dmc.GridCol([
                    dmc.Text("머리기사 목록", fw=600, fz="h5"),
                ], span=12),
            ]),
            dmc.Text("언론사의 머리기사를 모아서 보여드립니다.", c="dimmed", size="sm"),
            dmc.Space(h=5),
            dmc.Grid([create_news_detail(companies, titles, leads, urls)],
                     ),
        ])
    ], className="detail-grid")