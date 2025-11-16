from openai import OpenAI

# Initialize OpenAI client
client = OpenAI()

# Paragraph-length task descriptions
descriptions = [
    """I’m trying to clean up the shared office area before everyone comes back for the new semester. 
    There are piles of old papers that need to be sorted, labeled, and either recycled or scanned 
    so they can be stored digitally. The whole point is to make the space easier to use and less cluttered.""",
    """Our student group is planning a small event for next month. We need to reserve a room, 
    set up a simple sign-up form, spread the word so people know about it, and make sure a few volunteers 
    can help run things. The main goal is to keep everything organized so the event goes smoothly."""
]

def summarize_task(paragraph: str) -> str:
    """Send a paragraph to GPT-5-mini and return a short summary phrase."""
    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[{
            "role": "user",
            "content": f"Summarize this task as a short phrase:\n{paragraph}"
        }]
    )
    return response.choices[0].message["content"].strip()

def main():
    print("\nTask 4 Summaries:\n")
    for i, paragraph in enumerate(descriptions, start=1):
        print(f"{i}. {summarize_task(paragraph)}")

# Optional: allow running directly with python
if __name__ == "__main__":
    main()
