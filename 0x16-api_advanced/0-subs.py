#!/usr/bin/python3
"""
Function that gets the number of subcribers in a given subreddit
by querying the reddit api
"""
import requests


def number_of_subscribers(subreddit):
    """
       Returns the number of total subscribers in a given subreddit
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    res = requests.get(url)
    if res.status_code > 300:
        return 0
    subred = res.json()
    data = subred.get('data')
    subscribers = data.get('subscribers')
    return subscribers
