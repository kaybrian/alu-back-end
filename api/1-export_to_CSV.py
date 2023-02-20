#!/usr/bin/python3
"""
    python script that exports data in the CSV format
"""
import csv
import json
import requests
import sys


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
