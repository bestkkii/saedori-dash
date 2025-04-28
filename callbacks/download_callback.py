from dash import callback, Input, Output, State, no_update
from datetime import datetime, timedelta
from fetch.fetch_downlonds_data import parse_downloads
import io
import pandas as pd
from dash import dcc
import dash_mantine_components as dmc
from dash import html

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

# 키워드, 컨텐츠 다운로드
@callback(
    [Output("download-dataframe-csv", "data"),
     Output("download-alert", "children"),
     Output("download-alert", "style")],
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
        end_timestamp = int((datetime.strptime(end_date.split('T')[0], '%Y-%m-%d') + timedelta(days=1)).timestamp())
        
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
            return no_update, dmc.Alert(
                dmc.Text("다운로드할 데이터가 없습니다.", className="font"),
                title=dmc.Text("알림", className="font"),
                color="yellow",
                variant="light",
                style={
                    "margin": "20px",
                    "backgroundColor": "#FFF3CD",
                    "border": "none",
                    "padding": "10px",
                    "borderRadius": "4px",
                    "overflow": "auto"
                }
            ), {"display": "block", "margin": "20px", "backgroundColor": "transparent"}
            
        # Excel 파일로 저장
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            for category, df in category_dfs.items():
                df.to_excel(writer, sheet_name=category, index=False)
        
        output.seek(0)
        return dcc.send_bytes(output.getvalue(), "새도리.xlsx"), None, {"display": "none"}