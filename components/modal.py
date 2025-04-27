import dash_mantine_components as dmc
from dash import callback, Input, Output, State
from dash import dcc
from datetime import datetime, timedelta, date
from fetch.fetch_downlonds import parse_downloads
import pandas as pd
import io
from dash_iconify import DashIconify

def interest_modal():
    return dmc.Modal(
        title=dmc.Text(
            "관심 분야를 선택 해 주세요", 
            className="font",
            style={"fontWeight": "bold", "width": "100%", "textAlign": "center"}
        ),
        id="interest-modal",
        children=[
            dmc.Space(h=10),
            dmc.Container(
                children=[
                    dmc.MultiSelect(
                        description="선택한 순서대로 우선순위가 부여됩니다.",
                        id="interest-multiselect",
                        data=["코인", "노래", "실시간 검색어", "뉴스"],
                        value=["코인", "노래", "실시간 검색어", "뉴스"],
                        w="100%",
                        mb=10,
                    ),
                    dmc.Space(h=20),
                    dmc.Paper(
                        id="interest-select-view",
                        shadow="xs",
                        radius="xl",
                        p="xs",
                        className="interest-select-view"
                    ),
                    dmc.Space(h=30),
                    dmc.Button("확인", id="interest-submit-button", variant="filled", color="black"),
                    dcc.Store(id={'type': 'storage', 'index': 'local'}, storage_type='local'),
                ],
                style={
                    "display": "flex",
                    "flexDirection": "column",
                    "alignItems": "center",
                    "width": "100%"
                }
            )
        ],
        className="interest-modal-box"
    )

def download_modal():
    return dmc.Modal(
        title=dmc.Text(
            "오늘의 단어와 관심사 분야의 컨텐츠 내려받기", 
            className="font",
            style={"fontWeight": "bold", "width": "100%", "textAlign": "center"}
        ),
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
                            dmc.Button("다운로드", "download-submit-button", n_clicks=0, variant="filled", color="black"),
                        ],
                        justify="flex-start",
                        style={'width': '100%', 'flexWrap': 'nowrap', 'display': 'flex', 'alignItems': 'center'}
                    )
                ],
                style={
                    'height': '400px',
                    'overflow': 'auto',
                    'position': 'relative',
                    'width': '100%', 
                }
            ),
            dcc.Download(id="download-dataframe-csv")
        ],
        className="download-modal-box",
        size="xl"
    )