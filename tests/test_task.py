from datetime import datetime
from code_projet.models import Task


def test_task_creation():
    task = Task("Test Title", "Test Description")
    assert task.title == "Test Title"
    assert task.description == "Test Description"
    assert isinstance(task.created_at, datetime)
    assert task.completed is False


def test_mark_as_complete():
    task = Task("Test Title", "Test Description")
    task.mark_as_complete()
    assert task.completed is True


def test_task_str_representation():
    task = Task("Test Title", "Test Description")
    assert str(task) == "Test Title - Test Description (En attente)"
    task.mark_as_complete()
    assert str(task) == "Test Title - Test Description (Terminée)"


def test_task_id_uniqueness():
    task1 = Task("Title1", "Description1")
    task2 = Task("Title2", "Description2")
    assert task1.id != task2.id


def test_task_created_at_order():
    task1 = Task("Title1", "Description1")
    task2 = Task("Title2", "Description2")
    assert task2.created_at >= task1.created_at
