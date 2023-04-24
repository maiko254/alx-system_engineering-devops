#!/usr/bin/python3
"""
using JSONPlaceholder to get information on an employee ID's TODO list
and exporting it in a JSON format with the filename 'USER_ID'.json
"""
import requests
import sys
import json


if __name__ == "__main__":
    employee_id = sys.argv[1]
    # Make a request to the JSONPlaceholder API
    response = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(employee_id))

    user = response.json()
    employee_name = user.get("name")

    # Make another request to get the todos for the employee
    resp = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                        .format(employee_id))

    todos = resp.json()
    total_tasks = len(todos)
    done_tasks = 0
    done_titles = []
    data = {}
    data[employee_id] = []

    for todo in todos:
        if todo.get("completed"):
            done_tasks += 1
            done_titles.append(todo.get("title"))
        task = {
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": user.get("username")
        }
        data[employee_id].append(task)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, done_tasks, total_tasks))
    for title in done_titles:
        print("\t {}".format(title))

    with open("{}.json".format(employee_id), "w") as f:
        json.dump(data, f)
