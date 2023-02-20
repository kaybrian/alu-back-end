#!/usr/bin/python3
"""
python script that returns TODO list progress for a given employee ID
and saves that information in a csv file
"""

import csv
import requests
import sys
import json

if __name__ == "__main__":
    USER_ID = sys.argv[1]
    """
        Module to get the user tasks
    """
    USER = requests.request(
        "GET", f'https://jsonplaceholder.typicode.com/users/{USER_ID}/'
    ).json()
    """
        Module to get the user tasks
    """
    USER_TASKS = requests.request(
        "GET", f"https://jsonplaceholder.typicode.com/users/{USER_ID}/todos"
    ).json()

    """
        the main module that creates and writes the info in the csv file
    """
    with open(str(USER_ID)+".csv", "w", encoding="utf8") as file:

        for task in USER_TASKS:
            file.write('"' + str(USER_ID) + '"' +
                       "," + '"' + str(USER["username"]) + '"' +
                       "," + '"' + str(task["completed"]) + '"' +
                       "," + '"' + str(task["title"]) + '"' + "\n")
