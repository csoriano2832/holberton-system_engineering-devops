#!/usr/bin/python3
"""
For a given employee ID, returns information about his/her TODO list progress
    - Export data in the JSON format
"""
import json
import requests


if __name__ == "__main__":
    """ Only executes as main """

    user_id = 0
    username = ""
    title = ""
    status = ""
    employee_todos = {}

    users = requests.get('https://jsonplaceholder.typicode.com/users').json()

    for user in users:
        user_id = user.get('id')
        username = user.get('username')

        todos = requests.get('https://jsonplaceholder.typicode.com/\
                             todos?userId={}'.format(user_id)).json()

        tasks = []
        for i in todos:
            task = {"username": username, "task": i.get("title"),
                    "completed": i.get("completed")}
            tasks.append(task)

        employee_todos[user_id] = tasks

    with open('todo_all_employees.json', 'w') as f:
        json.dump(employee_todos, f)
