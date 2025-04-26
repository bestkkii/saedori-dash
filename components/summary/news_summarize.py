import dash_mantine_components as dmc

def create_news_summary_row(company_summary, title_summary):
    style_c = {
        "align-self": "center",
        "margin-left": "15px",
        "color" : "#808080",
        "whiteSpace": "nowrap",  # 글자가 길어지면 숨기기
        "maxWidth": "6ch",  # company 폭 고정
        "minWidth": "6ch",  # 폭 줄어들지 않게
        }
    style_t = {
        "align-self": "center",
        "whiteSpace": "nowrap",  # 글자가 길어지면 숨기기
        "text-overflow": "ellipsis",
        }
    return dmc.Box([
        dmc.Grid([
            dmc.GridCol(
                dmc.Flex([
                        dmc.Text(company_summary, fw=500, size="sm", style=style_c),
                        dmc.Text(title_summary, fw=500, size="md", style=style_t),
                    ], justify="flex-start", gap="xl")
            ),
            dmc.GridCol(dmc.Divider()),
        ])
    ])

def create_news_summary(news_companies_summary, news_titles_summary):
    return dmc.GridCol([
            dmc.Grid([
                dmc.GridCol(dmc.Stack([
                    create_news_summary_row(item[0], item[1])
                    for item in zip(news_companies_summary, news_titles_summary)]), 
                ),
            ])
    ])
