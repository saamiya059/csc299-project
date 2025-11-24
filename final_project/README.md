README.md
AI-Assisted Personal Knowledge and Task Manager
This project is my final software engineering assignment for CSC299. It is an AI-assisted Personal Knowledge Management System with tasks, notes, conversation memory, and some lightweight AI-powered summaries. The whole project was developed with ChatGPT as my main assistant, acting like a guide while I wrote, tested, and debugged the software.
The goal of the software is to give the user a simple command-line interface where they can add tasks, list them, add notes, manage them, summarize information, and keep track of small pieces of conversation context. Everything is organized into separate modules so each part stays clean and easy to test.
How to Run the Program
Make sure you activate the virtual environment for the project. On my machine, the command looks like this:
source ~/Documents/csc299-project/.venv/bin/activate
Once the venv is activated, go to the root of the big project folder:
cd ~/Documents/csc299-project
Set the Python import path so the program knows where to find the source files:
export PYTHONPATH=$(pwd)/final_project/src
Now you can run the main program with:
python final_project/main.py
This will start the Command Line Interface and show the menu of available commands.
How to Run the Tests
All tests are inside the final_project/tests folder. To run them:
pytest final_project/tests
If everything is set up correctly, you will see all tests passing.
Project Structure
The src folder contains all of your actual Python logic. Inside it there are three main submodules which follow the layout of the assignment:
agents contains the conversation memory class and the assistant manager functions.
notes contains the note manager, which handles storing and listing notes.
tasks contains the task manager, which handles adding and listing tasks.
The tests folder mirrors this structure and contains separate tests for each module.
The main.py file is the entry point and contains the command-line interface that lets the user interact with the system.
The video.txt file contains a link to the demonstration video for this project.
The SUMMARY.md file contains the explanation of my development process, including how I used AI and what challenges came up.
Requirements
Everything runs on Python 3.10 or higher. The only test dependency is pytest, which is automatically installed when setting up the project environment.
What This Software Does
This system lets the user enter commands to add tasks, store personal notes, view all saved information, and get small summaries from the AI assistant. The goal was not to build something huge but to build something clean, testable, and well structured. The program behaves the same each time it runs and keeps its logic separate so everything is easy to test and maintain.
Final Notes
This project was built step by step through conversation and debugging. Every fix, improvement, and structural change happened because of something I tested or broke and then corrected. The commit history shows the full evolution from an empty folder to a working system with tests and a clean CLI.
If you clone this project and follow the setup steps, everything should work exactly the same way it works for me.
