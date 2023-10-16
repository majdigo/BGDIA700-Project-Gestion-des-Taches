import argparse
from code_projet.models import TaskList


def main():
    """
    Point d'entrée principal pour l'interface CLI de la bibliothèque de gestion des tâches.
    """
    parser = argparse.ArgumentParser(description="Gestion des Tâches - CLI")

    # Création de sous-parsers pour chaque commande
    subparsers = parser.add_subparsers(dest="command")

    # Sous-parser pour ajouter une tâche
    add_task_parser = subparsers.add_parser(
        "add", help="Ajoute une nouvelle tâche à la liste.")
    add_task_parser.add_argument("name", type=str, help="Nom de la tâche.")
    add_task_parser.add_argument(
        "description", type=str, help="Description de la tâche.")

    # Sous-parser pour marquer une tâche comme terminée
    complete_task_parser = subparsers.add_parser(
        "complete", help="Marque une tâche comme terminée.")
    complete_task_parser.add_argument(
        "name", type=str, help="Nom de la tâche à marquer comme terminée.")

    # Sous-parser pour supprimer une tâche
    remove_task_parser = subparsers.add_parser(
        "remove", help="Supprime une tâche de la liste.")
    remove_task_parser.add_argument(
        "name", type=str, help="Nom de la tâche à supprimer.")

    # Sous-parser pour afficher toutes les tâches
    subparsers.add_parser("display", help="Affiche toutes les tâches.")

    args = parser.parse_args()

    # Instance de la liste de tâches
    task_list = TaskList()

    # Exécution des commandes en fonction des arguments
    if args.command == "add":
        task_list.add_task(args.name, args.description)
        print(f"La tâche '{args.name}' a été ajoutée avec succès!")
    elif args.command == "complete":
        task_list.complete_task(args.name)
        print(f"La tâche '{args.name}' a été marquée comme terminée!")
    elif args.command == "remove":
        task_list.remove_task(args.name)
        print(f"La tâche '{args.name}' a été supprimée!")
    elif args.command == "display":
        tasks = task_list.display_tasks()
        for task in tasks:
            print(task)


if __name__ == "__main__":
    main()
