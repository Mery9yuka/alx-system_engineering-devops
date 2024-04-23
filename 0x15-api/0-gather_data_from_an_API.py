#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    uRl = "https://jsonplaceholder.typicode.com/"
    user_id = requests.get(uRl + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(uRl + "todos", params={"userId": sys.argv[1]}).json()

    achived = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user_id.get("name"), len(achived), len(todos)))
    [print("\t {}".format(c)) for c in achived]
