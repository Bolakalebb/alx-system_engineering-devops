#!/usr/bin/python3
"""A function that queries the Reddit API and returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
	""" Queries to Reddit API """
	
	if subreddit is None or not isinstance(subreddit, str):
        return 0

	user_agent = {'User-agent': 'myBot/0.0.1'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)
    results = response.json()

	try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
