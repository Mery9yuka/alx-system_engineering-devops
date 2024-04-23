#!/usr/bin/python3
"""extend the Python script in task 0 to export
   data in the JSON format, to all employees
"""
import json
import requests

if __name__ == "__main__":
    uRl = "https://jsonplaceholder.typicode.com/"
    users_id = requests.get(uRl + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(uRl + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in users_id}, jsonfile)
