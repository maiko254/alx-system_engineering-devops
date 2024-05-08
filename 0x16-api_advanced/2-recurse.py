#!/usr/bin/python3
"""
Queries the Reddit API and returns a list containing the titles
of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit, returning None if
    no results are found
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    headers = {'User-Agent': 'My Reddit Bot 1.0'}
    response = requests.get(url, headers=headers)
    response_data = response.json()
    if 'error' in response_data:
        return None
    articles = response_data['data']['children']
    for article in articles:
        hot_list.append(article['data']['title'])
    next_cursor = response_data['data']['after']
    if next_cursor:
        return recurse(subreddit, hot_list, after=next_cursor)
    else:
        return hot_list
