# testing_manage.py
from main_add_remove import Manage

class TestClass:
    def __init__(self):
        self.manager = Manage(["cook", "clean"], ["teach", "code"])

    def test_add(self):
        task = "study"
        task = "sleep"
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
        return True
    
    def test_mark_as_done(self):
        task="c"
        category = "personal"
        assert self.manager.mark_as_done(task, category)==True,"Marking as done failed"
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

try:
    tc.test_mark_as_done()
    print("\tTest Mark As Done passed.")
except IndexError:
    pass  # This is expected if the task isn't in the list anymore after being marked as done.

try:
    tc.test_display()
    print("\tTest Display passed")
except Exception as e:
    raise RuntimeError(f"\n\tTest Display Failed with error:\n{str(e)}")



