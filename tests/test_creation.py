
import sys
import os

# Obtenir le répertoire dans lequel se trouve le fichier courant
current_directory = os.path.dirname(os.path.realpath(__file__ ))

# Obtenir le répertoire racine du projet
project_root = os.path.abspath(os.path.join(current_directory, ".."))

# Ajouter le répertoire racine du projet au chemin de recherche des modules
sys.path.append(project_root)
import io
import pytest
import random
from code_projet.version_2 import Task

test=Task()
def test_add_task():
    # Effacer tous les tâches dans dictionnaire
    test.reset_dict()  
    test.add_task('Task1', 'Description for Task1')
    assert 'Task1' in test.task_dict
    task_info = test.task_dict['Task1']
    assert task_info['description'] == 'Description for Task1'
    assert task_info['status'] == 'en cours'

    
def test_complete_task():
# Effacer tous les tâches dans dictionnaire
    test.reset_dict()  
    test.add_task('Task3', 'Description for Task3')
    test.complete_task('Task3')
    assert Task.task_dict['Task3']['status'] == 'terminée'

def test_delete_task():
# Effacer tous les tâches dans dictionnaire
    test.reset_dict()  
    test.add_task('Task4', 'Description for Task4')
    test.delete_task('Task4')
    assert 'Task4' not in test.task_dict
    
def test_reset_task():
# Effacer tous les tâches dans dictionnaire
    test.reset_dict()
    test_init = len(test.task_dict)
    test.add_task('Task4', 'Description for Task4')
    test.reset_dict()
    test_final = len(test.task_dict)    
    assert test_init == test_final

def test_display():
# Effacer tous les tâches dans dictionnaire
    test.reset_dict()
    nb_task = random.randint(1, 10)
    for i in range(nb_task):
        test.add_task('Task'+str(i+1), 'Description for Task'+str(i+1))
    nb_complete_task = random.randint(1, nb_task)
    for i in range(nb_complete_task):
        test.complete_task('Task'+str(i+1))
    test_dict = [item for item in test.task_dict.keys() if test.task_dict[item]['status'] == 'en cours']    
# Appelez la méthode display() et capturez sa sortie
    io_obj = io.StringIO()
    sys.stdout = io_obj
    
    test.display()
    
    sys.stdout = sys.__stdout__
    captured = io_obj.getvalue()
    captured = eval(captured)
    captured = set(captured)
    
    assert set(test_dict).issubset(captured)



if __name__ == "__main__":
    # do the tests
    pytest.main()

