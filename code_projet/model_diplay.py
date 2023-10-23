import sys
import os

# Obtenir le répertoire dans lequel se trouve le fichier courant
current_directory = os.path.dirname(os.path.realpath(__file__ ))

# Obtenir le répertoire racine du projet
project_root = os.path.abspath(os.path.join(current_directory, ".."))

# Ajouter le répertoire racine du projet au chemin de recherche des modules
sys.path.append(project_root)

from code_projet.version_2 import Task


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, simpledialog            



class TaskManagerApp:
    def __init__(self, root,task_instance):
        self.root = root
        self.root.title("TO-DO List")
        self.task_list = task_instance
        self.root.configure(bg="#6593c0")

        # 创建一个布局容器
        self.container = ttk.Frame(root)
        self.container.grid(row=0, column=0, padx=50, pady=50)

        # 创建一个样式对象
        self.style = ttk.Style()
        self.style.configure("Title.TLabel", background="#FAEBD7", foreground="#8B4513", font=("Helvetica", 20))

        # 创建标题标签
        self.title_label = ttk.Label(self.container, text="To-Do List", style="Title.TLabel")
        self.title_label.grid(row=0, column=0, columnspan=4,padx=50, pady=50,sticky='n')

        # 创建任务名称输入框
        add_name_entry=ttk.Style()
        add_name_entry.configure("TEntry", borderwidth=2, relief="solid")
        self.add_task_name_entry = ttk.Entry(self.container,style="TEntry")
        self.add_task_name_entry.grid(row=1, column=0,padx=10, pady=20)

        # 创建“添加任务”按钮
        self.add_task_button = ttk.Button(self.container, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=1, column=1)



        # 创建删除任务名称输入框
        Del_name_entry=ttk.Style()
        Del_name_entry.configure("TEntry", borderwidth=2, relief="solid")
        self.Del_task_name_entry = ttk.Entry(self.container,style="TEntry")
        self.Del_task_name_entry.grid(row=1, column=2,padx=10, pady=20)

        # 创建“删除”按钮
        self.add_task_button = ttk.Button(self.container, text="Delete Task", command=self.delete_task)
        self.add_task_button.grid(row=1, column=3)

        # 创建完成任务名称输入框
        Complet_name_entry=ttk.Style()
        Complet_name_entry.configure("TEntry", borderwidth=2, relief="solid")
        self.Complet_task_name_entry = ttk.Entry(self.container,style="TEntry")
        self.Complet_task_name_entry.grid(row=2, column=0,padx=10, pady=20)

        # 创建“完成”按钮
        self.Complet_task_button = ttk.Button(self.container, text="Complete Task", command=self.complet_task)
        self.Complet_task_button.grid(row=2, column=1)

       # 创建一件删除所有任务的按钮
        self.clear_all_button = ttk.Button(self.container, text="Clear All Tasks", command=self.clear_all_tasks)
        self.clear_all_button.grid(row=2, column=3, columnspan=2, padx=10, pady=20)

        # 创建任务描述输入框
        # self.task_description_entry = ttk.Entry(self.container, style="TEntry")
        # self.task_description_entry.grid(row=2, column=2, padx=10, pady=20)

        # 创建“添加描述”按钮
        self.add_description_button = ttk.Button(self.container, text="Add Description", command=self.add_description_to_task)
        self.add_description_button.grid(row=2, column=2)

        self.task_listbox = ttk.Treeview(self.container, columns=("name","description", "status", "date"), show="headings")
        self.task_listbox.grid(row=3, column=0, columnspan=4,sticky='n')
        self.task_listbox.heading("name", text="name",anchor="center")
        self.task_listbox.heading("description", text="Description",anchor="center")
        self.task_listbox.heading("status", text="Status",anchor="center")
        self.task_listbox.heading("date", text="Date",anchor="center")

        self.task_listbox.column("name", anchor="center")
        self.task_listbox.column("status", anchor="center")
        self.task_listbox.column("date", anchor="center")
       



    def add_task(self):
        input_text = self.add_task_name_entry.get()
        task_parts = input_text.split(',', 1)  # 使用逗号进行第一次分割，最多分割一次
        task_name = task_parts[0].strip()

        if task_name:
            task_description = task_parts[1].strip() if len(task_parts) > 1 else ""
            if task_name in self.task_list.task_dict:
                messagebox.showinfo("ERROR", "The task already exists")
                self.add_task_name_entry.delete(0, "end")
            else:
                self.task_list.add_task(task_name, task_description)
                self.update_task_listbox()
                self.add_task_name_entry.delete(0, "end")
        else:
            messagebox.showinfo("ERROR", "Task name cannot be empty.")
  
    def delete_task(self):
        task_name = self.Del_task_name_entry.get()
        if task_name:
            self.task_list.delete_task(task_name)
            self.update_task_listbox()
            self.Del_task_name_entry.delete(0, "end")

    def complet_task(self):
        task_name = self.Complet_task_name_entry.get()
        if task_name:
            if task_name in self.task_list.task_dict:
                # 更改任务状态为已完成
                self.task_list.task_dict[task_name]['status'] = 'terminée'
                self.update_task_listbox()
                self.Complet_task_name_entry.delete(0, "end")
            else:
                # 任务不存在，向用户显示消息
                messagebox.showinfo("ERROR", "Task not found in the task list.")
                self.Complet_task_name_entry.delete(0, "end")

    def clear_all_tasks(self):
        # 弹出确认框，询问用户是否确定要清除所有任务
        confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks?")
        if confirmed:
            # 用户确认后，清除所有任务
            self.task_list.clear_all()
            self.update_task_listbox()
     
    def add_description_to_task(self):
        tasks_without_description = [task for task in self.task_list.task_dict if not self.task_list.task_dict[task]['description']]
        
        if tasks_without_description:
            # 创建任务选择对话框
            task_selection_dialog = TaskSelectionDialog(self.root, tasks_without_description)
            self.root.wait_window(task_selection_dialog.top)

            if task_selection_dialog.selected_task:
                selected_task = task_selection_dialog.selected_task
                # 弹出对话框获取任务描述
                task_description = simpledialog.askstring("Add Description", f"Enter a description for the task '{selected_task}':", parent=self.root)
                if task_description:
                    self.task_list.task_dict[selected_task]['description'] = task_description
                    self.update_task_listbox()
        else:
            messagebox.showinfo("INFO", "All tasks already have descriptions.")
 
    def update_task_listbox(self):
        # 清空现有的项目
        for item in self.task_listbox.get_children():
            self.task_listbox.delete(item)

        for task, info in self.task_list.task_dict.items():
            self.task_listbox.insert("", "end", values=(task, info['description'], info['status'], info['date']))


class TaskSelectionDialog:
    def __init__(self, parent, tasks):
        self.top = tk.Toplevel(parent)
        self.selected_task = None

        self.label = ttk.Label(self.top, text="Select a task to add a description:")
        self.label.pack(pady=5)

        self.task_var = tk.StringVar()
        self.task_var.set(tasks[0])
        self.task_menu = ttk.Combobox(self.top, textvariable=self.task_var, values=tasks)
        self.task_menu.pack(pady=5)

        self.ok_button = ttk.Button(self.top, text="OK", command=self.ok)
        self.ok_button.pack(pady=5)

    def ok(self):
        self.selected_task = self.task_var.get()
        self.top.destroy()

    def cancel(self):
        self.top.destroy()



if __name__ == "__main__":
    root = tk.Tk()
    task_instance=Task()
    app = TaskManagerApp(root,task_instance)
    root.mainloop()
