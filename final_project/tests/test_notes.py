from notes.manager import add_note, list_notes, search_notes

def test_add_and_search_note():
    add_note("Test Note", "Some content")
    results = search_notes("Test")
    assert any(n['title'] == "Test Note" for n in results)
