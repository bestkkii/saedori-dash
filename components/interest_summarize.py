import dash_mantine_components as dmc
from dash import html
from fetch.fetch_music_data import parse_music_data

def render_music():
    # api 호출을 통해 가져온 데이터 저장
    musics = parse_music_data()

    def create_chart(title, chart_data):
        return dmc.GridCol([
            dmc.Text(title),
            dmc.Stack([
                create_chart_row(item["rank"], item["title"], item["artist"])
                for item in chart_data
            ]),
        ], span=6)

    def create_chart_row(rank, title, artist):
        return dmc.Grid([
            dmc.GridCol(dmc.Text(str(rank)), span="content"),
            dmc.GridCol(
                dmc.Stack([
                    dmc.Text(title),
                    dmc.Text(artist),
                ]), span="content",
            ),
        ])

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
        dmc.GridCol("Coin summary", ta="center"),
        className="summary-grid"
    )

def render_news():
    return dmc.Container(
        dmc.GridCol("News summary", ta="center"),
        className="summary-grid",
    )

def render_realtime_search():
    return dmc.Container(
        dmc.GridCol("Realtime Search Words summary", ta="center"),
    )

def render_interest_summary():
    return dmc.Grid(
        children=[
            dmc.GridCol(render_music(), span=4),
            dmc.GridCol(render_coin(), span=4,),
            dmc.GridCol(render_news(), span=4,),
        ],
    )