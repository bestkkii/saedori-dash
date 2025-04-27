from dash import callback, Input, Output, State, no_update
import plotly.express as px
import pandas as pd
import requests
import dash_mantine_components as dmc
from dash.dependencies import ALL
from dash import ctx
from components.interest_detail import render_music_detail, render_realtime_search_detail, render_news_detail
from components.interest_summarize import render_interest_summary
from fetch.fetch_keywords import parse_keywords
from datetime import datetime
from fetch.fetch_downlonds import parse_downloads
from dash import dcc
import io

# MultiSelect 값 변경 시 바로 결과 표시
@callback(
    Output("interest-select-view", "children", allow_duplicate=True),
    Input("interest-multiselect", "value"),
    prevent_initial_call='initial_duplicate'
)
def update_interest_view(selected_values):
    if not selected_values:
        selected_values = []
    
    interest_text = dmc.Group(
        [dmc.Text(f"{i+1}. {item}  ", className="font", fw=500) for i, item in enumerate(selected_values)],
        gap="xs"
    )
    
    return interest_text

# 로컬 스토리지에 저장된 관심사 불러오기
@callback(
    Output("interest-multiselect", "value"),                # 모달창 multiselect 선택
    Output("interest-select-view", "children"),             # 모달창 text로 출력
    Output("carousel-container", "children"),               # Summary 칸에 노출
    Input({'type': 'storage', 'index': 'local'}, 'data'),   # 로컬 스토리지에 바뀐게 있을 경우
    prevent_initial_call=False
)
def load_interest_from_local_storage(saved_data):
    if saved_data is None:
        saved_data = ["코인", "노래", "실시간 검색어", "뉴스"]
    
    interest_text = dmc.Group(
        [dmc.Text(f"{i+1} {item}  ", className="font", fw=500) for i, item in enumerate(saved_data)],
        gap="xs"
    )
    
    return saved_data, interest_text, render_interest_summary(saved_data)

# 관심사 설정 버튼 클릭 시 모달 열기
@callback(
    Output("interest-modal", "opened", allow_duplicate=True), 
    Input("interest-button", "n_clicks"), 
    State("interest-modal", "opened"), 
    prevent_initial_call=True
)
def select_interest(n_clicks, is_open):
    if n_clicks:
        return not is_open
    return is_open

# 관심 분야 선택 후 확인 버튼 클릭 시 저장
@callback(
    Output({'type': 'storage', 'index': 'local'}, "data"),
    Output("interest-modal", "opened"),
    Input("interest-submit-button", "n_clicks"),
    State("interest-multiselect", "value"),
    prevent_initial_call=True
)
def save_interest(n_clicks, selected_values):
    if n_clicks:
        return selected_values or [], False
    return no_update, no_update


# 코인 시세 콜백 함수
krw_usd_flag = 0

@callback(
    Output('price-bitcoin', 'children'), 
    Output('price-ethereum', 'children'), 
    Output('price-xrp', 'children'),
    Input('interval-component-bit', 'n_intervals'), 
    Input('interval-component-eth', 'n_intervals'), 
    Input('interval-component-xrp', 'n_intervals')
)
def update_price(a, b, c):
    global krw_usd_flag
    url = "https://api.upbit.com/v1/ticker"
    market_type = "USDT" if krw_usd_flag % 2 == 1 else "KRW"
    querystring = {"markets": f"{market_type}-BTC,{market_type}-ETH,{market_type}-XRP"}

    response = requests.get(url, params=querystring)
    data = response.json()

    # 시세 정보와 변동 정보 추출
    prices_changes = [(coin['trade_price'], update_change(coin['change'])) for coin in data]

    krw_usd_flag += 1

    return tuple(
        f'{price:,} {market_type} {change}' for price, change in prices_changes
    )

def update_change(change):
    change_symbols = {
        'RISE': '▲',
        'FALL': '▼'
    }
    return change_symbols.get(change, 'ᐉ')
        

# Summary 클릭 시 Detail 열기
@callback(
    Output("detail-content", "children"), Output("collapse-detail", "opened"),
    Input({"type": "carousel-slide", "name": ALL}, "n_clicks"),
    prevent_initial_call=True
)
def show_detail(n_clicks):
    triggered = ctx.triggered_id

    if not triggered:
        return "", False

    name = triggered["name"]

    if name == "music":
        return render_music_detail(), True
    elif name == "coin":
        return dmc.Text("코인 상세 설명입니다."), True
    elif name == "news":
        return render_news_detail(), True
    elif name == "realtime":
        return render_realtime_search_detail(), True
    return "", False

