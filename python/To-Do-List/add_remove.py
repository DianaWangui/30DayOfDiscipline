"""This class will manage the To Do List by adding and removing
items from the list."""

class Manage:
  """ Two list, personal and work to store Tasks separately."""
  def __init__(self, personal=[], work=[], ):
    self.personal = personal
    self.work = work

  # This is the method to add tasks to any of the To Do List
  def add_to_list(self, task, category):
    if category.lower() == "personal":
      self.personal.append(task)
      return True
    elif category.lower() == "work":
      self.work.append(task)
      return True
    else:
      return False
        
  # This is the method to remove tasks from the To Do lists
  def remove_from_list(self, task, category):
    if category.lower == "personal" and task in self.personal:
      self.personal.remove(task)
      return True
    elif category.lower() == "work" and task in self.work:
      self.work.remove(task)
      return True
    else:
        return False
