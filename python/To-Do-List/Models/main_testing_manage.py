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
    def test_display(self):
        assert self.manager.display(category= "personal"), f"Error displaying tasks."

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
try:
    tc.test_display()
    print("\tTest Display passed")
except Exception as e:
    raise RuntimeError(f"\n\tTest Display Failed with error:\n{str(e)}")

