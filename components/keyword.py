import dash_mantine_components as dmc

def render_today_word():
    return dmc.Grid(
        children=[
            dmc.Paper(
                dmc.GridCol("오늘의 단어 1", ta="center", fw=600),
                className="keyword-box"
            ),
            dmc.Paper(
                dmc.GridCol("오늘의 단어 2", ta="center", fw=600),
                className="keyword-box"
            ),
            dmc.Paper(
                dmc.GridCol("오늘의 단어 3", ta="center", fw=600),
                className="keyword-box"
            ),
        ],
        gutter="md",
        justify="center"
    )

def render_random_word():
    return dmc.Grid(
        children=[
            dmc.Text("오늘은", fw=700, ta="center"),
            dmc.Paper(
                dmc.GridCol("랜덤 단어 1", ta="center"),
                className="random-box"
            ),
            dmc.Text("그리고", ta="center", fw=700),
            dmc.Paper(
                dmc.GridCol("랜덤 단어 2", ta="center"),
                className="random-box"
            ),
            dmc.Text("조합을 추천해!", ta="center", fw=700)
        ],
        gutter="md",
        justify="center"
    )
