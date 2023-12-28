"""Creating a class with test files much readable and short"""
class Manage:
    def __init__(self, personal=[], work=[]):
        self.personal = personal
        self.work = work

    def add_to_list(self, task, category):
        if category.lower() == "personal":
            self.personal.append(task)
            return True
        elif category.lower() == "work":
            self.work.append(task)
            return True
        else:
            return False

    def remove_from_list(self, task, category):
        if category.lower() == "personal" and task in self.personal:
            self.personal.remove(task)
            return True
        elif category.lower() == "work" and task in self.work:
            self.work.remove(task)
            return True
        else:
            return False
        
    def mark_as_done(self, task, category):
        tasks_list = self.personal if category.lower() == "personal" else self.work
        for index, t in enumerate(tasks_list):
            if t == task:
                tasks_list[index] = f"{t} (Done)"
                return True
        return False
            
    def display(self, category):
        tasks_list = self.personal if category.lower() == "personal" else self.work
        return tasks_list