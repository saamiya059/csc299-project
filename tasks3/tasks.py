import json
import os
import uuid

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "habits.json")


class HabitManager:
    def __init__(self):
        self.habits = self._load()

    def _load(self):
        if not os.path.exists(DATA_FILE):
            return []

        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    def _save(self):
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, "w") as f:
            json.dump(self.habits, f, indent=2)

    def add_habit(self, title, description, tags):
        new_habit = {
            "id": uuid.uuid4().hex[:8],
            "title": title,
            "description": description,
            "tags": tags,
            "completed": False,
        }
        self.habits.append(new_habit)
        self._save()
        return new_habit

    def list_habits(self):
        return self.habits

    def mark_complete(self, habit_id):
        for h in self.habits:
            if h["id"] == habit_id:
                h["completed"] = True
                self._save()
                return h
        return None
