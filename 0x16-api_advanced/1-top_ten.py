#!/usr/bin/python3
"""
Function that queries the Reddit API 
& prints the titles of the first 10 hot posts
"""

import requests


def top_ten(subreddit):
    """
    Function that querie the Reddit API
    """
    request = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        p={"limit": 10},
    )
    if request.status_code == 200:
        for get_d in request.json().get("data").get("children"):
            data = get_d.get("data")
            t = data.get("title")
            print(t)
    else:
        print(None)
