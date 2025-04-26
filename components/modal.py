import dash_mantine_components as dmc
from dash import callback, Input, Output, State
from dash import dcc
from datetime import datetime, timedelta, date
from fetch.fetch_downlonds import parse_downloads
import pandas as pd
import io

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
        children=[
            dmc.Container(
                children=[
                    dmc.Group(
                        children=[
                            dcc.DatePickerRange(
                                id="date-picker",
                                min_date_allowed=date(2025, 1, 1),
                                max_date_allowed=date.today(),
                                style={'padding': '20px', 'margin': '10px', 'width': '500px'}
                            ),
                            dmc.Button(
                                "다운로드", 
                                id="download-submit-button",
                                style={'margin': '10px 10px'}
                            ),
                        ],
                        justify="flex-start",
                        style={'width': '100%', 'flexWrap': 'nowrap', 'display': 'flex', 'alignItems': 'center'}
                    )
                ],
                style={
                    'height': '400px',
                    'overflow': 'auto',
                    'position': 'relative',
                    'width': '800px'
                }
            ),
            dcc.Download(id="download-dataframe-csv")
        ],
        className="download-modal-box",
        size="xl"
    )