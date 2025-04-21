# saedori-dash
새도리 대시보드 레포지토리


## 디렉토리 구조

```
my_dash_app/
├── app.py                          # 메인 실행 파일
├── layout.py                       # 전체 레이아웃 구성
├── components/                     # UI 컴포넌트
│   ├── keyword.py                  # top3, 랜덤 키워드 UI
│   ├── setting.py                  # 다운로드, 관심사 분야 세팅 버튼 UI
│   ├── setting.py                  # 다운로드, 관심사 분야 모달 UI
│   ├── interest_summarize.py       # 관심사 분야 요약 내용 UI
│   ├── interest_detail.py          # 관심사 분야 세부 내용 UI
│   └── title.py                    # 로고, 제목 UI
├── callbacks.py                    # 콜백 함수
├── assets/      
│   └── images           
│   └── style.css
├── requirements.txt                # 필요한 패키지 목록
└── README.md                       # 설명서
```

## 실행 방법

1. 필수 패키지 설치
pip install -r requirements.txt
패키지 추가로 설치했을 경우, 
pip freeze > requirements.txt

2. 앱 실행
python app.py
