#!/usr/bin/python3
"""queries the Reddit API"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords
    """
    if counts is None:
        counts = {}
        for word in word_list:
            counts[word.lower()] = 0

    headers = {"User-Agent": "my-app/0.1"}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"after": after}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None

    data = response.json().get("data")
    posts = data.get("children")
    for post in posts:
        title = post.get("data").get("title").lower()
        words = title.split()
        for word in word_list:
            word = word.lower()
            count = words.count(word)
            counts[word] += count

    after = data.get("after")
    if after is None:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for key, value in sorted_counts:
            if value > 0:
                print("{}: {}".format(key, value))
        return counts
    else:
        return count_words(subreddit, word_list, after, counts)
