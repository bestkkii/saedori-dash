import requests
from config import Config
import re


def fetch_news_data():
    try:
        response = requests.get(f"{Config.API_BASE_URL}/api/v1/interest/detail", params={"category": "news"})
        response.raise_for_status()
        return response.json().get("result", [])[0]['news']
    except Exception as e:
        print("API 호출 에러:", e)
        return []

def clean_text(text):
    # 1. 앞뒤 공백 제거
    text = text.strip()

    # 2. 맨 앞에 [ ]로 감싼 부분 제거
    # 정규표현식 사용: 문자열 맨 앞에 [내용] 패턴이 있으면 제거
    text = re.sub(r'^\[[^\]]*\]\s*', '', text)
    text = text.strip()

    return text

def get_news_summary():
    data = fetch_news_data()
    news_companies_summary = []
    news_titles_summary = []

    try:
        news_companies_summary = [item['company'] for item in data]
        news_titles_summary = [clean_text(item['title']) for item in data]

    finally:
        return [news_companies_summary, news_titles_summary]


