import requests
from dash import callback, Input, Output, State
from components.interest_summarize import render_interest_summary

# 로컬 스토리지에 저장된 관심사 불러오기
@callback(
    Output("interest-multiselect", "value"),        # 모달창 multiselect 선택
    Output("interest-select-view", "children"),     # 모달창 text로 출력
    Output("carousel-container", "children"),       # Summary 칸에 노출
    Input({'type': 'storage', 'index': 'local'}, 'data'),   # 로컬 스토리지에 바뀐게 있을 경우
    prevent_initial_call=False
)
def load_interest_from_local_storage(saved_data):
    if saved_data is None:
        saved_data = ["실시간 검색어", "뉴스", "코인", "노래"]
    return saved_data,  f"선택된 항목: {saved_data}", render_interest_summary(saved_data)

# 관심사 설정 버튼 클릭 시 모달 열기
@callback(
    Output("interest-modal", "opened"), 
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
    Input("interest-submit-button", "n_clicks"),
    State("interest-multiselect", "value"),
    prevent_initial_call=True
)
def save_interest(n_clicks, selected_values):
    return selected_values or []