import dash_mantine_components as dmc

def create_news_summary_row(company_summary, title_summary):
    style_company = {
        "overflow": "hidden",
        "textOverflow": "clip",
        "whiteSpace": "nowrap",
        "color": "#808080",
        "paddingLeft": "11px",
    }
    style_title = {
        "overflow": "hidden",
        "textOverflow": "ellipsis",
        "display": "-webkit-box",
        "-webkit-line-clamp": "1",
        "-webkit-box-orient": "vertical",
    }
    style2 = {
        "display": "flex",
        "alignItems": "center",
    }
    return dmc.Grid([
            dmc.GridCol(dmc.Text(company_summary, fw=500, size="sm", ta="left", style=style_company), span=2, style=style2),
            dmc.GridCol(dmc.Text(title_summary, fw=500, size="md", ta="left", style=style_title), span=10, style=style2),
            dmc.GridCol(dmc.Divider(), span=12),
        ], style={"width": "100%"})

def create_news_summary(news_companies_summary, news_titles_summary):
    return dmc.Stack([
                    create_news_summary_row(item[0], item[1])
                    for item in zip(news_companies_summary, news_titles_summary)
                ], style={"width": "100%", "maxWidth": "100%"})