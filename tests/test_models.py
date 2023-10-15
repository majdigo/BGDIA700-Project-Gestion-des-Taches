
import sys
import os

# Obtenir le répertoire dans lequel se trouve le fichier courant
current_directory = os.path.dirname(os.path.realpath(__file__ ))

# Obtenir le répertoire racine du projet
project_root = os.path.abspath(os.path.join(current_directory, ".."))

# Ajouter le répertoire racine du projet au chemin de recherche des modules
sys.path.append(project_root)

from code_projet.version_2 import Task
test=Task()

test.add_task('test_1')
test.add_task('test_2')
test.add_task('test_3')
test.complete_task('test_2')
test.display()
print(test.task_dict)