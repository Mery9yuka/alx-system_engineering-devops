#!/usr/bin/python3

"""Function that count words in all hot articles of a Reddit subreddit"""

import requests


def count_words(subreddit, word_list, counts=None, after="", count=0):
    """Function that prints a sorted count of given keywords found
       in hot articles of a given subreddit.
    """
    if counts is None:
        counts = {word.lower(): 0 for word in word_list}

    url_api = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/meryuka20)"
    }
    req_params = {
        "after": after,
        "limit": 100
    }

    try:
        response = requests.get(
            url_api, headers=headers, params=req_params, timeout=10
            )
        response.raise_for_status()
        results = response.json().get("data")
    except requests.RequestException as e:
        print(f"Error fetching data from Reddit API: {e}")
        return

    after_id = results.get("after")
    count += results.get("dist")

    for i in results.get("children"):
        title = i.get("data").get("title").lower().split()
        for w in word_list:
            if w.lower() in title:
                time = len([t for t in title if t == w.lower()])
                counts[w.lower()] += time  # Use lowercase key to access counts

    if after_id is None:
        if len(counts) == 0:
            print("")
            return
        sorted_counts = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
        for word, count in sorted_counts:
            if count > 0:
                print(f"{word}: {count}")
    else:
        count_words(subreddit, word_list, counts, after_id, count)
