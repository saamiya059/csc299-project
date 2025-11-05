Prototype 1 — Habit Tracker: Add Habits
This document describes Prototype 1 of the Habit Tracker project for CSC299, focusing on Task 1: Adding Habits via a Command-Line Interface (CLI).
1. Overview
Prototype 1 demonstrates the ability to add habits using a Python command-line application. The prototype allows users to:
Create new habits with a title, description, and tags.
Store habits persistently in a JSON file.
Automatically assign a unique ID and timestamp to each habit.
This prototype lays the foundation for future functionality, such as listing, searching, and managing habits.
2. Folder Structure
tasks1/
├── data/           # Stores habits.json (created automatically)
├── main.py         # Entry point for CLI commands
├── cli.py          # Command-line interface logic
├── tasks.py        # HabitManager class for handling habits
└── README.md       # This file
Notes:
The data/ folder and habits.json file are automatically created when you first add a habit.
__pycache__/ may appear when running Python; it can be ignored or gitignored.
3. Habit Data Model
Each habit has the following fields:
Field	Description
id	Unique identifier (generated automatically)
title	Name of the habit
description	Optional description/frequency
tags	Optional tags to categorize habits
created	Timestamp when the habit was added
completed	Boolean flag (default False)
All habits are stored in JSON format in tasks1/data/habits.json. Example:
[
  {
    "id": "c9cc98a3",
    "title": "Drink Water",
    "description": "3 times per day",
    "tags": ["morning", "health"],
    "created": "2025-10-27T18:04:21.877762Z",
    "completed": false
  }
]
4. Requirements
Python 3.x
No external libraries required
5. Usage Instructions
Open a terminal, navigate to the repository root (csc299-project), and run the following commands:
Add a Habit
python3 tasks1/main.py add "Drink Water" -d "3 times per day" -t morning,health
python3 tasks1/main.py add "Meditate" -d "10 minutes" -t evening,mental
Example Output:
Added habit:
[c9cc98a3] Drink Water
  3 times per day
  tags: morning, health
  created: 2025-10-27T18:04:21.877762Z
  completed: False
Each new habit is automatically saved to tasks1/data/habits.json.
Notes
Run each command separately to avoid duplicate outputs.
Make sure you are running the command from the repo root (csc299-project).
The data/ folder and habits.json file are created automatically.
6. Next Steps
Prototype 1 focuses solely on adding habits. Future prototypes (Prototype 2 and beyond) will expand functionality to:
List all habits
Filter habits by tags
Search habits by title, description, or tags
Mark habits as completed or delete them
7. AI Assistance Disclosure
Some parts of this project, including the Habit Tracker CLI prototype and README documentation, were assisted by an AI tool (ChatGPT).
The AI helped with:
Generating prototype code structure
Troubleshooting imports and CLI commands
Writing and formatting the README documentation
All code was tested, run, and fully understood by the student, and the final submission reflects the student’s own learning and adaptations.