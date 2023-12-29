class Task:
    def __init__(self, name):
        self.name = name
        self.done = False

class Manage:
    def __init__(self, tasks=[]):
        self.tasks = tasks

    def add_task(self, task_name):
        task = Task(task_name)
        self.tasks.append(task)

    def mark_as_done(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.done = True
                print(f'Task "{task_name}" marked as done.')
                return
        print(f'Task "{task_name}" not found.')

    def display_tasks(self):
        for task in self.tasks:
            status = "Done" if task.done else "Not Done"
            print(f'Task: {task.name} - Status: {status}')

# Example usage:
manager = Manage()
manager.add_task("Task 1")
manager.add_task("Task 2")
manager.display_tasks()

# Mark Task 1 as done
manager.mark_as_done("Task 1")

# Display tasks after marking as done
manager.display_tasks()
