import requests
from config import Config
import pandas as pd
from datetime import datetime
import json

def fetch_downloads(categories=None, start_date=None, end_date=None):
    url = f"{Config.API_BASE_URL}/api/v1/download"
    params = []
    if categories:
        # categories가 리스트인 경우 쉼표로 구분된 문자열로 변환
        if isinstance(categories, list):
            categories = ",".join(categories)
        params.append(f"category={categories}")
    if start_date:
        params.append(f"start_date={start_date}")
    if end_date:
        params.append(f"end_date={end_date}")
        
    url += "?" + "&".join(params)
                
    response = requests.get(url, headers={'Accept-Charset': 'utf-8'})
    response.raise_for_status()
    return response.json()


def parse_downloads(categories=None, start_date=None, end_date=None):
    data = fetch_downloads(categories, start_date, end_date).get("result", {})
    if not data:
        return None

    # 각 카테고리별 DataFrame을 저장할 딕셔너리
    res_df = {}

    # keywords 데이터 처리
    if data.get("dn_keywords"):
        keyword_dfs = []
        for keyword_item in data["dn_keywords"]:
            temp_df = pd.DataFrame({
                'category': keyword_item['category'],
                'type': 'keyword',
                'content': ', '.join(keyword_item['keyword']),
                'created_at': datetime.fromtimestamp(keyword_item['created_at']).strftime('%Y-%m-%d %H:%M:%S')
            }, index=[0])
            keyword_dfs.append(temp_df)
        if keyword_dfs:
            res_df['keywords'] = pd.concat(keyword_dfs, ignore_index=True)

    # news 데이터 처리
    if data.get("dn_news"):
        news_dfs = []
        for news_item in data["dn_news"]:
            for news in news_item["news"]:
                temp_df = pd.DataFrame({
                    'category': 'news',
                    'type': 'news',
                    'company': news['company'],
                    'title': news['title'],
                    'url': news['url'],
                    'created_at': datetime.fromtimestamp(news_item['created_at']).strftime('%Y-%m-%d %H:%M:%S')
                }, index=[0])
                news_dfs.append(temp_df)
        if news_dfs:
            res_df['news'] = pd.concat(news_dfs, ignore_index=True)

    # realtime-search 데이터 처리
    if data.get("dn_realtime_search"):
        search_dfs = []
        
        for search_item in data["dn_realtime_search"]:
            # 한국 실시간 검색어 처리
            temp_df = pd.DataFrame({
                'category': 'realtime-search',
                'type': 'realtime-search',
                'region': 'kr',
                'content': ', '.join(search_item["realtime_search"]["kr"]),
                'created_at': datetime.fromtimestamp(search_item['created_at']).strftime('%Y-%m-%d %H:%M:%S')
            }, index=[0])
            search_dfs.append(temp_df)
            
            # 미국 실시간 검색어 처리
            temp_df = pd.DataFrame({
                'category': 'realtime-search',
                'type': 'realtime-search',
                'region': 'us',
                'content': ', '.join(search_item["realtime_search"]["us"]),
                'created_at': datetime.fromtimestamp(search_item['created_at']).strftime('%Y-%m-%d %H:%M:%S')
            }, index=[0])
            search_dfs.append(temp_df)
        
        # 한국/미국 df 병합
        if search_dfs:
            res_df['realtime-search'] = pd.concat(search_dfs, ignore_index=True)

    # music 데이터 처리
    if data.get("dn_music"):
        music_dfs = []
        
        for music_item in data["dn_music"]:
            # 국내 음악 처리
            for music in music_item["music"]["domestic"]:
                temp_df = pd.DataFrame({
                    'category': 'music',
                    'type': 'music',
                    'region': 'domestic',
                    'singer': music['singer'],
                    'title': music['title'],
                    'url': music['url'],
                    'created_at': datetime.fromtimestamp(music_item['created_at']).strftime('%Y-%m-%d %H:%M:%S')
                }, index=[0])
                music_dfs.append(temp_df)
            
            # 해외 음악 처리
            for music in music_item["music"]["global"]:
                temp_df = pd.DataFrame({
                    'category': 'music',
                    'type': 'music',
                    'region': 'global',
                    'singer': music['singer'],
                    'title': music['title'],
                    'url': music['url'],
                    'created_at': datetime.fromtimestamp(music_item['created_at']).strftime('%Y-%m-%d %H:%M:%S')
                }, index=[0])
                music_dfs.append(temp_df)
        
        # 국내/해외 음악 df 병합
        if music_dfs:
            res_df['music'] = pd.concat(music_dfs, ignore_index=True)

    return res_df