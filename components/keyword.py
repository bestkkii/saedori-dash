import dash_mantine_components as dmc
from dash import html
from fetch.fetch_keywords import parse_keywords
import random

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
    # 모든 키워드 가져오기
    all_keywords = parse_keywords()
    
    # 랜덤으로 2개의 키워드 선택
    random_keywords = random.sample(all_keywords, min(2, len(all_keywords))) if all_keywords else ["키워드 없음", "키워드 없음"]

    return dmc.Grid(
        className="keyword-grid",
        children=[
            dmc.GridCol(
                dmc.Text("오늘은", fw=700), 
                span="auto",
                className="random-word-text"
            ),
            dmc.GridCol(
                dmc.Text(random_keywords[0], ta="center"),
                className="random-box",
                span="auto"
            ),
            dmc.GridCol(
                dmc.Text("그리고", fw=700), 
                span="auto",
                className="random-word-text"
            ),
            dmc.GridCol(
                dmc.Text(random_keywords[1], ta="center"),
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
