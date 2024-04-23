#!/usr/bin/python3
"""extend the Python script in task 0 to export data in the JSON format."""

import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    uRl = "https://jsonplaceholder.typicode.com/"
    uSer = requests.get(uRl + "users/{}".format(user_id)).json()
    user_name = uSer.get("username")
    todos_l = requests.get(uRl + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": user_name
            } for t in todos_l]}, jsonfile)
