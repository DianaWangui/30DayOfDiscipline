from add_remove import Manage
class TestClass:
  def __init__(self):
    self.manager = Manage(["cook", "clean"], ["teach", "code"])
  def test_add(self):
    task = "iron"
    category = "personal"
    assert self.manager.add_to_list(task, category), f"failed to add {task} to {category}"
    return True
  def test_remove(self):
    task = "teach"
    category = "personal"
    assert self.manager.remove_from_list(task, category), f"failed to remove {task} from {category}"
    return True
  
tc = TestClass()
print("Running tests...")
try:
  tc.test_add()
  print("\tTest Add passed", end="\n")
except Exception as e:
  print("\tTest Add Failed with error: ", str(e))

try:
  tc.test_remove()
  print("\tTest Remove passed")
except AssertionError as e:
  print("\tTest Remove Failed with error: ", str(e))

    