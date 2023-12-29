"""Creating a class with test files much readable and short"""
class Manage:
    def __init__(self, personal=[], work=[]):
        self.personal = personal
        self.work = work

    def add_to_list(self, task, category):
        if category.lower() == "personal":
            with open("personal.txt", "a", encoding="utf-8") as file:
                file.write(f"\n{task}")
            return True
        elif category.lower() == "work":
            with open("work.txt", "a", encoding="utf-8") as file:
                file.write(f"{task}")
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
        if category.lower() == "personal":
            with open("personal.txt", "r", encoding="utf-8") as file:
                file.seek(0)
                personal_task = file.readlines()
                for line in personal_task:
                    print(line.strip())
        elif category.lower() == "work":
            with open("work.txt", "r", encoding="utf-8") as file:
                file.seek(0)  # Set the pointer to start of the file
                work_task = file.readlines()
                for line in work_task:
                    print(line.strip())

            return self.work
        else:
            return None