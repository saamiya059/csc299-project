from tasks.summarizer import summarize_task
from notes.summarizer import summarize_note

def summarize_item(item):
    if 'description' in item:
        return summarize_task(item)
    elif 'content' in item:
        return summarize_note(item)
    else:
        return "Unknown item type."
