#!/usr/bin/python3
"""
using JSONPlaceholder to get information on an employee ID's TODO list
and exporting user data to a CSV format, Filename - 'USER_ID'.csv
"""
import csv
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    # Make a request to the JSONPlaceholder API
    response = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(employee_id))

    user = response.json()
    employee_name = user.get("name")
    username = user.get("username")

    # Make another request to get the todos for the employee
    resp = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                        .format(employee_id))

    todos = resp.json()
    total_tasks = len(todos)
    done_tasks = 0
    done_titles = []
    rows = []

    for todo in todos:
        if todo.get("completed"):
            done_tasks += 1
            done_titles.append(todo.get("title"))
        rows.append([employee_id, username, todo.get("completed"),
                    todo.get("title")])

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, done_tasks, total_tasks))
    for title in done_titles:
        print("\t {}".format(title))

    with open("{}.csv".format(employee_id), "w") as csv_file:
        csv_writer = csv.writer(csv_file, quotechar='"', quoting=csv.QUOTE_ALL)
        for row in rows:
            csv_writer.writerow(row)
