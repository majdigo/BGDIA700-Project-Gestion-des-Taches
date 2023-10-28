"""
This is a sample module for the code_projet package.

This module contains various functions and classes related to tasks.
"""
import datetime as dt
from collections import defaultdict
import logging

# Create a logger
logging.basicConfig(filename='myapp.log', level=logging.INFO)


class Task:
    """
    This class represents a task manager.

    Attributes:
        task_dict (defaultdict): A dictionary to store tasks.
        task_counter (int): A counter for generating task IDs.
    """

    # Create a dictionary to store tasks
    task_dict = defaultdict(lambda: {'ID': None,
                                     'description': '',
                                     'status': 'en cours'})
    task_counter = 1

    def __init__(self):
        """Initialize a task object."""
        self.nom = ''
        self.description = ''
        # initialize the task dictionary by each call of the class
        Task.reset_dict()

    @classmethod
    def add_task(cls, task, description=None):
        """
        Add a new task to the task manager.

        Args:
            task (str): The name of the task.
            description (str, optional): The description of the task.

        Raises:
            ValueError: If the task already exists.
        """
        if task in cls.task_dict:
            raise ValueError('The task already exists')
        task_info = {
            'ID': cls.task_counter,
            'description': description,
            'status': 'en cours',
            'date': dt.datetime.now().strftime("%Y-%m-%d")
        }
        cls.task_dict[task].update(task_info)
        cls.task_counter += 1
        # Ajouter la journalisation
        logging.info(
                        f"Added task: {task}, "
                        f"ID: {task_info['ID']}, "
                        f"Description: {description}"
            )

    @classmethod
    def complete_task(cls, *args):
        """
        Mark one or more tasks as completed.

        Args:
            *args (str): The names of the tasks to mark as completed.
        """
        # complete one or more tasks
        for arg in args:
            task_info = cls.task_dict.get(arg)
            if task_info:
                task_info['status'] = 'terminée'
        # Ajouter la journalisation
        logging.info(f"Completed task(s): {', '.join(args)}")

    @classmethod
    def delete_task(cls, *noms):
        """
        Delete one or more tasks.

        Args:
            *noms (str): The names of the tasks to delete.
        """
        # delete one or more tasks
        for nom in noms:
            cls.task_dict.pop(nom, None)
        # Ajouter la journalisation
        logging.info(f"Deleted task(s): {', '.join(noms)}")

    @classmethod
    def display(cls):
        """Display all tasks that are not completed."""
        # display all tasks which are not completed
        task_names = [
                        task
                        for task, info in cls.task_dict.items()
                        if info['status'] == 'en cours'
                        ]
        print(task_names)

    @classmethod
    def reset_dict(cls):
        """Reset the task dictionary."""
        # reset the task dictionary
        cls.task_dict.clear()
        cls.task_counter = 1

    @classmethod
    def clear_all(cls):
        """Clear all tasks."""
        # clear all tasks
        cls.reset_dict()


if __name__ == "__main__":
    # Configurer la journalisation vers le fichier et la console
    logging.basicConfig(
        filename='myapp.log',
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    console_handler.setFormatter(
        logging.
        Formatter('%(asctime)s -%(name)s - %(levelname)s - %(message)s')
    )
    logging.getLogger('').addHandler(console_handler)
