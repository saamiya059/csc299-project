import pytest
from agents.conversation_memory import ConversationMemory
from agents.assistant_manager import summarize_item

def test_conversation_memory():
    cm = ConversationMemory()
    cm.add("Hello")
    cm.add("Hi there")
    formatted = cm.format()
    assert formatted[0]["role"] == "user"
    assert formatted[1]["role"] == "assistant"

def test_summarize_item_task():
    task = {"title": "Test", "description": "Do something important"}
    summary = summarize_item(task)
    assert "Task Summary" in summary

def test_summarize_item_note():
    note = {"title": "Note", "content": "Write content"}
    summary = summarize_item(note)
    assert "Note Summary" in summary
