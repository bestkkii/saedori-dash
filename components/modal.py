import dash_mantine_components as dmc
from dash import callback, Input, Output, State
from dash import dcc

def render_modals():
    return dmc.Modal(
        title=dmc.Text("관심 분야를 선택 해 주세요", className="modal-box"),
        id="interest-modal",
        children=[
            dmc.MultiSelect(
                label="선택한 순서대로 우선순위가 부여됩니다.",
                id="interest-multiselect",
                data=["코인", "노래", "실시간 검색어", "뉴스"],
                w=400,
                mb=10,
            ),
            dmc.Space(h=20),
            dmc.Text(id="interest-select-view"),
            dmc.Space(h=20),
            dmc.Button("확인", id="modal-submit-button"),
            dcc.Store(id="saved-interest"),     # 세션별 저장
            dmc.Text(id="interest-select-print-view"),
        ],
        className="modal-box"
    )
