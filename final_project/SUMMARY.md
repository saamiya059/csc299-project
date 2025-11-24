This project honestly became way more of a journey than I expected. When I started, I thought I’d just write some code, pass some tests, and call it a semester. Instead, it turned into a full detective mission where I was fighting my own file paths, virtual environments, and VS Code yelling at me about missing imports even though the files were literally right there. The funny part? Most of the “progress” didn’t happen in code at first  it happened in ChatGPT.

Development Process (aka: me vs. Python)
I used only ChatGPT / OpenAI tools to build this entire project. No GitHub Copilot, no fancy IDE assistants, nothing magical generating entire files for me. Everything was through ChatGPT conversations — planning, debugging, asking “why is this not working,” and then asking the same question again five minutes later.
Most of my planning happened directly in ChatGPT. I didn’t have separate design documents; instead, ChatGPT basically was the planning document. I’d come in saying something like: “Okay, I need this PKMS system to actually run,” or “Why does pytest hate me today,” or “How do I structure this folder so VS Code stops fighting me?” And ChatGPT would walk me through what I needed step-by-step.
Sometimes I would think I understood, then I’d break something, then I would go back and ask again  which I guess is still part of the design process. So yes, the design evolved through conversations, but it still counts as planning. I promise.

What Worked
The number one thing that worked was using ChatGPT like a coding mentor sitting next to me. I didn’t have to wait for office hours, and I didn’t feel stupid asking “what even is PYTHONPATH and why does it ruin my life.” It helped me:
Create the file structure correctly
Write the classes logically
Understand what tests expected
Fix broken imports
Fix my virtual environment setup
Run pytest correctly without launching my entire CLI by mistake
Make VS Code stop screaming with Pylance errors
Confirm my program actually behaves like the assignment wanted
Write the CLI
Keep the code organized so it didn’t turn into spaghetti
Every time I hit a wall, ChatGPT was the thing pushing me through it. Sometimes gently. Sometimes roasting my command-line mistakes. Either way, it worked.
What DIDN’T Work (aka: my bloopers)
Let me be very honest: a lot didn’t work the first time.
I kept activating the wrong virtual environment.
At one point, I ran my CLI and tried typing pytest inside the CLI, wondering why it didn’t work.
I forgot how PYTHONPATH works at least four times.
My tests weren’t running because I was in the wrong directory.
VS Code was screaming about “missing imports” that absolutely existed.
I renamed folders and broke everything.
I kept thinking cli.py existed when it didn’t.
I kept switching between Desktop and the actual project folder like it was a part-time job.
All of this led to many “Okay ChatGPT I messed something up again” moments.
Despite all that, every mistake turned into a lesson. I now actually understand project structure, virtual environments, why tests need the correct root directory, and how Python modules resolve imports.
AI Use Transparency
I used ChatGPT to:
Explain concepts that were confusing in the moment
Guide me through structuring my PKMS system logically
Help debug errors that weren’t obvious
Improve clarity and naming in my code
Plan features and tests indirectly through conversation
Fix issues with pytest, file paths, and VS Code
Simplify and rewrite code when I got stuck
Keep me from losing my mind when things didn’t run
What I did not do:
I didn’t ask AI to generate entire files for me without understanding them
I didn’t copy-paste large blocks without reading
I didn’t outsource the whole project — I used AI as a helper, not a replacement for thinking
Final Reflection
Honestly, this project taught me more about real debugging than any previous assignment. I actually understand how Python package structure works now, and I learned how to use AI responsibly — not as a shortcut, but as a guide when I’m stuck. Most of all, I learned that development is messy, nonlinear, and full of moments where you swear you already fixed that folder path.
But in the end:
my code works, my tests pass, VS Code stopped crying, and I actually feel proud of this project.