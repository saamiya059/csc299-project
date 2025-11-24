# AI-Assisted Personal Knowledge and Task Manager

This project is my final software engineering assignment for **CSC299**.  
It is an AI-assisted Personal Knowledge Management System with tasks, notes, conversation memory, and lightweight AI summaries. The entire project was developed with ChatGPT as my main assistant, acting like a guide while I wrote, tested, and debugged the software.

The goal of the software is to provide a simple command-line interface where the user can:

- Add and list tasks  
- Add and list notes  
- Summarize content using the assistant  
- Store small pieces of conversation context  
- Keep everything organized into clean, testable modules  

---

## ⭐ How to Run the Program

### 1. Activate the virtual environment

```bash
source ~/Documents/csc299-project/.venv/bin/activate
```

### 2. Go to the main project folder

```bash
cd ~/Documents/csc299-project
```

### 3. Set the Python import path

```bash
export PYTHONPATH=$(pwd)/final_project/src
```

### 4. Run the program

```bash
python final_project/main.py
```

This will launch the CLI menu.

---

## 🧪 How to Run the Tests

All tests live in `final_project/tests`.

Run them with:

```bash
pytest final_project/tests
```

If everything is configured correctly, all tests should pass.

---

## 📁 Project Structure

```
final_project/
│
├── src/
│   ├── agents/
│   │   ├── conversation_memory.py
│   │   └── assistant_manager.py
│   │
│   ├── notes/
│   │   └── manager.py
│   │
│   └── tasks/
│       └── manager.py
│
├── tests/
│   ├── test_agents.py
│   ├── test_notes.py
│   └── test_tasks.py
│
├── main.py
├── SUMMARY.md
└── video.txt
```

- **agents** → Conversation memory + assistant summary logic  
- **notes** → Add/store/list notes  
- **tasks** → Task management  
- **main.py** → Entry point + command-line interface  
- **tests** → Unit tests for each module  

---

## 📦 Requirements

- Python **3.10+**  
- `pytest` (installed when the project environment is set up)

---

## 💡 What This Software Does

This system gives the user a small but well-organized PKMS + Task Manager they can interact with through a CLI.  
It allows users to store tasks, notes, summaries, and conversational snippets. The focus wasn’t on making a huge app, but on making something:

- Clean  
- Testable  
- Easy to maintain  
- Easy to understand from reading the code  

All logic is separated into modules so tests can run independently.

---

## 📝 Final Notes

This project was built step by step through constant conversation, debugging, and trial-and-error.  
Every improvement happened because of something I tested, broke, fixed, or redesigned.

The GitHub commit history shows the entire evolution — from an empty folder to a working system with tests and a full CLI.

If you clone the repo and follow the setup steps, everything should run exactly as it does on my machine.

---
