#!/usr/bin/python3
"""
using JSONPlaceholder REST API to get all tasks from all employees and
exporting the data in a json format
"""
import json
import requests
import sys


if __name__ == "__main__":
    # Make a request to get all the users from the API
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    users = response.json()
    data = {}
    for user in users:
        employee_id = user.get("id")
        employee_name = user.get("name")
        r = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                         .format(employee_id))
        todos = r.json()
        data[employee_id] = []
        for todo in todos:
            task = {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username")
                }
            data[employee_id].append(task)
    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)
