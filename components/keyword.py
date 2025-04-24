import dash_mantine_components as dmc
from dash import html


def render_today_word():
    # words 리스트에 api 호출을 통해 얻어온 '오늘의 단어' 넣기
    words = ["오늘의 단어 1", "오늘의 단어 2", "오늘의 단어 3"]

    return dmc.Grid(
        className="keyword-grid",
        children=[
            dmc.GridCol(
                dmc.Text(words[0], ta="center", fw=600),
                className="keyword-box",
                span="auto"
            ),
            dmc.GridCol(
                dmc.Text(words[1], ta="center", fw=600),
                className="keyword-box",
                span="auto"
            ),
            dmc.GridCol(
                dmc.Text(words[2], ta="center", fw=600),
                className="keyword-box",
                span="auto"
            ),
        ]
    )


def render_random_word():
    # words 리스트에 api 호출을 통해 얻어온 '랜덤 단어' 넣기
    return dmc.Grid(
        className="keyword-grid",
        children=[
            dmc.GridCol(
                dmc.Text("오늘은", fw=700), 
                span="auto",
                className="random-word-text"
            ),
            dmc.GridCol(
                dmc.Text("랜덤 단어 1", ta="center"),
                className="random-box",
                span="auto"
            ),
            dmc.GridCol(
                dmc.Text("그리고", fw=700), 
                span="auto",
                className="random-word-text"
            ),
            dmc.GridCol(
                dmc.Text("랜덤 단어 2", ta="center"),
                className="random-box",
                span="auto"
            ),
            dmc.GridCol(
                dmc.Text("조합을 추천해!", fw=700), 
                span="auto",
                className="random-word-text"
            )
        ]
    )
