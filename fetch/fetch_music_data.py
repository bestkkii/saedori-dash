import requests
from config import Config

def fetch_music_data():
    try:
        response = requests.get(f"{Config.API_BASE_URL}/api/v1/interest/detail", params={"category": "music"})
        response.raise_for_status()
        return response.json().get("result", [])
    except Exception as e:
        print("API 호출 에러:", e)
        return []

def parse_music_data():
    data = fetch_music_data()
    charts = {
        "국내 차트": [],
        "해외 차트": []
    }
    if not data:
        return charts

    latest = data[-1]["music"]
    for i, item in enumerate(latest.get("domestic", [])[:10], start=1):
        charts["국내 차트"].append({
            "rank": i,
            "title": item.get("title", ""),
            "artist": item.get("singer", ""),
            "url": item.get("url", "")
        })
    for i, item in enumerate(latest.get("global", [])[:10], start=1):
        charts["해외 차트"].append({
            "rank": i,
            "title": item.get("title", ""),
            "artist": item.get("singer", ""),
            "url": item.get("url", "")
        })
    return charts