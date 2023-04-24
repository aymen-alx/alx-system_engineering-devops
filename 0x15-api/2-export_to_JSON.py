#!/usr/bin/python3
""" Task2 """
import json
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    link = 'https://jsonplaceholder.typicode.com/'
    user = requests.get('{}{}{}'.format(link, 'users/', user_id)).json()
    name = user.get('username')
    todos = requests.get('{}{}{}'.format(
        link, 'todos?userId=', user_id)).json()
    total_tasks = len(todos)

    with open("{}.json".format(user_id), "w") as f:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": name
            } for t in todos]}, f)
