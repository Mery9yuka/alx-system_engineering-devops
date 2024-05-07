#!/usr/bin/python3
"""Function that queries the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """Return the nb of subscribers for a given subreddit"""
     resp = requests.get(
             "https://www.reddit.com/r/{}/about.json".format(subreddit),
             Headers={"User-Agent": "Custom"},
             )

     if resp.status_code == 200:
         return resp.json().get("data").get("subscribers")
    else:
        return 0

