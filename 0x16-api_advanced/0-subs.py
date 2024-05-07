#!/usr/bin/python3
"""Function that queries the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """Return the nb of subscribers for a given subreddit"""
    Url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
            }
    resp = requests.get(url, headers=headers, allow_redirects=False)
    if resp.status_code == 404:
        return 0
    rlts = response.json().get("data")
    return rlts.get("subscribers")


