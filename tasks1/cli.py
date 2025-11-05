import argparse
from tasks import HabitManager
import json
import sys

def pretty_print(habit):
    print(f"[{habit['id']}] {habit['title']}")
    if habit.get("description"):
        print("  " + habit["description"])
    if habit.get("tags"):
        print("  tags:", ", ".join(habit["tags"]))
    print("  created:", habit.get("created"))
    print("  completed:", habit.get("completed"))
    print()

def main(argv=None):
    parser = argparse.ArgumentParser(prog="habits", description="Habit Tracker CLI")
    sub = parser.add_subparsers(dest="cmd")

    add = sub.add_parser("add", help="Add a new habit")
    add.add_argument("title", help="Name of the habit")
    add.add_argument("-d", "--description", help="Description/frequency", default="")
    add.add_argument("-t", "--tags", help="Comma-separated tags", default="")

    listp = sub.add_parser("list", help="List habits")
    listp.add_argument("-t", "--tag", help="Filter by tag", default=None)
    listp.add_argument("--json", action="store_true", help="Output JSON")

    search = sub.add_parser("search", help="Search habits by text or tag")
    search.add_argument("query", help="Query to search")

    args = parser.parse_args(argv)
    hm = HabitManager()

    if args.cmd == "add":
        tags = [t.strip() for t in args.tags.split(",")] if args.tags else []
        habit = hm.add_habit(args.title, args.description, tags)
        print("Added habit:")
        pretty_print(habit)

    elif args.cmd == "list":
        habits = hm.list_habits(tag=args.tag)
        if args.json:
            print(json.dumps(habits, indent=2))
        else:
            if not habits:
                print("No habits found.")
            for h in habits:
                pretty_print(h)

    elif args.cmd == "search":
        results = hm.search_habits(args.query)
        if not results:
            print("No results.")
        for h in results:
            pretty_print(h)

    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
