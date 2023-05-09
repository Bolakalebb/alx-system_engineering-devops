#!/usr/bin/python3
"""
A recursive function that queries the Reddit API,
parses the title of all hot articles, and prints a sorted count of given keywords.
@authour: Bolakale Aduloju
"""

import requests


def count_words(subreddit, word_list, count_dict=None, after=None):
  """count all words"""

    if count_dict is None:
        count_dict = {}
        
    url = "https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, params={"limit": 100, "after": after})
    if response.status_code == 200:
        data = response.json()["data"]
        children = data["children"]
        for child in children:
            title = child["data"]["title"].lower()
            for word in word_list:
                if title.count(word.lower()) > 0:
                    if word.lower() in count_dict:
                        count_dict[word.lower()] += title.count(word.lower())
                    else:
                        count_dict[word.lower()] = title.count(word.lower())
        if data["after"] is not None:
            count_words(subreddit, word_list, count_dict=count_dict, after=data["after"])
        else:
            for key, value in sorted(count_dict.items(), key=lambda item: (-item[1], item[0])):
                print(key, value)
    else:
        return None
