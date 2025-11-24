from tasks.manager import add_task, list_tasks, search_tasks
from notes.manager import add_note, list_notes, search_notes
from agents.assistant_manager import summarize_item
from agents.conversation_memory import ConversationMemory

conversation = ConversationMemory()

def main():
    print("Welcome to your AI-assisted PKMS & Task Manager!")
    
    while True:
        cmd = input("\nEnter command (help for options): ").strip().lower()
        
        if cmd == "exit":
            print("Exiting CLI. Goodbye!")
            break
        elif cmd == "help":
            print("Commands: add_task, list_tasks, search_task, add_note, list_notes, search_note, summarize_task, summarize_note, exit")
        elif cmd == "add_task":
            title = input("Task title: ")
            desc = input("Task description: ")
            add_task(title, desc)
            conversation.add(f"Task added: {title}")
            print("Task added!")
        elif cmd == "list_tasks":
            list_tasks()
        elif cmd == "search_task":
            keyword = input("Keyword: ")
            results = search_tasks(keyword)
            for t in results:
                print(t)
        elif cmd == "add_note":
            title = input("Note title: ")
            content = input("Note content: ")
            add_note(title, content)
            conversation.add(f"Note added: {title}")
            print("Note added!")
        elif cmd == "list_notes":
            list_notes()
        elif cmd == "search_note":
            keyword = input("Keyword: ")
            results = search_notes(keyword)
            for n in results:
                print(n)
        elif cmd == "summarize_task":
            for t in list_tasks(return_list=True):
                print(summarize_item(t))
        elif cmd == "summarize_note":
            for n in list_notes(return_list=True):
                print(summarize_item(n))
        else:
            print("Unknown command. Type 'help' for options.")
