#!/usr/bin/python3
""" Queries the reddit api for data on a subreddit """
import requests


def top_ten(subreddit):
    """
      Prints the first 10 hot posts titles after querying the reddit api
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'My Reddit bot 1.0'}
    res = requests.get(url, headers=headers)
    if res.status_code > 300:
        return None
    hot = res.json()
    data = hot.get('data')
    children = data.get('children')
    for child in children:
        v = child['data']
        print(v['title'])
