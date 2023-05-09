#!/usr/bin/python3
"""queries the REDDIT API"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    queries the Reddit API recursively and returns a list with all hot
    articles in a given sub.
    Returns None if no results are found
    """
    if subreddit is None or type(subreddit) is not str:
        return None
    headers = {'User-Agent': 'api-recursive'}
    params = {'after': after}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json()
    posts = data['data']['children']
    for post in posts:
        title = post['data']['title']
        hot_list.append(title)
    # Get the next page token
    after = data['data']['after']
    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
