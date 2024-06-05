#!/usr/bin/python3
"""
Function that queries the Reddit API
& prints the titles of the first 10 hot posts
"""

import requests
import sys


def top_ten(subreddit):
    """
    Function that querie the Reddit API
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Custom"}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        for post in response.json().get("data", {}).get("children", []):
            title = post.get("data", {}).get("title")
            if title:
                print(title)
    else:
        print(None)
