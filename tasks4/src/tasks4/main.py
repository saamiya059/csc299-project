# tasks4/main.py
import os
from openai import OpenAI, OpenAIError  # <-- Import OpenAIError directly

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY is not set. Please set your OpenAI API key.")
        return 1  # non-zero exit code indicates failure

    client = OpenAI(api_key=api_key)

    descriptions = [
        """The user wants to build a small command-line helper tool that tracks
        daily study habits. The tool should let the user enter how long they
        studied, what subject they worked on, and whether they completed their
        goals for the day. The user wants an output report that summarizes
        the week in a simple text table.""",

        """This task involves designing a microservice that receives messages from
        an internal queue and reformats them into a structured JSON output.
        The service must validate message types, log errors, and expose a
        health-check endpoint to ensure it is running correctly."""
    ]

    summaries = []

    for text in descriptions:
        try:
            response = client.chat.completions.create(
                model="gpt-5-mini",
                messages=[
                    {"role": "system", "content": "Summarize the task as a short phrase."},
                    {"role": "user", "content": text},
                ]
            )
            summary = response.choices[0].message.content.strip()
            summaries.append(summary)
        except OpenAIError as e:
            print(f"Error calling OpenAI API: {e}")
            return 1

    print("Task summaries:")
    for s in summaries:
        print("-", s)

    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
