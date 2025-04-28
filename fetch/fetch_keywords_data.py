import requests
from config import Config

def fetch_keywords():
    try:
        response = requests.get(f"{Config.API_BASE_URL}/api/v1/keywords")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("API 호출 에러:", e)
        return None

def parse_keywords():
    data = fetch_keywords()
    if not data:
        return {
            "music": [],
            "realtime_search": [],
            "news": [],
            "coin": []
        }

    keywords = {
        "music": [],
        "realtime_search": [],
        "news": [],
        "coin": []
    }

    for item in data.get("top3_keywords", []):
        category = item.get("category")
        if category in keywords:
            keywords[category].extend(item.get("keyword", []))

    return keywords