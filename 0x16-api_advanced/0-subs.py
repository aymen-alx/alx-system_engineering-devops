#!/usr/bin/python3
"""Module for getting the number of subscribers for a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    for the subreddit"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers={'User-Agent': 'My-User-Agent'},
                            allow_redirects=False)
    if response.status_code >= 300:
        return 0

    return response.json().get('data').get('subscribers')
