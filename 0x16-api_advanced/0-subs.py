#!/usr/bin/python3
"""A function that queries the Reddit API and returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
	""" Queries to Reddit API """
	
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {"User-Agent": "myBot/0.0.1"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()["data"]
        return data["subscribers"]
    else:
        return 0
