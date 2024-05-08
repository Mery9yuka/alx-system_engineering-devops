#!/usr/bin/python3
"""Function that queries the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """Return the nb of subscribers for a given subreddit
       returns the number of subscribers for a given subreddit. 
       If an invalid subreddit is given, the function should return 0.    
    """
    Url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
            }
    resp = requests.get(Url, headers=headers, allow_redirects=False)
    if resp.status_code == 404:
        return 0
    results = resp.json().get("data")
    return results.get("subscribers")
