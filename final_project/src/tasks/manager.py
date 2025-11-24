tasks_list = []

def add_task(title, description):
    tasks_list.append({"title": title, "description": description})

def list_tasks(return_list=False):
    if return_list:
        return tasks_list
    for i, t in enumerate(tasks_list, 1):
        print(f"{i}. {t['title']}: {t['description']}")

def search_tasks(keyword):
    return [t for t in tasks_list if keyword.lower() in t['title'].lower() or keyword.lower() in t['description'].lower()]
