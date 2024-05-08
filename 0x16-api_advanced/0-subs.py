#!/usr/bin/python3
"""Function that queries the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """Return the nb of subscribers for a given subreddit
       returns the number of subscribers for a given subreddit.
       If an invalid subreddit is given, the function should return 0
    """
    def number_of_subscribers(subreddit):
        url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
