#!/usr/bin/python3
"""Module for Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively fetch all the hot posts from a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": 100, "after": after}
    headers = {"User-Agent": "My-User-Agent"}
    response = requests.get(url, params=params, headers=headers,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data")
    if not data:
        return hot_list

    posts = [child.get("data").get("title") for child in data.get("children")]
    hot_list.extend(posts)

    after = data.get("after")
    if not after:
        return hot_list

    return recurse(subreddit, hot_list, after)
