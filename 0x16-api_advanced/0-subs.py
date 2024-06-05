#!/usr/bin/python3
"""Function that queries the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """Return the nb of subscribers for a given subreddit
       returns the number of subscribers for a given subreddit.
       If an invalid subreddit is given, the function should return 0
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'python:subscribers:v1.0 (by /u/meryuka20@gmail.com)'
        }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data_u = response.json()
            return data_u['data']['subscribers']
    except requests.exceptions.RequestException:
        pass

    return 0
