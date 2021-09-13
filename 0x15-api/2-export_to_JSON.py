#!/usr/bin/python3
"""
For a given employee ID, returns information about his/her TODO list progress
    - Export data in the JSON format
"""
import json
import requests
import sys


if __name__ == "__main__":
    """ Only executes as main """

    ID = sys.argv[1]
    username = ""
    title = ""
    status = ""
    task = {}
    tasks = []
    employee_todos = {}

    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                     format(ID))

    username = (r.json().get('username'))

    r = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                     format(ID))

    for i in r.json():
        task = {"task": i.get("title"), "completed": i.get("completed"),
                "username": username}
        tasks.append(task)

    employee_todos[ID] = tasks

    with open('{}.json'.format(ID), 'w') as f:
        json.dump(employee_todos, f)
