
import sys
import os

# Obtenir le répertoire dans lequel se trouve le fichier courant
current_directory = os.path.dirname(os.path.realpath(__file__ ))

# Obtenir le répertoire racine du projet
project_root = os.path.abspath(os.path.join(current_directory, ".."))

# Ajouter le répertoire racine du projet au chemin de recherche des modules
sys.path.append(project_root)
import pytest
from code_projet.version_2 import Task
from code_projet.model_diplay import TaskManagerApp
import tkinter as tk
import time

# test=Task()
# root=tk.Tk()
# app = TaskManagerApp(root,test)
# root.mainloop()

def test_task_integration():
    # 创建 Task 实例
    task = Task()

    # 在 TaskManagerApp 中添加任务
    app = TaskManagerApp(tk.Tk(), task)
    app.add_task('task1')

    # 检查任务是否成功添加
    assert 'task1' in task.task_dict
    # assert task.task_dict['task1']['description'] == 'Description for task1'

    # 还可以继续编写其他测试用例来测试不同的功能交互

if __name__ == "__main__":
    pytest.main()


# print(test.task_dict)