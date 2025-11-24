tasks4: OpenAI Chat Completions API task summarizer
tasks4 is a Python package that demonstrates using the OpenAI Chat Completions API (GPT-5-mini) to summarize paragraph-length task descriptions into short, concise phrases. It allows you to feed multiple descriptions and get independent summaries for each.
Features
Summarizes multiple paragraph-length descriptions of tasks.
Uses OpenAI GPT-5-mini model.
Simple command-line interface.
Handles API errors gracefully.
Installation
Make sure you have Python 3.13+ and uv installed.
Clone the repository and install the package in editable mode:
uv pip install -e tasks4
Setup
Set your OpenAI API key as an environment variable:
export OPENAI_API_KEY="your_openai_api_key_here"
Replace "your_openai_api_key_here" with your actual OpenAI API key.
Usage
Run the package using uv:
uv run tasks4
Example output:
Task summaries:
- CLI study habit tracker: record daily study duration, subject, and goal completion; produce a weekly summary table.
- Queue-to-JSON microservice: message validation, error logging, and health-check
Contributing
This project is a standalone experiment. Contributions are welcome to improve functionality or add features, like reading task descriptions from a file or supporting more models.