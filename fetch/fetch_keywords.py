import requests

def fetch_keywords():
    try:
        response = requests.get("http://localhost:8080/api/v1/keywords")        
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("API 호출 에러:", e)
        return []

def parse_keywords():
    data = fetch_keywords()
    if not data:
        print("데이터를 가져오지 못했습니다.")
        return []

    all_keywords = []
    for item in data.get("top3_keywords", []):
        all_keywords.extend(item.get("keyword", []))

    return all_keywords