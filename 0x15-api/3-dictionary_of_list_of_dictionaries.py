#!/usr/bin/python3
"""Export data in the JSON format"""

import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)
    users = response.json()

    dictionary = {}
    for user in users:
        employee_id = user.get('id')
        username = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
        url = url + '/todos/'
        response = requests.get(url)
        tasks = response.json()
        dictionary[employee_id] = []
        for task in tasks:
            dictionary[employee_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            })
    with open('todo_all_employees.json', 'w') as file:
        json.dump(dictionary, file)
