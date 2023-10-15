import datetime as dt


class Task:
    task_dict = {}  # Create a task dictionary to store information

    def __init__(self):
        """_summary_

        Args:
            nom (_type_): the nom of the task
            description (_type_): the description of the task
            statuts (str, optional): the status of task,default is 'en cours'.
        """
        self.nom = ''
        self.description = ''
        self.statuts = 'en cours'

    @classmethod
    def add_task(cls, task, description=None, date=None):
        """_summary_
            cls:class
            task:the name of the task
            description: the description of the task
        """
        "# TODO: add the task to the dictionary#"
        if task in cls.task_dict.keys():
            raise ValueError('The task already exists')
        else:
            description = description if description is not None else ''
            date = date if date is not None else dt.datetime.now().strftime("%Y-%m-%d")
            task_info = {
                'nom': task,
                'description': description,
                'statuts': 'en cours',
                'date': date
            }
            cls.task_dict[task] = task_info                 

    @classmethod
    # change the status of the task to 'terminée' 
    def complete_task(cls, *args):
        for arg in args:
            if arg in cls.task_dict.keys():
                cls.task_dict[arg]['statuts'] = 'terminée'

    @classmethod
    #delete the task from the dictionary
    def delete_task(cls, *noms):
        for nom in noms:
            del cls.task_dict[nom]
    
    @classmethod
    # display the task names whose statuts are 'en cours'
    def display(cls):
        task_names = []
        for key in cls.task_dict.keys():
            if cls.task_dict[key]['statuts'] is not None and cls.task_dict[key]['statuts'] == 'en cours':
                task_names.append(cls.task_dict[key]['nom'])
        print (task_names)    
  
        