import tempfile
from tasks3.src.tasks import HabitManager

def test_add_habit():
    with tempfile.NamedTemporaryFile() as tmp:
        manager = HabitManager(tmp.name)
        habit = manager.add_habit("Test Habit", "desc", ["tag1"])
        assert habit["title"] == "Test Habit"
        assert habit["completed"] is False

def test_mark_complete():
    with tempfile.NamedTemporaryFile() as tmp:
        manager = HabitManager(tmp.name)
        habit = manager.add_habit("Complete Me")
        manager.mark_complete(habit["id"])
        assert habit["completed"] is True
