from dash import callback, Input, Output, State
from dash import dcc
import json
from components.interest_summarize import render_interest_summary
from fetch.fetch_keywords import parse_keywords

@callback(
    [Output("today-word-1", "children"),
     Output("today-word-2", "children"),
     Output("today-word-3", "children")],
    Input({'type': 'storage', 'index': 'local'}, 'data'),
    prevent_initial_call=False
)
def get_today_words(interest_categories):
    if interest_categories is None:
        interest_categories = ["실시간 검색어", "뉴스", "코인", "노래"]

    today_words = []
    category_mapping = {
        "코인": "coin",
        "노래": "music",
        "실시간 검색어": "search_word",
        "뉴스": "news"
    }
    
    keywords = parse_keywords()
    
    if len(interest_categories) == 1:
        # 관심분야가 1개일 경우: 해당 카테고리의 키워드 3개 사용
        category = category_mapping.get(interest_categories[0])
        if category in keywords and keywords[category]:
            today_words = keywords[category][:3]
    elif len(interest_categories) == 2:
        # 관심분야가 2개일 경우: 첫 번째 카테고리의 키워드 2개, 두 번째 카테고리의 키워드 1개 사용
        category1 = category_mapping.get(interest_categories[0])
        category2 = category_mapping.get(interest_categories[1])
        
        if category1 in keywords and keywords[category1]:
            today_words.extend(keywords[category1][:2])
        if category2 in keywords and keywords[category2]:
            today_words.append(keywords[category2][0])
    else:
        # 그 외의 경우: 각 카테고리의 첫 번째 키워드 사용
        for interest in interest_categories:
            category = category_mapping.get(interest)
            if category in keywords and keywords[category]:
                today_words.append(keywords[category][0])

    # 키워드가 3개 미만일 경우 '실시간 검색어', '뉴스', '코인' 키워드 사용
    while len(today_words) < 3:
        today_words.append(keywords["search_word"][0])
        today_words.append(keywords["news"][0])
        today_words.append(keywords["coin"][0])

    return today_words[0], today_words[1], today_words[2]