#!/usr/bin/python3
"""
function to query the Reddit API and returns the number of subscribers.
Return 0 if an invalid subreddit is given
"""
import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subcribers for a subreddit or 0 if subreddit is
    invalid
    """
    if subreddit is None or type(subreddit) is not str:
        return 0
    headers = {'User-Agent': 'my-app/0.0.1'}

    response = requests.get("https://www.reddit.com/r/{}/about.json".
                            format(subreddit), headers=headers,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0
