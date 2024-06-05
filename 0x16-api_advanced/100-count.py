#!/usr/bin/python3

"""Function that count words in all hot articles of a Reddit subreddit"""

import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """Prints a sorted count of given keywords found
       in hot articles of a given subreddit.
    """
    url_api = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/meryuka20)"
    }
    req_params = {
        "after": after_id,
        "count": count_key,
        "limit": 100
    }
    response = requests.get(url_api, headers=headers, params=req_params,
                            allow_redirects=False)
    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    results = results.get("data")
    after_id = results.get("after")
    count_key += results.get("dist")
    for i in results.get("children"):
        title = i.get("data").get("title").lower().split()
        for w in word_list:
            if w.lower() in title:
                time = len([t for t in title if t == w.lower()])
                if instances.get(w) is None:
                    instances[w] = time
                else:
                    instances[w] += time

    if after_id is None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
