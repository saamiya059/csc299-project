from pathlib import Path
import json
import uuid
from datetime import datetime

DEFAULT_FILENAME = Path(__file__).parent / "data" / "habits.json"

class HabitManager:
    def __init__(self, data_path=DEFAULT_FILENAME):
        self.data_path = Path(data_path)
        # create data folder if it doesn't exist
        self.data_path.parent.mkdir(parents=True, exist_ok=True)
        # initialize habits.json if it doesn't exist
        if not self.data_path.exists():
            self._write([])
        self.habits = self._read()

    def _read(self):
        try:
            with self.data_path.open("r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []

    def _write(self, habits):
        with self.data_path.open("w", encoding="utf-8") as f:
            json.dump(habits, f, indent=2, ensure_ascii=False)

    def _save(self):
        self._write(self.habits)

    def add_habit(self, title, description="", tags=None):
        if tags is None:
            tags = []
        habit = {
            "id": uuid.uuid4().hex[:8],
            "title": title,
            "description": description,
            "tags": tags,
            "created": datetime.utcnow().isoformat() + "Z",
            "completed": False
        }
        self.habits.append(habit)
        self._save()
        return habit

    def list_habits(self, tag=None):
        if tag:
            return [h for h in self.habits if tag in h.get("tags", [])]
        return list(self.habits)

    def search_habits(self, query):
        q = query.lower()
        results = []
        for h in self.habits:
            if q in h.get("title", "").lower() or q in h.get("description", "").lower():
                results.append(h)
            else:
                for tag in h.get("tags", []):
                    if q in tag.lower():
                        results.append(h)
                        break
        return results
