import dash_mantine_components as dmc
from fetch.fetch_realtime_search_keyword_data import parse_realtime_search_keyword_data

def render_realtime_search_detail():
    def create_chart(country, keyword):
        return dmc.GridCol([
            dmc.Text(country),
            dmc.Stack([
                create_chart_row(item["index"], item["value"])
                for item in keyword
            ]),
        ], span=6)

    def create_chart_row(rank, keyword):
        return dmc.Grid([
            dmc.GridCol(dmc.Text(str(rank)), span="content"),
            dmc.GridCol(
                dmc.Stack([
                    dmc.Text(keyword),
                ]), span="content",
            ),
        ])
    
    realtime_search_keywords = parse_realtime_search_keyword_data()

    return dmc.Box([
        dmc.Divider(my=10),
            dmc.Text("실시간 검색어 세부 정보", fw=600, fz='h5'),
            dmc.Text("대한민국, 미국에서의 실시간 구글 인기 검색어 순위입니다.", c='dimmed', size='sm'),
            dmc.Box(id="realtime-search-detail-content", mt=10),
            dmc.Grid([
                create_chart(country, keyword)
                for country, keyword in realtime_search_keywords.items()
            ]),
    ])