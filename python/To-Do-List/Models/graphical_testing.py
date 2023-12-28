import tkinter as tk
from main_add_remove import Manage

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My To Do List")

        self.manager = Manage()

        self.label = tk.Label(root, text="My To-Do List")
        self.label.pack(pady=10)
        
        self.task_label = tk.Label(root, text="Task:")
        self.task_label.pack()
        
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack(pady=10)

        self.category_label = tk.Label(root, text="Category:")
        self.category_label.pack()

        self.category_entry = tk.Entry(root, width=30)
        self.category_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", fg = "red", command=self.add_task)
        self.add_button.pack(pady=10)

        self.remove_button = tk.Button(root, text="Remove Task",fg = "red", command=self.remove_task)
        self.remove_button.pack(pady=10)

        self.display_button = tk.Button(root, text="Display Tasks", fg = "red", command=self.display_tasks)
        self.display_button.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get()
        category = self.category_entry.get()
        self.manager.add_to_list(task, category)
        self.clear_entries()

        print(f"The task added: {task}, Category: {category}")

    def remove_task(self):
        task = self.task_entry.get()
        category = self.category_entry.get()
        self.manager.remove_from_list(task, category)
        self.clear_entries()

    def display_tasks(self):
        category = self.category_entry.get()
        tasks = self.manager.display(category)
        

        if tasks:
            print(f"Tasks in {category} category:")
            for task in tasks:
                print(task)
        else:
            print(f"No tasks found in {category} category.")

    def clear_entries(self):
        self.task_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
