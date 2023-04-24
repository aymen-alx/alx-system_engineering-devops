#!/usr/bin/python3
""" Task0 """
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

    done_tasks = 0
    for task in todos:
        if task.get('completed') is True:
            done_tasks += 1
    print('Employee {} is done with tasks({}/{}):'.format(
        name, done_tasks, total_tasks))
    for task in todos:
        if task.get('completed') is True:
            print('\t', task.get('title'))
