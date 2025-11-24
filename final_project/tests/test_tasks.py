from tasks.manager import add_task, list_tasks, search_tasks

def test_add_and_search_task():
    add_task("Test Task", "Description")
    results = search_tasks("Test")
    assert any(r['title'] == "Test Task" for r in results)
