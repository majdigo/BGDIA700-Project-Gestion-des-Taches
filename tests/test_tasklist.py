from code_projet.models import TaskList, Task


def test_add_task():
    task_list = TaskList()
    task_list.add_task("Test Title", "Test Description")

    assert len(task_list.tasks) == 1
    assert isinstance(task_list.tasks[0], Task)
    assert task_list.tasks[0].title == "Test Title"
    assert task_list.tasks[0].description == "Test Description"


def test_remove_task():
    task_list = TaskList()
    task_list.add_task("Test Title", "Test Description")

    task_id = task_list.tasks[0].id
    task_list.remove_task(task_id)

    assert len(task_list.tasks) == 0


def test_complete_task():
    task_list = TaskList()
    task_list.add_task("Test Title", "Test Description")

    task_id = task_list.tasks[0].id
    task_list.complete_task(task_id)

    assert task_list.tasks[0].completed == True
