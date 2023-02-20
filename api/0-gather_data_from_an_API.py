#!/usr/bin/python3
"""Module"""

import requests
import sys


"""Module"""

if __name__ == '__main__':
    user_id = sys.argv[1]
    user = requests.request(
        'GET', f'https://jsonplaceholder.typicode.com/users/{user_id}').json()
    user_tasks = requests.request(
        'GET', f'https://jsonplaceholder.typicode.com/users/{user_id}/todos/').json()

    EMPLOYEE_NAME = user['name']
    NUMBER_OF_DONE_TASKS = len(
        [x for x in user_tasks if x['completed'] == True])
    TOTAL_NUMBER_OF_TASKS = len(user_tasks)

    print(
        f'Employee {EMPLOYEE_NAME} is done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS})')
    [print("\t " + task["title"])
     for task in [x for x in user_tasks if x['completed'] == True]]
