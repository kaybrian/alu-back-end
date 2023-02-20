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
    USER = requests.request(
        "GET", f'https://jsonplaceholder.typicode.com/users/{USER_ID}/'
    ).json()
    USER_TASKS = requests.request(
        "GET", f"https://jsonplaceholder.typicode.com/users/{USER_ID}/todos"
    ).json()

    with open(str(USER_ID)+".csv", "w", encoding="utf8") as file:
        for task in USER_TASKS:
            file.write('"' + str(USER_ID) + '"' +
                       "," + '"' + str(USER["username"]) + '"' +
                       "," + '"' + str(task["completed"]) + '"' +
                       "," + '"' + str(task["title"]) + '"' + "\n")
