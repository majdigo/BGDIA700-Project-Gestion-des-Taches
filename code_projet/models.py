from datetime import datetime
from typing import List


class Task:
    """Classe représentant une tâche individuelle."""

    def __init__(self, title: str, description: str):
        self.id = id(self)  # Utilisation de l'ID unique pour l'identification
        self.title = title
        self.description = description
        self.created_at = datetime.now()
        self.completed = False

    def mark_as_complete(self):
        """Marquer la tâche comme terminée."""
        self.completed = True

    def __str__(self):
        status = 'Completed' if self.completed else 'Pending'
        return f"{self.title} - {self.description} ({status})"


class TaskList:
    """Classe représentant une liste de tâches."""

    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, title: str, description: str):
        """Ajouter une nouvelle tâche à la liste."""
        task = Task(title, description)
        self.tasks.append(task)

    def remove_task(self, task_id: int):
        """Supprimer une tâche de la liste en utilisant son ID."""
        self.tasks = [task for task in self.tasks if task.id != task_id]

    def complete_task(self, task_id: int):
        """Marquer une tâche comme terminée en utilisant son ID."""
        for task in self.tasks:
            if task.id == task_id:
                task.mark_as_complete()

    def display_tasks(self):
        """Afficher toutes les tâches."""
        for task in self.tasks:
            print(task)
