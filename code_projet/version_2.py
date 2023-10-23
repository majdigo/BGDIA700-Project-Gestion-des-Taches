import datetime as dt
from collections import defaultdict


class Task:
    #Create a dictionary to store tasks
    task_dict = defaultdict(lambda: {'description': '', 'status': 'en cours'})

    def __init__(self):
        self.nom = ''
        self.description = ''
        #initialize the task dictionary by each call of the class
        Task.reset_dict()

    @classmethod
    def add_task(cls, task, description=None):
        """_summary_

        Args:
            task (_type_): _description_
            description (_type_, optional): _description_. Defaults to None.

        Raises:
            ValueError: _description_
        """
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
        #complete one or more tasks
        for arg in args:
            task_info = cls.task_dict.get(arg)
            if task_info:
                task_info['status'] = 'terminée'

    @classmethod
    def delete_task(cls, *noms):
        #delete one or more tasks
        for nom in noms:
            cls.task_dict.pop(nom, None)

    @classmethod
    def display(cls):
        #display all tasks which are not completed
        task_names = [
                        task
                        for task, info in cls.task_dict.items()
                        if info['status'] == 'en cours'
                        ]
        print(task_names)

    @classmethod
    def reset_dict(cls):
        #reset the task dictionary
        cls.task_dict.clear()

    @classmethod
    def clear_all(cls):
        #clear all tasks
        cls.reset_dict()   

if __name__ =="__main__":
    task=Task()
    task.add_task('task1')
    print(task.task_dict)