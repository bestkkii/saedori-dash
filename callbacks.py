from dash import callback, Input, Output, State
import plotly.express as px
import pandas as pd

# 관심사 설정 버튼 클릭 시 모달 열기
@callback(
    Output("interest-modal", "opened"), 
    Input("interest-button", "n_clicks"), State("interest-modal", "opened"), 
    prevent_initial_call=True
)
def select_interest(n_clicks, is_open):
    if n_clicks:
        return not is_open
    return is_open

# 관심 분야 선택 시 리스트 출력
@callback(
    Output("interest-select-view", "children"),
    Input("interest-multiselect", "value")
)
def print_interest(value):
    if not value:
        return "선택된 항목이 없습니다."
    return ", ".join(value)

# 관심 분야 선택 후 확인 버튼 클릭 시 저장
@callback(
    Output("saved-interest", "data"),
    Input("modal-submit-button", "n_clicks"),
    State("interest-multiselect", "value"),
    prevent_initial_call=True
)
def save_interest(n_clicks, selected_values):
    return selected_values or []

# 선택된 관심 분야 출력하기 - 데이터 필요할 경우 주석 제거 후 사용
# @callback(
#     Output("interest-select-print-view", "children"),
#     Input("saved-interest", "data")
# )
# def print_interest(saved):
#     print("저장된 관심분야:", saved)