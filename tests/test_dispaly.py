
import os
import sys
import pytest
import tkinter as tk

# Obtenir le répertoire dans lequel se trouve le fichier courant
current_directory = os.path.dirname(os.path.realpath(__file__))

# Obtenir le répertoire racine du projet
project_root = os.path.abspath(os.path.join(current_directory, ".."))

# Ajouter le répertoire racine du projet au chemin de recherche des modules
sys.path.append(project_root)


from code_projet.model_task import Task
from code_projet.model_display import TaskManagerApp


task = Task()
root = tk.Tk()
app = TaskManagerApp(root, task)


def test_add_task():
    # Reset list
    app.task_list.reset_dict()
    # Add tasks and update lists
    app.task_list.add_task('task_name', 'description')
    app.update_task_listbox()
    # Check the results
    sub_item_ids = app.task_listbox.get_children()
    item = app.task_listbox.item(sub_item_ids)
    assert item['values'][0] == 'task_name'
    assert item['values'][1] == 1
    assert item['values'][2] == 'description'


def test_delete_task():
    # Reset list
    app.task_list.reset_dict()
    # Add tasks and update lists
    app.task_list.add_task('Test Task', 'description1')
    app.update_task_listbox()
    # Delete tasks and update lists

    app.task_list.delete_task('Test Task')
    app.update_task_listbox()

    # Check the results
    assert len(app.task_list.task_dict) == 0


def test_add_description_into_task():
    # Reset list
    app.task_list.reset_dict()
    # Add tasks and update lists
    app.task_list.add_task('Test Task')
    app.update_task_listbox()
    # test the content of the task
    assert app.task_list.task_dict['Test Task']['description'] is None

    # Add description into the task
    app.task_list.task_dict['Test Task']['description'] = 'description2'
    app.update_task_listbox()

    # Check the results
    assert app.task_list.task_dict['Test Task']['description'] == 'description2'


def test_complete_task():
    # Reset list
    app.task_list.reset_dict()
    # Add tasks and update lists
    app.task_list.add_task('Test Task')
    app.update_task_listbox()
    # test the status of the task
    assert app.task_list.task_dict['Test Task']['status'] == 'en cours'

    # complete the task
    app.task_list.complete_task('Test Task')

    # Check the results
    assert app.task_list.task_dict['Test Task']['status'] == 'terminée'


if __name__ == "__main__":
    pytest.main()