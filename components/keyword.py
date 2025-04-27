import dash_mantine_components as dmc
from dash import html
from fetch.fetch_keywords_data import parse_keywords
import random

def render_today_word():
    return dmc.Grid(
        className="keyword-grid",
        id="today-word-grid",
        children=[
            dmc.GridCol(
                dmc.Group([
                    dmc.Text("1", fw=600, size="sm", c="dimmed"),
                    dmc.Text("오늘의 단어 1", fw=600, id="today-word-1", className="font")
                ], gap="xs", align="center", justify="center"),
                className="keyword-box",
                span="auto"
            ),
            dmc.GridCol(
                dmc.Group([
                    dmc.Text("2", fw=600, size="sm", c="dimmed"),
                    dmc.Text("오늘의 단어 2", fw=600, id="today-word-2", className="font")
                ], gap="xs", align="center", justify="center"),
                className="keyword-box",
                span="auto"
            ),
            dmc.GridCol(
                dmc.Group([
                    dmc.Text("3", fw=600, size="sm", c="dimmed"),
                    dmc.Text("오늘의 단어 3", fw=600, id="today-word-3", className="font")
                ], gap="xs", align="center", justify="center"),
                className="keyword-box",
                span="auto"
            ),
        ]
    )


def render_random_word():
    # 모든 카테고리의 키워드를 하나의 리스트로 합치기
    keywords = parse_keywords()
    all_keywords = []
    for category_keywords in keywords.values():
        all_keywords.extend(category_keywords)
    
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
                dmc.Text(random_keywords[0], ta="center", className="random-word-text"),
                className="random-box",
                span="auto"
            ),
            dmc.GridCol(
                dmc.Text("그리고", fw=700), 
                span="auto",
                className="random-word-text"
            ),
            dmc.GridCol(
                dmc.Text(random_keywords[1], ta="center", className="random-word-text"),
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
