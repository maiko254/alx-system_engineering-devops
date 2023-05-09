#!/usr/bin/python3
"""queries Reddit API"""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed for a subreddit"""

    headers = {'User-Agent': 'my-app/0.0.1'}
    response = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10".
                            format(subreddit), headers=headers,
                            allow_redirects=False)
    if response.status_code == 200:
        hot_10 = response.json()
        posts = hot_10['data']['children']
        for v in posts:
            print(v['data']['title'])
    else:
        return None
