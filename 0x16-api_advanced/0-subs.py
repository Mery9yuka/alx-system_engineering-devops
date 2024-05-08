#!/usr/bin/python3
"""Function that queries the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """Return the nb of subscribers for a given subreddit
       returns the number of subscribers for a given subreddit.
       If an invalid subreddit is given, the function should return 0
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data['data']['subscribers']
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            print("Subreddit not found.")
        else:
            print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    return 0
