#!/usr/bin/python3
"""Export data in the JSON format"""

import json
import requests
import sys


if __name__ == '__main__':
    USER_ID = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + USER_ID

    response = requests.get(url)
    username = response.json().get('username')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    dictionary = {USER_ID: []}
    for task in tasks:
        dictionary[USER_ID].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })
    with open('{}.json'.format(USER_ID), 'w') as filename:
        json.dump(dictionary, filename)
