#!/usr/bin/python3

import requests
import sys


"""A module to handle users and their todos in a day"""

if __name__ == '__main__':
    """"The main function that is called when the file runs"""
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
