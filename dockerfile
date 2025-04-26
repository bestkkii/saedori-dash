# Python 환경 설정
FROM python:3.12-slim

# 컨테이너 안에서 사용할 작업 디렉토리
WORKDIR /app

# requirements 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn==23.0.0
# 나머지 파일 복사
COPY . .

# Dash 앱 실행 (Gunicorn)
CMD ["gunicorn", "--bind", "0.0.0.0:8050", "app:server"]