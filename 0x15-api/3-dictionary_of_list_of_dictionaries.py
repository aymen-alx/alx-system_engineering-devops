#!/usr/bin/python3
""" Task3 """
import json
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv
    link = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(link + "users").json()
    # name = user.get('username')
    todos = requests.get('{}{}{}'.format(
        link, 'todos?userId=', user_id)).json()
    total_tasks = len(todos)

    with open("todo_all_employees.json", "w") as f:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(link + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in user}, f)
