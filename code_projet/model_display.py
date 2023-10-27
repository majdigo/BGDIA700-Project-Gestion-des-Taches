import logging
import datetime
from tkinter import ttk
from tkinter import messagebox, simpledialog
import tkinter as tk

# Configurer le logger
logging.basicConfig(filename='task_manager.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logging.getLogger('').addHandler(console_handler)

class TaskManagerApp:
    def __init__(self, root, task_instance):
        self.root = root
        self.root.title("TO-DO List")
        self.task_list = task_instance
        self.root.configure(bg="#6593c0")

        # create a container
        self.container = ttk.Frame(root)
        self.container.grid(row=0, column=0, padx=50, pady=50)

        # create a style object
        self.style = ttk.Style()
        self.style.configure("Title.TLabel", background="#FAEBD7",
                             foreground="#8B4513", font=("Helvetica", 20))

        # create a label
        self.title_label = ttk.Label(self.container,
                                     text="To-Do List",
                                     style="Title.TLabel")

        self.title_label.grid(row=0, column=0, columnspan=4,
                              padx=50, pady=50, sticky='n')

        # create a task name entry
        self.add_task_name_entry = self.create_styled_entry(self.container, 1, 0, "TEntry")

        # create a button of adding task
        self.add_task_button = self.create_button("Add Task",
                                                  self.add_task, 1, 1)

        # create a task name entry of deleting task
        self.Del_task_name_entry = self.create_styled_entry(self.container,
                                                            1, 2, "TEntry")

        # create a button of deleting task
        self.add_task_button = self.create_button("Delete Task",
                                                  self.delete_task, 1, 3)

        # create a entry of completing task
        self.Complet_task_name_entry = self.create_styled_entry(self.container,
                                                                2, 0, "TEntry")

        # create a button of completing task
        self.Complet_task_button = self.create_button("Complete Task",
                                                      self.complet_task, 2, 1)

        # create a button of clearing all tasks
        self.clear_all_button = self.create_button("Clear All",
                                                   self.clear_all_tasks, 2, 3)

        # create a button of adding description
        self.add_description_button = self.create_button("Add Description",
                                                         self.add_description_to_task, 2, 2)

        self.task_listbox = ttk.Treeview(self.container,
                                         columns=("name", "description", "status", "date"),
                                         show="headings")

        self.task_listbox.grid(row=3, column=0, columnspan=4, sticky='n')
        self.task_listbox.heading("name", text="name", anchor="center")

        self.task_listbox.heading("description",
                                  text="Description",
                                  anchor="center")

        self.task_listbox.heading("status",
                                  text="Status",
                                  anchor="center")

        self.task_listbox.heading("date",
                                  text="Date",
                                  anchor="center")

        self.task_listbox.column("name", anchor="center")
        self.task_listbox.column("status", anchor="center")
        self.task_listbox.column("date", anchor="center")

    def create_button(self, text, command, row, column):
        button = ttk.Button(self.container, text=text, command=command)
        button.grid(row=row, column=column)
        return button

    def create_styled_entry(self, container, row, column, style_name):
        entry = ttk.Entry(container, style=style_name)
        entry.grid(row=row, column=column, padx=10, pady=20)
        return entry

    def add_task(self):
        input_text = self.add_task_name_entry.get()
        task_parts = input_text.split(',', 1)
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
                # Ajouter la journalisation
                logging.info(f"Added task: {task_name}, Description: {task_description}")

        else:
            messagebox.showinfo("ERROR", "Task name cannot be empty.")
            # Ajouter la journalisation
            logging.warning("Tried to add a task with an empty name.")


    def delete_task(self):
        task_name = self.Del_task_name_entry.get()
        if task_name:
            self.task_list.delete_task(task_name)
            self.update_task_listbox()
            self.Del_task_name_entry.delete(0, "end")
            # Ajouter la journalisation
            logging.info(f"Deleted task: {task_name}")
        else:
            messagebox.showinfo("ERROR", "Task name cannot be empty.")
            # Ajouter la journalisation
            logging.warning("Tried to delete a task with an empty name.")


    def complet_task(self):
        task_name = self.Complet_task_name_entry.get()
        if task_name:
            if task_name in self.task_list.task_dict:
                # change the status of the task to completed
                self.task_list.task_dict[task_name]['status'] = 'terminée'
                self.update_task_listbox()
                self.Complet_task_name_entry.delete(0, "end")
                # Ajouter la journalisation
                logging.info(f"Completed task: {task_name}")

            else:
                # task does not exist, show message to user
                messagebox.showinfo("ERROR", "Task not found in the task list.")
                self.Complet_task_name_entry.delete(0, "end")
                # Ajouter la journalisation
                logging.warning(f"Tried to complete a non-existent task: {task_name}")
        else:
            messagebox.showinfo("ERROR", "Task name cannot be empty.")
            # Ajouter la journalisation
            logging.warning("Tried to complete a task with an empty name.")

    def clear_all_tasks(self):
        # show confirmation dialog to user
        confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks?")
        if confirmed:
            # if confirmed, clear all tasks
            self.task_list.clear_all()
            self.update_task_listbox()
            # Ajouter la journalisation
            logging.info("Cleared all tasks.")
        else:
            # Ajouter la journalisation
            logging.info("User canceled task clearing operation.")


    def add_description_to_task(self):
        tasks_without_description = [task for task in self.task_list.task_dict if not self.task_list.task_dict[task]['description']]

        if tasks_without_description:
            # create a task selection dialog
            task_selection_dialog = TaskSelectionDialog(self.root,
                                                        tasks_without_description)
            self.root.wait_window(task_selection_dialog.top)

            if task_selection_dialog.selected_task:
                selected_task = task_selection_dialog.selected_task
                # show dialog to get task description
                task_description = simpledialog.askstring("Add Description",
                                                          f"Enter a description for the task '{selected_task}':",
                                                          parent=self.root)
                if task_description:
                    self.task_list.task_dict[selected_task]['description'] = task_description
                    self.update_task_listbox()
                    # Ajouter la journalisation
                    logging.info(f"Added description to task: {selected_task}")

        else:
            messagebox.showinfo("INFO", "All tasks already have descriptions.")
            # Ajouter la journalisation
            logging.info("All tasks already have descriptions.")


    def update_task_listbox(self):
        # delete all items from the treeview
        for item in self.task_listbox.get_children():
            self.task_listbox.delete(item)

        for task, info in self.task_list.task_dict.items():
            self.task_listbox.insert("", "end",
                                     values=(task,
                                             info['description'],
                                             info['status'],
                                             info['date']))


class TaskSelectionDialog:
    def __init__(self, parent, tasks):
        self.top = tk.Toplevel(parent)
        self.selected_task = None

        self.label = ttk.Label(self.top,
                               text="Select a task to add a description:")
        self.label.pack(pady=5)

        self.task_var = tk.StringVar()
        self.task_var.set(tasks[0])
        self.task_menu = ttk.Combobox(self.top,
                                      textvariable=self.task_var,
                                      values=tasks)
        self.task_menu.pack(pady=5)

        self.ok_button = ttk.Button(self.top, text="OK", command=self.ok)
        self.ok_button.pack(pady=5)

    def ok(self):
        self.selected_task = self.task_var.get()
        self.top.destroy()

    def cancel(self):
        self.top.destroy()


if __name__ == "__main__":
    pass
