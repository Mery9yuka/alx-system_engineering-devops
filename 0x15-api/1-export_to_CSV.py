#!/usr/bin/python3
"""extend the Python script in task 0 to export data in the CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    uRl = "https://jsonplaceholder.typicode.com/"
    uSer = requests.get(uRl + "users/{}".format(user_id)).json()
    user_name = uSer.get("username")
    todos_l = requests.get(uRl + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        input = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [input.writerow(
            [user_id, user_name, t.get("completed"), t.get("title")]
         ) for t in todos_l]
