import dash_mantine_components as dmc

def render_title():
    return dmc.Center(
        style={"height": 100, "width": "100%"},
        children= [
            dmc.Image(src="/assets/images/SaeDoRi.png", h=50, fit="contain"),
            dmc.Text(
                "세상 돌아가는 이야기로 새로운 아이디어를 얻어봐!",
                # ta="center",
                # style={"flex": 1, "textAlign": "center", "fontSize": "1.25rem", "fontWeight": "bold"}
            ),
        ],
    )
