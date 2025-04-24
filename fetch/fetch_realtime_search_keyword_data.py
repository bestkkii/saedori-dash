import requests

def fetch_realtime_search_keyword_data():
    try:
        response = requests.get("http://localhost:8080/api/v1/interest/detail", params={"category": "realtime-search"})
        response.raise_for_status()
        return response.json().get("result", [])
    except Exception as e:
        print("API 호출 에러:", e)
        return []

def parse_realtime_search_keyword_data():
    data = fetch_realtime_search_keyword_data()
    realtime_search_keywords = {
        "kr": [],
        "us": []
    }
    if not data:
        return realtime_search_keywords

    latest = data["realtime_search"]
    if "kr" in latest:
        kr_list = [{"index": i+1, "value": value} for i, value in enumerate(latest["kr"])]
        realtime_search_keywords["kr"] = kr_list
        
    if "us" in latest:
        us_list = [{"index": i+1, "value": value} for i, value in enumerate(latest["us"])]
        realtime_search_keywords["us"] = us_list
    
    return realtime_search_keywords