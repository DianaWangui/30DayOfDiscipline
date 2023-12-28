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

# testing_manage.py
from main_add_remove import Manage

class TestClass:
    def __init__(self):
        self.manager = Manage(["cook", "clean"], ["teach", "code"])

    def test_add(self):
        task = "study"
        category = "personal"
        assert self.manager.add_to_list(task, category), f"Addition of {task} to {category} failed"
        return True

    def test_remove(self):
        task = "clean"
        category = "personal"
        assert self.manager.remove_from_list(task, category), f"Removal of {task} from {category} failed"
        return True

tc = TestClass()
print("Running tests...")

try:
    tc.test_add()
    print("\tTest Add passed", end="\n")
except AssertionError as e:
    print("\tTest Add Failed with error:", str(e))

try:
    tc.test_remove()
    print("\tTest Remove passed")
except AssertionError as e:
    print("\tTest Remove Failed with error:", str(e))
