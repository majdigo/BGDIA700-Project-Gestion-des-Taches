import datetime as dt
from collections import defaultdict


class Task:
    task_dict = defaultdict(lambda: {'description': '', 'status': 'en cours'})

    def __init__(self):
        self.nom = ''
        self.description = ''
        Task.reset_dict()

    @classmethod
    def add_task(cls, task, description=None):
        if task in cls.task_dict:
            raise ValueError('The task already exists')  
        task_info = {
            'description': description,
            'status': 'en cours',
            'date': dt.datetime.now().strftime("%Y-%m-%d")
        }
        cls.task_dict[task].update(task_info)

    @classmethod
    def complete_task(cls, *args):
        for arg in args:
            task_info = cls.task_dict.get(arg)
            if task_info:
                task_info['status'] = 'terminée'

    @classmethod
    def delete_task(cls, *noms):
        for nom in noms:
            cls.task_dict.pop(nom, None)

    @classmethod
    def display(cls):
        task_names = [
                        task
                        for task, info in cls.task_dict.items()
                        if info['status'] == 'en cours'
                        ]
        print(task_names)

    @classmethod
    def reset_dict(cls):
        cls.task_dict.clear()

    @classmethod
    def clear_all(cls):
        cls.reset_dict()   
