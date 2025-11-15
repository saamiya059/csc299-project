import argparse
from tasks3.tasks import HabitManager


manager = HabitManager()

def print_habit(h):
    status = "✓" if h["completed"] else "✗"
    print(f'{h["id"]}: {h["title"]} [{status}] - {h["description"]} (tags: {",".join(h["tags"])})')

def main():
    parser = argparse.ArgumentParser(prog="tasks3")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("title")
    add_parser.add_argument("-d", "--description", default="")
    add_parser.add_argument("-t", "--tags", default="", help="comma separated tags")

    list_parser = subparsers.add_parser("list")

    complete_parser = subparsers.add_parser("complete")
    complete_parser.add_argument("habit_id")

    args = parser.parse_args()

    if args.command == "add":
        tags = [t.strip() for t in args.tags.split(",")] if args.tags else []
        habit = manager.add_habit(args.title, args.description, tags)
        print("Added habit:")
        print_habit(habit)

    elif args.command == "list":
        habits = manager.list_habits()
        if not habits:
            print("No habits found.")
        for h in habits:
            print_habit(h)

    elif args.command == "complete":
        habit = manager.mark_complete(args.habit_id)
        if habit:
            print("Marked as complete:")
            print_habit(habit)
        else:
            print(f"Habit {args.habit_id} not found.")

if __name__ == "__main__":
    main()