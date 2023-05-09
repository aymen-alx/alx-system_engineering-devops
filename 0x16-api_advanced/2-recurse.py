#!/usr/bin/python3
"""Module for Reddit API"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Fetches all the hot posts from a subreddit recursively"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code >= 300:
        print("None")
    else:
        for post in response.json().get("data").get("children"):
            print(post.get("data").get("title"))
