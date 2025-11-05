import argparse
from .tasks import HabitManager


def main():
    parser = argparse.ArgumentParser(description="Habit Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add habit
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("title")
    add_parser.add_argument("-d", "--description", default="")
    add_parser.add_argument("-t", "--tags", default="", help="Comma-separated tags")

    # List habits
    list_parser = subparsers.add_parser("list")
    list_parser.add_argument("-t", "--tag", default=None, help="Filter by tag")

    # Complete habit
    complete_parser = subparsers.add_parser("complete")
    complete_parser.add_argument("id", help="ID of habit to mark complete")

    args = parser.parse_args()
    manager = HabitManager()

    if args.command == "add":
        tags = [t.strip() for t in args.tags.split(",")] if args.tags else []
        habit = manager.add_habit(args.title, args.description, tags)
        print(f"Added habit:\n[{habit['id']}] {habit['title']}\n  {habit['description']}\n  tags: {', '.join(habit['tags'])}\n  created: {habit['created']}\n  completed: {habit['completed']}")

    elif args.command == "list":
        habits = manager.list_habits(args.tag)
        for h in habits:
            print(f"[{h['id']}] {h['title']}\n  {h['description']}\n  tags: {', '.join(h['tags'])}\n  created: {h['created']}\n  completed: {h['completed']}")

    elif args.command == "complete":
        habit = manager.mark_complete(args.id)
        if habit:
            print(f"Habit marked complete: [{habit['id']}] {habit['title']}")
        else:
            print("Habit ID not found")
