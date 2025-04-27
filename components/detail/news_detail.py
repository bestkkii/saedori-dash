import dash_mantine_components as dmc

def create_news_detail_row(company, title, lead, url):
    lead = '리드가 없습니다.' if lead =="" else lead
    style_company = {
        "whiteSpace": "nowrap",
        "overflow": "hidden",
        "textOverflow": "clip",
        "color": "#808080",
    }
    style_title = {
        "whiteSpace": "nowrap",
        "overflow": "hidden",
        "textOverflow": "ellipsis",
    }
    style_lead = {
        "whiteSpace": "nowrap",
        "overflow": "hidden",
        "textOverflow": "clip",
    }
    style2 = {
        "display": "flex",
        "alignItems": "center",
    }

    return dmc.Grid([
            dmc.GridCol(dmc.Text(company, fw=500, fz="h6", ta="left", style=style_company, className="font"), span=1, style=style2),
            dmc.GridCol(dmc.Text(title, fw=500, fz="h4", ta="left", style=style_title, className="font"), span=6, style=style2),
            dmc.GridCol(dmc.Text(lead, fw=500, fz="h5", ta="left", style=style_lead, className="font"), span=5, style=style2),
            dmc.GridCol(dmc.Divider(), span=12),
        ])


def create_news_detail(companies, titles, leads, urls):
        return dmc.Stack([
                    create_news_detail_row(company, title, lead, url)
                    for company, title, lead, url in zip(companies, titles, leads, urls)])
