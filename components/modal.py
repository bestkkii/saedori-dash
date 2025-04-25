import dash_mantine_components as dmc
from dash import callback, Input, Output, State
from dash import dcc
from datetime import datetime, timedelta, date

def interest_modal():
    return dmc.Modal(
        title=dmc.Text("관심 분야를 선택 해 주세요", className="modal-box"),
        id="interest-modal",
        children=[
            dmc.MultiSelect(
                label="선택한 순서대로 우선순위가 부여됩니다.",
                id="interest-multiselect",
                data=["코인", "노래", "실시간 검색어", "뉴스"],
                value=["코인", "노래", "실시간 검색어", "뉴스"],
                w=400,
                mb=10,
            ),
            dmc.Space(h=20),
            dmc.Text(id="interest-select-view"),
            dmc.Space(h=20),
            dmc.Button("확인", id="interest-submit-button"),
            dcc.Store(id={'type': 'storage', 'index': 'local'}, storage_type='local'),
        ],
        className="interest-modal-box"
    )

def download_modal():
    return dmc.Modal(
        title=dmc.Text("오늘의 단어와 관심사 분야의 컨텐츠 내려받기", className="modal-box"),
        id="download-modal",
        style={
            "height": "600px",         # ✅ 원하는 높이
            "maxHeight": "90vh",       # ✅ 뷰포트 기준 최대 높이
            "overflowY": "auto",       # ✅ 내부 콘텐츠 스크롤
        },
        children=[
            dcc.DatePickerRange(
                id="date-picker",
                min_date_allowed=date(1995, 8, 5),
                max_date_allowed=date(2017, 9, 19),
            ),
            dmc.Space(h=20),
            dmc.Button("다운로드", id="download-submit-button"),
        ],
        className="download-modal-box"
    )