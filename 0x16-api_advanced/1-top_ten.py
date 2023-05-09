#!/usr/bin/python3
"""Module to interact with the Reddit API"""
import requests


def top_ten(subreddit):
    """Fetches the top 10 hot posts from a given subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    response = requests.get(url, headers={'User-Agent': 'My-User-Agent'},
                            allow_redirects=False)
    if response.status_code >= 300:
        print('None')
    else:
        for post in response.json().get('data').get('children'):
            print(post.get('data').get('title'))
