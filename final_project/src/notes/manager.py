notes_list = []

def add_note(title, content):
    notes_list.append({"title": title, "content": content})

def list_notes(return_list=False):
    if return_list:
        return notes_list
    for i, n in enumerate(notes_list, 1):
        print(f"{i}. {n['title']}: {n['content']}")

def search_notes(keyword):
    return [n for n in notes_list if keyword.lower() in n['title'].lower() or keyword.lower() in n['content'].lower()]
