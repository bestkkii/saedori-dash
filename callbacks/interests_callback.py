from dash import callback, Input, Output, State, no_update
import dash_mantine_components as dmc
from components.interest_summarize import render_interest_summary

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
