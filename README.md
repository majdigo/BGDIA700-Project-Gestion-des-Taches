# BGDIA700 Project Gestion des Tâches

Ce projet consiste à créer une bibliothèque Python pour la gestion des tâches personnelles (To-Do List).

## Structure du Projet

BGDIA700-Project-Gestion-des-Taches/
├── .gitignore # Liste des fichiers/répertoires à ignorer pour Git
├── Arboresence.txt # Description de l'arborescence du projet
├── LICENSE # Licence du projet
├── README.md # Ce fichier, avec la documentation initiale du projet
├── requirements.txt # Dépendances Python du projet
├── setup.py # Script pour empaqueter le projet en tant que module Python
├── .github/
│ └── workflows/ # Configuration pour GitHub Actions (CI/CD)
├── code_projet/
│ ├── cli.py # Interface en ligne de commande
│ ├── exceptions.py # Exceptions personnalisées pour le projet
│ ├── main.py # Point d'entrée principal du projet
│ ├── models.py # Définitions des classes Task et TaskList
│ └── init.py # Fichier pour faire du répertoire un package Python
├── docs/ # Documentation du projet (par exemple, avec Sphinx)
├── logs/
│ └── log.log # Fichier de logs pour l'application
└── tests/
├── task_list.py # Tests pour la classe TaskList
├── test_models.py # Tests pour les classes du fichier models.py
└── init.py # Fichier pour faire du répertoire un package Python


## Comment commencer

1. Clonez ce dépôt.
2. Installez les dépendances en utilisant `pip install -r requirements.txt`.
3. Exécutez `main.py` pour démarrer l'application.

## Contribution

Si vous souhaitez contribuer au projet, veuillez suivre les directives suivantes :

1. Créez une nouvelle branche pour votre fonctionnalité ou correction.
2. Faites vos modifications et assurez-vous de tester votre code.
3. Ouvrez une Pull Request pour fusionner votre branche dans la branche `main`.

## Licence

Ce projet est sous licence MIT. Pour plus de détails, voir le fichier [LICENSE](LICENSE).