# 다운로드 버튼 클릭 시 모달 열기
@callback(
    Output("download-modal", "opened"), 
    Input("download-button", "n_clicks"), 
    State("download-modal", "opened"), 
    prevent_initial_call=True
)
def select_donwload(n_clicks, is_open):
    if n_clicks:
        return not is_open
    return is_open

# 키워드 콜백 함수
@callback(
    [Output("today-word-1", "children"),
     Output("today-word-2", "children"),
     Output("today-word-3", "children")],
    Input({'type': 'storage', 'index': 'local'}, 'data'),
    prevent_initial_call=False
)
def get_today_words(interest_categories):
    if interest_categories is None:
        interest_categories = ["실시간 검색어", "뉴스", "코인", "노래"]

    today_words = []
    category_mapping = {
        "코인": "coin",
        "노래": "music",
        "실시간 검색어": "search_word",
        "뉴스": "news"
    }
    
    keywords = parse_keywords()
    
    if len(interest_categories) == 1:
        # 관심분야가 1개일 경우: 해당 카테고리의 키워드 3개 사용
        category = category_mapping.get(interest_categories[0])
        if category in keywords and keywords[category]:
            today_words = keywords[category][:3]
    elif len(interest_categories) == 2:
        # 관심분야가 2개일 경우: 첫 번째 카테고리의 키워드 2개, 두 번째 카테고리의 키워드 1개 사용
        category1 = category_mapping.get(interest_categories[0])
        category2 = category_mapping.get(interest_categories[1])
        
        if category1 in keywords and keywords[category1]:
            today_words.extend(keywords[category1][:2])
        if category2 in keywords and keywords[category2]:
            today_words.append(keywords[category2][0])
    else:
        # 그 외의 경우: 각 카테고리의 첫 번째 키워드 사용
        for interest in interest_categories:
            category = category_mapping.get(interest)
            if category in keywords and keywords[category]:
                today_words.append(keywords[category][0])

    # 키워드가 3개 미만일 경우 '실시간 검색어', '뉴스', '코인' 키워드 사용
    while len(today_words) < 3:
        today_words.append(keywords["search_word"][0])
        today_words.append(keywords["news"][0])
        today_words.append(keywords["coin"][0])

    return today_words[0], today_words[1], today_words[2]


# 키워드, 컨텐츠 다운로드
@callback(
    Output("download-dataframe-csv", "data"),
    Input("download-submit-button", "n_clicks"),
    State("date-picker", "start_date"),
    State("date-picker", "end_date"),
    State({'type': 'storage', 'index': 'local'}, 'data'),
    prevent_initial_call=True
)
def handle_download(n_clicks, start_date, end_date, storage_data):
    if n_clicks:
        # 날짜를 타임스탬프로 변환
        start_timestamp = int(datetime.strptime(start_date.split('T')[0], '%Y-%m-%d').timestamp())
        end_timestamp = int(datetime.strptime(end_date.split('T')[0], '%Y-%m-%d').timestamp())
        
        # 로컬 스토리지에서 선택된 카테고리 가져오기
        selected_categories = storage_data if storage_data else ["코인", "노래", "실시간 검색어", "뉴스"]
        
        # 카테고리 매핑 (한글 -> API 카테고리)
        category_mapping = {
            "뉴스": "news",
            "실시간 검색어": "realtime-search",
            "노래": "music",
            "코인": "coin"
        }
        
        # 선택된 카테고리를 API 카테고리로 변환
        category = [category_mapping[cat] for cat in selected_categories if cat in category_mapping]
        
        # 기간 동안 선택한 카테고리에 해당하는 데이터 가져오기
        category_dfs = parse_downloads(categories=",".join(category), start_date=start_timestamp, end_date=end_timestamp)
        
        if not category_dfs:
            return None
            
        # Excel 파일로 저장
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            for category, df in category_dfs.items():
                df.to_excel(writer, sheet_name=category, index=False)
        
        output.seek(0)
        return dcc.send_bytes(output.getvalue(), "새도리.xlsx")