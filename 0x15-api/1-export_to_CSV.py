#!/usr/bin/python3
""" Task0 """
import csv
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    link = 'https://jsonplaceholder.typicode.com/'
    name = requests.get('{}{}{}'.format(
        link, 'users/', user_id)).json().get('name')
    todos = requests.get('{}{}{}'.format(
        link, 'todos?userId=', user_id)).json()
    total_tasks = len(todos)

    with open("{}.csv".format(user_id), "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, name, t.get("completed"), t.get("title")]
         ) for t in todos]
