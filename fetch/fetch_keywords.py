import requests

def fetch_keywords():
    try:
        response = requests.get("http://localhost:8080/api/v1/keywords")
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
            "search_word": [],
            "news": [],
            "coin": []
        }

    keywords = {
        "music": [],
        "search_word": [],
        "news": [],
        "coin": []
    }

    for item in data.get("top3_keywords", []):
        category = item.get("category")
        if category in keywords:
            keywords[category].extend(item.get("keyword", []))

    return keywords