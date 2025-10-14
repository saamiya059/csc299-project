import json

tasks = []

def add_task(task):
    tasks.append(task)
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

def list_tasks():
    print("Tasks:")
    for t in tasks:
        print("-", t)

add_task("Finish CSC299 prototype")
list_tasks()
