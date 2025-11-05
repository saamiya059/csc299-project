import json
import uuid
from datetime import datetime
from pathlib import Path

class HabitManager:
    def __init__(self, data_file=None):
        self.data_file = Path(data_file or Path(__file__).parent / "data" / "habits.json")
        self.data_file.parent.mkdir(exist_ok=True)
        if not self.data_file.exists():
            self.data_file.write_text("[]")
        self.habits = self.load_habits()

    def load_habits(self):
        with open(self.data_file, "r") as f:
            return json.load(f)

    def save_habits(self):
        with open(self.data_file, "w") as f:
            json.dump(self.habits, f, indent=2)

    def add_habit(self, title, description="", tags=None):
        habit = {
            "id": uuid.uuid4().hex[:8],
            "title": title,
            "description": description,
            "tags": tags or [],
            "created": datetime.utcnow().isoformat() + "Z",
            "completed": False
        }
        self.habits.append(habit)
        self.save_habits()
        return habit

    def list_habits(self, tag=None):
        if tag:
            return [h for h in self.habits if tag in h["tags"]]
        return self.habits

    def mark_complete(self, habit_id):
        for h in self.habits:
            if h["id"] == habit_id:
                h["completed"] = True
                self.save_habits()
                return h
        return None
