#!/usr/bin/python3
"""
For a given employee ID, returns information about his/her TODO list progress
    - Export data in the CSV format
"""
import csv
import requests
import sys


if __name__ == "__main__":
    """ Only executes as main """

    user_id = sys.argv[1]
    username = ""
    task_status = ""
    task_title = ""

    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                     format(user_id))

    username = (r.json().get('username'))

    r = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                     format(user_id))

    with open('{}.csv'.format(user_id), mode='w') as employee_file:
        writer = csv.writer(employee_file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)

        for i in r.json():
            status = i.get('completed')
            title = i.get('title')
            writer.writerow([user_id, username, status, title])
