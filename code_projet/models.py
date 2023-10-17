from datetime import datetime
from typing import List


class Task:
    """
    Représente une tâche individuelle.

    Attributs:
        id (int): Identifiant unique pour la tâche.
        title (str): Titre de la tâche.
        description (str): Brève description de la tâche.
        created_at (datetime): Date et heure de création de la tâche.
        completed (bool): Indique si la tâche est terminée ou non.
    """

    def __init__(self, title: str, description: str):
        """
        Initialise la tâche avec un titre et une description.

        Args:
            title (str): Titre de la tâche.
            description (str): Description de la tâche.
        """
        self.id = id(self)
        self.title = title
        self.description = description
        self.created_at = datetime.now()
        self.completed = False

    def mark_as_complete(self):
        """Marque la tâche comme étant terminée."""
        self.completed = True

    def __str__(self):
        """
        Renvoie une représentation string de la tâche.

        Returns:
            str: Représentation de la tâche (titre, description et statut)
        """
        status = 'Terminée' if self.completed else 'En attente'
        return f"{self.title} - {self.description} ({status})"


class TaskList:
    """
    Représente une liste de tâches.

    Attributs:
        tasks (List[Task]): Liste des tâches.
    """

    def __init__(self):
        """Initialise une liste de tâches vide."""
        self.tasks: List[Task] = []

    def add_task(self, title: str, description: str):
        """
        Ajoute une nouvelle tâche à la liste.

        Args:
            title (str): Titre de la tâche.
            description (str): Description de la tâche.
        """
        task = Task(title, description)
        self.tasks.append(task)

    def remove_task(self, task_id: int):
        """
        Supprime une tâche de la liste en utilisant son ID.

        Args:
            task_id (int): ID de la tâche à supprimer.
        """
        self.tasks = [task for task in self.tasks if task.id != task_id]

    def complete_task(self, task_id: int):
        """
        Marque une tâche comme terminée en utilisant son ID.

        Args:
            task_id (int): ID de la tâche à marquer comme terminée.
        """
        for task in self.tasks:
            if task.id == task_id:
                task.mark_as_complete()

    def display_tasks(self):
        """Affiche toutes les tâches dans la console."""
        for task in self.tasks:
            print(task)
