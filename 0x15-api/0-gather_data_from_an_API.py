#!/usr/bin/python3
"""
For a given employee ID, returns information about his/her TODO list progress
"""
import requests
import sys


if __name__ == "__main__":
    """ Only executes as main """

    ID = sys.argv[1]
    employee_name = ""
    tasks_completed = 0
    total_tasks = 0
    tasks = []

    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                     format(ID))

    employee_name = (r.json().get('name'))

    r = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                     format(ID))

    for i in r.json():
        if i['completed'] is True:
            tasks_completed += 1
            tasks.append(i['title'])
        total_tasks += 1

    print('Employee {} is done with tasks({}/{}):'.
          format(employee_name, tasks_completed, total_tasks))

    for i in tasks:
        print('\t {}'.format(i))
