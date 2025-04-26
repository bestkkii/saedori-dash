from dash import callback, Input, Output, State
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