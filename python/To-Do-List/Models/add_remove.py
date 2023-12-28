"""This class will manage the To Do List by adding and removing
items from the list."""

class Manage:
  """ Two list, personal and work to store Tasks separately."""
  def __init__(self, personal=[], work=[]):
    self.personal = personal
    self.work = work

  # This is the method to add tasks to any of the To Do list handling all edge cases
  def add_to_list(self):
    print("List available are\n1. Personal\n2. Work")
    while(True):
      option = input("Do you want to add to your list yes or no: ")
      if option.lower() == "yes":
        selected_list = input("Which list to you want to add to: ")
        if selected_list.lower() == "personal":
          while(True):
            print("PERSONAL LIST")
            add = input("Enter task for personal list: ")
            self.personal.append(add)
            add_new = input("Would you like to add new task?(yes or no)")
            if (add_new.lower() != "yes"):
              break
        else:
          while(True):
            print("WORK LIST")
            add = input("Enter task for work list: ")
            self.work.append(add)
            add_new = input("Would you like to add new task?(yes or no)")
            if (add_new.lower() != "yes"):
              break
      else:
        break

  # This is the method to remove tasks from any of the To Do lists handling all edge cases
  def remove_from_list(self):
    print("Removing item fro the list.")
    while(True):
      remove_item = input("Do you want to remove items from the list? yes of no: ")
      if remove_item.lower() == "yes":
        selected_list = input("Which list do you want to remove from?\n1. Personal\n2. Work\nEnter the list here: ")
        if selected_list.lower() == "personal":
          if len(self.personal) == 0:
            print("Your personal list is empty")
            break
          else:
            rmv = input("\nEnter task number to remove:> ")
            try:
              num = int(rmv) - 1
              if num >= len(self.personal):
                print("Task not in the list")
              del self.personal[num]
              print("Task removed successfully\n")
              break
            except (ValueError, IndexError):
              print("Please enter a valid task number..")

        elif selected_list.lower() == "work":
          if len(self.work) == 0:
            print("Your work list is empty")
            break
          else:
            rmv = input("\nEnter task number to remove:> ")
            try:
              num = int(rmv) - 1
              if num >= len(self.work):
                print("Task not in the list")
              del self.work[num]
              print("Task removed successfully\n")
              break
            except (ValueError, IndexError):
              print("Please enter a valid task number.")
      print("\nOkey bye!")
      break

    
# testing
man = Manage()
man.add_to_list()
print(man.personal)
print(man.work)
man.remove_from_list()
print(man.personal)
print(man.work)
